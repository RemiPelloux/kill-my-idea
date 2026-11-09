# Security

## Reporting

Please report security issues privately via [GitHub security advisories](https://github.com/RemiPelloux/kill-my-idea/security/advisories/new), not in public issues.

## Threat model

kill-my-idea reads web pages by design, so **everything in a report is treated as untrusted**.

| Layer | Protection |
|---|---|
| Skills | Fetched content is data, never instructions. No invented URLs. The skills never publish, buy, sign up or contact anyone. A self-check runs before files are written. |
| `report.html` | Every data string is escaped. Links are limited to `http(s)`. Tooltips are plain text (`textContent`). Numbers and enums are checked when the data loads. Strings and lists are capped. |
| Content-Security-Policy | Only the pinned inline script (sha256) and `report-data.js` can run. No network calls except fonts, no forms, no `<base>`. |
| Errors | Malformed data shows an error card, never a blank page. |

### Known limitation

`report-data.js` is written by the model as JavaScript (`window.KMI_DATA = {...};`), because browsers can't load a JSON file from `file://`. If a model were manipulated into writing code instead of a data literal, that code would run in the report page. The skill's self-check requires a single data statement. Before opening a report built from sources you don't trust, check that `report-data.js` starts with `window.KMI_DATA = {` and contains nothing else.

## Maintainers

After any change to `skills/kill/report.html`, run `python3 scripts/update-csp.py` to re-pin the script hash. Otherwise the page refuses to run its own script.
