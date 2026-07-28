# CI-OS Market Field Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the approved Market Field-first CI-OS / Argus product experience as the live dashboard surface, with source-backed semantics, click-to-reveal actions, proof, unknowns, time windows, responsive behavior, and validation.

**Architecture:** Add a focused Market Field view-model layer inside the CI-OS dashboard package, render that model through the existing self-contained cockpit HTML renderer, and extend dashboard click validation to test the approved journey. Keep backend intelligence, Product Muscle, Audience Demand, and Evidence/Admin data sources as inputs to the view model rather than hardcoding UI claims.

**Tech Stack:** Python 3, Pydantic dashboard types, existing `cios.dashboard` renderer/publisher, pytest, existing Playwright dashboard validator, Chrome/Playwright for live validation.

## Global Constraints

- Hermes remains the runtime OS.
- CI-OS remains a separately versioned extension.
- Do not modify Hermes core.
- Do not wire production UI without tests.
- Do not show unknown product proof as confirmed absence, broken comparison, or empty UI.
- Evidence and Admin remain secondary routes, not first-screen content.
- Time controls must support Today, 7D, 30D, and Custom semantics.
- Mobile must use a focused mini-field plus stacked disclosure sections.
- Live acceptance must prove a user can answer the first-read questions in `docs/workspace/arrie-market-field/03-candidate-ux-ia-spec.md`.

---

## File Structure

Implementation lives in `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`.

- Modify: `src/cios/dashboard/types.py`
  - Add Market Field view-model types or extend existing dashboard state with a `market_field` property.
- Modify: `src/cios/dashboard/state_builder.py`
  - Compile Market Field data from existing `ProductMarketRunStatus`, pattern, recommendation, demand, feature comparison, source health, and competitor data.
- Modify: `src/cios/dashboard/cockpit_renderer.py`
  - Replace the current first-read shell with Market Field-first markup/CSS/JS, keeping output self-contained.
- Modify: `scripts/validate_dashboard_clicks.py`
  - Validate the approved journey: hotspot selection, time window change, action reveal, proof drawer, Evidence route, Admin route, responsive viewports.
- Modify: `tests/dashboard/test_cockpit_renderer.py`
  - Add renderer tests for Market Field structure, unknown semantics, actions, proof, and mobile fallback copy.
- Add or modify: `tests/dashboard/test_market_field_view_model.py`
  - Test the Market Field view-model independently from HTML.
- Modify if needed: `tests/dashboard/conftest.py`
  - Add fake Product Market rows that exercise hotspot, unknown, demand, proof, and recommendation states.
- Modify after implementation: `docs/workspace/arrie-market-field/_status.md`
  - Record implementation status and validation evidence.
- Modify after implementation: `docs/status/2026-07-13-ci-os-project-dossier.md`
  - Only at verified gate, record UX / IA gate progress.

---

### Task 1: Add Market Field View-Model Types

**Files:**
- Modify: `src/cios/dashboard/types.py`
- Test: `tests/dashboard/test_market_field_view_model.py`

**Interfaces:**
- Produces: `MarketFieldNode`, `MarketFieldEdge`, `MarketFieldHotspot`, `MarketFieldAction`, `MarketFieldProofItem`, `MarketFieldState`
- Consumes later: `DashboardState.market_field`

- [ ] **Step 1: Write the failing tests**

Create `tests/dashboard/test_market_field_view_model.py` with:

```python
from cios.dashboard.types import (
    MarketFieldAction,
    MarketFieldEdge,
    MarketFieldHotspot,
    MarketFieldNode,
    MarketFieldProofItem,
    MarketFieldState,
)


def test_market_field_state_distinguishes_unknown_from_absence() -> None:
    state = MarketFieldState(
        selected_hotspot_id="ai-commerce",
        nodes=[
            MarketFieldNode(
                node_id="unknown-ai-agent",
                label="Unknown boundary",
                node_type="unknown_boundary",
                status="confidence_limit",
                summary="Competitor capability cells are unresolved.",
            )
        ],
        edges=[],
        hotspots=[
            MarketFieldHotspot(
                hotspot_id="ai-commerce",
                label="AI commerce ownership",
                movement="rising",
                confidence_label="medium-high",
                proof_status="partial",
                unknowns=["Competitor capability cells are unresolved."],
            )
        ],
        actions=[],
        proof=[],
        time_windows=["today", "7d", "30d", "custom"],
    )

    assert state.nodes[0].node_type == "unknown_boundary"
    assert state.nodes[0].status == "confidence_limit"
    assert "absence" not in state.nodes[0].summary.lower()
    assert state.hotspots[0].unknowns == ["Competitor capability cells are unresolved."]


def test_market_field_state_carries_actions_and_proof_chain() -> None:
    state = MarketFieldState(
        selected_hotspot_id="ai-commerce",
        nodes=[
            MarketFieldNode(node_id="constructor", label="Constructor", node_type="competitor"),
            MarketFieldNode(node_id="demand-agentic", label="Audience demand", node_type="audience_demand"),
        ],
        edges=[
            MarketFieldEdge(
                source_node_id="constructor",
                target_node_id="demand-agentic",
                edge_type="overlaps_demand",
                strength="medium",
            )
        ],
        hotspots=[
            MarketFieldHotspot(
                hotspot_id="ai-commerce",
                label="AI commerce ownership",
                argus_read="AI commerce ownership is becoming the active competitive frame.",
                movement="rising",
                confidence_label="medium-high",
                proof_status="partial",
            )
        ],
        actions=[
            MarketFieldAction(
                owner="PMM",
                priority="P1",
                action="Sharpen AI commerce positioning.",
                why_now="Competitor narrative is moving faster than Algolia's visible story.",
                confidence_label="medium-high",
            )
        ],
        proof=[
            MarketFieldProofItem(
                plane="audience_demand",
                summary="Audience response overlaps the agentic shopping topic.",
                source_count=3,
            )
        ],
        time_windows=["today", "7d", "30d", "custom"],
    )

    assert state.selected_hotspot.label == "AI commerce ownership"
    assert state.actions[0].owner == "PMM"
    assert state.proof[0].plane == "audience_demand"
```

- [ ] **Step 2: Run test to verify it fails**

Run:

```bash
cd /Users/arijitchowdhury/Dropbox/AI-Development/CI-OS
python3 -m pytest tests/dashboard/test_market_field_view_model.py -q
```

Expected: FAIL because `MarketFieldState` and related classes do not exist.

- [ ] **Step 3: Add minimal types**

In `src/cios/dashboard/types.py`, add Pydantic models near the other dashboard view objects:

```python
class MarketFieldNode(BaseModel):
    node_id: str
    label: str
    node_type: str
    status: str = "present"
    summary: Optional[str] = None
    entity_id: Optional[int] = None
    href: Optional[str] = None


class MarketFieldEdge(BaseModel):
    source_node_id: str
    target_node_id: str
    edge_type: str
    strength: str = "weak"
    status: str = "present"
    summary: Optional[str] = None


class MarketFieldHotspot(BaseModel):
    hotspot_id: str
    label: str
    argus_read: Optional[str] = None
    movement: str = "unknown"
    confidence_label: str = "unknown"
    proof_status: str = "unknown"
    time_window: str = "7d"
    connected_node_ids: list[str] = Field(default_factory=list)
    unknowns: list[str] = Field(default_factory=list)


class MarketFieldAction(BaseModel):
    owner: str
    priority: str
    action: str
    why_now: str
    evidence_basis: list[str] = Field(default_factory=list)
    confidence_label: str = "unknown"


class MarketFieldProofItem(BaseModel):
    plane: str
    summary: str
    source_count: int = 0
    href: Optional[str] = None


class MarketFieldState(BaseModel):
    selected_hotspot_id: Optional[str] = None
    nodes: list[MarketFieldNode] = Field(default_factory=list)
    edges: list[MarketFieldEdge] = Field(default_factory=list)
    hotspots: list[MarketFieldHotspot] = Field(default_factory=list)
    actions: list[MarketFieldAction] = Field(default_factory=list)
    proof: list[MarketFieldProofItem] = Field(default_factory=list)
    time_windows: list[str] = Field(default_factory=lambda: ["today", "7d", "30d", "custom"])

    @property
    def selected_hotspot(self) -> Optional[MarketFieldHotspot]:
        if self.selected_hotspot_id:
            for hotspot in self.hotspots:
                if hotspot.hotspot_id == self.selected_hotspot_id:
                    return hotspot
        return self.hotspots[0] if self.hotspots else None
```

Add a field to `DashboardState`:

```python
market_field: MarketFieldState = Field(default_factory=MarketFieldState)
```

- [ ] **Step 4: Run test to verify it passes**

Run:

```bash
python3 -m pytest tests/dashboard/test_market_field_view_model.py -q
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/cios/dashboard/types.py tests/dashboard/test_market_field_view_model.py
git commit -m "Add Market Field dashboard state types"
```

---

### Task 2: Build Market Field State From Existing Intelligence Data

**Files:**
- Modify: `src/cios/dashboard/state_builder.py`
- Modify: `tests/dashboard/conftest.py` if existing fakes need richer rows
- Test: `tests/dashboard/test_market_field_view_model.py`

**Interfaces:**
- Consumes: `DashboardStateBuilder.build(...)`, `ProductMarketRunStatus`, existing product-market repository protocol rows
- Produces: populated `DashboardState.market_field`

- [ ] **Step 1: Add failing builder test**

Append to `tests/dashboard/test_market_field_view_model.py`:

```python
from tests.dashboard.conftest import FakeProductMarketRepository
from cios.dashboard.state_builder import DashboardStateBuilder


def test_builder_compiles_market_field_from_patterns_recommendations_and_unknowns(
    dashboard_builder_factory,
) -> None:
    product_market = FakeProductMarketRepository(
        patterns={
            1: [
                {
                    "id": 10,
                    "pattern_label": "AI commerce ownership",
                    "pattern_type": "theme",
                    "summary": "Constructor and Coveo are concentrating around AI commerce.",
                    "confidence": 0.72,
                    "entities": ["Constructor", "Coveo"],
                    "capabilities": ["AI shopping agents"],
                    "demand_topics": ["agentic shopping"],
                }
            ]
        },
        recommendations={
            1: [
                {
                    "id": 20,
                    "pattern_observation_id": 10,
                    "owner": "PMM",
                    "priority": "P1",
                    "action": "Sharpen AI commerce positioning.",
                    "why_now": "Competitor narrative is moving faster than Algolia's visible story.",
                }
            ]
        },
        feature_matrix={
            1: [
                {
                    "company_name": "Constructor",
                    "capability": "AI shopping agents",
                    "status": "unknown",
                    "summary": "No product proof captured yet; unknown is not absence.",
                }
            ]
        },
        demand_signals={
            1: [
                {
                    "topic": "agentic shopping",
                    "summary": "Audience demand is rising for agentic shopping pages.",
                    "change_pct": 0.31,
                    "source_count": 3,
                }
            ]
        },
    )
    builder = dashboard_builder_factory(product_market=product_market)

    state = builder.build(tenant_id=1, cadence="daily")

    field = state.market_field
    assert field.selected_hotspot.label == "AI commerce ownership"
    assert any(node.node_type == "audience_demand" for node in field.nodes)
    assert any(node.node_type == "unknown_boundary" for node in field.nodes)
    assert field.actions[0].owner == "PMM"
    assert "absence" not in " ".join(node.summary or "" for node in field.nodes).lower()
```

If `dashboard_builder_factory` does not accept `product_market`, update the fixture in `tests/dashboard/conftest.py` to pass it into `DashboardStateBuilder`.

- [ ] **Step 2: Run test to verify it fails**

```bash
python3 -m pytest tests/dashboard/test_market_field_view_model.py::test_builder_compiles_market_field_from_patterns_recommendations_and_unknowns -q
```

Expected: FAIL because the builder does not populate `market_field`.

- [ ] **Step 3: Add builder helper**

In `src/cios/dashboard/state_builder.py`, add a helper near product-market compilation code:

```python
def _build_market_field_state(
    *,
    patterns: list[dict],
    recommendations: list[dict],
    demand_signals: list[dict],
    feature_matrix: list[dict],
) -> MarketFieldState:
    nodes: dict[str, MarketFieldNode] = {}
    edges: list[MarketFieldEdge] = []
    hotspots: list[MarketFieldHotspot] = []
    actions: list[MarketFieldAction] = []
    proof: list[MarketFieldProofItem] = []

    top_pattern = patterns[0] if patterns else None
    if top_pattern:
        hotspot_id = _slugify(str(top_pattern.get("pattern_label") or top_pattern.get("label") or "market-hotspot"))
        entities = [str(value) for value in top_pattern.get("entities") or [] if value]
        capabilities = [str(value) for value in top_pattern.get("capabilities") or [] if value]
        demand_topics = [str(value) for value in top_pattern.get("demand_topics") or [] if value]

        nodes[hotspot_id] = MarketFieldNode(
            node_id=hotspot_id,
            label=str(top_pattern.get("pattern_label") or "Market hotspot"),
            node_type="theme",
            summary=str(top_pattern.get("summary") or ""),
        )
        for entity in entities:
            node_id = _slugify(entity)
            nodes[node_id] = MarketFieldNode(node_id=node_id, label=entity, node_type="competitor")
            edges.append(MarketFieldEdge(source_node_id=node_id, target_node_id=hotspot_id, edge_type="claims", strength="medium"))
        for capability in capabilities:
            node_id = f"capability-{_slugify(capability)}"
            nodes[node_id] = MarketFieldNode(node_id=node_id, label=capability, node_type="capability")
            edges.append(MarketFieldEdge(source_node_id=hotspot_id, target_node_id=node_id, edge_type="ships", strength="medium"))
        for topic in demand_topics:
            node_id = f"demand-{_slugify(topic)}"
            nodes[node_id] = MarketFieldNode(node_id=node_id, label=topic, node_type="audience_demand")
            edges.append(MarketFieldEdge(source_node_id=node_id, target_node_id=hotspot_id, edge_type="overlaps_demand", strength="medium"))

        unknowns: list[str] = []
        for row in feature_matrix:
            status = str(row.get("status") or row.get("own_status") or row.get("position_status") or "").lower()
            if status == "unknown":
                label = str(row.get("capability") or row.get("capability_label") or "Unknown capability")
                summary = str(row.get("summary") or "Product proof not captured yet; unknown is not absence.")
                node_id = f"unknown-{_slugify(label)}"
                nodes[node_id] = MarketFieldNode(
                    node_id=node_id,
                    label=label,
                    node_type="unknown_boundary",
                    status="confidence_limit",
                    summary=summary,
                )
                edges.append(MarketFieldEdge(source_node_id=hotspot_id, target_node_id=node_id, edge_type="limits_confidence", strength="weak", status="confidence_limit"))
                unknowns.append(summary)

        hotspots.append(
            MarketFieldHotspot(
                hotspot_id=hotspot_id,
                label=str(top_pattern.get("pattern_label") or "Market hotspot"),
                argus_read=str(top_pattern.get("summary") or ""),
                movement="rising",
                confidence_label="medium-high" if float(top_pattern.get("confidence") or 0) >= 0.7 else "medium",
                proof_status="partial" if unknowns else "present",
                connected_node_ids=list(nodes),
                unknowns=unknowns,
            )
        )

    for recommendation in recommendations:
        actions.append(
            MarketFieldAction(
                owner=str(recommendation.get("owner") or "PMM"),
                priority=str(recommendation.get("priority") or "P1"),
                action=str(recommendation.get("action") or recommendation.get("recommendation") or "Inspect this movement."),
                why_now=str(recommendation.get("why_now") or recommendation.get("rationale") or "This movement is material in the selected window."),
                confidence_label="medium-high",
            )
        )

    for demand in demand_signals:
        proof.append(
            MarketFieldProofItem(
                plane="audience_demand",
                summary=str(demand.get("summary") or demand.get("topic") or "Audience demand signal captured."),
                source_count=int(demand.get("source_count") or 0),
            )
        )

    return MarketFieldState(
        selected_hotspot_id=hotspots[0].hotspot_id if hotspots else None,
        nodes=list(nodes.values()),
        edges=edges,
        hotspots=hotspots,
        actions=actions,
        proof=proof,
    )
```

Import the new types at the top of `state_builder.py`.

If `_slugify` does not exist in `state_builder.py`, add:

```python
def _slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "unknown"
```

and import `re`.

Wire this helper into `DashboardStateBuilder.build` after product-market rows are loaded.

- [ ] **Step 4: Run focused tests**

```bash
python3 -m pytest tests/dashboard/test_market_field_view_model.py -q
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/cios/dashboard/state_builder.py tests/dashboard/conftest.py tests/dashboard/test_market_field_view_model.py
git commit -m "Build Market Field state from intelligence data"
```

---

### Task 3: Render The Market Field-First Dashboard

**Files:**
- Modify: `src/cios/dashboard/cockpit_renderer.py`
- Test: `tests/dashboard/test_cockpit_renderer.py`

**Interfaces:**
- Consumes: `DashboardState.market_field`
- Produces: self-contained HTML with `#market-field`, `#selected-movement`, `#action-layer`, `#proof-drawer`, `#evidence-lab`, `#admin`

- [ ] **Step 1: Add failing renderer test**

Append to `tests/dashboard/test_cockpit_renderer.py`:

```python
from cios.dashboard.types import (
    MarketFieldAction,
    MarketFieldHotspot,
    MarketFieldNode,
    MarketFieldProofItem,
    MarketFieldState,
)


def test_renders_market_field_first_experience() -> None:
    state = DashboardState(
        tenant_id=1,
        cadence="daily",
        market_field=MarketFieldState(
            selected_hotspot_id="ai-commerce",
            nodes=[
                MarketFieldNode(node_id="ai-commerce", label="AI commerce ownership", node_type="theme"),
                MarketFieldNode(node_id="constructor", label="Constructor", node_type="competitor"),
                MarketFieldNode(node_id="unknown-ai-agent", label="Unknown boundary", node_type="unknown_boundary", status="confidence_limit", summary="Unknown is not absence."),
            ],
            hotspots=[
                MarketFieldHotspot(
                    hotspot_id="ai-commerce",
                    label="AI commerce ownership",
                    argus_read="AI commerce ownership is becoming the active competitive frame.",
                    movement="rising",
                    confidence_label="medium-high",
                    proof_status="partial",
                    unknowns=["Unknown is not absence."],
                )
            ],
            actions=[
                MarketFieldAction(
                    owner="PMM",
                    priority="P1",
                    action="Sharpen AI commerce positioning.",
                    why_now="Competitor narrative is moving faster than Algolia's visible story.",
                    confidence_label="medium-high",
                )
            ],
            proof=[
                MarketFieldProofItem(
                    plane="audience_demand",
                    summary="Audience demand overlaps the selected movement.",
                    source_count=3,
                )
            ],
        ),
    )

    html = render_cockpit_html(state)

    assert 'id="market-field"' in html
    assert 'id="selected-movement"' in html
    assert 'id="action-layer"' in html
    assert 'id="proof-drawer"' in html
    assert 'id="evidence-lab"' in html
    assert 'id="admin"' in html
    assert "Where the market is concentrating" in html
    assert "AI commerce ownership" in html
    assert "Sharpen AI commerce positioning." in html
    assert "Unknown is not absence." in html
    assert "confirmed absence" not in html.lower()
```

- [ ] **Step 2: Run test to verify it fails**

```bash
python3 -m pytest tests/dashboard/test_cockpit_renderer.py::test_renders_market_field_first_experience -q
```

Expected: FAIL because the renderer does not expose Market Field-first IDs/copy.

- [ ] **Step 3: Implement renderer sections**

In `src/cios/dashboard/cockpit_renderer.py`:

- Update the module docstring to reference the approved Market Field contract.
- Add `_render_market_field(state: DashboardState) -> str`.
- Add `_render_selected_movement(state: DashboardState) -> str`.
- Add `_render_action_layer(state: DashboardState) -> str`.
- Add `_render_proof_drawer(state: DashboardState) -> str`.
- Add `_render_evidence_lab_route(state: DashboardState) -> str`.
- Add `_render_admin_route(state: DashboardState) -> str`.
- Add CSS and JS based on the validated mockup, adapted to backend data.

The rendered HTML must include:

```html
<section id="market-field" aria-label="Market Field">
  <div class="market-field-canvas" data-market-field-canvas>
    <button type="button" data-market-hotspot="ai-commerce" aria-pressed="true">AI commerce ownership</button>
  </div>
</section>
<aside id="selected-movement" aria-label="Selected movement">
  <h2 data-selected-hotspot-title>AI commerce ownership</h2>
  <p data-selected-hotspot-read>AI commerce ownership is becoming the active competitive frame.</p>
</aside>
<section id="action-layer" aria-label="What Algolia should do next">
  <article data-market-action>
    <h3>PMM</h3>
    <p>Sharpen AI commerce positioning.</p>
  </article>
</section>
<section id="proof-drawer" aria-label="Proof chain">
  <button type="button" data-proof-drawer-toggle aria-expanded="false">Open proof drawer</button>
  <div data-proof-drawer-panel hidden>Audience demand overlaps the selected movement.</div>
</section>
<section id="evidence-lab" aria-label="Evidence Lab">
  <a href="#evidence-lab">Inspect raw proof</a>
</section>
<section id="admin" aria-label="Admin">
  <a href="#admin">Inspect run controls and diagnostics</a>
</section>
```

The renderer must escape all dynamic strings through existing escaping helpers.

- [ ] **Step 4: Run renderer tests**

```bash
python3 -m pytest tests/dashboard/test_cockpit_renderer.py -q
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/cios/dashboard/cockpit_renderer.py tests/dashboard/test_cockpit_renderer.py
git commit -m "Render Market Field first dashboard"
```

---

### Task 4: Extend Dashboard Click Validation For Approved Journey

**Files:**
- Modify: `scripts/validate_dashboard_clicks.py`
- Test: `tests/scripts/test_validate_dashboard_clicks_dependencies.py` or add `tests/scripts/test_validate_dashboard_clicks_market_field.py`

**Interfaces:**
- Consumes: live or local dashboard URL
- Produces: PASS checks for Market Field journey

- [ ] **Step 1: Add validator tests for dependency-free selectors**

Create `tests/scripts/test_validate_dashboard_clicks_market_field.py` with pure helper tests if the validator exposes helper functions. If it does not, add selector constants to the script and test them:

```python
from scripts import validate_dashboard_clicks as validator


def test_market_field_selector_contract_names_required_sections() -> None:
    assert "#market-field" in validator.MARKET_FIELD_REQUIRED_SELECTORS
    assert "#selected-movement" in validator.MARKET_FIELD_REQUIRED_SELECTORS
    assert "#action-layer" in validator.MARKET_FIELD_REQUIRED_SELECTORS
    assert "#proof-drawer" in validator.MARKET_FIELD_REQUIRED_SELECTORS
    assert "#evidence-lab" in validator.MARKET_FIELD_REQUIRED_SELECTORS
    assert "#admin" in validator.MARKET_FIELD_REQUIRED_SELECTORS
```

- [ ] **Step 2: Run test to verify it fails**

```bash
python3 -m pytest tests/scripts/test_validate_dashboard_clicks_market_field.py -q
```

Expected: FAIL because `MARKET_FIELD_REQUIRED_SELECTORS` does not exist.

- [ ] **Step 3: Add validator coverage**

In `scripts/validate_dashboard_clicks.py`, add:

```python
MARKET_FIELD_REQUIRED_SELECTORS = (
    "#market-field",
    "#selected-movement",
    "#action-layer",
    "#proof-drawer",
    "#evidence-lab",
    "#admin",
)
```

Add function:

```python
def validate_market_field(page: Page) -> CheckResult:
    for selector in MARKET_FIELD_REQUIRED_SELECTORS:
        _assert(page.locator(selector).count() == 1, f"{selector} missing")
    _assert(page.locator("[data-market-hotspot]").count() > 0, "market hotspots missing")
    first = page.locator("[data-market-hotspot]").first
    first.click()
    page.wait_for_timeout(150)
    _assert(page.locator("#selected-movement").is_visible(), "selected movement did not remain visible")
    proof_button = page.locator("[data-proof-drawer-toggle]")
    _assert(proof_button.count() == 1, "proof drawer toggle missing")
    proof_button.click()
    page.wait_for_timeout(150)
    _assert(page.locator("#proof-drawer").is_visible(), "proof drawer did not open")
    for label in ("Today", "7D", "30D"):
        page.locator(f'[data-window="{label}"]').click()
        page.wait_for_timeout(100)
    return CheckResult("market_field", "Hotspot selection, time windows, action layer, proof drawer, Evidence, and Admin sections validated")
```

Call it from the main validation sequence before legacy semantic-layer checks. If legacy checks are still required during transition, keep them until the new page fully replaces old sections.

- [ ] **Step 4: Run tests**

```bash
python3 -m pytest tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_validate_dashboard_clicks_dependencies.py -q
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add scripts/validate_dashboard_clicks.py tests/scripts/test_validate_dashboard_clicks_market_field.py
git commit -m "Validate Market Field dashboard journey"
```

---

### Task 5: Local Render, Responsive, And Accessibility Smoke

**Files:**
- Modify only if tests reveal defects:
  - `src/cios/dashboard/cockpit_renderer.py`
  - `scripts/validate_dashboard_clicks.py`
- Add validation evidence:
  - `docs/workspace/arrie-market-field/05-local-implementation-validation.md`

**Interfaces:**
- Consumes: local generated dashboard HTML
- Produces: rendered screenshots and validation note

- [ ] **Step 1: Generate local dashboard HTML**

Use the project’s existing generation command. If no single fixture command exists, run the focused renderer tests and write a small temporary fixture script under `/tmp`, not the repo.

Required command:

```bash
cd /Users/arijitchowdhury/Dropbox/AI-Development/CI-OS
python3 -m pytest tests/dashboard/test_cockpit_renderer.py tests/dashboard/test_market_field_view_model.py -q
```

Expected: PASS.

- [ ] **Step 2: Run full dashboard/script test subset**

```bash
python3 -m pytest tests/dashboard tests/scripts -q
```

Expected: PASS.

- [ ] **Step 3: Run local click validator**

If the dashboard can be generated to an HTML file:

```bash
python3 scripts/validate_dashboard_clicks.py --url file:///absolute/path/to/generated-dashboard.html
```

If the script only accepts HTTP URLs, start a temporary local server:

```bash
python3 -m http.server 8787 --directory /absolute/path/to/generated-dashboard-dir
python3 scripts/validate_dashboard_clicks.py --url http://127.0.0.1:8787/generated-dashboard.html
```

Expected: PASS including `market_field`.

- [ ] **Step 4: Render screenshots**

Use Chrome or Playwright to capture:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new \
  --disable-gpu \
  --hide-scrollbars \
  --window-size=1440,1100 \
  --screenshot=/tmp/cios-market-field-desktop.png \
  "file:///absolute/path/to/generated-dashboard.html"

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new \
  --disable-gpu \
  --hide-scrollbars \
  --window-size=390,1100 \
  --screenshot=/tmp/cios-market-field-mobile.png \
  "file:///absolute/path/to/generated-dashboard.html"
```

Expected: screenshots are nonblank, no title/node overlap, mobile wraps selected movement title.

- [ ] **Step 5: Record validation evidence**

Create `docs/workspace/arrie-market-field/05-local-implementation-validation.md`:

```markdown
# Market Field Local Implementation Validation

Date: 2026-07-28
Status: local implementation validation

## Commands

- `python3 -m pytest tests/dashboard/test_cockpit_renderer.py tests/dashboard/test_market_field_view_model.py -q`
- `python3 -m pytest tests/dashboard tests/scripts -q`
- `python3 scripts/validate_dashboard_clicks.py --url file:///absolute/path/to/generated-dashboard.html`

## Results

- dashboard tests:
- script tests:
- click validation:
- desktop screenshot:
- mobile screenshot:

## Judgment

Record one of these exact judgments:

- `ready_for_staging`: all local dashboard, script, click, and screenshot checks passed.
- `not_ready_for_staging`: one or more local checks failed; list each failed command and screenshot finding before any staging attempt.
```

- [ ] **Step 6: Commit**

```bash
git add docs/workspace/arrie-market-field/05-local-implementation-validation.md
git commit -m "Validate Market Field implementation locally"
```

---

### Task 6: Stage Through CI-OS Package Path And Live Validation

**Files:**
- Modify only if validation reveals defects:
  - CI-OS package files from earlier tasks
- Add status docs after verified stage gate:
  - `docs/status/2026-07-28-ci-os-market-field-ux-gate.md` in ChowMes

**Interfaces:**
- Consumes: CI-OS package branch and Chowmes deployment path
- Produces: live `https://ci.chowmes.com/` Market Field validation evidence

- [ ] **Step 1: Confirm clean CI-OS package status**

```bash
cd /Users/arijitchowdhury/Dropbox/AI-Development/CI-OS
git status --short
```

Expected: only intended Market Field implementation changes are present.

- [ ] **Step 2: Run package tests**

```bash
python3 -m pytest tests/dashboard tests/scripts tests/intelligence -q
```

Expected: PASS.

- [ ] **Step 3: Deploy through existing cgroup-safe package path**

Use the already documented CI-OS deploy/Hermes wrapper path. Do not modify Hermes core.

Expected:

- CI-OS runs as the `cios` application user.
- Hermes remains scheduler / runtime OS.
- Package publish completes with one run ID.

- [ ] **Step 4: Validate public status and semantic dashboard match**

```bash
curl -fsS https://ci.chowmes.com/data/argus-latest-run-status.json -o /tmp/status.json
curl -fsS https://ci.chowmes.com/v2/data/semantic-dashboard.json -o /tmp/semantic.json
python3 - <<'PY'
import json
status=json.load(open('/tmp/status.json'))
semantic=json.load(open('/tmp/semantic.json'))
print(status.get('run_id'), status.get('status'), status.get('publish_status'))
print(semantic.get('run_id'))
assert status.get('run_id') == semantic.get('run_id')
assert status.get('status') == 'published'
assert status.get('publish_status') == 'published'
PY
```

Expected: assertions pass.

- [ ] **Step 5: Run live click validator**

```bash
cd /Users/arijitchowdhury/Dropbox/AI-Development/CI-OS
python3 scripts/validate_dashboard_clicks.py --url https://ci.chowmes.com/
```

Expected: PASS including `market_field`, responsive viewports, Evidence/Admin routes.

- [ ] **Step 6: Record gate evidence**

Create or update ChowMes status doc:

```markdown
# CI-OS Market Field UX Gate

Date: 2026-07-28
Status: passed

## Approval

Arijit approved Market Field-first UX / IA for implementation planning.

## Build Evidence

- commit:
- tests:
- package run:
- public run id:
- semantic match:
- live click validation:

## Judgment

The UX / IA gate is cleared for the next CI-OS phase because the approved Market Field-first journey passed live validation.
```

If live validation fails, write a separate `Status: failed` note with the failed command output and do not claim the gate is cleared.

- [ ] **Step 7: Commit**

```bash
cd /Users/arijitchowdhury/Dropbox/AI-Development/Personal/ChowMes
git add docs/status/2026-07-28-ci-os-market-field-ux-gate.md
git commit -m "Record CI-OS Market Field UX gate"
```

---

## Self-Review

### Spec Coverage

- Market Field home: Task 3.
- Click-to-reveal: Tasks 3 and 4.
- Time windows: Tasks 1, 3, 4, 5.
- Actions: Tasks 1, 2, 3.
- Proof drawer: Tasks 1, 3, 4.
- Unknown semantics: Tasks 1, 2, 3.
- Evidence/Admin separation: Tasks 3, 4.
- Responsive validation: Tasks 4, 5, 6.
- Live-data validation: Task 6.
- Hermes boundary: Global constraints and Task 6.

### Known Gaps

- This plan does not complete Product Muscle queue items or pilot release. Those remain governed by the broader CI-OS phase plan after the UX / IA gate passes.
- This plan does not decide true 3D. It implements a production-safe Market Field surface first; true 3D remains a later visual/system decision.

### Execution Choice

Recommended execution: inline task-by-task with TDD checkpoints, because the CI-OS repo is already dirty only with `data/` and the renderer is a large shared file that benefits from tight review after each task.
