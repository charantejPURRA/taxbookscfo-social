# TaxBooks.CFO Marketing Operating System — v1

## Mandate

Build a measurable marketing machine for TaxBooks.CFO and OCTA.

Primary commercial objectives:
1. Build authority with U.S. business owners and finance decision-makers.
2. Generate qualified conversations for CFO services and financial diligence.
3. Build awareness and qualified demand for OCTA.
4. Turn social performance into a feedback loop that improves future content.

Primary channel: LinkedIn.
Secondary distribution: Instagram and Facebook.
LinkedIn should receive the highest-quality, most opinionated version. Instagram/Facebook should be adaptations, not copy-pastes.

## Positioning

Core territory:

> Financial intelligence for business owners who want to know what can go wrong before it becomes expensive.

TaxBooks.CFO should sound like an institutional finance advisor, not a marketing agency or generic accounting firm.

OCTA is the software/product layer.
CFO services are the operating/advisory layer.
Financial diligence is the transaction-risk layer.

Do not make every post promotional.

## Priority audiences

Tier 1:
- Owner-led SMB / lower-middle-market CEOs
- CFOs / controllers
- CPA and accounting firms
- M&A advisors / business brokers

Tier 2:
- Lenders / commercial bankers
- Search funds / PE professionals
- Investment bankers / transaction advisors

## Editorial pillars

1. CASH — liquidity, cash runway, cash conversion, working capital
2. PROFITABILITY — EBITDA, margins, profit quality, EBITDA-to-cash
3. RISK — concentration, leverage, DSCR, Z-score, weak controls, warning signals
4. TRANSACTION READINESS — QoE, diligence, working-capital peg, buyer scrutiny, lender readiness
5. OWNER DECISIONS — growth, hiring, capex, debt, pricing, exit readiness
6. FINANCE INTELLIGENCE — rates, credit, M&A and macro events only when they change an owner's decision

## Content mix

Default 7-post weekly mix:
- 2 cash/profit education
- 1 risk/warning signal
- 1 transaction/diligence insight
- 1 owner decision framework
- 1 current-market interpretation
- 1 commercial/offer post

Commercial posts should normally be <15% of total output.

## Signature formats

A. The Number That Should Make an Owner Look Twice
B. Profit vs. Cash
C. What the Buyer Sees
D. What the Lender Sees
E. Before You Sign the Deal
F. CFO Monday
G. One-Minute Financial Check

## Post construction

Every LinkedIn post should normally follow:

HOOK
→ BUSINESS CONSEQUENCE
→ FINANCIAL MECHANISM
→ PRACTICAL TEST / FRAMEWORK
→ DECISION
→ LOW-FRICTION CTA

Avoid:
- generic motivational language
- empty engagement bait
- fake urgency
- excessive hashtags
- repeated "TaxBooksCFO helps..." endings
- saying the same idea three times across networks
- unsupported statistics
- invented client results

## Platform rules

LinkedIn:
- Highest editorial quality.
- Strong POV.
- Usually one primary idea.
- Use a document/image when it materially improves comprehension.
- Prefer comments/conversation over hard selling.

Instagram:
- Visual-first.
- Shorter caption.
- Strong save/share utility.
- Convert frameworks into clean single graphics or carousels.

Facebook:
- Practical owner language.
- Shorter copy.
- Community/value orientation.
- Do not simply paste the LinkedIn version.

## Cadence

Do not optimize for maximum volume.

Default:
- LinkedIn Page: 5–7 quality posts/week.
- Instagram: 5–7 adapted posts/week.
- Facebook: 3–5 adapted posts/week.

The agent must detect already-scheduled content before adding new content and enforce a no-duplicate window.

## Distribution timing

Use Metricool's account/network timing data when available.

Do not hard-code a universal "best time".
The system should compare:
- historical performance by day
- historical performance by hour
- post format
- topic/pillar
- audience/network

Then choose the next slot.

## Learning loop

For every published post, store:

- network
- publication timestamp
- pillar
- format
- hook type
- CTA type
- media type
- topic
- impressions
- reactions
- comments
- shares
- clicks
- follower change
- engagement rate where available

Calculate a normalized score rather than optimizing raw likes.

Recommended score:

Content Score =
40% normalized impressions
+ 25% normalized comments
+ 15% normalized shares
+ 10% normalized clicks
+ 10% follower gain

For commercial posts, add a separate Conversion Score:
- profile/page visits
- link clicks
- inbound messages
- qualified conversations
- booked calls
- attributable opportunities

Never allow a high-engagement entertainment post to automatically outrank a lower-reach post that generates qualified demand.

## Weekly decision engine

Every week the agent should answer:

1. Which three topics performed best?
2. Which three hooks performed best?
3. Which format performed best?
4. Which audience signals appeared?
5. Which posts generated commercial intent?
6. What should we publish more of?
7. What should we stop?
8. What should we test next week?

The next week's content plan must be generated from these answers.

## Guardrails

Before scheduling:
- reject duplicate ideas inside the configured lookback window
- reject unsupported factual claims
- reject excessive promotional density
- reject generic AI-sounding copy
- reject repeated hooks
- reject platform-inappropriate formatting
- verify every external link
- require media for Instagram image/video posts
- preserve alt text
- keep LinkedIn within platform limits

## Current strategic correction

The current local agent can already generate and schedule content across LinkedIn, Instagram and Facebook, and it falls back to the local model when Gemini is unavailable. That reliability is good.

The next version should NOT be a larger content generator.

It should become a closed-loop Marketing OS:

RESEARCH
→ STRATEGY
→ CONTENT PLAN
→ GENERATE
→ QUALITY CONTROL
→ SCHEDULE
→ MEASURE
→ SCORE
→ LEARN
→ NEXT PLAN

The scheduler is the last step, not the product.

## Human approval policy

Default automation:
- research: automatic
- content planning: automatic
- drafting: automatic
- quality control: automatic
- scheduling: automatic for normal educational content
- commercial claims / major campaigns: hold for approval
- deleting or materially rewriting already-published content: never automatic

## Executive KPI dashboard

Track weekly:

Awareness:
- followers
- impressions
- unique reach where available

Authority:
- comments per 1,000 impressions
- shares per 1,000 impressions
- saves where available
- repeat engagers

Demand:
- profile/page visits
- website clicks
- inbound DMs
- qualified conversations
- booked calls

Commercial:
- CFO opportunities
- diligence opportunities
- OCTA trials/signups
- attributable revenue

The north-star metric is NOT follower count.

North star:
**qualified financial conversations generated per 1,000 impressions.**
