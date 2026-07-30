# CI-OS Phase 1 Argus Intelligence Packet Contract

Date: 2026-07-30
Status: draft for human approval
Goal: `docs/goals/2026-07-30-ci-os-intelligence-spine-autonomous-goal.md`
Phase: 1, Intelligence Packet Contract
Workflow: `development-loop`
Runtime boundary: Hermes remains the runtime OS. CI-OS remains a separately versioned extension. This contract does not authorize Hermes core changes.

## Phase 1 Decision

CI-OS should introduce a new versioned top-level packet:

`ArgusIntelligencePacket`

It should not simply rename or expand `ProductMarketIntelligenceBrief`.

Reason:

- `ProductMarketIntelligenceBrief` is currently a useful synthesis artifact, but it does not carry enough run identity, consumer status, proof graph, contradiction, stale-data, delivery, weekly-window, and consumer-parity semantics to be the source of truth for the whole product.
- `IntelligenceSpine` and `MarketFieldState` are dashboard-facing view models. They are consumers or adapters, not the canonical business object.
- `ArgusDecisionRead`, `MarketMovementMap`, pattern observations, recommendations, and source-health rows are valid upstream components. They should feed the packet, not compete with it.
- Telegram, dashboard, 3D Market Field, weekly synthesis, Evidence Lab, Admin, and public status must render from this packet or explicitly say that no current packet exists.

## Contract Thesis

The packet is the one run-bound Argus read.

It answers:

1. What moved?
2. Who caused the movement?
3. What changed over the selected time window?
4. Is the movement daily noise, weekly pattern, monthly trend, or custom-window movement?
5. Why does it matter to Algolia?
6. What should a named team do next?
7. Why this action, now?
8. What evidence supports it?
9. What contradicts or weakens it?
10. What is unknown or confidence-limiting?
11. Which sources failed, and how does trust change?
12. What should Argus monitor next?
13. How can a user drill into proof without losing the story?
14. How can a user switch from Telegram to dashboard and see the same run?
15. How can a user know Hermes executed and CI-OS produced this intelligence?

If the packet cannot answer a question, it must say why, not leave the consumer to infer meaning from raw rows.

## Packet Shape

`ArgusIntelligencePacket`

Required fields:

- `schema_version`: integer, starting at `1`.
- `packet_id`: stable id for this packet publication.
- `tenant`: `{tenant_id, slug, display_name}`.
- `run`: `RunIdentity`.
- `cadence`: `daily`, `weekly`, `monthly`, or `custom`.
- `time_window`: `TimeWindow`.
- `status`: `PacketStatus`.
- `executive_read`: `ExecutiveRead`.
- `market_movements`: list of `MarketMovement`.
- `attention_state`: `AttentionState`.
- `recommendations`: list of `PacketRecommendation`.
- `blocked_actions`: list of `BlockedAction`.
- `evidence_planes`: list of `EvidencePlane`.
- `proof_graph`: `ProofGraph`.
- `contradictions`: list of `Contradiction`.
- `unknowns`: list of `UnknownBoundary`.
- `source_health`: `SourceHealthSummary`.
- `next_monitoring_actions`: list of `NextMonitoringAction`.
- `consumer_state`: `ConsumerState`.
- `quality`: `PacketQuality`.
- `lineage`: `PacketLineage`.

No top-level string field may carry a business conclusion without proof references or a stated missing-proof boundary.

## Core Types

### RunIdentity

Required fields:

- `run_id`
- `generated_at`
- `started_at`, optional
- `completed_at`, optional
- `hermes_job_id`, optional
- `hermes_profile`, optional
- `package_commit`
- `package_release_id`, optional
- `package_sha256`, optional
- `produced_by_user`: expected `cios` for production paths
- `source`: `hermes_cron`, `manual_forced`, `local_test`, or `unknown`

Rule:

- A public packet may not claim `current` unless `run_id`, `generated_at`, `package_commit`, and production execution source are known.

### TimeWindow

Required fields:

- `label`: `today`, `7d`, `30d`, `monthly`, `weekly`, or `custom`
- `start_at`
- `end_at`
- `comparison_start_at`, optional
- `comparison_end_at`, optional
- `grain`: `daily`, `weekly`, `monthly`, or `custom`
- `movement_basis`: `new`, `rising`, `cooling`, `persistent`, `quiet_verified`, or `unknown`

Rule:

- Consumers must display the time window near every promoted movement or recommendation.
- A weekly packet must identify pattern formation across the window, not re-title a daily brief.

### PacketStatus

Allowed statuses:

- `actionable`: enough evidence exists to promote at least one named-owner recommendation.
- `watch`: meaningful movement exists, but action is withheld by missing evidence, confidence, or scoring gates.
- `quiet_verified`: required sources were checked and no material movement qualified.
- `degraded`: the packet exists but source failures, stale inputs, missing demand, or runtime issues materially reduce trust.
- `blocked`: CI-OS could not produce a trustworthy packet for a known reason.
- `failed`: run or packet generation failed.
- `stale`: last successful packet is older than the accepted freshness window.

Rule:

- `watch` plus `can_recommend=true` is invalid unless at least one recommendation is marked `monitoring_only`.
- `stale` may wrap a prior packet for display, but consumers must disclose freshness before any recommendation.

### ExecutiveRead

Required fields:

- `headline`
- `plain_read`
- `why_it_matters_to_algolia`
- `market_belief_implied`
- `what_may_happen_next`
- `decision_posture`: `act`, `watch`, `wait_for_proof`, `quiet`, `investigate`, or `blocked`
- `primary_movement_id`, optional
- `primary_recommendation_id`, optional
- `proof_ref_ids`
- `confidence_ref_ids`

Rule:

- This is the user-facing story. It must be short enough for Telegram and strong enough to anchor the dashboard first screen.

### EvidencePlane

Allowed planes:

- `product_reality`
- `market_conversation`
- `audience_demand`
- `source_health`
- `learning_memory`

Required fields:

- `plane`
- `status`: `present`, `partial`, `missing`, `stale`, `failed`, or `not_required`
- `summary`
- `signal_count`
- `evidence_count`
- `coverage`
- `proof_ref_ids`
- `confidence_impact`

Rule:

- Audience Demand is tenant-side audience response, not competitor proof.
- Missing Audience Demand can block action promotion, but it does not erase outward market movement.

### MarketMovement

Required fields:

- `movement_id`
- `label`
- `summary`
- `movement_type`: `product`, `positioning`, `demand`, `partnership`, `customer_proof`, `executive_narrative`, `analyst`, `pricing`, `platform`, or `mixed`
- `direction`: `rising`, `cooling`, `steady`, `new`, `quiet`, or `unknown`
- `velocity`: `high`, `medium`, `low`, or `unknown`
- `materiality`: `high`, `medium`, `low`, or `unknown`
- `time_window`
- `entities`
- `capabilities`
- `themes`
- `evidence_plane_refs`
- `proof_ref_ids`
- `contradiction_ref_ids`
- `unknown_ref_ids`
- `recommendation_ref_ids`
- `field_graph_ref_id`

Rule:

- A Market Field hotspot must represent a `MarketMovement`, not a decorative cluster or arbitrary list item.

### PacketRecommendation

Required fields:

- `recommendation_id`
- `owner`: `PMM`, `Product`, `Sales`, `Content`, `Executive`, `Partner`, or `Operator`
- `action`
- `why_now`
- `expected_outcome`
- `urgency`
- `confidence`
- `priority_rank`
- `status`: `open`, `accepted`, `dismissed`, `monitoring_only`, or `blocked`
- `movement_ref_ids`
- `proof_ref_ids`
- `scorecard`
- `next_review_at`

Rule:

- A recommendation cannot be promoted unless it references at least one movement, one scorecard, and one proof ref or explicit accepted proof boundary.

### BlockedAction

Required fields:

- `blocked_action_id`
- `owner`
- `proposed_action`
- `blocked_reason`
- `needed_evidence`
- `next_monitoring_action_ref_ids`
- `movement_ref_ids`

Rule:

- The UI must show blocked actions as useful restraint, not as empty failure.

### ProofGraph

Required fields:

- `nodes`: list of `ProofNode`
- `edges`: list of `ProofEdge`
- `root_claim_ids`

Allowed node types:

- `source_event`
- `claim`
- `signal`
- `move`
- `pattern`
- `implication`
- `recommendation`
- `evidence_plane`
- `unknown`
- `contradiction`
- `source_health`

Allowed edge types:

- `supports`
- `weakens`
- `contradicts`
- `depends_on`
- `derived_from`
- `limits_confidence`
- `requires_monitoring`

Rule:

- Every promoted headline, movement, recommendation, weekly pattern, and Market Field hotspot must trace to this graph.

### ConsumerState

Required fields:

- `telegram_daily`: `ConsumerRunState`
- `telegram_weekly`: `ConsumerRunState`
- `dashboard`: `ConsumerRunState`
- `market_field`: `ConsumerRunState`
- `evidence_lab`: `ConsumerRunState`
- `admin`: `ConsumerRunState`
- `public_status`: `ConsumerRunState`

Each `ConsumerRunState` includes:

- `status`: `rendered`, `sent`, `published`, `skipped`, `failed`, `blocked`, `stale`, or `not_applicable`
- `run_id`
- `packet_id`
- `artifact_url`, optional
- `artifact_path`, optional
- `delivery_id`, optional
- `rendered_at`, optional
- `error`, optional

Rule:

- Consumers must never claim a different run than the packet. If they are stale, failed, or skipped, the state must say so.

### PacketQuality

Required fields:

- `quality_review_status`
- `freshness_status`
- `redaction_status`
- `source_coverage_status`
- `run_identity_status`
- `consumer_parity_status`
- `known_failures`
- `residual_risks`

Rule:

- Public display must prefer an honest degraded packet over a confident stale packet.

## Consumer Contract

### Telegram Daily

Must render:

- headline
- status
- time window
- primary movement
- why it matters
- named-owner action or blocked action
- top proof link or dashboard deep link
- freshness and failure disclosure

Must not render:

- raw source walls
- dashboard-only field names
- ambiguous errors as if they are intelligence

### Telegram Weekly

Must render:

- weekly pattern formation
- what rose, cooled, persisted, or stayed quiet
- owner action or watch posture
- proof and same-run dashboard link

Must not render:

- daily recap with a weekly title
- stale weekly rows from a prior date without disclosure

### Dashboard

Must render:

- Market Field or executive read first, but only from packet movements
- selected movement
- decision layer
- proof drawer
- confidence and source-health disclosure
- time-window controls that change packet view or query

Must not render:

- independent business reads built from raw tables
- admin/run diagnostics in the first-read journey
- unknown feature comparisons as broken product truth

### 3D Market Field

Must render from:

- `market_movements`
- `proof_graph`
- `evidence_planes`
- `recommendations`
- `unknowns`
- `contradictions`

Visual semantics:

- node type means durable object type
- edge type means evidence relationship
- size means materiality or total signal weight
- brightness means freshness
- pulse means new movement in selected window
- trail means change over time
- warning ring means confidence limitation
- halo means hotspot

Must not:

- animate without semantic purpose
- use graph nodes that cannot trace back to packet ids

### Evidence Lab

Must render:

- proof graph
- claim chain
- source URLs
- contradiction and weakening evidence
- unknowns
- failed sources and confidence impact

Must not:

- become the primary business read

### Admin

Must render:

- Hermes schedule status
- queue status
- packet freshness
- production execution user
- source registry health
- delivery ledger
- publication status
- release/package identity

Must not:

- create intelligence conclusions outside the packet

### Public Status

Must render:

- packet id
- run id
- status
- generated time
- freshness state
- published consumers and failures
- current recommendation count from the packet, not from an independent dashboard fragment

## Mapping From Current Code

| Current object | Contract role |
|---|---|
| `ProductMarketIntelligenceBrief` | upstream synthesis component and compatibility adapter |
| `ArgusDecisionRead` | feeds `executive_read`, `recommendations`, `blocked_actions`, `evidence_planes` |
| `MarketMovementMap` | feeds `market_movements` and time-window movement state |
| `PatternObservation` | feeds `market_movements` and proof graph pattern nodes |
| `Recommendation` / `argus_recommendations` | feeds `recommendations` |
| `EvidenceRef` | feeds proof nodes and source-event refs |
| `IntelligenceSpine` | dashboard adapter generated from packet |
| `MarketFieldState` | dashboard / 3D adapter generated from packet |
| `semantic-dashboard.json` | consumer artifact, not canonical source |
| `argus-latest-run-status.json` | public status consumer artifact |
| `reports` and `bot_deliveries` | delivery truth for `consumer_state` |
| Hermes cron job state | runtime evidence for Admin and packet lineage |

## Required Contract Tests

Create tests before implementation:

1. `tests/intelligence/test_argus_packet_contract.py`
   - `test_packet_requires_run_identity_and_time_window`
   - `test_actionable_packet_requires_recommendation_proof_and_scorecard`
   - `test_watch_packet_blocks_action_when_audience_demand_missing`
   - `test_quiet_verified_requires_checked_source_coverage`
   - `test_degraded_packet_discloses_source_failures_and_freshness`
   - `test_packet_rejects_consumer_run_id_drift`
   - `test_packet_carries_contradictions_unknowns_and_rejected_reads`

2. `tests/intelligence/test_argus_packet_adapter.py`
   - `test_product_market_brief_maps_into_packet_without_losing_existing_fields`
   - `test_decision_read_maps_status_action_blockers_and_confidence_basis`
   - `test_movement_map_maps_heat_cells_into_market_movements`
   - `test_recommendation_rows_map_to_packet_recommendations`

3. `tests/dashboard/test_packet_consumers.py`
   - `test_dashboard_state_is_generated_from_packet`
   - `test_market_field_hotspots_reference_packet_movements`
   - `test_public_status_recommendation_count_comes_from_packet`
   - `test_latest_json_cannot_publish_stale_packet_as_current`

4. `tests/delivery/test_packet_telegram_format.py`
   - `test_daily_telegram_brief_uses_packet_headline_action_and_proof`
   - `test_weekly_telegram_brief_uses_weekly_pattern_not_daily_recap`
   - `test_failed_packet_renders_failure_not_fake_intelligence`

5. `tests/scenarios/test_argus_packet_scenarios.py`
   - actionable day
   - quiet verified day
   - degraded day
   - contradiction day
   - stale evidence day
   - missing demand day
   - weekly trend day
   - noisy duplicate day

## Phase 1 Exit Gate

This phase can pass only when:

- Arijit approves this packet contract or requests changes.
- Contract tests are added before implementation.
- The tests either fail for missing `ArgusIntelligencePacket` behavior or explicitly prove equivalent existing behavior.
- No runtime repair, Telegram implementation, dashboard rebuild, 3D implementation, Evidence Lab, Admin, or production deployment has started before this gate.

## Immediate Next Step After Approval

Start Phase 2 by adding deterministic scenario fixtures and failing contract/scenario tests in the CI-OS repo. Then implement only enough packet code to satisfy the contract and scenario harness.
