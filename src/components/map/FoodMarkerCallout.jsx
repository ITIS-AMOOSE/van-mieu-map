import React, { memo } from "react";
import styles from "./FoodMarkerCallout.module.css";
import { KhueVanCacIcon } from "../icons/FoodIcons";

function truncateText(str, max = 22) {
  if (!str) return "";
  if (str.length <= max) return str;
  return str.slice(0, max - 1) + "…";
}

/**
 * ROCK-SOLID ANCHORING:
 * In this design, the absolute coordinate (0, 0) is mathematically the needle tip.
 * - (0, 0) touches the exact GPS coordinate on the map.
 * - When zooming in or out, the needle tip NEVER shifts even by 1 pixel.
 * - When hovering or scaling, transform-origin is (0, 0) so it expands from the anchor point.
 */
export const FoodMarkerCallout = memo(function FoodMarkerCallout({
  place,
  isSelected = false,
  isHovered = false,
  isCompact = false,
  onClick,
}) {
  const isVanMieu = place.isCenterLandmark;
  const rating = Math.min(5, Math.max(1, Math.round(place.rating || 5)));
  const icon = place.categoryIcon || "🍜";

  // 1. VAN MIEU CENTER LANDMARK
  if (isVanMieu) {
    return (
      <div
        className={`${styles.markerWrapper} ${styles.centerLandmark}`}
        onClick={(e) => {
          e.stopPropagation();
          onClick?.(place);
        }}
      >
        {/* Radar Pulse Ring at (0, 0) */}
        <div className={styles.pulseRing} />
        {/* Anchor point ground dot */}
        <div className={styles.anchorDotCenter} />

        <svg
          className={styles.markerSvg}
          width="200"
          height="54"
          viewBox="-16 -46 200 54"
        >
          <defs>
            <filter id="shadow-vm" x="-20%" y="-20%" width="140%" height="150%">
              <feDropShadow dx="0" dy="2" stdDeviation="3" floodColor="#2B0E0E" floodOpacity="0.3" />
            </filter>
          </defs>

          {/* Card Pill attached to the right */}
          <rect
            filter="url(#shadow-vm)"
            x="8"
            y="-42"
            width="170"
            height="32"
            rx="8"
            fill="#FFF5F2"
            stroke="#DC2626"
            strokeWidth="1.8"
          />

          {/* Needle Pin pointing to (0, 0) */}
          <path d="M -4 -16 L 0 0 L 4 -16 Z" fill="#991B1B" />
          <circle cx="0" cy="-26" r="14" fill="#991B1B" stroke="#FFFFFF" strokeWidth="1.5" />
          <circle cx="0" cy="0" r="2.5" fill="#DC2626" />

          {/* Khue Van Cac Icon */}
          <g transform="translate(-9, -35)">
            <KhueVanCacIcon size={18} color="#FFFFFF" />
          </g>

          {/* Texts */}
          <text
            x="24"
            y="-27"
            fontSize="12"
            fontWeight="700"
            fill="#991B1B"
            fontFamily="'Be Vietnam Pro', sans-serif"
          >
            Văn Miếu – Quốc Tử Giám
          </text>
          <text
            x="24"
            y="-15"
            fontSize="10"
            fontWeight="600"
            fill="#B45309"
            fontFamily="'Be Vietnam Pro', sans-serif"
          >
            ★ Tâm điểm khảo sát (0m)
          </text>
        </svg>
      </div>
    );
  }

  // 2. COMPACT MODE (Zoomed out view: Clean teardrop needle pin locked at (0, 0))
  if (isCompact && !isSelected && !isHovered) {
    return (
      <div
        className={`${styles.markerWrapper} ${styles.compactMode}`}
        onClick={(e) => {
          e.stopPropagation();
          onClick?.(place);
        }}
        title={`${place.name} (${place.distance_m}m • ${place.rating}★)`}
      >
        {/* Anchor Ground Dot */}
        <div className={styles.anchorDot} />

        <svg
          className={styles.markerSvg}
          width="32"
          height="38"
          viewBox="-16 -36 32 38"
        >
          <defs>
            <filter id={`sh-c-${place.place_id}`} x="-30%" y="-30%" width="160%" height="160%">
              <feDropShadow dx="0" dy="1.5" stdDeviation="2" floodColor="#2B0E0E" floodOpacity="0.25" />
            </filter>
          </defs>

          {/* Teardrop needle path pointing directly to (0, 0) */}
          <path
            filter={`url(#sh-c-${place.place_id})`}
            d="M 0 0 C -3.5 -6, -13 -13, -13 -21 A 13 13 0 1 1 13 -21 C 13 -13, 3.5 -6, 0 0 Z"
            fill="#7A1E1E"
            stroke="#FFFFFF"
            strokeWidth="1.2"
          />
          {/* Inner white circle */}
          <circle cx="0" cy="-21" r="9.5" fill="#FFFFFF" />
          {/* Food Category Emoji */}
          <text x="0" y="-17.5" textAnchor="middle" fontSize="10.5">
            {icon}
          </text>
          {/* Needle tip dot at (0, 0) */}
          <circle cx="0" cy="0" r="1.5" fill="#DC2626" />
        </svg>
      </div>
    );
  }

  // 3. FULL EXPANDED CALLOUT (Zoomed in or Selected/Hovered)
  const title = truncateText(place.name, 22);
  const subtitleDist = place.distance_m ? `${place.distance_m}m` : "";
  const charWidth = 6.8;
  const cardWidth = Math.max(128, title.length * charWidth + 50);

  const pinColor = isSelected ? "#991B1B" : "#7A1E1E";
  const strokeColor = isSelected ? "#DC2626" : "#EAD9D4";
  const strokeWidth = isSelected ? 1.8 : 1;
  const bg = isSelected ? "#FFF5F2" : "#FFFFFF";

  return (
    <div
      className={`${styles.markerWrapper} ${isSelected ? styles.selected : ""} ${
        isHovered ? styles.hovered : ""
      }`}
      onClick={(e) => {
        e.stopPropagation();
        onClick?.(place);
      }}
    >
      {/* Anchor Ground Dot at (0, 0) */}
      <div className={styles.anchorDot} />

      <svg
        className={styles.markerSvg}
        width={cardWidth + 30}
        height="50"
        viewBox={`-16 -44 ${cardWidth + 30} 50`}
      >
        <defs>
          <filter id={`sh-${place.place_id}`} x="-20%" y="-20%" width="140%" height="150%">
            <feDropShadow
              dx="0"
              dy={isSelected ? 3 : 2}
              stdDeviation={isSelected ? 3.5 : 2.5}
              floodColor="#2B0E0E"
              floodOpacity={isSelected ? 0.3 : 0.18}
            />
          </filter>
        </defs>

        {/* Card Pill attached to the right of pin */}
        <rect
          filter={`url(#sh-${place.place_id})`}
          x="6"
          y="-38"
          width={cardWidth}
          height="30"
          rx="7"
          fill={bg}
          stroke={strokeColor}
          strokeWidth={strokeWidth}
        />

        {/* Needle Pin pointing to (0, 0) */}
        <path d="M -3.5 -14 L 0 0 L 3.5 -14 Z" fill={pinColor} />
        <circle cx="0" cy="-23" r="12" fill={pinColor} stroke="#FFFFFF" strokeWidth="1.2" />
        <circle cx="0" cy="0" r="2" fill="#DC2626" />

        {/* Food Icon inside Pin */}
        <text x="0" y="-19" textAnchor="middle" fontSize="11" fill="#FFFFFF">
          {icon}
        </text>

        {/* Venue Title */}
        <text
          x="19"
          y="-25"
          fontSize="11"
          fontWeight="700"
          fill={isSelected ? "#991B1B" : "#1F2937"}
          fontFamily="'Be Vietnam Pro', sans-serif"
        >
          {title}
        </text>

        {/* Stars Rating and Distance */}
        <text
          x="19"
          y="-14"
          fontSize="10"
          fontWeight="700"
          fill="#D97706"
          fontFamily="'Be Vietnam Pro', sans-serif"
        >
          {"★".repeat(rating)}
        </text>
        <text
          x={19 + rating * 7 + 4}
          y="-14"
          fontSize="9"
          fontWeight="600"
          fill="#6B7280"
          fontFamily="'Be Vietnam Pro', sans-serif"
        >
          {subtitleDist}
        </text>
      </svg>
    </div>
  );
});
