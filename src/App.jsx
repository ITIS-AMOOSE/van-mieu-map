import React, { useState, useMemo, useCallback } from "react";
import styles from "./App.module.css";
import FoodMapLibre from "./components/map/FoodMapLibre";
import LeftPanel from "./components/left-panel/LeftPanel";
import FoodDetailSheet from "./components/detail-sheet/FoodDetailSheet";
import foodMapData from "./data/foodMapData.json";
import { VAN_MIEU_COORDS } from "./components/map/mapConstants";

export default function App() {
  const { metadata, category_meta, places, dishes, hanoi_boundary, survey_circle } = foodMapData;

  // Filter & Search states
  const [searchQuery, setSearchQuery] = useState("");
  const [activeCategory, setActiveCategory] = useState("all");
  const [distanceFilter, setDistanceFilter] = useState("all");
  const [ratingFilter, setRatingFilter] = useState("all");
  const [sortBy, setSortBy] = useState("distance");
  const [viewMode, setViewMode] = useState("places"); // 'places' | 'dishes'

  // Selection states
  const [selectedPlace, setSelectedPlace] = useState(null);
  const [selectedDish, setSelectedDish] = useState(null);
  const [hoveredPlaceId, setHoveredPlaceId] = useState(null);
  const [isDetailOpen, setIsDetailOpen] = useState(false);

  // Filtered places
  const filteredPlaces = useMemo(() => {
    return places
      .filter((place) => {
        // Search query
        if (searchQuery.trim()) {
          const q = searchQuery.toLowerCase().trim();
          const matchName = place.name.toLowerCase().includes(q);
          const matchAddr = place.address.toLowerCase().includes(q);
          const matchDishes = (place.dishes || []).some(
            (d) =>
              d.dish_name_vi.toLowerCase().includes(q) ||
              (d.dish_name_en && d.dish_name_en.toLowerCase().includes(q)) ||
              (d.menu_item_name_vi && d.menu_item_name_vi.toLowerCase().includes(q))
          );
          if (!matchName && !matchAddr && !matchDishes) return false;
        }

        // Category filter
        if (activeCategory !== "all") {
          const hasCategory =
            place.primary_category === activeCategory ||
            (place.dishes || []).some((d) => d.category === activeCategory);
          if (!hasCategory) return false;
        }

        // Distance filter
        if (distanceFilter !== "all") {
          const maxDist = parseFloat(distanceFilter);
          if (place.distance_m > maxDist) return false;
        }

        // Rating filter
        if (ratingFilter !== "all") {
          const minRating = parseFloat(ratingFilter);
          if ((place.rating || 0) < minRating) return false;
        }

        return true;
      })
      .sort((a, b) => {
        if (sortBy === "distance") {
          return (a.distance_m || 0) - (b.distance_m || 0);
        }
        if (sortBy === "rating") {
          return (b.rating || 0) - (a.rating || 0);
        }
        if (sortBy === "price_asc") {
          return (a.price_min_vnd || 999999) - (b.price_min_vnd || 999999);
        }
        if (sortBy === "name") {
          return a.name.localeCompare(b.name, "vi");
        }
        return 0;
      });
  }, [places, searchQuery, activeCategory, distanceFilter, ratingFilter, sortBy]);

  // Filtered dishes
  const filteredDishes = useMemo(() => {
    return dishes
      .filter((dish) => {
        // Search query
        if (searchQuery.trim()) {
          const q = searchQuery.toLowerCase().trim();
          const matchName = dish.name_vi.toLowerCase().includes(q);
          const matchEn = dish.name_en && dish.name_en.toLowerCase().includes(q);
          const matchDesc = dish.description_vi && dish.description_vi.toLowerCase().includes(q);
          const matchIng = (dish.ingredients || []).some((ing) =>
            ing.name_vi.toLowerCase().includes(q)
          );
          if (!matchName && !matchEn && !matchDesc && !matchIng) return false;
        }

        // Category filter
        if (activeCategory !== "all") {
          if (dish.category !== activeCategory) return false;
        }

        // Distance filter (by min distance of serving places)
        if (distanceFilter !== "all") {
          const maxDist = parseFloat(distanceFilter);
          if (dish.min_distance_m > maxDist) return false;
        }

        return true;
      })
      .sort((a, b) => {
        if (sortBy === "distance") {
          return (a.min_distance_m || 0) - (b.min_distance_m || 0);
        }
        if (sortBy === "name") {
          return a.name_vi.localeCompare(b.name_vi, "vi");
        }
        return 0;
      });
  }, [dishes, searchQuery, activeCategory, distanceFilter, sortBy]);

  // Handle place selection
  const handleSelectPlace = useCallback((place) => {
    setSelectedPlace(place);
    setSelectedDish(null);
    setIsDetailOpen(true);
  }, []);

  // Handle dish selection
  const handleSelectDish = useCallback(
    (dishSummary) => {
      const fullDish = dishes.find((d) => d.dish_id === dishSummary.dish_id) || dishSummary;
      setSelectedDish(fullDish);
      setSelectedPlace(null);
      setIsDetailOpen(true);
    },
    [dishes]
  );

  // Handle closing detail sheet
  const handleCloseDetail = useCallback(() => {
    setIsDetailOpen(false);
  }, []);

  return (
    <div className={styles.appContainer}>
      {/* Left Panel Sidebar */}
      <LeftPanel
        places={filteredPlaces}
        dishes={filteredDishes}
        categoryMeta={category_meta}
        selectedPlace={selectedPlace}
        selectedDish={selectedDish}
        hoveredPlaceId={hoveredPlaceId}
        onSelectPlace={handleSelectPlace}
        onSelectDish={handleSelectDish}
        onHoverPlace={setHoveredPlaceId}
        searchQuery={searchQuery}
        onSearchChange={setSearchQuery}
        activeCategory={activeCategory}
        onSelectCategory={setActiveCategory}
        distanceFilter={distanceFilter}
        onDistanceFilterChange={setDistanceFilter}
        ratingFilter={ratingFilter}
        onRatingFilterChange={setRatingFilter}
        sortBy={sortBy}
        onSortByChange={setSortBy}
        viewMode={viewMode}
        onViewModeChange={setViewMode}
        onRecenterVanMieu={() => {
          setSelectedPlace({
            place_id: "CENTER_VAN_MIEU",
            name: "Văn Miếu – Quốc Tử Giám",
            isCenterLandmark: true,
            lat: VAN_MIEU_COORDS[1],
            lng: VAN_MIEU_COORDS[0],
            distance_m: 0,
            rating: 5.0,
          });
          setIsDetailOpen(true);
        }}
      />

      {/* Main Interactive Map Viewport */}
      <main className={styles.mapContainer}>
        <FoodMapLibre
          places={filteredPlaces}
          selectedPlace={selectedPlace}
          hoveredPlaceId={hoveredPlaceId}
          onSelectPlace={handleSelectPlace}
          isDetailOpen={isDetailOpen}
          hanoiBoundaryGeoJson={hanoi_boundary}
          surveyCircleGeoJson={survey_circle}
          categoryMeta={category_meta}
        />
      </main>

      {/* Slide-in Detail Drawer / Popup Sheet */}
      {isDetailOpen && (
        <FoodDetailSheet
          place={selectedPlace}
          dish={selectedDish}
          onClose={handleCloseDetail}
          onSelectPlace={handleSelectPlace}
          onSelectDish={handleSelectDish}
          categoryMeta={category_meta}
        />
      )}
    </div>
  );
}

