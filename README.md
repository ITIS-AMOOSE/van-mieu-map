# BẢN ĐỒ ẨM THỰC HÀ NỘI — VÙNG KHẢO SÁT VĂN MIẾU QUỐC TỬ GIÁM

Hệ thống bản đồ ẩm thực tương tác cao cấp được xây dựng dựa trên dữ liệu khảo sát ẩm thực thực tế của **Demo Văn Miếu** kết hợp công nghệ lõi bản đồ từ dự án **DeepCulture** (`E:\DeepCulture\deepculture_v2`).

---

## 1. PHÂN TÍCH CÔNG NGHỆ LÕI (Từ DeepCulture v2)

Sau khi nghiên cứu mã nguồn của `E:\DeepCulture\deepculture_v2` (đặc biệt tại `src/pages/culture-map/components/map`), hệ thống đã kế thừa và tối ưu hóa các công nghệ cốt lõi:

| Thành phần | Công nghệ từ DeepCulture | Ứng dụng vào Bản Đồ Ẩm Thực Văn Miếu |
| :--- | :--- | :--- |
| **Bản đồ nền (Map Engine)** | **MapLibre GL JS** (`maplibre-gl`) | Kết xuất WebGL vector/raster siêu tốc, mượt mà ở mọi mức zoom. |
| **Kiểu hiển thị (Basemap Style)** | MapTiler Streets v2 + Carto Tiles | Tích hợp đa dạng: Cổ điển (Carto Voyager tone màu ấm phù hợp văn hóa), Đường phố (MapTiler), Tối giản (Positron), OSM. |
| **Marker tùy biến (Custom Callout)** | SVG Pin Callout (Figma Frame 333) | Khung thẻ pill màu trắng, đuôi ghim chỉ đúng tọa độ GPS, icon ẩm thực, tên quán và hàng sao vàng rực rỡ. Hiệu ứng hover nhún nảy `cubic-bezier(0.34, 1.56, 0.64, 1)`. |
| **Địa giới hành chính** | GeoJSON ADM1 Boundary + Turf.js | Trích xuất ranh giới chính xác của toàn bộ Thành phố Hà Nội (2.509 điểm polygon), phủ lớp màu đỏ thắm `#7A1E1E` thanh nhã. |
| **Vùng bán kính tâm điểm** | GeoJSON Buffering | Tạo vành đai tròn bán kính 2.000m tâm tại Văn Miếu kèm các vòng đồng tâm 500m, 1.000m để du khách ước lượng khoảng cách. |
| **Bảng điều khiển (Left Panel)** | Responsive Panel & Theme Filter | Bộ lọc danh mục ẩm thực chuẩn mực (Phở, Bún chả, Món cuốn, Bánh mì, Cà phê...), tìm kiếm thời gian thực, lọc theo khoảng cách và sao đánh giá. |
| **Ngăn chi tiết (Detail Drawer)** | Slide-in Sheet (HeritageDetailPopup) | Trượt mượt mà từ cạnh phải, cung cấp đầy đủ thông tin địa chỉ, thực đơn món, khoảng giá, 308 nguyên liệu định danh, cách ăn chuẩn vị Hà Nội và chỉ đường Google Maps. |

---

## 2. TỌA ĐỘ VÀ DỮ LIỆU ĐẶC THÙ VĂN MIẾU

- **Tọa độ trung tâm bản đồ:** `[105.835953, 21.02879]` (58 Quốc Tử Giám, Đống Đa, Hà Nội).
- **Phạm vi khảo sát:** Bán kính 2.000m (2.0 km) tính từ Văn Miếu.
- **Tổng số địa điểm quán ăn:** 70 quán đặc sản (có tọa độ GPS, số sao đánh giá, giờ mở cửa, khoảng giá, khoảng cách chính xác tính bằng mét).
- **Tổng số món ăn đặc sắc:** 50 món truyền thống Hà Nội (Phở bò, Phở gà, Bún chả, Bánh cuốn, Cà phê trứng, Bánh mì, Chè sắn nóng...).
- **Nguyên liệu định danh:** 308 thành phần (chia theo nhóm Nước dùng, Thịt/Chính, Rau thơm, Gia vị, Nước chấm).

---

## 3. CÁCH KHỞI CHẠY VÀ SỬ DỤNG

### Cách 1: Chạy trực tiếp (Không cần cài đặt Node.js)
- Mở trực tiếp file `food_map_preview.html` trong thư mục này hoặc trong `Demo Văn Miếu/food_map_preview.html` bằng trình duyệt web (Google Chrome, Microsoft Edge, Cốc Cốc, v.v.).
- Bạn cũng có thể mở file `Demo Văn Miếu/preview_catalog.html` và bấm nút **"Mở Bản Đồ Ẩm Thực MapLibre"** ở thanh điều hướng trên cùng.

### Cách 2: Chạy môi trường phát triển (Vite + React)
Trong thư mục `E:\Demo Văn Miếu`:
```powershell
npm.cmd run dev
```
Truy cập: `http://localhost:5173`

### Cách 3: Xem bản build Production
```powershell
npm.cmd run preview
```
Hoặc mở trực tiếp file `dist/index.html`.

---

## 4. CẤU TRÚC THƯ MỤC DỰ ÁN

```
E:\Demo Văn Miếu\
├── food_map_preview.html         # File chạy độc lập all-in-one có thể mở ngay
├── hanoi_boundary.geojson        # Ranh giới hành chính trích xuất của Thành phố Hà Nội
├── package.json                  # Cấu hình dự án React 19 + MapLibre GL
├── vite.config.js                # Cấu hình Vite bundler
├── index.html                    # File HTML gốc
├── dist/                         # Bản build production tối ưu hóa
│   └── index.html
├── src/
│   ├── App.jsx                   # Quản lý trạng thái và luồng đồng bộ bản đồ & danh sách
│   ├── components/
│   │   ├── map/
│   │   │   ├── FoodMapLibre.jsx      # Component lõi MapLibre GL JS
│   │   │   ├── FoodMarkerCallout.jsx # Marker SVG tùy biến theo Figma Frame 333
│   │   │   ├── mapConstants.js       # Tọa độ Văn Miếu, cấu hình zoom, basemap styles
│   │   │   └── mapGeoUtils.js        # Tiện ích tính khoảng cách, bán kính, định dạng
│   │   ├── left-panel/
│   │   │   └── LeftPanel.jsx         # Bảng tìm kiếm, lọc danh mục, danh sách quán ăn
│   │   ├── theme-filter/
│   │   │   └── FoodThemeFilter.jsx   # Thanh chip lọc danh mục món ăn
│   │   ├── detail-sheet/
│   │   │   └── FoodDetailSheet.jsx   # Drawer chi tiết quán ăn, món ăn, cách ăn & công thức
│   │   └── icons/
│   │       └── FoodIcons.jsx         # Bộ biểu tượng SVG: Khuê Văn Các, bát phở, bún chả...
│   └── data/
│       └── foodMapData.json          # Dữ liệu JSON đã được chuẩn hóa và liên kết
└── Demo Văn Miếu/                # Thư mục dữ liệu nguồn gốc ban đầu
    ├── preview_catalog.html      # Đã tích hợp nút liên kết nhanh sang Bản đồ
    ├── van_mieu_foods_combined.json
    └── ...
```

