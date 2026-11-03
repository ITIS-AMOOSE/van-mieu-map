// Haversine formula to calculate distance between two coordinates in meters
export function getDistanceMeters(lat1, lon1, lat2, lon2) {
  const R = 6371e3; // metres
  const phi1 = (lat1 * Math.PI) / 180;
  const phi2 = (lat2 * Math.PI) / 180;
  const deltaPhi = ((lat2 - lat1) * Math.PI) / 180;
  const deltaLambda = ((lon2 - lon1) * Math.PI) / 180;

  const a =
    Math.sin(deltaPhi / 2) * Math.sin(deltaPhi / 2) +
    Math.cos(phi1) * Math.cos(phi2) * Math.sin(deltaLambda / 2) * Math.sin(deltaLambda / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

  return Math.round(R * c);
}

export function formatDistance(meters) {
  if (meters == null || isNaN(meters)) return "-";
  if (meters < 1000) {
    return `${Math.round(meters)}m`;
  }
  return `${(meters / 1000).toFixed(1)}km`;
}

export function formatPrice(priceVnd) {
  if (!priceVnd) return "Liên hệ";
  return new Intl.NumberFormat("vi-VN").format(priceVnd) + "đ";
}

export function formatPriceRange(min, max) {
  if (!min && !max) return "Đang cập nhật";
  if (min && !max) return `Từ ${formatPrice(min)}`;
  if (!min && max) return `Đến ${formatPrice(max)}`;
  if (min === max) return formatPrice(min);
  return `${(min / 1000).toLocaleString("vi-VN")}k - ${(max / 1000).toLocaleString("vi-VN")}k`;
}

// Generate circular polygon GeoJSON
export function generateGeoJsonCircle(centerLng, centerLat, radiusMeters, points = 64) {
  const coords = [];
  const R = 6378137.0; // Earth radius
  const latRad = (centerLat * Math.PI) / 180;
  const lngRad = (centerLng * Math.PI) / 180;
  const d = radiusMeters / R;

  for (let i = 0; i <= points; i++) {
    const bearing = (2 * Math.PI * i) / points;
    const ptLat = Math.asin(
      Math.sin(latRad) * Math.cos(d) + Math.cos(latRad) * Math.sin(d) * Math.cos(bearing)
    );
    const ptLng =
      lngRad +
      Math.atan2(
        Math.sin(bearing) * Math.sin(d) * Math.cos(latRad),
        Math.cos(d) - Math.sin(latRad) * Math.sin(ptLat)
      );
    coords.push([(ptLng * 180) / Math.PI, (ptLat * 180) / Math.PI]);
  }

  return {
    type: "FeatureCollection",
    features: [
      {
        type: "Feature",
        properties: { radius_m: radiusMeters },
        geometry: {
          type: "Polygon",
          coordinates: [coords]
        }
      }
    ]
  };
}

