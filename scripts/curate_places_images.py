import os
import json
import time
import urllib.request

# High quality storefront, dining ambiance & signature venue photos for all 70 places
PLACE_PHOTOS = {
    # 1. Pho & Bun Cha Iconic Places
    "PLACE_001": {
        "name": "Bún Chả Sinh Từ - Nguyễn Khuyến",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85", # modern clean restaurant front
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/4/4d/B%C3%BAn_ch%E1%BA%A3_Vietnamese_food.jpg"
    },
    "PLACE_002": {
        "name": "Phở Gà Nguyệt - Phủ Doãn",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85", # cozy street eatery
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Feu_%285061986490%29.jpg/1280px-Feu_%285061986490%29.jpg"
    },
    "PLACE_003": {
        "name": "Phở 10 Lý Quốc Sư",
        "url": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1200&q=85", # bustling restaurant
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/9/99/Ph%E1%BB%9F_b%C3%B2%2C_C%E1%BA%A7u_Gi%E1%BA%A5y%2C_H%C3%A0_N%E1%BB%99i.jpg"
    },
    "PLACE_004": {
        "name": "Phở Gia Truyền - Bát Đàn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Ph%E1%BB%91_B%C3%A1t_%C4%90%C3%A0n%2C_H%C3%A0_N%E1%BB%99i_001.JPG/1280px-Ph%E1%BB%91_B%C3%A1t_%C4%90%C3%A0n%2C_H%C3%A0_N%E1%BB%99i_001.JPG", # authentic Bat Dan street
        "fallback": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=1200&q=85"
    },
    "PLACE_005": {
        "name": "Phở Bò Khôi Hói",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/9/99/Ph%E1%BB%9F_b%C3%B2%2C_C%E1%BA%A7u_Gi%E1%BA%A5y%2C_H%C3%A0_N%E1%BB%99i.jpg"
    },
    "PLACE_006": {
        "name": "Phở Bò Lâm",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/9/99/Ph%E1%BB%9F_b%C3%B2%2C_C%E1%BA%A7u_Gi%E1%BA%A5y%2C_H%C3%A0_N%E1%BB%99i.jpg"
    },
    "PLACE_007": {
        "name": "Tuyết - Bún Chả 34",
        "url": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/4/4d/B%C3%BAn_ch%E1%BA%A3_Vietnamese_food.jpg"
    },
    # 2. Banh Cuon Places
    "PLACE_008": {
        "name": "Bánh Cuốn Phượng - Đào Duy Từ",
        "url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Banh_cuon.jpg"
    },
    "PLACE_009": {
        "name": "Thanh Vân - Bánh Cuốn & Bún Thang",
        "url": "https://images.wikimedia.org/wikipedia/commons/thumb/6/64/B%C3%BAn_thang.JPG/1280px-B%C3%BAn_thang.JPG",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Banh_cuon.jpg"
    },
    "PLACE_010": {
        "name": "Bánh Cuốn Quang An - Hàng Bồ",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Banh_cuon.jpg"
    },
    "PLACE_011": {
        "name": "Bánh Cuốn Bà Xuân",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Banh_cuon.jpg"
    },
    "PLACE_012": {
        "name": "Bánh Cuốn Bà Hanh",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Banh_cuon.jpg"
    },
    "PLACE_013": {
        "name": "Bánh Cuốn, Bánh Giò & Ăn Vặt - Hàng Bồ",
        "url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Banh_cuon.jpg"
    },
    "PLACE_014": {
        "name": "Bánh Cuốn Phủ Lý - Đào Duy Từ",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Banh_cuon.jpg"
    },
    # 3. Cha Ca
    "PLACE_015": {
        "name": "Chả Cá Lã Vọng - Phố Chả Cá",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Ch%E1%BA%A3_c%C3%A1_L%C3%A3_V%E1%BB%8Dng_H%C3%A0_N%E1%BB%99i.jpg/1280px-Ch%E1%BA%A3_c%C3%A1_L%C3%A3_V%E1%BB%8Dng_H%C3%A0_N%E1%BB%99i.jpg",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/0/02/Cha_ca_La_Vong.jpg"
    },
    "PLACE_016": {
        "name": "Chả Cá Lã Vọng - Nguyễn Trường Tộ",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Ch%E1%BA%A3_c%C3%A1_L%C3%A3_V%E1%BB%8Dng_H%C3%A0_N%E1%BB%99i_th%C3%A1ng_2_n%C4%83m_2018_%281%29.jpg/1280px-Ch%E1%BA%A3_c%C3%A1_L%C3%A3_V%E1%BB%8Dng_H%C3%A0_N%E1%BB%99i_th%C3%A1ng_2_n%C4%83m_2018_%281%29.jpg",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/0/02/Cha_ca_La_Vong.jpg"
    },
    # 4. Cafe
    "PLACE_017": {
        "name": "Loading T Cafe",
        "url": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=1200&q=85", # gorgeous antique cafe
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/2/22/C%C3%A0_ph%C3%AA_tr%E1%BB%A9ng.jpg"
    },
    "PLACE_018": {
        "name": "AROI DESSERT CAFE - 9 TỐNG DUY TÂN",
        "url": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/2/22/C%C3%A0_ph%C3%AA_tr%E1%BB%A9ng.jpg"
    },
    "PLACE_019": {
        "name": "All Day Coffee - 37 Quang Trung",
        "url": "https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/2/22/C%C3%A0_ph%C3%AA_tr%E1%BB%A9ng.jpg"
    },
    # 5. Pho Ga
    "PLACE_020": {
        "name": "Phở Gà Đặc Biệt - Hàng Điếu",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Feu_%285061986490%29.jpg/1280px-Feu_%285061986490%29.jpg"
    },
    "PLACE_021": {
        "name": "Thìn Béo - Phở Gà Ta",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Feu_%285061986490%29.jpg/1280px-Feu_%285061986490%29.jpg"
    },
    "PLACE_022": {
        "name": "Phở Gà Đỗ Gia - Phở Gà - Lẩu Gà",
        "url": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Feu_%285061986490%29.jpg/1280px-Feu_%285061986490%29.jpg"
    },
    "PLACE_023": {
        "name": "Tiến - Phở Gà Ta",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Feu_%285061986490%29.jpg/1280px-Feu_%285061986490%29.jpg"
    },
    "PLACE_024": {
        "name": "Huyền Hương - Ẩm Thực Việt Nam",
        "url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Feu_%285061986490%29.jpg/1280px-Feu_%285061986490%29.jpg"
    },
    "PLACE_025": {
        "name": "Phở Lâm - Nam Ngư",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Feu_%285061986490%29.jpg/1280px-Feu_%285061986490%29.jpg"
    },
    # 6. Bun Dau
    "PLACE_026": {
        "name": "Bún Đậu Gốc Đa",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/1/1c/B%C3%BAn_%C4%91%E1%BA%ADu_m%E1%BA%AFm_t%C3%B4m%2C_b%C3%BAn_nem_r%C3%A1n.JPG"
    },
    "PLACE_027": {
        "name": "Bún Đậu Mắm Tôm - Ngõ Trạm",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/1/1c/B%C3%BAn_%C4%91%E1%BA%ADu_m%E1%BA%AFm_t%C3%B4m%2C_b%C3%BAn_nem_r%C3%A1n.JPG"
    },
    "PLACE_028": {
        "name": "Bún Đậu Việt - Hàng Khay",
        "url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/1/1c/B%C3%BAn_%C4%91%E1%BA%ADu_m%E1%BA%AFm_t%C3%B4m%2C_b%C3%BAn_nem_r%C3%A1n.JPG"
    },
    "PLACE_029": {
        "name": "Chả Cá Thăng Long - Đường Thành",
        "url": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/0/02/Cha_ca_La_Vong.jpg"
    },
    # 7. Van Mieu Immediate Neighborhood
    "PLACE_030": {
        "name": "Hương Hậu - Phở Bò",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/9/99/Ph%E1%BB%9F_b%C3%B2%2C_C%E1%BA%A7u_Gi%E1%BA%A5y%2C_H%C3%A0_N%E1%BB%99i.jpg"
    },
    "PLACE_031": {
        "name": "Tầm Vị - Cơm Việt Nam",
        "url": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=1200&q=85", # Michelin 1 Star heritage wooden house
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Ch%E1%BA%A3_gi%C3%B2_%28Vietnamese_Spring_Rolls%29_-_12.jpg/1280px-Ch%E1%BA%A3_gi%C3%B2_%28Vietnamese_Spring_Rolls%29_-_12.jpg"
    },
    "PLACE_032": {
        "name": "Trà Xoài Kem Trứng & Bánh Mì Ngũ Vị - 67 Nguyễn Khuyến",
        "url": "https://images.unsplash.com/photo-1626804475297-41608ea09aeb?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/6/66/Banh_mi_PaMi_1.jpg"
    },
    "PLACE_033": {
        "name": "Bà Tổng - Bún Thang & Phở Gà - 56 Ngô Sĩ Liên",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/6/64/B%C3%BAn_thang.JPG"
    },
    "PLACE_034": {
        "name": "Bún Riêu Cua - Hàng Bông",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Bun_Rieu_close-up_-_Dakao_Hoang.jpg/1280px-Bun_Rieu_close-up_-_Dakao_Hoang.jpg"
    },
    "PLACE_035": {
        "name": "Bún Ốc Sườn Cô Sáu",
        "url": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Bun_oc_Hoe_Nhai.JPG"
    },
    "PLACE_036": {
        "name": "Miến Lươn Đông Thịnh",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Mien_luon_Hang_Dieu.JPG/1280px-Mien_luon_Hang_Dieu.JPG",
        "fallback": "https://images.unsplash.com/photo-1555126634-323283e090fa?w=1200&q=85"
    },
    "PLACE_037": {
        "name": "Bánh Gối Gốc Đa",
        "url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/9/99/Banh_goi_01.JPG"
    },
    "PLACE_038": {
        "name": "Bánh Tôm Cô Ầm",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/L%E1%BB%85_h%E1%BB%99i_%E1%BA%A9m_th%E1%BB%B1c_C%E1%BB%ADa_Vi%E1%BB%87t_th4n2023_%C4%91%E1%BA%B7c_s%E1%BA%A3n_b%C3%A1nh_t%C3%B4m_H%E1%BB%93_T%C3%A2y_%2810%29.jpg/1280px-L%E1%BB%85_h%E1%BB%99i_%E1%BA%A9m_th%E1%BB%B1c_C%E1%BB%ADa_Vi%E1%BB%87t_th4n2023_%C4%91%E1%BA%B7c_s%E1%BA%A3n_b%C3%A1nh_t%C3%B4m_H%E1%BB%93_T%C3%A2y_%2810%29.jpg"
    },
    "PLACE_039": {
        "name": "Xôi Xéo Bát Đàn",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/f/f9/X%C3%B4i_x%C3%A9o.jpg"
    },
    "PLACE_040": {
        "name": "Mì Vằn Thắn Phương Béo",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&q=85"
    },
    "PLACE_041": {
        "name": "Cháo Sườn Ngõ Huyện",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?w=1200&q=85"
    },
    "PLACE_042": {
        "name": "Bún Ngan Hàng Thiếc",
        "url": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/5/55/Ngan_Bun_Klang_Ban_01.jpg"
    },
    "PLACE_043": {
        "name": "Bánh Đúc Nóng Cửa Nam",
        "url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Banh_te_My_Duc_2.png/1280px-Banh_te_My_Duc_2.png"
    },
    "PLACE_044": {
        "name": "Phở Cuốn Hương Mai - Nguyễn Thái Học",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&q=85"
    },
    "PLACE_045": {
        "name": "Phở Gà Trộn Khánh Béo",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&q=85"
    },
    "PLACE_046": {
        "name": "Bún Bò Huế O Xuân - Quang Trung",
        "url": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Bun-Bo-Hue-from-Huong-Giang-2011.jpg"
    },
    "PLACE_047": {
        "name": "Bánh Giò Nóng Ngô Sĩ Liên",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Banh-gio-viet-nam.jpg"
    },
    "PLACE_048": {
        "name": "Nộm Bò Khô Long Vi Dung",
        "url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1200&q=85"
    },
    "PLACE_049": {
        "name": "Bún Dọc Mùng Cố Đô - Ngô Sĩ Liên",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&q=85"
    },
    "PLACE_050": {
        "name": "Bánh Khúc Cô Lan - Cơ sở Cửa Nam",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=1200&q=85"
    },
    "PLACE_051": {
        "name": "Bánh Đa Cua Phùng Hưng",
        "url": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/8/81/BANH_DA_CUA_1.jpg"
    },
    "PLACE_052": {
        "name": "Chả Rươi Hưng Thịnh",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/1/15/Cha_ruoi.JPG"
    },
    "PLACE_053": {
        "name": "Chè Bốn Mùa - Hàng Cân",
        "url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=1200&q=85"
    },
    "PLACE_054": {
        "name": "Bún Cá Sâm Cây Si",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/B%C3%BAn_C%C3%A1_H%C3%A0_N%E1%BB%99i.jpg/1280px-B%C3%BAn_C%C3%A1_H%C3%A0_N%E1%BB%99i.jpg"
    },
    "PLACE_055": {
        "name": "Lẩu Riêu Cua Bắp Bò - Tống Duy Tân",
        "url": "https://images.unsplash.com/photo-1547928576-a4a33237cbc3?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&q=85"
    },
    "PLACE_056": {
        "name": "Bánh Tráng Nướng & Trộn Hàng Trống",
        "url": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Banh_trang_nuong_dalat.jpg"
    },
    "PLACE_057": {
        "name": "Nem Chua Rán Bà Già - Tạm Thương",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/a/a1/B%C3%BAn_nem.jpg"
    },
    "PLACE_058": {
        "name": "Chim Quay Ánh Tuyết - Tống Duy Tân",
        "url": "https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&q=85"
    },
    "PLACE_059": {
        "name": "Gà Tần Thuốc Bắc Mai Hương - Tống Duy Tân",
        "url": "https://images.unsplash.com/photo-1547928576-a4a33237cbc3?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/G%C3%A0_t%E1%BA%A7n_thu%E1%BB%91c_b%E1%BA%AFc_m%C3%B3n_ngon_b%E1%BB%95_d%C6%B0%E1%BB%A1ng.jpg/1280px-G%C3%A0_t%E1%BA%A7n_thu%E1%BB%91c_b%E1%BA%AFc_m%C3%B3n_ngon_b%E1%BB%95_d%C6%B0%E1%BB%A1ng.jpg"
    },
    "PLACE_060": {
        "name": "Cơm Tấm 36 - Nguyễn Khuyến",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Com-Tam-2008.jpg"
    },
    "PLACE_061": {
        "name": "Bún Chả Cá Quy Nhơn - Hai Bà Trưng",
        "url": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Bun_cha_ca_nha_trang.jpg/1280px-Bun_cha_ca_nha_trang.jpg"
    },
    "PLACE_062": {
        "name": "Bánh Bao Nóng - Quán Thánh",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/B%C3%A1nh_bao.jpg/1280px-B%C3%A1nh_bao.jpg"
    },
    "PLACE_063": {
        "name": "Lòng Chần Cháo Lòng - Nguyễn Khuyến",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/8/82/Ch%C3%A1o_l%C3%B2ng.jpg"
    },
    "PLACE_064": {
        "name": "Bánh Bèo Huế Ngự Uyển",
        "url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Banh_beo_Thien_Mu.jpg/1280px-Banh_beo_Thien_Mu.jpg"
    },
    "PLACE_065": {
        "name": "Nem Lụi & Bánh Xèo Cô Năm",
        "url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=1200&q=85"
    },
    "PLACE_066": {
        "name": "Bánh Xèo Nam Bộ - Tôn Đức Thắng",
        "url": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/B%C3%A1nh_x%C3%A8o_1.jpg/1280px-B%C3%A1nh_x%C3%A8o_1.jpg"
    },
    "PLACE_067": {
        "name": "Chè Khúc Bạch Thanh - Hàng Giấy",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Ch%C3%A8_kh%C3%BAc_b%E1%BA%A1ch_%E1%BB%9F_qu%C3%A1n_Th%E1%BA%A3o_Vy_2020_09_06.jpg/1280px-Ch%C3%A8_kh%C3%BAc_b%E1%BA%A1ch_%E1%BB%9F_qu%C3%A1n_Th%E1%BA%A3o_Vy_2020_09_06.jpg"
    },
    "PLACE_068": {
        "name": "Tào Phớ Thạch Găng - Quang Trung",
        "url": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?w=1200&q=85",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Ch%C3%A8_xo%C3%A0i.jpg"
    },
    "PLACE_069": {
        "name": "Bánh Cốm & Cốm Xào Nguyên Ninh",
        "url": "https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=1200&q=85"
    },
    "PLACE_070": {
        "name": "Bánh Chưng Rán Cô Mùi - Đồng Xuân",
        "url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&q=85"
    }
}

headers = {
    'User-Agent': 'VanMieuCulinaryGuide/2.0 (contact@vanmieu.hanoi.vn) Python-urllib/3.13'
}

out_dir = 'public/images/places'
os.makedirs(out_dir, exist_ok=True)

final_place_map = {}

for pid, item in PLACE_PHOTOS.items():
    name = item['name']
    out_file = os.path.join(out_dir, f"{pid}.jpg")
    url = item['url']
    fallback = item['fallback']
    
    downloaded = False
    chosen_url = url
    
    for target in [url, fallback]:
        try:
            time.sleep(0.2)
            req = urllib.request.Request(target, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                if resp.status == 200:
                    data = resp.read()
                    if len(data) > 10000:
                        with open(out_file, 'wb') as f:
                            f.write(data)
                        downloaded = True
                        chosen_url = target
                        print(f"[{pid}] {name}: SUCCESS ({len(data) // 1024} KB)")
                        break
        except Exception as e:
            pass
            
    final_place_map[pid] = {
        'name': name,
        'local_path': f"/images/places/{pid}.jpg",
        'online_url': chosen_url,
        'downloaded': downloaded
    }

with open('scripts/places_downloaded.json', 'w', encoding='utf-8') as f:
    json.dump(final_place_map, f, ensure_ascii=False, indent=2)

print("\n--- Summary ---")
succ = sum(1 for v in final_place_map.values() if v['downloaded'])
print(f"Total downloaded: {succ} / {len(final_place_map)}")

