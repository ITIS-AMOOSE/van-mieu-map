import React, { memo } from "react";
import styles from "./FoodMarkerCallout.module.css";
import { KhueVanCacIcon } from "../icons/FoodIcons";

const SCALE = 0.65;
const CARD_H = 54 * SCALE;
const CARD_RX = 12 * SCALE;
const PIN_R = 19 * SCALE;
const PIN_CX = 10 * SCALE + PIN_R;
const PIN_CY = CARD_H / 2;
const TAIL_TIP_Y = CARD_H + 9 * SCALE;
const DOT_R = 2.5 * SCALE;
const DOT_CY = TAIL_TIP_Y + DOT_R * 0.8;
const ANCHOR_X = PIN_CX;
const ANCHOR_Y = DOT_CY + DOT_R;

const TEXT_X = PIN_CX + PIN_R + 10 * SCALE;
const TITLE_Y = 22 * SCALE;
const SUBTITLE_Y = 38 * SCALE;

function truncateText(str, max = 22) {
  if (!str) return "";
  if (str.length <= max) return str;
  return str.slice(0, max - 1) + "…";
}

export const FoodMarkerCallout = memo(function FoodMarkerCallout({
  place,
  isSelected = false,
  isHovered = false,
  isCompact = false,
  onClick,
}) {
  const isVanMieu = place.isCenterLandmark;
  const rating = Math.min(5, Math.max(1, Math.round(place.rating || 5)));
  const title = truncateText(place.name, isVanMieu ? 26 : 22);

  // If in compact mode and not hovered/selected, show clean circular pin
  if (isCompact && !isSelected && !isHovered && !isVanMieu) {
    return (
      <div
        className={`${styles.markerContainer} ${styles.compactPin}`}
        onClick={(e) => {
          e.stopPropagation();
          onClick?.(place);
        }}
        title={`${place.name} (${place.distance_m}m)`}
      >
        <div className={styles.compactCircle}>
          <span className={styles.compactEmoji}>{place.categoryIcon || "🍜"}</span>
        </div>
        <div className={styles.compactDot} />
      </div>
    );
  }

  // Full Expanded Card Callout (Figma Frame 333)
  const subtitle = isVanMieu ? "Tâm điểm khảo sát" : `${place.distance_m}m • ${place.rating || "4.5"}★`;
  const charWidth = 8.5 * SCALE;
  const contentWidth = Math.max(title.length, subtitle.length) * charWidth;
  const cardWidth = Math.max(120 * SCALE, TEXT_X + contentWidth + 18 * SCALE);

  const shadowId = `shadow-${place.place_id || "vm"}`;
  const pinColor = isVanMieu ? "#B91C1C" : isSelected ? "#991B1B" : "#7A1E1E";
  const pinAccent = isVanMieu ? "#F59E0B" : isSelected ? "#EA580C" : "#C2410C";

  return (
    <div
      className={`${styles.markerContainer} ${isSelected ? styles.selected : ""} ${
        isHovered ? styles.hovered : ""
      } ${isVanMieu ? styles.centerLandmark : ""}`}
      onClick={(e) => {
        e.stopPropagation();
        onClick?.(place);
      }}
    >
      {isVanMieu && <div className={styles.pulseRing} />}
      <svg
        className={styles.calloutSvg}
        width={cardWidth + 8}
        height={ANCHOR_Y + 8}
        viewBox={`-${4} -${4} ${cardWidth + 8} ${ANCHOR_Y + 8}`}
        style={{
          transform: `translate(-${ANCHOR_X + 4}px, -${ANCHOR_Y + 4}px)`,
        }}
      >
        <defs>
          <filter id={shadowId} x="-20%" y="-20%" width="140%" height="150%">
            <feDropShadow
              dx="0"
              dy={isSelected ? 4 : 2}
              stdDeviation={isSelected ? 4 : 2.5}
              floodColor="#2B0E0E"
              floodOpacity={isSelected ? 0.28 : 0.16}
            />
          </filter>
        </defs>

        {/* Card pill background */}
        <g filter={`url(#${shadowId})`}>
          <rect
            className={styles.cardBg}
            x="0"
            y="0"
            width={cardWidth}
            height={CARD_H}
            rx={CARD_RX}
            ry={CARD_RX}
            fill={isSelected ? "#FFF5F2" : "#FFFFFF"}
            stroke={isSelected ? "#E11D48" : isVanMieu ? "#D97706" : "#EAD9D4"}
            strokeWidth={isSelected ? 1.8 : 1}
          />
        </g>

        {/* Pin Shape */}
        <path
          d={`M ${PIN_CX - 4.5 * SCALE} ${PIN_CY + PIN_R - 2} L ${PIN_CX} ${TAIL_TIP_Y} L ${
            PIN_CX + 4.5 * SCALE
          } ${PIN_CY + PIN_R - 2} Z`}
          fill={pinColor}
        />
        <circle cx={PIN_CX} cy={PIN_CY} r={PIN_R} fill={pinColor} />
        <circle cx={PIN_CX} cy={DOT_CY} r={DOT_R} fill={pinAccent} />

        {/* Icon in Pin */}
        {isVanMieu ? (
          <g transform={`translate(${PIN_CX - 9}, ${PIN_CY - 9})`}>
            <KhueVanCacIcon size={18} color="#FFFFFF" />
          </g>
        ) : (
          <text
            x={PIN_CX}
            y={PIN_CY + 4.5}
            textAnchor="middle"
            fontSize="12"
            fill="#FFFFFF"
          >
            {place.categoryIcon || "🍜"}
          </text>
        )}

        {/* Title */}
        <text
          x={TEXT_X}
          y={TITLE_Y}
          className={styles.title}
          fill={isVanMieu ? "#991B1B" : "#1F2937"}
          fontSize={11.5 * SCALE + 3}
          fontWeight="600"
        >
          {title}
        </text>

        {/* Subtitle / Stars */}
        {isVanMieu ? (
          <text
            x={TEXT_X}
            y={SUBTITLE_Y}
            fill="#B45309"
            fontSize={10.5 * SCALE + 2}
            fontWeight="600"
          >
            ★ Tâm điểm Văn Miếu
          </text>
        ) : (
          <g>
            <text
              x={TEXT_X}
              y={SUBTITLE_Y}
              fill="#D97706"
              fontSize={10.5 * SCALE + 2}
              fontWeight="600"
            >
              {"★".repeat(rating)}
            </text>
            <text
              x={TEXT_X + rating * 8 + 4}
              y={SUBTITLE_Y}
              fill="#6B7280"
              fontSize={9.5 * SCALE + 2}
              fontWeight="500"
            >
              {place.distance_m ? `${place.distance_m}m` : ""}
            </text>
          </g>
        )}
      </svg>
    </div>
  );
});
