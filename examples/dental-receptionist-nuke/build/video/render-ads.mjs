// Renders one PNG per ad in src/props.json: out/ads/<id>.png
import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";

const props = JSON.parse(readFileSync(new URL("./src/props.json", import.meta.url), "utf8"));
for (const ad of props.ads) {
  const out = `out/ads/${ad.id}.png`;
  execFileSync("npx", ["remotion", "still", `Ad-${ad.id}`, out], { stdio: "inherit" });
}
