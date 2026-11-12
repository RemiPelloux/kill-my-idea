import React from "react";
import { Composition, Still } from "remotion";
import data from "./props.json";
import { AdStill } from "./AdStill";
import { Promo } from "./Promo";
import type { Props } from "./types";

const props = data as Props;
const { fps, width, height, scenes } = props.motion;
const frames = scenes.reduce((sum, s) => sum + Math.round(s.duration_s * fps), 0);

export const Root: React.FC = () => (
  <>
    <Composition
      id="Promo"
      component={Promo}
      durationInFrames={frames}
      fps={fps}
      width={width}
      height={height}
      defaultProps={{ brand: props.brand, scenes }}
    />
    {props.ads.map((ad) => (
      <Still
        key={ad.id}
        id={`Ad-${ad.id}`}
        component={AdStill}
        width={ad.width}
        height={ad.height}
        defaultProps={{ brand: props.brand, ad }}
      />
    ))}
  </>
);
