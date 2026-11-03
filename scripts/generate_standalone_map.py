import json

with open(r'E:\Demo Văn Miếu\src\data\foodMapData.json', encoding='utf-8') as f:
    bundle = json.load(f)

json_data_str = json.dumps(bundle, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bản Đồ Ẩm Thực Văn Miếu - Hà Nội | Demo Data</title>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🍜</text></svg>">
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
  <!-- MapLibre GL JS -->
  <link rel="stylesheet" href="https://unpkg.com/maplibre-gl@5.2.0/dist/maplibre-gl.css" />
  <script src="https://unpkg.com/maplibre-gl@5.2.0/dist/maplibre-gl.js"></script>

  <style>
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    html, body {{
      width: 100%;
      height: 100%;
      overflow: hidden;
      font-family: "Be Vietnam Pro", system-ui, -apple-system, sans-serif;
      background: #fbf7f4;
      color: #1f2937;
    }}
    #app {{
      display: flex;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      position: relative;
    }}

    /* LEFT PANEL */
    .left-panel {{
      width: 430px;
      min-width: 380px;
      max-width: 460px;
      height: 100%;
      background: #ffffff;
      border-right: 1px solid #ebdcd6;
      box-shadow: 2px 0 16px rgba(122, 30, 30, 0.04);
      display: flex;
      flex-direction: column;
      z-index: 30;
      overflow: hidden;
    }}
    .panel-header {{
      padding: 16px 20px 12px;
      background: #fff8f6;
      border-bottom: 1px solid #f2e2dc;
    }}
    .brand-row {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .logo-badge {{
      width: 42px;
      height: 42px;
      border-radius: 12px;
      background: #ffebe5;
      border: 1px solid #f8cfc6;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      flex-shrink: 0;
    }}
    .brand-title {{
      font-family: "Playfair Display", Georgia, serif;
      font-size: 20px;
      font-weight: 700;
      color: #7a1e1e;
      line-height: 1.2;
    }}
    .brand-subtitle {{
      font-size: 12px;
      color: #78716c;
      margin-top: 2px;
    }}
    .center-card {{
      display: flex;
      align-items: center;
      gap: 12px;
      background: #ffffff;
      border: 1px solid #f4d0c8;
      border-radius: 12px;
      padding: 10px 14px;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 0 2px 6px rgba(122, 30, 30, 0.04);
    }}
    .center-card:hover {{
      background: #fff3f0;
      border-color: #e11d48;
      transform: translateY(-1px);
    }}
    .center-card .icon {{ font-size: 22px; }}
    .center-card .meta {{ flex: 1; }}
    .center-card .title {{
      font-size: 13.5px;
      font-weight: 700;
      color: #991b1b;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .center-badge {{
      font-size: 10px;
      background: #fef2f2;
      color: #dc2626;
      padding: 1px 6px;
      border-radius: 9999px;
      border: 1px solid #fecaca;
    }}
    .center-card .addr {{
      font-size: 11.5px;
      color: #78716c;
      margin-top: 2px;
    }}
    .search-box {{
      padding: 12px 20px 8px;
    }}
    .search-input-wrap {{
      display: flex;
      align-items: center;
      gap: 10px;
      background: #fbf7f4;
      border: 1px solid #e7d8d2;
      border-radius: 12px;
      padding: 8px 14px;
      transition: all 0.2s ease;
    }}
    .search-input-wrap:focus-within {{
      border-color: #7a1e1e;
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(122, 30, 30, 0.1);
    }}
    .search-input-wrap input {{
      flex: 1;
      border: none;
      background: transparent;
      outline: none;
      font-size: 13.5px;
      color: #1c1917;
    }}
    .toggle-row {{
      display: flex;
      padding: 0 20px 8px;
      gap: 8px;
    }}
    .toggle-btn {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      background: #f5eeea;
      border: 1px solid transparent;
      border-radius: 10px;
      padding: 8px 10px;
      font-size: 12.5px;
      font-weight: 600;
      color: #57534e;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .toggle-btn.active {{
      background: #ffffff;
      border-color: #e7d5ce;
      color: #7a1e1e;
      font-weight: 700;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    }}
    .toggle-badge {{
      background: #ebdcd6;
      font-size: 11px;
      padding: 1px 6px;
      border-radius: 9999px;
      color: #44403c;
    }}
    .toggle-btn.active .toggle-badge {{
      background: #ffebe5;
      color: #991b1b;
    }}
    .theme-scroll {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding: 0 20px 8px;
      scrollbar-width: thin;
      scrollbar-color: #f1dfd8 transparent;
    }}
    .theme-chip {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #ffffff;
      border: 1px solid #ebdcd6;
      border-radius: 9999px;
      padding: 5px 12px;
      font-size: 12.5px;
      font-weight: 500;
      color: #4b5563;
      white-space: nowrap;
      cursor: pointer;
      transition: all 0.2s ease;
      flex-shrink: 0;
    }}
    .theme-chip:hover {{
      background: #fff5f2;
      border-color: #fca5a5;
      color: #991b1b;
    }}
    .theme-chip.active {{
      background: #7a1e1e;
      border-color: #7a1e1e;
      color: #ffffff;
      font-weight: 600;
    }}
    .toolbar {{
      padding: 8px 20px;
      display: flex;
      gap: 8px;
      background: #faf6f4;
      border-top: 1px solid #f0e4df;
      border-bottom: 1px solid #f0e4df;
    }}
    .toolbar select {{
      flex: 1;
      background: #ffffff;
      border: 1px solid #e2d3cd;
      border-radius: 8px;
      padding: 6px 10px;
      font-size: 12px;
      font-weight: 500;
      color: #44403c;
      outline: none;
      cursor: pointer;
    }}
    .results-bar {{
      padding: 8px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12.5px;
      color: #57534e;
    }}
    .list-container {{
      flex: 1;
      overflow-y: auto;
      padding: 8px 20px 24px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      scrollbar-width: thin;
      scrollbar-color: #ebdcd6 transparent;
    }}
    .card-item {{
      background: #ffffff;
      border: 1px solid #eeddd7;
      border-radius: 14px;
      padding: 12px;
      cursor: pointer;
      display: flex;
      gap: 12px;
      transition: all 0.2s ease;
    }}
    .card-item:hover {{
      border-color: #fca5a5;
      background: #fffafa;
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(122, 30, 30, 0.08);
    }}
    .card-item.selected {{
      border-color: #dc2626 !important;
      background: #fff8f6 !important;
      box-shadow: 0 0 0 2px rgba(220, 38, 38, 0.2), 0 6px 16px rgba(122, 30, 30, 0.12) !important;
    }}
    .card-thumb-wrap {{
      width: 88px;
      height: 88px;
      border-radius: 10px;
      overflow: hidden;
      flex-shrink: 0;
      position: relative;
      background: #f5ede8;
    }}
    .card-thumb {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .card-cat-badge {{
      position: absolute;
      bottom: 4px;
      left: 4px;
      right: 4px;
      background: rgba(0, 0, 0, 0.65);
      color: #fff;
      font-size: 9.5px;
      font-weight: 600;
      padding: 2px 4px;
      border-radius: 4px;
      text-align: center;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .card-info {{
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .card-name {{
      font-size: 14px;
      font-weight: 700;
      color: #1f2937;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .card-addr {{
      font-size: 12px;
      color: #57534e;
      margin: 3px 0 6px;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      line-height: 1.35;
    }}
    .card-badges {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .badge-dist {{
      font-size: 11px;
      font-weight: 600;
      color: #991b1b;
      background: #fef2f2;
      padding: 1px 6px;
      border-radius: 6px;
      border: 1px solid #fecaca;
    }}
    .badge-rate {{
      font-size: 11px;
      font-weight: 700;
      color: #b45309;
      background: #fffbeb;
      padding: 1px 6px;
      border-radius: 6px;
      border: 1px solid #fde68a;
    }}
    .card-foot {{
      display: flex;
      justify-content: space-between;
      border-top: 1px dashed #f0e4df;
      padding-top: 4px;
      margin-top: 4px;
      font-size: 11.5px;
    }}
    .card-dish-tag {{
      color: #78716c;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .card-price-tag {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    /* MAP CONTAINER */
    .map-container {{
      flex: 1;
      height: 100%;
      position: relative;
    }}
    #map {{
      width: 100%;
      height: 100%;
    }}

    /* TOP BANNER */
    .top-banner {{
      position: absolute;
      top: 16px;
      left: 20px;
      z-index: 20;
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      padding: 8px 16px;
      border-radius: 9999px;
      box-shadow: 0 4px 16px rgba(122, 30, 30, 0.1);
      border: 1px solid #f2e7e3;
    }}
    .banner-title {{
      font-size: 13.5px;
      font-weight: 700;
      color: #7a1e1e;
    }}
    .banner-badge {{
      font-size: 12px;
      font-weight: 600;
      color: #b45309;
      background: #fffbeb;
      padding: 2px 10px;
      border-radius: 9999px;
      border: 1px solid #fde68a;
      transition: all 0.2s ease;
    }}
    .banner-badge:hover {{
      background: #fef3c7;
    }}

    /* MAP CONTROLS */
    .map-controls {{
      position: absolute;
      top: 16px;
      right: 20px;
      z-index: 20;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .map-btn {{
      background: #ffffff;
      border: 1px solid #e8ded9;
      border-radius: 10px;
      padding: 8px 12px;
      font-size: 13px;
      font-weight: 600;
      color: #374151;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}
    .map-btn:hover {{
      background: #fff8f6;
      border-color: #f8cfc6;
      color: #7a1e1e;
      transform: translateY(-1px);
    }}
    .zoom-group {{
      display: flex;
      flex-direction: column;
      background: #ffffff;
      border: 1px solid #e8ded9;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }}
    .zoom-btn {{
      width: 36px;
      height: 36px;
      border: none;
      background: transparent;
      font-size: 18px;
      font-weight: 600;
      color: #4b5563;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .zoom-btn:hover {{
      background: #fff5f2;
      color: #7a1e1e;
    }}

    /* BOTTOM BAR */
    .bottom-bar {{
      position: absolute;
      bottom: 16px;
      left: 20px;
      right: 20px;
      z-index: 20;
      display: flex;
      justify-content: space-between;
      align-items: center;
      pointer-events: none;
    }}
    .pill-group {{
      display: flex;
      gap: 8px;
      pointer-events: auto;
    }}
    .pill-btn {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(6px);
      border: 1px solid #e5e7eb;
      padding: 6px 12px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 600;
      color: #4b5563;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);
    }}
    .pill-btn.active {{
      background: #ffffff;
      border-color: #d1d5db;
      color: #111827;
      font-weight: 700;
    }}
    .dot-amber {{ width: 8px; height: 8px; border-radius: 50%; background: #d97706; }}
    .dot-red {{ width: 8px; height: 8px; border-radius: 50%; background: #7a1e1e; }}

    /* ZERO-OFFSET EXACT NEEDLE MARKERS */
    .marker-wrap {{
      position: absolute;
      left: 0;
      top: 0;
      width: 0;
      height: 0;
      cursor: pointer;
      user-select: none;
      transform-origin: 0 0;
      transition: transform 0.28s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .marker-wrap:hover {{
      transform: scale(1.15);
      z-index: 9999 !important;
    }}
    .marker-wrap.active {{
      transform: scale(1.18);
      z-index: 10000 !important;
    }}

    .anchor-dot {{
      position: absolute;
      left: -2px;
      top: -2px;
      width: 4px;
      height: 4px;
      border-radius: 50%;
      background: #7a1e1e;
      opacity: 0.5;
      pointer-events: none;
    }}

    .pulse-ring {{
      position: absolute;
      left: -24px;
      top: -24px;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: rgba(220, 38, 38, 0.25);
      animation: pulse 2s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
      pointer-events: none;
    }}
    @keyframes pulse {{
      0% {{ transform: scale(0.5); opacity: 0.9; }}
      70% {{ transform: scale(2.4); opacity: 0; }}
      100% {{ transform: scale(2.6); opacity: 0; }}
    }}

    /* DETAIL DRAWER */
    .detail-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.4);
      backdrop-filter: blur(2px);
      z-index: 100;
      display: flex;
      justify-content: flex-end;
    }}
    .detail-sheet {{
      width: 480px;
      max-width: 90vw;
      height: 100%;
      background: #ffffff;
      display: flex;
      flex-direction: column;
      box-shadow: -4px 0 24px rgba(0, 0, 0, 0.15);
      animation: slideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      overflow: hidden;
    }}
    @keyframes slideIn {{
      from {{ transform: translateX(100%); }}
      to {{ transform: translateX(0); }}
    }}
    .detail-img-wrap {{
      position: relative;
      width: 100%;
      height: 220px;
      background: #2b0e0e;
    }}
    .detail-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .detail-close {{
      position: absolute;
      top: 14px;
      right: 14px;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.55);
      color: #fff;
      border: none;
      font-size: 14px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .detail-img-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0, 0, 0, 0.85) 0%, rgba(0, 0, 0, 0.2) 60%, transparent 100%);
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
    }}
    .detail-title {{
      font-family: "Playfair Display", Georgia, serif;
      font-size: 22px;
      font-weight: 700;
      color: #ffffff;
    }}
    .detail-sub {{
      font-size: 13px;
      color: #e5e7eb;
      margin-top: 2px;
    }}
    .detail-tabs {{
      display: flex;
      border-bottom: 1px solid #ebdcd6;
      background: #fff8f6;
      padding: 0 12px;
    }}
    .detail-tab {{
      background: transparent;
      border: none;
      border-bottom: 2px solid transparent;
      padding: 12px 14px;
      font-size: 13px;
      font-weight: 600;
      color: #6b7280;
      cursor: pointer;
    }}
    .detail-tab.active {{
      color: #7a1e1e;
      border-bottom-color: #7a1e1e;
    }}
    .detail-body {{
      flex: 1;
      overflow-y: auto;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .detail-box {{
      background: #fbf7f4;
      border: 1px solid #ebdcd6;
      border-radius: 12px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 13px;
    }}
    .btn-maps {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: #7a1e1e;
      color: #ffffff;
      padding: 10px 16px;
      border-radius: 10px;
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 700;
      box-shadow: 0 4px 12px rgba(122, 30, 30, 0.2);
    }}
  </style>
</head>
<body>
  <div id="app">
    <!-- LEFT PANEL -->
    <aside class="left-panel">
      <div class="panel-header">
        <div class="brand-row">
          <div class="logo-badge">🏛️</div>
          <div>
            <h1 class="brand-title">Ẩm Thực Văn Miếu</h1>
            <p class="brand-subtitle">Bản đồ ẩm thực Hà Nội • Demo Data</p>
          </div>
        </div>

        <div class="center-card" id="btn-recenter-card" title="Quay lại Văn Miếu">
          <span class="icon">🏛️</span>
          <div class="meta">
            <div class="title">
              <span>Văn Miếu – Quốc Tử Giám</span>
              <span class="center-badge">Tâm điểm</span>
            </div>
            <p class="addr">58 Quốc Tử Giám • Bán kính khảo sát 2km</p>
          </div>
          <span style="color: #dc2626; font-size: 16px;">🎯</span>
        </div>
      </div>

      <div class="search-box">
        <div class="search-input-wrap">
          <span style="color: #78716c;">🔍</span>
          <input type="text" id="search-input" placeholder="Tìm món ăn, tên quán, con phố, nguyên liệu...">
        </div>
      </div>

      <div class="toggle-row">
        <button class="toggle-btn active" id="btn-view-places">
          <span>📍 Địa điểm quán</span>
          <span class="toggle-badge" id="count-places">70</span>
        </button>
        <button class="toggle-btn" id="btn-view-dishes">
          <span>🍲 Danh mục món</span>
          <span class="toggle-badge" id="count-dishes">50</span>
        </button>
      </div>

      <div class="theme-scroll" id="theme-pills">
        <!-- Rendered by JS -->
      </div>

      <div class="toolbar">
        <select id="select-dist">
          <option value="all">Khoảng cách: Tất cả (≤2km)</option>
          <option value="500">Trong bán kính 500m</option>
          <option value="1000">Trong bán kính 1.0km</option>
          <option value="1500">Trong bán kính 1.5km</option>
          <option value="2000">Trong bán kính 2.0km</option>
        </select>
        <select id="select-sort">
          <option value="distance">Gần Văn Miếu nhất</option>
          <option value="rating">Đánh giá cao nhất</option>
          <option value="name">Tên A-Z</option>
        </select>
      </div>

      <div class="results-bar">
        <span id="results-count-text">Tìm thấy 70 kết quả</span>
      </div>

      <div class="list-container" id="list-items">
        <!-- Items rendered by JS -->
      </div>
    </aside>

    <!-- MAP CONTAINER -->
    <main class="map-container">
      <div id="map"></div>

      <!-- Top Banner -->
      <div class="top-banner">
        <span style="font-size: 16px;">🏛️</span>
        <span class="banner-title">Tâm điểm: Văn Miếu Quốc Tử Giám</span>
        <span class="banner-badge" id="banner-count" style="cursor: pointer;">Bán kính 2.0km • 70 quán ăn</span>
      </div>

      <!-- Map Controls -->
      <div class="map-controls">
        <button class="map-btn" id="btn-recenter" title="Quay lại Văn Miếu">
          <span>🏛️ Văn Miếu</span>
        </button>
        <button class="map-btn" id="btn-fit-hanoi" title="Toàn cảnh Hà Nội">
          <span>Toàn cảnh Hà Nội</span>
        </button>
        <div class="zoom-group">
          <button class="zoom-btn" id="btn-zoom-in">+</button>
          <button class="zoom-btn" id="btn-zoom-out">−</button>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="bottom-bar">
        <div class="pill-group">
          <button class="pill-btn active" id="btn-toggle-circle">
            <span class="dot-amber"></span> Vùng bán kính 2km
          </button>
          <button class="pill-btn active" id="btn-toggle-hanoi">
            <span class="dot-red"></span> Ranh giới Hà Nội
          </button>
        </div>
      </div>
    </main>

    <!-- DETAIL DRAWER -->
    <div id="detail-overlay" class="detail-overlay" style="display: none;">
      <div class="detail-sheet" id="detail-sheet">
        <!-- Rendered by JS -->
      </div>
    </div>
  </div>

  <script>
    const DATA = {json_data_str};
    const VAN_MIEU = [105.835953, 21.02879];
    const VENUE_MIN_ZOOM = 14.0; // Hide restaurant markers when zoom < 14.0

    let currentViewMode = "places";
    let activeCategory = "all";
    let searchQuery = "";
    let distanceFilter = "all";
    let sortBy = "distance";
    let selectedPlaceId = null;
    let markers = [];
    let showCircle = true;
    let showHanoi = true;

    // Use MapTiler Streets vector from DeepCulture v2
    const MAPTILER_KEY = "3YkDyiBlRz2j0AucReR8";
    const map = new maplibregl.Map({{
      container: "map",
      style: `https://api.maptiler.com/maps/streets-v2/style.json?key=${{MAPTILER_KEY}}`,
      center: VAN_MIEU,
      zoom: 14.8,
      minZoom: 10,
      maxZoom: 19,
      attributionControl: false
    }});

    map.on("load", () => {{
      // 1. Add Hanoi Boundary
      if (DATA.hanoi_boundary) {{
        map.addSource("hanoi-src", {{
          type: "geojson",
          data: DATA.hanoi_boundary
        }});
        map.addLayer({{
          id: "hanoi-fill",
          type: "fill",
          source: "hanoi-src",
          paint: {{ "fill-color": "#7A1E1E", "fill-opacity": 0.03 }}
        }});
        map.addLayer({{
          id: "hanoi-line",
          type: "line",
          source: "hanoi-src",
          paint: {{ "line-color": "#7A1E1E", "line-width": 1.5, "line-opacity": 0.5, "line-dasharray": [3, 2] }}
        }});
      }}

      // 2. Add Survey Circle 2000m
      if (DATA.survey_circle) {{
        map.addSource("circle-src", {{
          type: "geojson",
          data: DATA.survey_circle
        }});
        map.addLayer({{
          id: "circle-fill",
          type: "fill",
          source: "circle-src",
          paint: {{ "fill-color": "#D97706", "fill-opacity": 0.04 }}
        }});
        map.addLayer({{
          id: "circle-line",
          type: "line",
          source: "circle-src",
          paint: {{ "line-color": "#B45309", "line-width": 2, "line-opacity": 0.75, "line-dasharray": [4, 3] }}
        }});
      }}

      // 3. Add Center Landmark Marker (Van Mieu)
      addCenterMarker();

      // 4. Render Place Markers
      updateMapMarkers();
    }});

    map.on("zoom", () => {{
      updateMapMarkers();
    }});

    function addCenterMarker() {{
      const el = document.createElement("div");
      el.style.width = "0px";
      el.style.height = "0px";
      el.style.position = "absolute";
      el.innerHTML = `
        <div class="marker-wrap">
          <div class="pulse-ring"></div>
          <svg width="200" height="54" viewBox="-16 -46 200 54" style="position: absolute; left: -16px; top: -46px; width: 200px; height: 54px; overflow: visible;">
            <defs>
              <filter id="vm-shadow" x="-20%" y="-20%" width="140%" height="150%">
                <feDropShadow dx="0" dy="2" stdDeviation="3" floodColor="#2B0E0E" floodOpacity="0.3"/>
              </filter>
            </defs>
            <rect filter="url(#vm-shadow)" x="8" y="-42" width="170" height="32" rx="8" fill="#FFF5F2" stroke="#DC2626" stroke-width="1.8"/>
            <path d="M -4 -16 L 0 0 L 4 -16 Z" fill="#991B1B"/>
            <circle cx="0" cy="-26" r="14" fill="#991B1B" stroke="#FFFFFF" stroke-width="1.5"/>
            <circle cx="0" cy="0" r="3" fill="#DC2626" stroke="#FFFFFF" stroke-width="1"/>
            <text x="0" y="-21" text-anchor="middle" font-size="12" fill="#FFFFFF">🏛️</text>
            <text x="24" y="-27" font-size="12" font-weight="700" fill="#991B1B" font-family="'Be Vietnam Pro', sans-serif">Văn Miếu – Quốc Tử Giám</text>
            <text x="24" y="-15" font-size="10" font-weight="600" fill="#B45309" font-family="'Be Vietnam Pro', sans-serif">★ Tâm điểm khảo sát (0m)</text>
          </svg>
        </div>
      `;
      el.onclick = () => {{
        map.flyTo({{ center: VAN_MIEU, zoom: 15.5, duration: 800 }});
        openVanMieuDetail();
      }};
      new maplibregl.Marker({{ element: el, anchor: "top-left" }})
        .setLngLat(VAN_MIEU)
        .addTo(map);
    }}

    function createMarkerHtml(place, isSelected) {{
      const catMeta = DATA.category_meta[place.primary_category] || {{}};
      const icon = catMeta.icon || "🍜";

      // Full Expanded Callout pointing directly to (0, 0)
      const name = place.name.length > 20 ? place.name.slice(0, 19) + "…" : place.name;
      const dist = place.distance_m ? `${{place.distance_m}}m` : "";
      const rating = Math.min(5, Math.max(1, Math.round(place.rating || 5)));
      const stars = "★".repeat(rating);
      const width = Math.max(128, name.length * 6.8 + 48);

      const pinColor = isSelected ? "#991B1B" : "#7A1E1E";
      const strokeColor = isSelected ? "#DC2626" : "#EAD9D4";
      const strokeWidth = isSelected ? "1.8" : "1";
      const bg = isSelected ? "#FFF5F2" : "#FFFFFF";

      return `
        <div class="marker-wrap${{isSelected ? ' active' : ''}}">
          <svg width="${{width + 30}}" height="50" viewBox="-16 -44 ${{width + 30}} 50" style="position: absolute; left: -16px; top: -44px; width: ${{width + 30}}px; height: 50px; overflow: visible;">
            <defs>
              <filter id="sh-${{place.place_id}}" x="-20%" y="-20%" width="140%" height="150%">
                <feDropShadow dx="0" dy="2" stdDeviation="2.5" floodColor="#2B0E0E" floodOpacity="0.2"/>
              </filter>
            </defs>
            <rect filter="url(#sh-${{place.place_id}})" x="6" y="-38" width="${{width}}" height="30" rx="7" fill="${{bg}}" stroke="${{strokeColor}}" stroke-width="${{strokeWidth}}"/>
            <path d="M -3.5 -14 L 0 0 L 3.5 -14 Z" fill="${{pinColor}}"/>
            <circle cx="0" cy="-23" r="12" fill="${{pinColor}}" stroke="#FFFFFF" stroke-width="1.2"/>
            <circle cx="0" cy="0" r="2.5" fill="#DC2626" stroke="#FFFFFF" stroke-width="0.8"/>
            <text x="0" y="-19" text-anchor="middle" font-size="11" fill="#FFFFFF">${{icon}}</text>
            <text x="19" y="-25" font-size="11" font-weight="700" fill="${{isSelected ? '#991B1B' : '#1F2937'}}" font-family="'Be Vietnam Pro', sans-serif">${{name}}</text>
            <text x="19" y="-14" font-size="10" font-weight="700" fill="#D97706" font-family="'Be Vietnam Pro', sans-serif">${{stars}}</text>
            <text x="${{19 + rating * 7 + 4}}" y="-14" font-size="9" font-weight="600" fill="#6B7280" font-family="'Be Vietnam Pro', sans-serif">${{dist}}</text>
          </svg>
        </div>
      `;
    }}

    function updateMapMarkers() {{
      markers.forEach(m => m.remove());
      markers = [];

      const currentZoom = map.getZoom();
      const showVenues = currentZoom >= VENUE_MIN_ZOOM;
      const filtered = getFilteredPlaces();

      if (showVenues || selectedPlaceId) {{
        filtered.forEach(place => {{
          const isSelected = selectedPlaceId === place.place_id;
          if (!showVenues && !isSelected) return;

          const el = document.createElement("div");
          el.style.width = "0px";
          el.style.height = "0px";
          el.style.position = "absolute";
          el.innerHTML = createMarkerHtml(place, isSelected);
          el.onclick = (e) => {{
            e.stopPropagation();
            selectPlace(place);
          }};

          const marker = new maplibregl.Marker({{ element: el, anchor: "top-left" }})
            .setLngLat([place.lng, place.lat])
            .addTo(map);

          markers.push(marker);
        }});
      }}

      const bannerBadge = document.getElementById("banner-count");
      if (showVenues) {{
        bannerBadge.innerText = `Bán kính 2.0km • ${{filtered.length}} quán ăn đang hiển thị`;
      }} else {{
        bannerBadge.innerText = `Bán kính 2.0km • Phóng to gần để xem ${{filtered.length}} quán ăn 🔍`;
      }}
    }}

    function getFilteredPlaces() {{
      const q = searchQuery.toLowerCase().trim();
      return DATA.places.filter(p => {{
        if (q) {{
          const matchName = p.name.toLowerCase().includes(q);
          const matchAddr = p.address.toLowerCase().includes(q);
          const matchDish = (p.dishes || []).some(d => d.dish_name_vi.toLowerCase().includes(q));
          if (!matchName && !matchAddr && !matchDish) return false;
        }}
        if (activeCategory !== "all") {{
          const hasCat = p.primary_category === activeCategory || (p.dishes || []).some(d => d.category === activeCategory);
          if (!hasCat) return false;
        }}
        if (distanceFilter !== "all") {{
          if (p.distance_m > parseFloat(distanceFilter)) return false;
        }}
        return true;
      }}).sort((a, b) => {{
        if (sortBy === "distance") return a.distance_m - b.distance_m;
        if (sortBy === "rating") return b.rating - a.rating;
        return a.name.localeCompare(b.name, "vi");
      }});
    }}

    function getFilteredDishes() {{
      const q = searchQuery.toLowerCase().trim();
      return DATA.dishes.filter(d => {{
        if (q) {{
          const matchName = d.name_vi.toLowerCase().includes(q);
          const matchEn = d.name_en && d.name_en.toLowerCase().includes(q);
          const matchDesc = d.description_vi && d.description_vi.toLowerCase().includes(q);
          if (!matchName && !matchEn && !matchDesc) return false;
        }}
        if (activeCategory !== "all") {{
          if (d.category !== activeCategory) return false;
        }}
        if (distanceFilter !== "all") {{
          if (d.min_distance_m > parseFloat(distanceFilter)) return false;
        }}
        return true;
      }}).sort((a, b) => {{
        if (sortBy === "distance") return a.min_distance_m - b.min_distance_m;
        return a.name_vi.localeCompare(b.name_vi, "vi");
      }});
    }}

    function renderThemePills() {{
      const container = document.getElementById("theme-pills");
      container.innerHTML = "";

      const allBtn = document.createElement("button");
      allBtn.className = "theme-chip" + (activeCategory === "all" ? " active" : "");
      allBtn.innerHTML = `<span>✨</span><span>Tất cả</span>`;
      allBtn.onclick = () => {{ activeCategory = "all"; updateUI(); }};
      container.appendChild(allBtn);

      Object.entries(DATA.category_meta).forEach(([k, meta]) => {{
        const btn = document.createElement("button");
        btn.className = "theme-chip" + (activeCategory === k ? " active" : "");
        btn.innerHTML = `<span>${{meta.icon}}</span><span>${{meta.label}}</span>`;
        btn.onclick = () => {{ activeCategory = k; updateUI(); }};
        container.appendChild(btn);
      }});
    }}

    function renderList() {{
      const container = document.getElementById("list-items");
      container.innerHTML = "";

      if (currentViewMode === "places") {{
        const list = getFilteredPlaces();
        document.getElementById("results-count-text").innerText = `Tìm thấy ${{list.length}} quán ăn`;
        list.forEach(p => {{
          const catMeta = DATA.category_meta[p.primary_category] || {{}};
          const topDish = p.dishes?.[0]?.dish_name_vi || "Món đặc sản";
          const isSel = selectedPlaceId === p.place_id;

          const card = document.createElement("div");
          card.className = "card-item" + (isSel ? " selected" : "");
          card.innerHTML = `
            <div class="card-thumb-wrap">
              <img src="${{p.image_url}}" class="card-thumb" onerror="this.src='https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=300'">
              <span class="card-cat-badge">${{catMeta.icon || '🍜'}} ${{catMeta.label || 'Món ngon'}}</span>
            </div>
            <div class="card-info">
              <h3 class="card-name">${{p.name}}</h3>
              <p class="card-addr">${{p.address}}</p>
              <div class="card-badges">
                <span class="badge-dist">🧭 ${{p.distance_m}}m từ Văn Miếu</span>
                <span class="badge-rate">★ ${{p.rating}}</span>
              </div>
              <div class="card-foot">
                <span class="card-dish-tag">Món: ${{topDish}}</span>
                <span class="card-price-tag">${{p.price_min_vnd ? (p.price_min_vnd/1000)+'k' : ''}} - ${{p.price_max_vnd ? (p.price_max_vnd/1000)+'k' : ''}}</span>
              </div>
            </div>
          `;
          card.onclick = () => selectPlace(p);
          container.appendChild(card);
        }});
      }} else {{
        const list = getFilteredDishes();
        document.getElementById("results-count-text").innerText = `Tìm thấy ${{list.length}} món ăn`;
        list.forEach(d => {{
          const catMeta = DATA.category_meta[d.category] || {{}};
          const card = document.createElement("div");
          card.className = "card-item";
          card.innerHTML = `
            <div class="card-thumb-wrap">
              <img src="${{d.image_url}}" class="card-thumb" onerror="this.src='https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=300'">
              <span class="card-cat-badge">${{catMeta.icon || '🍲'}} ${{catMeta.label || 'Đặc sản'}}</span>
            </div>
            <div class="card-info">
              <h3 class="card-name">${{d.name_vi}}</h3>
              <p class="card-addr">${{d.short_description_vi || d.description_vi?.slice(0, 80) + '...'}}</p>
              <div class="card-badges">
                <span class="badge-dist">📍 ${{d.serving_places_count}} quán gần Văn Miếu</span>
                <span class="badge-rate">Gần nhất: ${{d.min_distance_m}}m</span>
              </div>
            </div>
          `;
          card.onclick = () => openDishDetail(d);
          container.appendChild(card);
        }});
      }}
    }}

    function selectPlace(place) {{
      selectedPlaceId = place.place_id;
      map.flyTo({{
        center: [place.lng, place.lat],
        zoom: 16,
        padding: {{ right: 380 }},
        duration: 900
      }});
      updateMapMarkers();
      renderList();
      openPlaceDetail(place);
    }}

    function openPlaceDetail(place) {{
      const catMeta = DATA.category_meta[place.primary_category] || {{}};
      const dishes = place.dishes || [];
      const overlay = document.getElementById("detail-overlay");
      const sheet = document.getElementById("detail-sheet");

      sheet.innerHTML = `
        <div class="detail-img-wrap">
          <img src="${{place.image_url}}" class="detail-img" onerror="this.src='https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=800'">
          <button class="detail-close" onclick="closeDetail()">✕</button>
          <div class="detail-img-overlay">
            <span style="background: rgba(220, 38, 38, 0.9); color: #fff; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 4px; align-self: flex-start;">${{catMeta.icon || '📍'}} ${{catMeta.label || 'Quán ăn'}}</span>
            <h2 class="detail-title">${{place.name}}</h2>
            <p class="detail-sub">${{place.branch_name || ''}} • ★ ${{place.rating}} • Cách Văn Miếu ${{place.distance_m}}m</p>
          </div>
        </div>
        <div class="detail-tabs">
          <button class="detail-tab active">Tổng quan & Thực đơn</button>
        </div>
        <div class="detail-body">
          <div class="detail-box">
            <div><strong>📍 Địa chỉ:</strong> ${{place.address}}</div>
            <div><strong>🕒 Giờ mở cửa:</strong> ${{place.opening_hours || '07:00 - 21:00'}}</div>
            <div><strong>💰 Khoảng giá:</strong> ${{place.price_min_vnd ? place.price_min_vnd.toLocaleString() + 'đ' : ''}} - ${{place.price_max_vnd ? place.price_max_vnd.toLocaleString() + 'đ' : ''}}</div>
            <div><strong>🧭 Khoảng cách:</strong> ${{place.distance_m}}m từ Văn Miếu Quốc Tử Giám</div>
          </div>
          <a href="https://www.google.com/maps/dir/?api=1&origin=21.02879,105.835953&destination=${{place.lat}},${{place.lng}}" target="_blank" class="btn-maps">🧭 Chỉ đường từ Văn Miếu</a>
          <h3 style="font-size: 15px; font-weight: 700; color: #1F2937; margin-top: 8px;">Món ăn phục vụ (${{dishes.length}})</h3>
          <div style="display: flex; flex-direction: column; gap: 8px;">
            ${{dishes.map(d => `
              <div style="background: #fbf7f4; border: 1px solid #ebdcd6; border-radius: 8px; padding: 10px; display: flex; justify-content: space-between; align-items: center;">
                <div>
                  <strong style="font-size: 13.5px; color: #1F2937;">${{d.dish_name_vi}}</strong>
                  ${{d.variant ? `<div style="font-size: 11.5px; color: #78716c;">Biến thể: ${{d.variant}}</div>` : ''}}
                </div>
                <span style="font-weight: 700; color: #b91c1c; font-size: 13px;">${{d.price_min_vnd ? d.price_min_vnd.toLocaleString() + 'đ' : 'Theo giá quán'}}</span>
              </div>
            `).join('')}}
          </div>
        </div>
      `;
      overlay.style.display = "flex";
    }}

    function openDishDetail(dish) {{
      const catMeta = DATA.category_meta[dish.category] || {{}};
      const overlay = document.getElementById("detail-overlay");
      const sheet = document.getElementById("detail-sheet");

      sheet.innerHTML = `
        <div class="detail-img-wrap">
          <img src="${{dish.image_url}}" class="detail-img" onerror="this.src='https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=800'">
          <button class="detail-close" onclick="closeDetail()">✕</button>
          <div class="detail-img-overlay">
            <span style="background: rgba(220, 38, 38, 0.9); color: #fff; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 4px; align-self: flex-start;">${{catMeta.icon || '🍲'}} ${{catMeta.label || 'Món ăn'}}</span>
            <h2 class="detail-title">${{dish.name_vi}}</h2>
            <p class="detail-sub">${{dish.name_en || ''}}</p>
          </div>
        </div>
        <div class="detail-tabs">
          <button class="detail-tab active">Thông tin & Công thức</button>
        </div>
        <div class="detail-body">
          <p style="font-size: 13.5px; line-height: 1.6; color: #44403c;">${{dish.description_vi || dish.short_description_vi || ''}}</p>
          ${{dish.how_to_eat_vi ? `
            <div style="background: #f0fdf4; border-left: 4px solid #16a34a; padding: 10px 14px; border-radius: 0 8px 8px 0; font-size: 13px; color: #15803d;">
              <strong>Cách thưởng thức chuẩn vị Hà Nội:</strong><br>${{dish.how_to_eat_vi}}
            </div>
          ` : ''}}
          ${{dish.ordering_phrase_vi ? `
            <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px 14px; border-radius: 0 8px 8px 0; font-size: 13px; color: #1d4ed8;">
              <strong>Cách gọi món sành điệu:</strong> "${{dish.ordering_phrase_vi}}"
            </div>
          ` : ''}}
          <h3 style="font-size: 15px; font-weight: 700; color: #1F2937; margin-top: 6px;">Quán phục vụ gần Văn Miếu (${{dish.serving_places_count}})</h3>
          <div style="display: flex; flex-direction: column; gap: 8px;">
            ${{(dish.serving_places || []).map(p => `
              <div style="background: #fdfaf8; border: 1px solid #ebdcd6; border-radius: 8px; padding: 10px; cursor: pointer;" onclick="flyToServingPlace('${{p.place_id}}')">
                <div style="display: flex; justify-content: space-between;">
                  <strong style="color: #1F2937; font-size: 13.5px;">${{p.name}}</strong>
                  <span style="color: #991b1b; font-weight: 700; font-size: 12px;">🧭 ${{p.distance_m}}m</span>
                </div>
                <div style="font-size: 12px; color: #78716c; margin-top: 2px;">${{p.address}}</div>
              </div>
            `).join('')}}
          </div>
        </div>
      `;
      overlay.style.display = "flex";
    }}

    function openVanMieuDetail() {{
      const overlay = document.getElementById("detail-overlay");
      const sheet = document.getElementById("detail-sheet");
      sheet.innerHTML = `
        <div class="detail-img-wrap">
          <img src="https://images.unsplash.com/photo-1599707367072-cd6ada2bc375?w=800" class="detail-img">
          <button class="detail-close" onclick="closeDetail()">✕</button>
          <div class="detail-img-overlay">
            <span style="background: #991B1B; color: #fff; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 4px; align-self: flex-start;">🏛️ Di Tích Quốc Gia Đặc Biệt</span>
            <h2 class="detail-title">Văn Miếu – Quốc Tử Giám</h2>
            <p class="detail-sub">Tâm điểm khảo sát ẩm thực Hà Nội</p>
          </div>
        </div>
        <div class="detail-body">
          <div class="detail-box">
            <div><strong>Tọa độ tâm điểm:</strong> 21.02879° N, 105.835953° E</div>
            <div><strong>Địa chỉ:</strong> 58 Quốc Tử Giám, Đống Đa, Hà Nội</div>
            <div><strong>Phạm vi khảo sát:</strong> Bán kính 2.0 km (70 quán ăn, 50 món ăn)</div>
          </div>
          <p style="font-size: 13.5px; line-height: 1.6; color: #44403c;">
            Văn Miếu – Quốc Tử Giám là trường đại học đầu tiên của Việt Nam, được chọn làm tọa độ gốc (0m) để đo khoảng cách và bán kính khảo sát văn hóa ẩm thực Thăng Long - Hà Nội.
          </p>
          <a href="https://www.google.com/maps/search/?api=1&query=Văn+Miếu+Quốc+Tử+Giám" target="_blank" class="btn-maps">🗺️ Mở trên Google Maps</a>
        </div>
      `;
      overlay.style.display = "flex";
    }}

    function closeDetail() {{
      document.getElementById("detail-overlay").style.display = "none";
    }}

    function flyToServingPlace(pid) {{
      const p = DATA.places.find(x => x.place_id === pid);
      if (p) selectPlace(p);
    }}

    function updateUI() {{
      renderThemePills();
      renderList();
      updateMapMarkers();
    }}

    // Events
    document.getElementById("search-input").addEventListener("input", (e) => {{
      searchQuery = e.target.value;
      updateUI();
    }});
    document.getElementById("btn-view-places").addEventListener("click", () => {{
      currentViewMode = "places";
      document.getElementById("btn-view-places").classList.add("active");
      document.getElementById("btn-view-dishes").classList.remove("active");
      updateUI();
    }});
    document.getElementById("btn-view-dishes").addEventListener("click", () => {{
      currentViewMode = "dishes";
      document.getElementById("btn-view-dishes").classList.add("active");
      document.getElementById("btn-view-places").classList.remove("active");
      updateUI();
    }});
    document.getElementById("select-dist").addEventListener("change", (e) => {{
      distanceFilter = e.target.value;
      updateUI();
    }});
    document.getElementById("select-sort").addEventListener("change", (e) => {{
      sortBy = e.target.value;
      updateUI();
    }});
    document.getElementById("btn-recenter").addEventListener("click", () => {{
      map.flyTo({{ center: VAN_MIEU, zoom: 14.8, duration: 800 }});
    }});
    document.getElementById("btn-recenter-card").addEventListener("click", () => {{
      map.flyTo({{ center: VAN_MIEU, zoom: 15.5, duration: 800 }});
      openVanMieuDetail();
    }});
    document.getElementById("banner-count").addEventListener("click", () => {{
      if (map.getZoom() < VENUE_MIN_ZOOM) {{
        map.flyTo({{ center: VAN_MIEU, zoom: 15.0, duration: 800 }});
      }}
    }});
    document.getElementById("btn-fit-hanoi").addEventListener("click", () => {{
      map.fitBounds([[105.2889615, 20.5645154], [106.0200407, 21.3854176]], {{ padding: 40, duration: 900 }});
    }});
    document.getElementById("btn-zoom-in").addEventListener("click", () => map.zoomIn());
    document.getElementById("btn-zoom-out").addEventListener("click", () => map.zoomOut());

    document.getElementById("btn-toggle-circle").addEventListener("click", (e) => {{
      showCircle = !showCircle;
      e.currentTarget.classList.toggle("active", showCircle);
      const vis = showCircle ? "visible" : "none";
      if (map.getLayer("circle-fill")) map.setLayoutProperty("circle-fill", "visibility", vis);
      if (map.getLayer("circle-line")) map.setLayoutProperty("circle-line", "visibility", vis);
    }});

    document.getElementById("btn-toggle-hanoi").addEventListener("click", (e) => {{
      showHanoi = !showHanoi;
      e.currentTarget.classList.toggle("active", showHanoi);
      const vis = showHanoi ? "visible" : "none";
      if (map.getLayer("hanoi-fill")) map.setLayoutProperty("hanoi-fill", "visibility", vis);
      if (map.getLayer("hanoi-line")) map.setLayoutProperty("hanoi-line", "visibility", vis);
    }});

    document.getElementById("detail-overlay").addEventListener("click", (e) => {{
      if (e.target.id === "detail-overlay") closeDetail();
    }});

    // Initialize UI
    renderThemePills();
    renderList();
  </script>
</body>
</html>
'''

with open(r'E:\Demo Văn Miếu\food_map_preview.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(r'E:\Demo Văn Miếu\Demo Văn Miếu\food_map_preview.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Regenerated food_map_preview.html with zoom-adaptive venue marker visibility!")
