# Decisions (ADRs)

## ADR-001: Stack is Node.js stdlib + Retell + Open Dental
- **Context:** One solo developer, 10 h/week, a $2,000 budget, and PHI on calls.
- **Decision:** Retell handles voice under its self-serve BAA. A Node 22 stdlib webhook service handles booking logic.
- **Consequences:** No framework and no dependencies, so the code stays small. We depend on Retell's pricing and on its BAA terms.

## ADR-002: Hosting is AWS EC2 under the AWS BAA
- **Context:** Booking data is PHI. Lightsail is not HIPAA-eligible.
- **Decision:** Run a small EC2 instance with encrypted EBS, and sign the AWS BAA in AWS Artifact.
- **Consequences:** About $20/month. We handle patching and backups ourselves.

## ADR-003: Build the fixed idea, not the original
- **Context:** The original scored PIVOT 56. Fix projects 60 with Open Dental-native booking, no contract and missed-call audit outreach.
- **Decision:** Build the fix path. It is Open Dental-only at $199/month, month to month.
- **Consequences:** The market is smaller (Open Dental practices only), but there is one specific difference and booking is cheap to integrate. Dentrix is out of scope.
