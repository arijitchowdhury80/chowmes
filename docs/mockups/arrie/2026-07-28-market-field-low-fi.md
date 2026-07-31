# aRRIe Candidate Low-Fi IA: Market Field First

Date: 2026-07-28
Status: candidate for review, not approved, not implementation-ready
Related gate: `docs/plan/2026-07-28-ci-os-arrie-ux-ia-gate.md`

## Intent

This is a low-fidelity information architecture proposal for the next CI-OS / Argus product direction.

It assumes the home screen is a Market Field: a spatial competitive-intelligence map where the user starts with the market shape, clicks a hotspot, then reveals Argus's interpretation, actions, proof, and unknowns.

This artifact does not approve production UI work. It exists so the direction can be reviewed, challenged, and revised before implementation resumes.

## Primary Screen Question

When the user lands on CI-OS, the first question should be:

> Where is the competitive market moving, and which hotspot deserves attention now?

The screen should not start with a long report, a table, a source ledger, or a dashboard of metrics.

## Screen 1: Market Field

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ ARGUS / CI-OS                    Tenant: Algolia       Today | 7D | 30D | ▾ │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  MARKET FIELD                                                                │
│  Competitive movement across product reality, market conversation,           │
│  and audience demand.                                                        │
│                                                                              │
│             [AI commerce ownership]                                          │
│                    ◉                                                         │
│                 ╱  │  ╲        pulse = new movement in selected window       │
│        Constructor  │   Coveo                                                │
│             ●───────●──────● Bloomreach                                      │
│             │       │      ╲                                                 │
│             │       ● Audience demand: agentic shopping                      │
│             │      ╱                                                          │
│             ● Algolia product proof                                           │
│                                                                              │
│      Elastic ●──────◌ TCO / infra narrative                                  │
│                                                                              │
│      Shopify ◌──────◌ Partner ecosystem                                      │
│                                                                              │
│  Selected hotspot: AI commerce ownership                                     │
│  Confidence: Medium-high    Movement: Rising    Window: 7D                  │
│                                                                              │
│  [Open Argus read] [Show time movement] [Open proof]                         │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Screen Job

The Market Field answers:

- what market movement exists
- who is connected to it
- whether it is fresh
- whether it has product proof, market conversation, audience demand, or only weak evidence
- where the user should click first

### Semantic Rules

- Competitor nodes are companies.
- Theme nodes are market narratives.
- Capability nodes are product realities.
- Audience Demand nodes are Algolia audience response signals.
- Edges explain relationship, not decoration.
- Pulses mean new movement in the selected time window.
- Warning rings mean Argus confidence is limited.
- Dotted edges mean inferred or weak relationship.

## Click-To-Reveal Behavior

The default screen shows the market. It does not overload the user with every explanation.

Clicking a hotspot reveals the first interpretation layer.

```text
Market Field
└── Hotspot: AI commerce ownership
    ├── Argus read
    ├── Why this matters
    ├── Recommended actions
    ├── Proof chain
    └── Unknowns / confidence limits
```

## Screen 2: Selected Movement

Appears as a right-side panel or lower reveal after selecting a hotspot.

```text
┌──────────────────────────────────────────────────────────────┐
│ SELECTED MOVEMENT                                             │
├──────────────────────────────────────────────────────────────┤
│ AI commerce ownership is becoming the active competitive      │
│ frame in commerce search. Constructor is pushing the clearest │
│ narrative. Coveo and Bloomreach provide supporting product    │
│ and proof movement.                                           │
│                                                              │
│ Why it matters                                                │
│ Algolia risks having product strength interpreted as generic  │
│ search infrastructure unless the AI commerce story is made    │
│ more explicit.                                                │
│                                                              │
│ Trust state                                                   │
│ Product proof: partial                                        │
│ Conversation proof: present                                   │
│ Audience demand: present                                      │
│ Confidence limit: several competitor capability cells remain  │
│ unknown, not absent.                                          │
│                                                              │
│ [Show actions] [Open proof drawer] [Compare over time]        │
└──────────────────────────────────────────────────────────────┘
```

### Screen Job

The Selected Movement layer turns spatial market shape into a business read.

It must distinguish:

- fact: captured source event or product proof
- inference: Argus interpretation from multiple signals
- recommendation: named action with owner and why now
- unknown: unverified or missing evidence
- blocked recommendation: action Argus refuses to recommend yet

## Screen 3: Action Layer

```text
┌──────────────────────────────────────────────────────────────┐
│ WHAT ALGOLIA SHOULD DO NEXT                                  │
├──────────────┬────────────────────────────────────┬──────────┤
│ PMM          │ Sharpen AI commerce positioning    │ P1       │
│              │ Why now: competitor narrative is   │          │
│              │ moving faster than Algolia's       │          │
│              │ visible story in this window.      │          │
├──────────────┼────────────────────────────────────┼──────────┤
│ Sales        │ Prepare Constructor and Coveo talk │ P1       │
│              │ tracks for AI commerce objections. │          │
├──────────────┼────────────────────────────────────┼──────────┤
│ Product      │ Review unknown capability cells    │ P2       │
│              │ before treating gaps as real.      │          │
└──────────────┴────────────────────────────────────┴──────────┘
```

### Screen Job

Actions must never be generic department cards.

Every action needs:

- named owner
- urgency
- why now
- evidence basis
- confidence state
- what would change the recommendation

## Screen 4: Proof Drawer

```text
┌──────────────────────────────────────────────────────────────┐
│ PROOF CHAIN                                                   │
├──────────────────────────────────────────────────────────────┤
│ Recommendation                                                │
│ PMM should sharpen AI commerce positioning.                   │
│                                                              │
│ Evidence chain                                                │
│ 1. Constructor market claim: captured from source             │
│ 2. Coveo / Bloomreach supporting product proof: partial       │
│ 3. Algolia Audience Demand: matching topic movement present   │
│ 4. Product Muscle Matrix: unknown cells still confidence-limiting │
│                                                              │
│ Contradictions                                                │
│ None material in selected window.                             │
│                                                              │
│ Unknowns                                                      │
│ Some competitor capabilities are not captured yet. Unknown    │
│ does not mean absent.                                         │
│                                                              │
│ [Open raw evidence] [Open source health] [Copy evidence chain]│
└──────────────────────────────────────────────────────────────┘
```

### Screen Job

The Proof Drawer lets a user trust, challenge, or audit the read without dragging raw rows onto the first screen.

## Time Dimension

The Market Field must support:

- Today: operating read
- 7D: weekly pattern formation
- 30D: strategic movement
- Custom: investigation mode

Time should not be a decorative filter. It must change:

- node freshness
- pulse activity
- edge strength
- selected movement summary
- action urgency
- proof chain contents

## Navigation Model

```text
Market Field
├── Hotspot selected
│   ├── Selected Movement
│   │   ├── Action Layer
│   │   ├── Proof Drawer
│   │   └── Time Movement
│   └── Entity Drilldown
├── Evidence Lab
└── Admin
```

## What This Replaces

This direction replaces:

- static daily report as the default mental model
- raw heatmap table
- long proof lists on the main screen
- source-health-led homepage
- generic SaaS dashboard frame
- text-heavy sections that require an admin guide

## Review Questions

1. Should the Market Field be the actual first screen?
2. Should the editorial Argus read be hidden until a hotspot is selected, or always visible beside the field?
3. Should the first prototype be true 3D, or low-fi 2D/2.5D first to settle IA before visual complexity?
4. Which objects must appear as first-class nodes: competitors, themes, capabilities, audience demand, recommendations, or sources?
5. What would make this feel intelligence-grade rather than decorative?

## Current Recommendation

Proceed with a Market Field-first prototype, but build the first mockup as a controlled 2.5D layout before true 3D. The reason is product clarity: if the IA does not work in a static layered model, animation and 3D will hide the confusion instead of solving it.

Once Arijit accepts the object model, reveal sequence, and time behavior, convert this into a high-fidelity 3D constellation prototype.

