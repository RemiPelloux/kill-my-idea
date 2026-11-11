import React from "react";
import {
  AbsoluteFill,
  Easing,
  Sequence,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import type { Brand, Scene } from "./types";

const FONT = "Inter, 'Helvetica Neue', Arial, sans-serif";

// Fade and lift in at the start of a scene, fade out over its last 8 frames.
const useSceneOpacity = (durationInFrames: number) => {
  const frame = useCurrentFrame();
  return interpolate(frame, [0, 8, durationInFrames - 8, durationInFrames], [0, 1, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
};

// Words appear one after another, each with a spring.
const Words: React.FC<{ text: string; size: number; color: string; delay?: number }> = ({
  text,
  size,
  color,
  delay = 0,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <div style={{ display: "flex", flexWrap: "wrap", gap: size * 0.28, justifyContent: "center" }}>
      {text.split(/\s+/).map((word, i) => {
        const s = spring({ frame: frame - delay - i * 3, fps, config: { damping: 200 } });
        return (
          <span
            key={i}
            style={{
              fontSize: size,
              fontWeight: 800,
              color,
              lineHeight: 1.1,
              opacity: s,
              transform: `translateY(${(1 - s) * 40}px)`,
              display: "inline-block",
            }}
          >
            {word}
          </span>
        );
      })}
    </div>
  );
};

const Sub: React.FC<{ text?: string; color: string; delay: number }> = ({ text, color, delay }) => {
  const frame = useCurrentFrame();
  if (!text) return null;
  const o = interpolate(frame, [delay, delay + 10], [0, 1], { extrapolateRight: "clamp", extrapolateLeft: "clamp" });
  return (
    <div style={{ fontSize: 44, color, opacity: o, marginTop: 40, textAlign: "center", lineHeight: 1.3 }}>{text}</div>
  );
};

// A number that counts up with an ease-out.
const Counter: React.FC<{ to: number; suffix?: string; color: string }> = ({ to, suffix, color }) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [4, 34], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });
  const value = to * t;
  const shown = Number.isInteger(to) ? Math.round(value).toLocaleString("en-US") : value.toFixed(1);
  return (
    <div style={{ fontSize: 220, fontWeight: 900, color, letterSpacing: -6 }}>
      {shown}
      {suffix ?? ""}
    </div>
  );
};

const AccentBar: React.FC<{ color: string }> = ({ color }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const w = spring({ frame, fps, config: { damping: 200 } }) * 180;
  return <div style={{ width: w, height: 14, background: color, borderRadius: 7, marginBottom: 56 }} />;
};

const SceneView: React.FC<{ scene: Scene; brand: Brand; frames: number }> = ({ scene, brand, frames }) => {
  const opacity = useSceneOpacity(frames);
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const c = brand.colors;
  const inverted = scene.kind === "problem" || scene.kind === "cta";
  const bg = inverted ? c.accent : c.bg;
  const fg = inverted ? c.bg : c.fg;
  const zoom = interpolate(frame, [0, frames], [1, 1.04]);

  let body: React.ReactNode;
  if (scene.kind === "stat" && typeof scene.stat === "number") {
    body = (
      <>
        <Counter to={scene.stat} suffix={scene.stat_suffix} color={c.accent} />
        <Words text={scene.text} size={64} color={fg} delay={10} />
      </>
    );
  } else if (scene.kind === "cta") {
    const pop = spring({ frame: frame - 12, fps, config: { damping: 12 } });
    body = (
      <>
        <div style={{ fontSize: 96, fontWeight: 900, color: fg, marginBottom: 40 }}>{brand.name}</div>
        <Words text={scene.text} size={72} color={fg} />
        <div
          style={{
            marginTop: 72,
            padding: "28px 64px",
            borderRadius: 999,
            background: c.bg,
            color: c.fg,
            fontSize: 48,
            fontWeight: 800,
            transform: `scale(${pop})`,
          }}
        >
          {scene.sub ?? brand.tagline}
        </div>
      </>
    );
  } else {
    body = (
      <>
        {scene.kind !== "problem" && <AccentBar color={c.accent} />}
        <Words text={scene.text} size={scene.kind === "hook" ? 110 : 84} color={fg} />
        <Sub text={scene.sub} color={inverted ? c.bg : c.muted} delay={14} />
      </>
    );
  }

  return (
    <AbsoluteFill
      style={{
        background: bg,
        fontFamily: FONT,
        justifyContent: "center",
        alignItems: "center",
        padding: 96,
        opacity,
        transform: `scale(${zoom})`,
      }}
    >
      {body}
    </AbsoluteFill>
  );
};

// A thin bar along the bottom that fills over the whole video, and the brand name in the corner.
const Chrome: React.FC<{ brand: Brand }> = ({ brand }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  return (
    <AbsoluteFill style={{ pointerEvents: "none", fontFamily: FONT }}>
      <div style={{ position: "absolute", top: 64, left: 72, fontSize: 34, fontWeight: 800, color: brand.colors.muted }}>
        {brand.name}
      </div>
      <div
        style={{
          position: "absolute",
          left: 0,
          bottom: 0,
          height: 10,
          width: `${(frame / durationInFrames) * 100}%`,
          background: brand.colors.muted,
          opacity: 0.6,
        }}
      />
    </AbsoluteFill>
  );
};

export const Promo: React.FC<{ brand: Brand; scenes: Scene[] }> = ({ brand, scenes }) => {
  const { fps } = useVideoConfig();
  let from = 0;
  return (
    <AbsoluteFill style={{ background: brand.colors.bg }}>
      {scenes.map((scene, i) => {
        const frames = Math.round(scene.duration_s * fps);
        const start = from;
        from += frames;
        return (
          <Sequence key={i} from={start} durationInFrames={frames}>
            <SceneView scene={scene} brand={brand} frames={frames} />
          </Sequence>
        );
      })}
      <Chrome brand={brand} />
    </AbsoluteFill>
  );
};
