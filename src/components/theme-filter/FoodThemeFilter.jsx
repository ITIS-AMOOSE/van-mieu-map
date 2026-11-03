import React from "react";
import styles from "./FoodThemeFilter.module.css";

export default function FoodThemeFilter({
  categories = {},
  activeCategory = "all",
  onSelectCategory,
  placeCountsByCategory = {},
  dishCountsByCategory = {},
  viewMode = "places",
}) {
  const allCount = viewMode === "places" 
    ? Object.values(placeCountsByCategory).reduce((a, b) => a + b, 0)
    : Object.values(dishCountsByCategory).reduce((a, b) => a + b, 0);

  return (
    <div className={styles.filterContainer}>
      <div className={styles.filterScroll}>
        <button
          type="button"
          className={`${styles.filterChip} ${activeCategory === "all" ? styles.active : ""}`}
          onClick={() => onSelectCategory("all")}
        >
          <span className={styles.icon}>✨</span>
          <span className={styles.label}>Tất cả</span>
          <span className={styles.badge}>{allCount}</span>
        </button>

        {Object.entries(categories).map(([key, meta]) => {
          const count = viewMode === "places" ? (placeCountsByCategory[key] || 0) : (dishCountsByCategory[key] || 0);
          if (count === 0) return null;

          return (
            <button
              key={key}
              type="button"
              className={`${styles.filterChip} ${activeCategory === key ? styles.active : ""}`}
              onClick={() => onSelectCategory(key)}
            >
              <span className={styles.icon}>{meta.icon}</span>
              <span className={styles.label}>{meta.label}</span>
              <span className={styles.badge}>{count}</span>
            </button>
          );
        })}
      </div>
    </div>
  );
}

