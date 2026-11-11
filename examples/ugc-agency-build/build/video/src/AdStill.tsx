import React from "react";
import { AbsoluteFill } from "remotion";
import type { Ad, Brand } from "./types";

const FONT = "Inter, 'Helvetica Neue', Arial, sans-serif";

// One static ad image. Sizes scale with the shorter side, so 1:1, 9:16 and 1.91:1 all work.
export const AdStill: React.FC<{ brand: Brand; ad: Ad }> = ({ brand, ad }) => {
  const c = brand.colors;
  const unit = Math.min(ad.width, ad.height) / 1080;
  const wide = ad.width / ad.height > 1.5;
  return (
    <AbsoluteFill
      style={{
        background: c.bg,
        fontFamily: FONT,
        padding: 80 * unit,
        justifyContent: "space-between",
        flexDirection: "column",
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: 20 * unit }}>
        <div style={{ width: 28 * unit, height: 28 * unit, borderRadius: 8 * unit, background: c.accent }} />
        <div style={{ fontSize: 40 * unit, fontWeight: 800, color: c.fg }}>{brand.name}</div>
      </div>

      <div>
        <div
          style={{
            fontSize: (wide ? 78 : 96) * unit,
            fontWeight: 900,
            color: c.fg,
            lineHeight: 1.05,
            letterSpacing: -2 * unit,
          }}
        >
          {ad.hook}
        </div>
        <div style={{ width: 160 * unit, height: 12 * unit, background: c.accent, margin: `${44 * unit}px 0` }} />
        <div style={{ fontSize: 46 * unit, color: c.muted, lineHeight: 1.3 }}>{ad.headline}</div>
      </div>

      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end", gap: 40 * unit }}>
        <div style={{ fontSize: 30 * unit, color: c.muted, maxWidth: "60%", lineHeight: 1.35 }}>{ad.proof ?? ""}</div>
        <div
          style={{
            background: c.accent,
            color: c.bg,
            fontSize: 40 * unit,
            fontWeight: 800,
            padding: `${24 * unit}px ${48 * unit}px`,
            borderRadius: 999,
            whiteSpace: "nowrap",
          }}
        >
          {ad.cta}
        </div>
      </div>
    </AbsoluteFill>
  );
};
