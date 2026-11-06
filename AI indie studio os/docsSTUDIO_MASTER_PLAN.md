# AI Indie Studio OS — Master Build Instruction

## Mission

Build an AI-driven operating system for a multi-product indie studio.

The studio creates and monetizes:

- Websites and Micro SaaS
    
- B2B SaaS and AI products
    
- Mobile applications
    
- Steam indie games
    
- Roblox experiences
    

Codex is the central natural-language orchestrator.

The owner defines business goals, approves critical decisions, controls spending and authorizes releases. AI agents handle research, planning, development, testing, launch preparation, marketing drafts, analytics and continuous improvement.

The goal is a reusable, evidence-driven business operating system, not merely a collection of prompts.

## 1. Non-negotiable principles

1. Inspect the repository, current files, available tools and existing project conventions before changing anything.
    
2. Never claim that a feature, integration, automation or test works without verification.
    
3. Ask concise clarification questions when missing information materially affects outcomes.
    
4. Do not repeat questions answered in project documents.
    
5. Make small, reversible technical decisions autonomously.
    
6. Delegate independent tasks to specialized agents when supported.
    
7. Prevent concurrent agents from modifying the same files without coordination.
    
8. Require explicit approval for production releases, paid services, financial commitments, external communications, destructive actions, sensitive-data changes and important legal decisions.
    
9. Maintain research sources, assumptions, decisions, test results, costs and handoff records.
    
10. Use the simplest implementation that satisfies the requirements.
    
11. Do not confuse hypothetical demand, estimated revenue or AI-generated research with verified business results.
    
12. Prefer reusable infrastructure without prematurely building unnecessary frameworks.
    

## 2. Global workflow

Implement a stateful product lifecycle:

DISCOVER  
→ IDEATE  
→ RESEARCH  
→ VALIDATE  
→ DECIDE  
→ PLAN  
→ DESIGN  
→ BUILD  
→ VERIFY  
→ LAUNCH  
→ ACQUIRE  
→ MONETIZE  
→ MEASURE  
→ OPTIMIZE  
→ LEARN

Every stage must define:

- Input requirements
    
- Responsible agent
    
- Tools and dependencies
    
- Expected artifacts
    
- Quality and evidence requirements
    
- Approval requirements
    
- Success and failure conditions
    
- Next possible states
    

Support HOLD, PIVOT and ARCHIVE states.

Do not automatically advance through validation or approval gates without sufficient evidence.

## 3. Orchestrator

Implement a Director/Orchestrator that:

- Parses natural-language requests
    
- Loads relevant studio and project context
    
- Identifies ambiguities and dependencies
    
- Chooses a product-type workflow
    
- Generates a task plan
    
- Assigns specialist responsibilities
    
- Executes safe, independent tasks in parallel when available
    
- Tracks status and artifacts
    
- Checks acceptance criteria
    
- Requests approval at critical gates
    
- Produces concise Korean progress and completion reports
    

Keep the orchestrator lightweight.

## 4. Specialist roles

Design reusable role instructions for:

- Research Analyst
    
- Venture Strategist
    
- Product Manager
    
- UX / Art Director
    
- Software Engineer
    
- Game Producer
    
- Game Engineer
    
- QA / Security Reviewer
    
- Release Manager
    
- Growth Marketer
    
- Finance / Analytics
    
- Learning Agent
    

Roles are logical responsibilities. Only create separate runtime agents when they provide measurable value.

## 5. Product strategies

Create separate strategy documents for:

1. Micro SaaS and utility websites
    
2. B2B and AI SaaS
    
3. Mobile applications
    
4. Steam indie games
    
5. Roblox games
    

Each strategy must include customer validation, MVP scope, platform requirements, pricing or monetization assumptions, launch checklist, acquisition channels and success metrics.

## 6. Research and idea system

Create an Idea Factory that:

- Collects customer problems and market signals
    
- Records source URLs and research dates
    
- Compares existing alternatives
    
- Generates differentiated product hypotheses
    
- Scores opportunities using explicit criteria
    
- Identifies unknowns requiring customer research
    
- Saves ideas in a structured backlog
    
- Recommends VALIDATE / HOLD / REJECT outcomes
    

Never fabricate market size, search volume, conversion rates, customer interviews or revenue.

## 7. Product delivery

For approved concepts:

- Create PRD or GDD
    
- Define scope and acceptance criteria
    
- Generate a task dependency graph
    
- Prepare design references and systems
    
- Implement the smallest useful version
    
- Run automated tests
    
- Perform visual and usability review
    
- Perform security and performance checks
    
- Produce release notes
    
- Prepare launch artifacts
    
- Request production approval
    

For games, verify actual gameplay and engine integration. A mockup alone is not a playable game.

## 8. Growth and monetization

Prepare reusable workflows for:

- Landing-page experiments
    
- SEO research and content drafts
    
- Launch announcements
    
- X and community content drafts
    
- App-store and Steam-store assets
    
- Customer feedback categorization
    
- Activation and retention analysis
    
- Pricing experiments
    
- Revenue and operating-cost reports
    

External publishing, customer messages and payment changes require the appropriate approvals.

## 9. Learning and self-improvement

Implement:

- Lazy Genius Senior: avoid unnecessary complexity
    
- Agent Manual: maintain verified operating knowledge
    
- Mistake Notebook: record reproduced failures and verified fixes
    
- Decision Log: preserve significant decisions
    
- Evidence Store: retain test, research and release records
    

Do not add a global rule solely because one mistake occurred.

Only promote a lesson to reusable policy after confirming its cause, correction and relevance.

## 10. Repository structure

Create a maintainable Studio OS repository containing:

- Root AGENTS.md
    
- Studio configuration
    
- Role instructions
    
- Reusable Skills with SKILL.md
    
- Product-type strategies
    
- Research and product templates
    
- Product registry
    
- Shared components
    
- Operating documentation
    
- Workflow scripts
    
- GitHub Actions where appropriate
    

Treat products as separate deployable repositories where appropriate.

## 11. Automation infrastructure

Assess available tools before integration.

Prefer the existing GitHub, Codex, Vercel and project-specific development workflow where practical.

Design:

- Manual task triggers
    
- Scheduled triggers
    
- GitHub event triggers
    
- Task state persistence
    
- Idempotent execution
    
- Retry and failure policies
    
- Budget limits
    
- Audit logs
    
- Approval gates
    
- Rollback procedures
    

Never state that a scheduled or autonomous process is running until it has actually been configured and tested.

## 12. Initial deliverables

First produce:

1. Current environment and repository assessment
    
2. Architecture proposal with risks and trade-offs
    
3. Studio repository scaffold
    
4. Root AGENTS.md
    
5. Minimum viable agent roles
    
6. Market research Skill
    
7. Idea scoring and validation workflow
    
8. Product planning Skill
    
9. Development and QA workflow
    
10. Approval and release policy
    
11. A sample end-to-end workflow using one hypothetical product
    
12. Test evidence and a prioritized next-task list
    

Start with the smallest useful implementation. Do not build a complete management dashboard before the core workflow is verified.

## 13. Reporting format

Respond in Korean using:

- Objective
    
- Current stage
    
- Completed work
    
- Evidence and test results
    
- Open risks
    
- Decisions requiring approval
    
- Recommended next actions
    

Clearly distinguish IMPLEMENTED, VERIFIED, PLANNED and BLOCKED.

## 14. Start now

Inspect the current environment and available integrations.

Create an implementation plan and begin building the safe, local Studio OS foundation.

Do not initiate paid services, public releases, destructive changes or external customer communications without authorization.

Use this instruction as the project bootstrap specification, then maintain concise operational rules in AGENTS.md and detailed procedures in specialized Skills.