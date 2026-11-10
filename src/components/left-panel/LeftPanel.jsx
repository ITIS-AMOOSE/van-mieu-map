import React, { useMemo } from "react";
import styles from "./LeftPanel.module.css";
import FoodThemeFilter from "../theme-filter/FoodThemeFilter";
import { KhueVanCacIcon } from "../icons/FoodIcons";
import { formatPriceRange, formatDistance } from "../map/mapGeoUtils";

export default function LeftPanel({
  places = [],
  dishes = [],
  categoryMeta = {},
  selectedPlace = null,
  selectedDish = null,
  hoveredPlaceId = null,
  onSelectPlace,
  onSelectDish,
  onHoverPlace,
  searchQuery = "",
  onSearchChange,
  activeCategory = "all",
  onSelectCategory,
  distanceFilter = "all",
  onDistanceFilterChange,
  ratingFilter = "all",
  onRatingFilterChange,
  sortBy = "distance",
  onSortByChange,
  viewMode = "places",
  onViewModeChange,
  onRecenterVanMieu,
}) {
  // Category counts
  const placeCountsByCategory = useMemo(() => {
    const counts = {};
    places.forEach((p) => {
      const cat = p.primary_category || "other";
      counts[cat] = (counts[cat] || 0) + 1;
    });
    return counts;
  }, [places]);

  const dishCountsByCategory = useMemo(() => {
    const counts = {};
    dishes.forEach((d) => {
      const cat = d.category || "other";
      counts[cat] = (counts[cat] || 0) + 1;
    });
    return counts;
  }, [dishes]);

  return (
    <aside className={styles.leftPanel}>
      {/* Header & Center Card */}
      <div className={styles.header}>
        <div className={styles.brandRow}>
          <div className={styles.logoBadge}>
            <KhueVanCacIcon size={22} color="#7A1E1E" />
          </div>
          <div className={styles.brandInfo}>
            <h1 className={styles.mainTitle}>Ẩm Thực Văn Miếu</h1>
            <p className={styles.subtitle}>Bản đồ ẩm thực Hà Nội • Data Demo</p>
          </div>
        </div>

        {/* Van Mieu Center Reference Card */}
        <div className={styles.centerCard} onClick={onRecenterVanMieu} title="Bấm để đưa bản đồ về Văn Miếu">
          <div className={styles.centerIcon}>🏛️</div>
          <div className={styles.centerDetails}>
            <div className={styles.centerTitleRow}>
              <span className={styles.centerName}>Văn Miếu – Quốc Tử Giám</span>
              <span className={styles.centerBadge}>Tâm điểm</span>
            </div>
            <p className={styles.centerAddress}>58 Quốc Tử Giám, Đống Đa • Khảo sát bán kính 2km</p>
          </div>
          <div className={styles.recenterIcon}>🎯</div>
        </div>
      </div>

      {/* Search Input */}
      <div className={styles.searchSection}>
        <div className={styles.searchBox}>
          <svg className={styles.searchSvg} viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <circle cx="11" cy="11" r="8" strokeWidth="2" />
            <line x1="21" y1="21" x2="16.65" y2="16.65" strokeWidth="2" strokeLinecap="round" />
          </svg>
          <input
            type="text"
            className={styles.searchInput}
            placeholder="Tìm món ăn, tên quán, con phố, nguyên liệu..."
            value={searchQuery}
            onChange={(e) => onSearchChange(e.target.value)}
          />
          {searchQuery && (
            <button className={styles.clearBtn} onClick={() => onSearchChange("")}>
              ✕
            </button>
          )}
        </div>
      </div>

      {/* View Mode Toggle: Places vs Dishes */}
      <div className={styles.toggleRow}>
        <button
          className={`${styles.toggleBtn} ${viewMode === "places" ? styles.toggleActive : ""}`}
          onClick={() => onViewModeChange("places")}
        >
          <span>📍 Địa điểm quán ăn</span>
          <span className={styles.toggleBadge}>{places.length}</span>
        </button>
        <button
          className={`${styles.toggleBtn} ${viewMode === "dishes" ? styles.toggleActive : ""}`}
          onClick={() => onViewModeChange("dishes")}
        >
          <span>🍲 Danh mục món ăn</span>
          <span className={styles.toggleBadge}>{dishes.length}</span>
        </button>
      </div>

      {/* Theme Filter */}
      <div className={styles.themeSection}>
        <FoodThemeFilter
          categories={categoryMeta}
          activeCategory={activeCategory}
          onSelectCategory={onSelectCategory}
          placeCountsByCategory={placeCountsByCategory}
          dishCountsByCategory={dishCountsByCategory}
          viewMode={viewMode}
        />
      </div>

      {/* Secondary Filter & Sort Toolbar */}
      <div className={styles.toolbar}>
        <div className={styles.filterGroup}>
          <select
            className={styles.selectFilter}
            value={distanceFilter}
            onChange={(e) => onDistanceFilterChange(e.target.value)}
          >
            <option value="all">Khoảng cách: Tất cả (≤2km)</option>
            <option value="500">Trong bán kính 500m</option>
            <option value="1000">Trong bán kính 1.0km</option>
            <option value="1500">Trong bán kính 1.5km</option>
            <option value="2000">Trong bán kính 2.0km</option>
          </select>

          <select
            className={styles.selectFilter}
            value={ratingFilter}
            onChange={(e) => onRatingFilterChange(e.target.value)}
          >
            <option value="all">Đánh giá: Tất cả</option>
            <option value="4.0">Từ 4.0 ★ trở lên</option>
            <option value="4.5">Từ 4.5 ★ trở lên</option>
          </select>
        </div>

        <div className={styles.sortGroup}>
          <label className={styles.sortLabel}>Sắp xếp:</label>
          <select
            className={styles.selectSort}
            value={sortBy}
            onChange={(e) => onSortByChange(e.target.value)}
          >
            <option value="distance">Gần Văn Miếu nhất</option>
            <option value="rating">Đánh giá cao nhất</option>
            <option value="price_asc">Giá từ thấp đến cao</option>
            <option value="name">Tên A-Z</option>
          </select>
        </div>
      </div>

      {/* Results Count Summary */}
      <div className={styles.resultsBar}>
        <span className={styles.resultsCount}>
          Tìm thấy <strong>{viewMode === "places" ? places.length : dishes.length}</strong> kết quả
        </span>
        {activeCategory !== "all" && (
          <button className={styles.resetFilterBtn} onClick={() => onSelectCategory("all")}>
            Xóa bộ lọc danh mục
          </button>
        )}
      </div>

      {/* Main Content List */}
      <div className={styles.listContainer}>
        {viewMode === "places" ? (
          places.length === 0 ? (
            <div className={styles.emptyState}>
              <div className={styles.emptyIcon}>🔍</div>
              <p className={styles.emptyTitle}>Không tìm thấy quán ăn phù hợp</p>
              <p className={styles.emptyDesc}>Hãy thử thay đổi từ khóa hoặc bộ lọc khoảng cách / danh mục.</p>
            </div>
          ) : (
            places.map((place) => {
              const isSelected = selectedPlace?.place_id === place.place_id;
              const isHovered = hoveredPlaceId === place.place_id;
              const catMeta = categoryMeta[place.primary_category] || {};
              const topDish = place.dishes?.[0]?.dish_name_vi || "Món đặc sản";

              return (
                <div
                  key={place.place_id}
                  className={`${styles.itemCard} ${isSelected ? styles.itemSelected : ""} ${
                    isHovered ? styles.itemHovered : ""
                  }`}
                  onClick={() => onSelectPlace(place)}
                  onMouseEnter={() => onHoverPlace?.(place.place_id)}
                  onMouseLeave={() => onHoverPlace?.(null)}
                >
                  <div className={styles.cardThumbWrapper}>
                    <img
                      src={place.image_url}
                      alt={place.name}
                      className={styles.cardThumb}
                      loading="lazy"
                      onError={(e) => {
                        e.target.src = place.online_image_url || "/images/dishes/DISH_001.jpg";
                      }}
                    />
                    <span className={styles.catBadge}>
                      {catMeta.icon || "🍜"} {catMeta.label || "Món ngon"}
                    </span>
                  </div>

                  <div className={styles.cardContent}>
                    <div className={styles.cardTitleRow}>
                      <h3 className={styles.placeName}>{place.name}</h3>
                    </div>

                    <p className={styles.placeAddress}>{place.address}</p>

                    <div className={styles.cardMetaRow}>
                      <span className={styles.distanceBadge}>
                        🧭 {formatDistance(place.distance_m)} từ Văn Miếu
                      </span>
                      <span className={styles.ratingBadge}>
                        ★ {place.rating} ({place.review_count})
                      </span>
                    </div>

                    <div className={styles.cardFooter}>
                      <span className={styles.topDishTag}>Món tiêu biểu: {topDish}</span>
                      <span className={styles.priceTag}>
                        {formatPriceRange(place.price_min_vnd, place.price_max_vnd)}
                      </span>
                    </div>

                    {place.image_source && (
                      <span className={styles.cardSourceText} title={`Nguồn ảnh: ${place.image_source}`}>
                        📷 {place.image_source}
                      </span>
                    )}
                  </div>
                </div>
              );
            })
          )
        ) : (
          dishes.length === 0 ? (
            <div className={styles.emptyState}>
              <div className={styles.emptyIcon}>🍜</div>
              <p className={styles.emptyTitle}>Không tìm thấy món ăn phù hợp</p>
              <p className={styles.emptyDesc}>Hãy thử tìm kiếm món ăn hoặc nguyên liệu khác.</p>
            </div>
          ) : (
            dishes.map((dish) => {
              const isSelected = selectedDish?.dish_id === dish.dish_id;
              const catMeta = categoryMeta[dish.category] || {};

              return (
                <div
                  key={dish.dish_id}
                  className={`${styles.itemCard} ${isSelected ? styles.itemSelected : ""}`}
                  onClick={() => onSelectDish(dish)}
                >
                  <div className={styles.cardThumbWrapper}>
                    <img
                      src={dish.image_url}
                      alt={dish.name_vi}
                      className={styles.cardThumb}
                      loading="lazy"
                      onError={(e) => {
                        e.target.src = dish.online_image_url || "/images/dishes/DISH_001.jpg";
                      }}
                    />
                    <span className={styles.catBadge}>
                      {catMeta.icon || "🍲"} {catMeta.label || "Đặc sản"}
                    </span>
                  </div>

                  <div className={styles.cardContent}>
                    <div className={styles.cardTitleRow}>
                      <h3 className={styles.dishName}>{dish.name_vi}</h3>
                    </div>
                    {dish.name_en && <p className={styles.dishEnName}>{dish.name_en}</p>}

                    <p className={styles.dishDesc}>
                      {dish.short_description_vi || dish.description_vi?.slice(0, 90) + "..."}
                    </p>

                    <div className={styles.cardMetaRow}>
                      <span className={styles.placesCountBadge}>
                        📍 Phục vụ tại {dish.serving_places_count} quán gần Văn Miếu
                      </span>
                      {dish.min_distance_m && dish.min_distance_m < 9999 && (
                        <span className={styles.distanceBadge}>
                          Gần nhất: {formatDistance(dish.min_distance_m)}
                        </span>
                      )}
                    </div>

                    {dish.taste_profile && dish.taste_profile.length > 0 && (
                      <div className={styles.tasteTags}>
                        {dish.taste_profile.map((t, idx) => (
                          <span key={idx} className={styles.tasteTag}>
                            #{t}
                          </span>
                        ))}
                      </div>
                    )}

                    {dish.image_source && (
                      <span className={styles.cardSourceText} title={`Nguồn ảnh: ${dish.image_source}`}>
                        📷 {dish.image_source}
                      </span>
                    )}
                  </div>
                </div>
              );
            })
          )
        )}
      </div>
    </aside>
  );
}

