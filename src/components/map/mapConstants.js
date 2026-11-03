export const VAN_MIEU_COORDS = [105.835953, 21.02879]; // [lng, lat]
export const VAN_MIEU_NAME = "Văn Miếu – Quốc Tử Giám";
export const VAN_MIEU_ADDRESS = "58 Phố Quốc Tử Giám, Văn Miếu, Đống Đa, Hà Nội";

export const MAP_DEFAULT_CENTER = VAN_MIEU_COORDS;
export const MAP_DEFAULT_ZOOM = 14.8;
export const MAP_MIN_ZOOM = 10;
export const MAP_MAX_ZOOM = 19;
export const SURVEY_RADIUS_METERS = 2000;
export const VENUE_MIN_ZOOM = 14.0; // Hide restaurant markers below this zoom level

export const HANOI_BBOX = [105.2889615, 20.5645154, 106.0200407, 21.3854176]; // [minLng, minLat, maxLng, maxLat]

// MapTiler key from DeepCulture v2
export const MAPTILER_KEY = "3YkDyiBlRz2j0AucReR8";

export const BASEMAP_STYLES = {
  maptiler: {
    id: "maptiler",
    name: "Đường phố (MapTiler Streets)",
    style: `https://api.maptiler.com/maps/streets-v2/style.json?key=${MAPTILER_KEY}`
  },
  esri: {
    id: "esri",
    name: "Đường phố HD (Esri World)",
    style: {
      version: 8,
      sources: {
        "esri-tiles": {
          type: "raster",
          tiles: [
            "https://services.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}"
          ],
          tileSize: 256,
          attribution: "© Esri, DeLorme, NAVTEQ"
        }
      },
      layers: [
        {
          id: "esri-tiles-layer",
          type: "raster",
          source: "esri-tiles",
          minzoom: 0,
          maxzoom: 20
        }
      ]
    }
  },
  topo: {
    id: "topo",
    name: "Địa hình (MapTiler Topo)",
    style: `https://api.maptiler.com/maps/topo-v2/style.json?key=${MAPTILER_KEY}`
  },
  basic: {
    id: "basic",
    name: "Tối giản (MapTiler Basic)",
    style: `https://api.maptiler.com/maps/basic-v2/style.json?key=${MAPTILER_KEY}`
  }
};
