// The shape of src/props.json, written by scripts/build-kit.py from build/plan.json.
// Every text here is plain data: React renders it as text, never as HTML or code.

export type SceneKind = "hook" | "problem" | "stat" | "product" | "proof" | "cta";

export type Scene = {
  kind: SceneKind;
  duration_s: number;
  text: string;
  sub?: string;
  stat?: number;
  stat_suffix?: string;
};

export type Brand = {
  name: string;
  tagline: string;
  colors: { bg: string; fg: string; accent: string; muted: string };
};

export type Ad = {
  id: string;
  width: number;
  height: number;
  hook: string;
  headline: string;
  cta: string;
  proof?: string;
};

export type Props = {
  brand: Brand;
  motion: { width: number; height: number; fps: number; scenes: Scene[] };
  ads: Ad[];
};
