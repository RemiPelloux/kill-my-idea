# Security

## Reporting

Please report security issues privately via [GitHub security advisories](https://github.com/RemiPelloux/kill-my-idea/security/advisories/new), not in public issues.

## Threat model

kill-my-idea reads web pages by design, so **everything in a report is treated as untrusted**.

| Layer | Protection |
|---|---|
| Skills | Fetched content is data, never instructions. No invented URLs. The skills never publish, buy, sign up or contact anyone. A self-check runs before files are written. |
| `report.html` | Every data string is escaped. Links are limited to `http(s)`. Tooltips are plain text (`textContent`). Numbers and enums are checked when the data loads. Strings and lists are capped. |
| Report data (1.0+) | The model writes `report-data.json`, plain data. `scripts/build-report.py` embeds it in `report.html` as an inert `application/json` block, with every `<` escaped. The page runs no code written by the model. |
| Content-Security-Policy | Only the pinned inline script (sha256) can run (plus `report-data.js` in the no-Bash fallback and in pre-1.0 reports). No network calls except fonts, no forms, no `<base>`. |
| Errors | Malformed data shows an error card, never a blank page. |
| `scripts/check-idea.py` | Checks that `report.html` embeds exactly `report-data.json` and no longer loads `report-data.js`. In the fallback, refuses a `report-data.js` that is not a single `window.KMI_DATA = {...};` literal in strict JSON or that contains a `<script` tag. Rejects any non-`http(s)` URL. |

### Known limitation (fallback only)

Since 1.0 the default report contains no script written by the model. Two cases still use
`report-data.js`, which the browser runs: the fallback when Bash isn't available, and reports
made before 1.0. If a model were manipulated into writing code instead of a data literal, that
code would run in the report page. `scripts/check-idea.py` refuses anything but one strict JSON
data statement, and `python3 scripts/migrate.py --json ideas/<folder>` moves an old folder to the
inert format. Before opening such a report from sources you don't trust, check that
`report-data.js` starts with `window.KMI_DATA = {` and contains nothing else.

## Maintainers

After any change to `skills/kill/report.html`, run `python3 scripts/update-csp.py` to re-pin the script hash. Otherwise the page refuses to run its own script.
