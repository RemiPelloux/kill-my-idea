# Rules for an agent building LunchLine

1. **Follow `pelloux-guidelines.md`. This is mandatory.** For every task, write 3 approaches and pick the simplest. Keep files at 300 lines or fewer and functions at 25 lines or fewer. Make only surgical changes. Work in the order Make, Test, Document.
2. Before any work, read `docs/prd.md` and the current sprint in `docs/sprints.md`.
3. Work one story at a time (`docs/user-stories.md`). A story is done only when `docs/definition-of-done.md` passes.
4. Never commit `.env`, keys or any patient data (PHI). Use synthetic patients in tests.
5. Keep the README's Run section true. If you change a command, update the README.
6. Every vendor that touches call audio or patient data must have a signed BAA (Retell, AWS). Do not add OpenAI or Twilio directly without one.
7. Never spend money, publish anything, sign up for anything or contact clinics without the founder's explicit yes.
