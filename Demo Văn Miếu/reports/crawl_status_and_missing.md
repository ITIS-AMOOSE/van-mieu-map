# BÁO CÁO TIẾN ĐỘ CRAWL VÀ THỐNG KÊ TRƯỜNG THIẾU — 50 MÓN ĂN HOÀN CHỈNH

- **Ngày cập nhật**: 2026-11-02 16:32:48 UTC
- **Tiến độ**: 50/50 món ăn hoàn thành (100% mục tiêu quy mô dự án)
- **Số quán ăn (<2000m)**: 70 quán
- **Số offering**: 82 offering
- **Số nguyên liệu**: 308 nguyên liệu

## Thống kê các trường có giá trị rỗng/null cho phép

Theo nguyên tắc kiểm định, các trường chưa có nguồn chính thống sẽ được lưu `null` thay vì bịa đặt dữ liệu:
- `places.branch_name`: Null khi quán là cửa hàng đơn lẻ không chia chi nhánh.
- `places.osm_ref` / `existing_map_place_id`: Null với các quán thu thập từ khảo sát thực tế hoặc ẩm thực địa phương chưa có ID trên OSM.
- `places.rating` / `review_count`: Null với các quán mẫu chưa thu thập được đánh giá chính thống.
- `offerings.variant`: Null với các món không chia biến thể kích cỡ.
- `dishes.short_description_vi/en`: Đầy đủ 100% cho toàn bộ 50 món.
