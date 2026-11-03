import React, { useEffect, useRef, useState, useCallback, useMemo } from "react";
import { createRoot } from "react-dom/client";
import maplibregl from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";
import styles from "./FoodMapLibre.module.css";
import { FoodMarkerCallout } from "./FoodMarkerCallout";
import {
  VAN_MIEU_COORDS,
  VAN_MIEU_NAME,
  VAN_MIEU_ADDRESS,
  MAP_DEFAULT_CENTER,
  MAP_DEFAULT_ZOOM,
  MAP_MIN_ZOOM,
  MAP_MAX_ZOOM,
  SURVEY_RADIUS_METERS,
  VENUE_MIN_ZOOM,
  BASEMAP_STYLES,
  HANOI_BBOX
} from "./mapConstants";
import { generateGeoJsonCircle } from "./mapGeoUtils";
import { KhueVanCacIcon } from "../icons/FoodIcons";

export default function FoodMapLibre({
  places = [],
  selectedPlace = null,
  hoveredPlaceId = null,
  onSelectPlace,
  isDetailOpen = false,
  hanoiBoundaryGeoJson = null,
  surveyCircleGeoJson = null,
  categoryMeta = {},
}) {
  const mapContainerRef = useRef(null);
  const mapRef = useRef(null);
  const markersRef = useRef([]);
  const centerMarkerRef = useRef(null);

  const [mapReady, setMapReady] = useState(false);
  const [activeStyleKey, setActiveStyleKey] = useState("maptiler");
  const [showSurveyZone, setShowSurveyZone] = useState(true);
  const [showHanoiBoundary, setShowHanoiBoundary] = useState(true);
  const [currentZoom, setCurrentZoom] = useState(MAP_DEFAULT_ZOOM);

  // Initialize MapLibre
  useEffect(() => {
    if (!mapContainerRef.current) return;

    if (mapRef.current) {
      try {
        mapRef.current.remove();
      } catch (err) {
        console.warn("Map removal error:", err);
      }
      mapRef.current = null;
    }

    const selectedStyle = BASEMAP_STYLES[activeStyleKey]?.style || BASEMAP_STYLES.maptiler.style;

    const map = new maplibregl.Map({
      container: mapContainerRef.current,
      style: selectedStyle,
      center: MAP_DEFAULT_CENTER,
      zoom: MAP_DEFAULT_ZOOM,
      minZoom: MAP_MIN_ZOOM,
      maxZoom: MAP_MAX_ZOOM,
      attributionControl: false,
    });

    map.on("load", () => {
      setMapReady(true);
      setCurrentZoom(map.getZoom());
    });

    map.on("zoom", () => {
      setCurrentZoom(Math.round(map.getZoom() * 10) / 10);
    });

    mapRef.current = map;

    return () => {
      markersRef.current.forEach((m) => {
        try {
          m._reactRoot?.unmount();
          m.remove();
        } catch (e) {}
      });
      markersRef.current = [];
      if (centerMarkerRef.current) {
        try {
          centerMarkerRef.current._reactRoot?.unmount();
          centerMarkerRef.current.remove();
        } catch (e) {}
        centerMarkerRef.current = null;
      }
      if (mapRef.current) {
        try {
          mapRef.current.remove();
        } catch (e) {}
        mapRef.current = null;
      }
    };
  }, [activeStyleKey]);

  // Handle ResizeObserver
  useEffect(() => {
    const map = mapRef.current;
    const container = mapContainerRef.current;
    if (!map || !container) return;

    const resizeObserver = new ResizeObserver(() => {
      map.resize();
    });
    resizeObserver.observe(container);

    return () => resizeObserver.disconnect();
  }, [mapReady]);

  // Add GeoJSON boundary layers
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady) return;

    // 1. Hanoi Boundary
    if (hanoiBoundaryGeoJson) {
      if (!map.getSource("hanoi-boundary-src")) {
        map.addSource("hanoi-boundary-src", {
          type: "geojson",
          data: hanoiBoundaryGeoJson,
        });

        map.addLayer({
          id: "hanoi-boundary-fill",
          type: "fill",
          source: "hanoi-boundary-src",
          paint: {
            "fill-color": "#7A1E1E",
            "fill-opacity": 0.03,
          },
        });

        map.addLayer({
          id: "hanoi-boundary-line",
          type: "line",
          source: "hanoi-boundary-src",
          paint: {
            "line-color": "#7A1E1E",
            "line-width": 1.5,
            "line-opacity": 0.55,
            "line-dasharray": [3, 2],
          },
        });
      }
    }

    // 2. Survey Circle (2km) & Rings (500m, 1000m)
    const circleData = surveyCircleGeoJson || generateGeoJsonCircle(VAN_MIEU_COORDS[0], VAN_MIEU_COORDS[1], SURVEY_RADIUS_METERS);
    const ring500Data = generateGeoJsonCircle(VAN_MIEU_COORDS[0], VAN_MIEU_COORDS[1], 500);
    const ring1000Data = generateGeoJsonCircle(VAN_MIEU_COORDS[0], VAN_MIEU_COORDS[1], 1000);

    if (!map.getSource("survey-circle-src")) {
      map.addSource("survey-circle-src", {
        type: "geojson",
        data: circleData,
      });

      map.addLayer({
        id: "survey-circle-fill",
        type: "fill",
        source: "survey-circle-src",
        paint: {
          "fill-color": "#D97706",
          "fill-opacity": 0.04,
        },
      });

      map.addLayer({
        id: "survey-circle-line",
        type: "line",
        source: "survey-circle-src",
        paint: {
          "line-color": "#B45309",
          "line-width": 2,
          "line-opacity": 0.75,
          "line-dasharray": [4, 3],
        },
      });
    }

    if (!map.getSource("survey-rings-src")) {
      map.addSource("survey-rings-src", {
        type: "geojson",
        data: {
          type: "FeatureCollection",
          features: [...ring500Data.features, ...ring1000Data.features],
        },
      });

      map.addLayer({
        id: "survey-rings-line",
        type: "line",
        source: "survey-rings-src",
        paint: {
          "line-color": "#D97706",
          "line-width": 1,
          "line-opacity": 0.35,
          "line-dasharray": [2, 3],
        },
      });
    }
  }, [mapReady, hanoiBoundaryGeoJson, surveyCircleGeoJson]);

  // Toggle layer visibility
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady) return;

    const hanoiVis = showHanoiBoundary ? "visible" : "none";
    if (map.getLayer("hanoi-boundary-fill")) {
      map.setLayoutProperty("hanoi-boundary-fill", "visibility", hanoiVis);
      map.setLayoutProperty("hanoi-boundary-line", "visibility", hanoiVis);
    }

    const zoneVis = showSurveyZone ? "visible" : "none";
    if (map.getLayer("survey-circle-fill")) {
      map.setLayoutProperty("survey-circle-fill", "visibility", zoneVis);
      map.setLayoutProperty("survey-circle-line", "visibility", zoneVis);
      map.setLayoutProperty("survey-rings-line", "visibility", zoneVis);
    }
  }, [mapReady, showSurveyZone, showHanoiBoundary]);

  // Center Landmark Marker (Văn Miếu)
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady) return;

    if (centerMarkerRef.current) {
      centerMarkerRef.current._reactRoot?.unmount();
      centerMarkerRef.current.remove();
      centerMarkerRef.current = null;
    }

    const centerPlace = {
      place_id: "CENTER_VAN_MIEU",
      name: VAN_MIEU_NAME,
      address: VAN_MIEU_ADDRESS,
      isCenterLandmark: true,
      rating: 5.0,
      distance_m: 0,
      categoryIcon: "🏛️",
    };

    const el = document.createElement("div");
    el.style.width = "0px";
    el.style.height = "0px";
    el.style.position = "absolute";
    el.style.overflow = "visible";
    const root = createRoot(el);
    root.render(
      <FoodMarkerCallout
        place={centerPlace}
        isSelected={selectedPlace?.place_id === centerPlace.place_id}
        isCompact={false}
        onClick={() => {
          map.flyTo({
            center: VAN_MIEU_COORDS,
            zoom: 15.5,
            duration: 800,
          });
          onSelectPlace?.(centerPlace);
        }}
      />
    );

    const marker = new maplibregl.Marker({
      element: el,
      anchor: "top-left",
    })
      .setLngLat(VAN_MIEU_COORDS)
      .addTo(map);

    marker._reactRoot = root;
    centerMarkerRef.current = marker;
  }, [mapReady, selectedPlace, onSelectPlace]);

  // Render food venue markers
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady) return;

    // Clean up old markers
    markersRef.current.forEach((m) => {
      try {
        m._reactRoot?.unmount();
        m.remove();
      } catch (e) {}
    });
    markersRef.current = [];

    // When zoomed out far (< VENUE_MIN_ZOOM), hide all restaurant markers (only show Center Van Mieu)
    const showVenues = currentZoom >= VENUE_MIN_ZOOM;

    places.forEach((place) => {
      if (typeof place.lat !== "number" || typeof place.lng !== "number") return;

      const isSelected = selectedPlace?.place_id === place.place_id;
      // If zoomed out, only show if it is actively selected
      if (!showVenues && !isSelected) return;

      const catMeta = categoryMeta[place.primary_category] || {};
      const placeWithMeta = {
        ...place,
        categoryIcon: catMeta.icon || "🍜",
      };

      const isHovered = hoveredPlaceId === place.place_id;

      const el = document.createElement("div");
      el.style.width = "0px";
      el.style.height = "0px";
      el.style.position = "absolute";
      el.style.overflow = "visible";
      const root = createRoot(el);
      root.render(
        <FoodMarkerCallout
          place={placeWithMeta}
          isSelected={isSelected}
          isHovered={isHovered}
          isCompact={false}
          onClick={() => onSelectPlace?.(place)}
        />
      );

      const marker = new maplibregl.Marker({
        element: el,
        anchor: "top-left",
      })
        .setLngLat([place.lng, place.lat])
        .addTo(map);

      marker._reactRoot = root;
      markersRef.current.push(marker);
    });
  }, [mapReady, places, selectedPlace, hoveredPlaceId, categoryMeta, onSelectPlace, currentZoom]);

  // Smooth camera flyTo when a place is selected
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !mapReady || !selectedPlace) return;

    const lng = selectedPlace.lng ?? selectedPlace.lon;
    const lat = selectedPlace.lat;

    if (typeof lng === "number" && typeof lat === "number") {
      const containerWidth = mapContainerRef.current?.clientWidth || 800;
      const rightPadding = isDetailOpen && containerWidth > 768 ? Math.min(420, Math.round(containerWidth * 0.4)) : 40;

      map.flyTo({
        center: [lng, lat],
        zoom: Math.max(map.getZoom(), 16),
        padding: {
          top: 50,
          bottom: 50,
          left: 50,
          right: rightPadding,
        },
        duration: 900,
        essential: true,
      });
    }
  }, [selectedPlace, isDetailOpen, mapReady]);

  // Camera action handlers
  const handleRecenter = useCallback(() => {
    const map = mapRef.current;
    if (!map) return;
    map.flyTo({
      center: VAN_MIEU_COORDS,
      zoom: MAP_DEFAULT_ZOOM,
      duration: 800,
    });
  }, []);

  const handleFitHanoi = useCallback(() => {
    const map = mapRef.current;
    if (!map) return;
    map.fitBounds(
      [
        [HANOI_BBOX[0], HANOI_BBOX[1]],
        [HANOI_BBOX[2], HANOI_BBOX[3]],
      ],
      {
        padding: 50,
        duration: 900,
      }
    );
  }, []);

  const handleZoomIn = () => mapRef.current?.zoomIn({ duration: 300 });
  const handleZoomOut = () => mapRef.current?.zoomOut({ duration: 300 });

  return (
    <div className={styles.mapWrapper}>
      {/* MapLibre container */}
      <div ref={mapContainerRef} className={styles.mapContainer} />

      {/* Top Map Status Banner */}
      <div className={styles.topBanner}>
        <div className={styles.bannerItem}>
          <KhueVanCacIcon size={18} color="#991B1B" />
          <span className={styles.bannerTitle}>Tâm điểm: Văn Miếu Quốc Tử Giám</span>
        </div>
        <div
          className={styles.bannerBadge}
          onClick={() => {
            if (currentZoom < VENUE_MIN_ZOOM) {
              mapRef.current?.flyTo({ center: VAN_MIEU_COORDS, zoom: 15.0, duration: 800 });
            }
          }}
          style={{ cursor: currentZoom < VENUE_MIN_ZOOM ? "pointer" : "default" }}
          title={currentZoom < VENUE_MIN_ZOOM ? "Bấm để phóng to vào vùng quán ăn Văn Miếu" : ""}
        >
          {currentZoom >= VENUE_MIN_ZOOM
            ? `Bán kính 2.0km • ${places.length} quán ăn đang hiển thị`
            : `Bán kính 2.0km • Phóng to gần để xem ${places.length} quán ăn 🔍`}
        </div>
      </div>

      {/* Map Control Buttons */}
      <div className={styles.mapControls}>
        <button
          className={`${styles.controlBtn} ${styles.recenterBtn}`}
          onClick={handleRecenter}
          title="Quay lại trung tâm Văn Miếu"
        >
          <KhueVanCacIcon size={18} color="#991B1B" />
          <span>Văn Miếu</span>
        </button>

        <button
          className={styles.controlBtn}
          onClick={handleFitHanoi}
          title="Xem toàn cảnh thành phố Hà Nội"
        >
          <span>Toàn cảnh Hà Nội</span>
        </button>

        <div className={styles.controlGroup}>
          <button className={styles.iconBtn} onClick={handleZoomIn} title="Phóng to">
            +
          </button>
          <div className={styles.zoomText}>z{currentZoom}</div>
          <button className={styles.iconBtn} onClick={handleZoomOut} title="Thu nhỏ">
            −
          </button>
        </div>
      </div>

      {/* Bottom Floating Layer Switcher */}
      <div className={styles.bottomBar}>
        <div className={styles.layerPills}>
          <button
            className={`${styles.pillBtn} ${showSurveyZone ? styles.pillActive : ""}`}
            onClick={() => setShowSurveyZone(!showSurveyZone)}
          >
            <span className={styles.pillDot} style={{ background: "#D97706" }} />
            Vùng bán kính 2km
          </button>
          <button
            className={`${styles.pillBtn} ${showHanoiBoundary ? styles.pillActive : ""}`}
            onClick={() => setShowHanoiBoundary(!showHanoiBoundary)}
          >
            <span className={styles.pillDot} style={{ background: "#7A1E1E" }} />
            Ranh giới Hà Nội
          </button>
        </div>

        <div className={styles.styleSelector}>
          <label className={styles.styleLabel}>Nền bản đồ:</label>
          <select
            value={activeStyleKey}
            onChange={(e) => setActiveStyleKey(e.target.value)}
            className={styles.styleSelect}
          >
            <option value="maptiler">Đường phố (MapTiler)</option>
            <option value="esri">Đường phố HD (Esri World)</option>
            <option value="basic">Tối giản (MapTiler Basic)</option>
            <option value="topo">Địa hình (MapTiler Topo)</option>
          </select>
        </div>
      </div>
    </div>
  );
}
