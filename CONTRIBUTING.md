# Contributing

Thanks for helping kill more bad ideas.

## Good contributions

- **New kill shots**: a check that has killed real ideas (add it to `skills/kill/SKILL.md` §3).
- **Country guides**: local competitors, channels, laws or payment habits that change verdicts.
- **Better metrics**: a formula or benchmark, with its source.
- **Real example verdicts**: your own idea, card + sources, in `examples/`.

## Rules

- Every number needs a source, or is labelled *(estimate)* with its reasoning.
- Keep the skills short and readable: they are prompts, so every line costs tokens.
- Test your change locally before opening a PR:

  ```sh
  claude plugin validate .
  claude --plugin-dir .   # then: kill my idea: <something>
  ```

- One change per PR, with a [Conventional Commit](https://www.conventionalcommits.org) title (`feat(kill): add pricing-page kill shot`).
