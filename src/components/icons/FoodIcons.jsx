import React from "react";

export function KhueVanCacIcon({ className = "", size = 24, color = "currentColor" }) {
  // Iconic pavilion architecture of Khue Van Cac (Van Mieu)
  return (
    <svg className={className} width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round">
      {/* Top roof */}
      <path d="M2 7l10-4 10 4M4 7l8-2 8 2" />
      {/* Upper chamber with circle window */}
      <rect x="7" y="7" width="10" height="6" rx="0.5" />
      <circle cx="12" cy="10" r="1.6" />
      {/* Lower roof */}
      <path d="M1 13h22" />
      {/* Pillars */}
      <line x1="6" y1="13" x2="6" y2="21" />
      <line x1="9" y1="13" x2="9" y2="21" />
      <line x1="15" y1="13" x2="15" y2="21" />
      <line x1="18" y1="13" x2="18" y2="21" />
      {/* Base */}
      <line x1="4" y1="21" x2="20" y2="21" />
    </svg>
  );
}

export function NoodleIcon({ size = 20, color = "currentColor" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M3 12c0 5 4 8 9 8s9-3 9-8H3z" />
      <path d="M3 12h18" />
      {/* Steam / Noodles */}
      <path d="M7 8V5c0-1 1-1 1-2" />
      <path d="M12 8V4c0-1 1-1 1-2" />
      <path d="M17 8V5c0-1 1-1 1-2" />
      {/* Chopsticks */}
      <line x1="14" y1="2" x2="21" y2="6" />
    </svg>
  );
}

export function GrilledIcon({ size = 20, color = "currentColor" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <line x1="4" y1="20" x2="20" y2="4" />
      <circle cx="9" cy="15" r="2.5" fill={color} fillOpacity="0.2" />
      <circle cx="15" cy="9" r="2.5" fill={color} fillOpacity="0.2" />
      <path d="M5 22l-2-2" />
    </svg>
  );
}

export function BanhMiIcon({ size = 20, color = "currentColor" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <ellipse cx="12" cy="12" rx="10" ry="5" transform="rotate(-25 12 12)" />
      <line x1="7" y1="13" x2="10" y2="10" />
      <line x1="11" y1="15" x2="14" y2="12" />
      <line x1="15" y1="17" x2="17" y2="14" />
    </svg>
  );
}

export function CoffeeIcon({ size = 20, color = "currentColor" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M17 8h1a4 4 0 0 1 0 8h-1" />
      <path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V8z" />
      <line x1="6" y1="2" x2="6" y2="4" />
      <line x1="10" y1="2" x2="10" y2="4" />
      <line x1="14" y1="2" x2="14" y2="4" />
    </svg>
  );
}

export function RiceIcon({ size = 20, color = "currentColor" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M4 11c0 5 3.5 8 8 8s8-3 8-8H4z" />
      <path d="M6 11c0-3 2.5-6 6-6s6 3 6 6" />
      <line x1="12" y1="2" x2="12" y2="5" />
    </svg>
  );
}

export function DessertIcon({ size = 20, color = "currentColor" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 12h14l-2 8H7l-2-8z" />
      <path d="M5 12a7 7 0 0 1 14 0" />
      <circle cx="12" cy="5" r="1.5" />
    </svg>
  );
}

export function RollIcon({ size = 20, color = "currentColor" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <rect x="4" y="6" width="16" height="12" rx="6" />
      <line x1="10" y1="6" x2="10" y2="18" strokeDasharray="2 2" />
      <line x1="14" y1="6" x2="14" y2="18" strokeDasharray="2 2" />
    </svg>
  );
}

export function DefaultFoodIcon({ size = 20, color = "currentColor" }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <circle cx="12" cy="12" r="9" />
      <path d="M8 12h8" />
      <path d="M12 8v8" />
    </svg>
  );
}

export function getCategoryIconComponent(catKey, props = {}) {
  switch (catKey) {
    case "noodle_soup":
      return <NoodleIcon {...props} />;
    case "grilled":
      return <GrilledIcon {...props} />;
    case "sandwich":
      return <BanhMiIcon {...props} />;
    case "drink":
      return <CoffeeIcon {...props} />;
    case "rice":
      return <RiceIcon {...props} />;
    case "sweet_soup":
      return <DessertIcon {...props} />;
    case "rolled":
      return <RollIcon {...props} />;
    default:
      return <DefaultFoodIcon {...props} />;
  }
}

