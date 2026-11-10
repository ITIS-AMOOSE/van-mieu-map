import os
import json
import time
import urllib.request
import urllib.parse

# Curated high-resolution image URLs for all 50 dishes
DISH_IMAGES = {
    "DISH_001": {
        "name": "Phở bò",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/99/Ph%E1%BB%9F_b%C3%B2%2C_C%E1%BA%A7u_Gi%E1%BA%A5y%2C_H%C3%A0_N%E1%BB%99i.jpg",
        "fallback": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=1200&q=85"
    },
    "DISH_002": {
        "name": "Phở gà",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Feu_%285061986490%29.jpg/1280px-Feu_%285061986490%29.jpg",
        "fallback": "https://images.unsplash.com/photo-1594998893017-36147cbcae05?w=1200&q=85"
    },
    "DISH_003": {
        "name": "Bún chả",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/B%C3%BAn_ch%E1%BA%A3_Vietnamese_food.jpg",
        "fallback": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=1200&q=85"
    },
    "DISH_004": {
        "name": "Bánh mì",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/66/Banh_mi_PaMi_1.jpg",
        "fallback": "https://images.unsplash.com/photo-1626804475297-41608ea09aeb?w=1200&q=85"
    },
    "DISH_005": {
        "name": "Bún thang",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/64/B%C3%BAn_thang.JPG",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Bun_Thang_-_Vietnamese_egg_and_pork_soup_with_shrimp_paste.jpg"
    },
    "DISH_006": {
        "name": "Bún đậu mắm tôm",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/B%C3%BAn_%C4%91%E1%BA%ADu_m%E1%BA%AFm_t%C3%B4m%2C_b%C3%BAn_nem_r%C3%A1n.JPG",
        "fallback": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&q=85"
    },
    "DISH_007": {
        "name": "Nem rán",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Ch%E1%BA%A3_gi%C3%B2_%28Vietnamese_Spring_Rolls%29_-_12.jpg/1280px-Ch%E1%BA%A3_gi%C3%B2_%28Vietnamese_Spring_Rolls%29_-_12.jpg",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Cha_gio.jpg"
    },
    "DISH_008": {
        "name": "Chả cá",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/02/Cha_ca_La_Vong.jpg",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Ch%E1%BA%A3_c%C3%A1_L%C3%A3_V%E1%BB%8Dng.jpg"
    },
    "DISH_009": {
        "name": "Bánh cuốn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Banh_cuon.jpg",
        "fallback": "https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4e/Banh_Cuon_2.jpg/1280px-Banh_Cuon_2.jpg"
    },
    "DISH_010": {
        "name": "Cà phê trứng",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/22/C%C3%A0_ph%C3%AA_tr%E1%BB%A9ng.jpg",
        "fallback": "https://thumb.wikimedia.org/wikipedia/commons/thumb/4/41/C%C3%80_PH%C3%8A_KEM_TR%E1%BB%A8NG_%28Egg_cream_coffee%29.jpg/1280px-C%C3%80_PH%C3%8A_KEM_TR%E1%BB%A8NG_%28Egg_cream_coffee%29.jpg"
    },
    "DISH_011": {
        "name": "Bún riêu",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Bun_Rieu_close-up_-_Dakao_Hoang.jpg/1280px-Bun_Rieu_close-up_-_Dakao_Hoang.jpg",
        "fallback": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&q=85"
    },
    "DISH_012": {
        "name": "Bún ốc",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Bun_oc_Hoe_Nhai.JPG",
        "fallback": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1200&q=85"
    },
    "DISH_013": {
        "name": "Miến lươn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Mien_luon_Hang_Dieu.JPG",
        "fallback": "https://images.unsplash.com/photo-1555126634-323283e090fa?w=1200&q=85"
    },
    "DISH_014": {
        "name": "Bánh gối",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/99/Banh_goi_01.JPG",
        "fallback": "https://images.unsplash.com/photo-1541592106381-b31e9677c0e5?w=1200&q=85"
    },
    "DISH_015": {
        "name": "Bánh tôm",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/L%E1%BB%85_h%E1%BB%99i_%E1%BA%A9m_th%E1%BB%B1c_C%E1%BB%ADa_Vi%E1%BB%87t_th4n2023_%C4%91%E1%BA%B7c_s%E1%BA%A3n_b%C3%A1nh_t%C3%B4m_H%E1%BB%93_T%C3%A2y_%2810%29.jpg/1280px-L%E1%BB%85_h%E1%BB%99i_%E1%BA%A9m_th%E1%BB%B1c_C%E1%BB%ADa_Vi%E1%BB%87t_th4n2023_%C4%91%E1%BA%B7c_s%E1%BA%A3n_b%C3%A1nh_t%C3%B4m_H%E1%BB%93_T%C3%A2y_%2810%29.jpg",
        "fallback": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=1200&q=85"
    },
    "DISH_016": {
        "name": "Xôi xéo",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f9/X%C3%B4i_x%C3%A9o.jpg",
        "fallback": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=1200&q=85"
    },
    "DISH_017": {
        "name": "Mì vằn thắn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Wonton_noodles_in_broth.jpg/1280px-Wonton_noodles_in_broth.jpg",
        "fallback": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&q=85"
    },
    "DISH_018": {
        "name": "Cháo sườn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Doujiang_and_youtiao_Taipei.jpg/1280px-Doujiang_and_youtiao_Taipei.jpg",
        "fallback": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?w=1200&q=85"
    },
    "DISH_019": {
        "name": "Bún ngan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/55/Ngan_Bun_Klang_Ban_01.jpg",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/9/90/Ngan_Bun_Klang_Ban_04.jpg"
    },
    "DISH_020": {
        "name": "Bánh đúc nóng",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Banh_te_My_Duc_2.png/1280px-Banh_te_My_Duc_2.png",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Banh_te_My_Duc.png"
    },
    "DISH_021": {
        "name": "Phở cuốn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Vietnamese_Fresh_Spring_Rolls.jpg/1280px-Vietnamese_Fresh_Spring_Rolls.jpg",
        "fallback": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&q=85"
    },
    "DISH_022": {
        "name": "Phở chiên phồng",
        "url": "https://images.unsplash.com/photo-1555126634-323283e090fa?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=1200&q=85"
    },
    "DISH_023": {
        "name": "Phở trộn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Ph%E1%BB%9F_tr%E1%BB%99n_n%C6%B0%E1%BB%9Bc_t%C6%B0%C6%A1ng_t%C3%A0u_%28th%E1%BB%A9c_%C4%83n_nhanh%29_%283%29.jpg/1280px-thumbnail.jpg",
        "fallback": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&q=85"
    },
    "DISH_024": {
        "name": "Bún bò Huế",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Bun-Bo-Hue-from-Huong-Giang-2011.jpg",
        "fallback": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=1200&q=85"
    },
    "DISH_025": {
        "name": "Bánh giò",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Banh-gio-viet-nam.jpg",
        "fallback": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&q=85"
    },
    "DISH_026": {
        "name": "Nộm bò khô",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Goi_du_du_bo_kho.jpg/1280px-Goi_du_du_bo_kho.jpg",
        "fallback": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1200&q=85"
    },
    "DISH_027": {
        "name": "Bún dọc mùng",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/B%C3%BAn_c%C3%A1.JPG/1280px-B%C3%BAn_c%C3%A1.JPG",
        "fallback": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&q=85"
    },
    "DISH_028": {
        "name": "Bánh khúc",
        "url": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&q=85"
    },
    "DISH_029": {
        "name": "Bánh đa cua",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/81/BANH_DA_CUA_1.jpg",
        "fallback": "https://upload.wikimedia.org/wikipedia/commons/d/d1/BANH_DA_CUA_2.jpg"
    },
    "DISH_030": {
        "name": "Chả rươi",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/15/Cha_ruoi.JPG",
        "fallback": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&q=85"
    },
    "DISH_031": {
        "name": "Chè sen long nhãn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/L%E1%BB%85_h%E1%BB%99i_%E1%BA%A9m_th%E1%BB%B1c_C%E1%BB%ADa_Vi%E1%BB%87t_th4n2023_%C4%91%E1%BA%B7c_s%E1%BA%A3n_m%C3%B3n_ch%C3%A8_Hu%E1%BA%BF_%28ch%C3%A8_h%E1%BA%A1t_sen%29_%282%29.jpg/1280px-thumbnail.jpg",
        "fallback": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=1200&q=85"
    },
    "DISH_032": {
        "name": "Bún cá",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/B%C3%BAn_C%C3%A1_H%C3%A0_N%E1%BB%99i.jpg/1280px-B%C3%BAn_C%C3%A1_H%C3%A0_N%E1%BB%99i.jpg",
        "fallback": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&q=85"
    },
    "DISH_033": {
        "name": "Lẩu riêu cua bắp bò",
        "url": "https://images.unsplash.com/photo-1547928576-a4a33237cbc3?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&q=85"
    },
    "DISH_034": {
        "name": "Bánh tráng nướng",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Banh_trang_nuong_dalat.jpg",
        "fallback": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=1200&q=85"
    },
    "DISH_035": {
        "name": "Bánh tráng trộn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Banh_trang_tron_%28mua_tai_truong_thpt_giadinh%29.jpg/1280px-Banh_trang_tron_%28mua_tai_truong_thpt_giadinh%29.jpg",
        "fallback": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=1200&q=85"
    },
    "DISH_036": {
        "name": "Nem chua rán",
        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a1/B%C3%BAn_nem.jpg",
        "fallback": "https://images.unsplash.com/photo-1541592106381-b31e9677c0e5?w=1200&q=85"
    },
    "DISH_037": {
        "name": "Chim quay",
        "url": "https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&q=85"
    },
    "DISH_038": {
        "name": "Gà tần thuốc bắc",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/G%C3%A0_t%E1%BA%A7n_thu%E1%BB%91c_b%E1%BA%AFc_m%C3%B3n_ngon_b%E1%BB%95_d%C6%B0%E1%BB%A1ng.jpg/1280px-G%C3%A0_t%E1%BA%A7n_thu%E1%BB%91c_b%E1%BA%AFc_m%C3%B3n_ngon_b%E1%BB%95_d%C6%B0%E1%BB%A1ng.jpg",
        "fallback": "https://images.unsplash.com/photo-1547928576-a4a33237cbc3?w=1200&q=85"
    },
    "DISH_039": {
        "name": "Cơm tấm",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Com-Tam-2008.jpg",
        "fallback": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=1200&q=85"
    },
    "DISH_040": {
        "name": "Bún chả cá",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Bun_cha_ca_nha_trang.jpg/1280px-Bun_cha_ca_nha_trang.jpg",
        "fallback": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=1200&q=85"
    },
    "DISH_041": {
        "name": "Bánh bao hấp",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/B%C3%A1nh_bao.jpg/1280px-B%C3%A1nh_bao.jpg",
        "fallback": "https://images.unsplash.com/photo-1541592106381-b31e9677c0e5?w=1200&q=85"
    },
    "DISH_042": {
        "name": "Cháo lòng",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/82/Ch%C3%A1o_l%C3%B2ng.jpg",
        "fallback": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?w=1200&q=85"
    },
    "DISH_043": {
        "name": "Lòng dồi rán",
        "url": "https://images.unsplash.com/photo-1544025162-d76694265947?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?w=1200&q=85"
    },
    "DISH_044": {
        "name": "Bánh bèo",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Banh_beo_Thien_Mu.jpg/1280px-Banh_beo_Thien_Mu.jpg",
        "fallback": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&q=85"
    },
    "DISH_045": {
        "name": "Nem lụi",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/AE_li%C3%AAn_hoan%2C_Nem_l%E1%BB%A5i_%E1%BB%9F_B%C3%ACnh_T%C3%A2y%2C_ng8th2n2020_%281%29.jpg/960px-AE_li%C3%AAn_hoan%2C_Nem_l%E1%BB%A5i_%E1%BB%9F_B%C3%ACnh_T%C3%A2y%2C_ng8th2n2020_%281%29.jpg",
        "fallback": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=1200&q=85"
    },
    "DISH_046": {
        "name": "Bánh xèo",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/B%C3%A1nh_x%C3%A8o_1.jpg/1280px-B%C3%A1nh_x%C3%A8o_1.jpg",
        "fallback": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&q=85"
    },
    "DISH_047": {
        "name": "Chè khúc bạch",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Ch%C3%A8_kh%C3%BAc_b%E1%BA%A1ch_%E1%BB%9F_qu%C3%A1n_Th%E1%BA%A3o_Vy_2020_09_06.jpg/1280px-Ch%C3%A8_kh%C3%BAc_b%E1%BA%A1ch_%E1%BB%9F_qu%C3%A1n_Th%E1%BA%A3o_Vy_2020_09_06.jpg",
        "fallback": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=1200&q=85"
    },
    "DISH_048": {
        "name": "Tào phớ",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Ch%C3%A8_xo%C3%A0i.jpg",
        "fallback": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=1200&q=85"
    },
    "DISH_049": {
        "name": "Cốm xào",
        "url": "https://images.unsplash.com/photo-1512058564366-18510be2db19?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&q=85"
    },
    "DISH_050": {
        "name": "Bánh chưng rán",
        "url": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=1200&q=85",
        "fallback": "https://images.unsplash.com/photo-1541592106381-b31e9677c0e5?w=1200&q=85"
    }
}

headers = {
    'User-Agent': 'VanMieuCulinaryGuide/2.0 (https://vanmieu.hanoi.vn; contact@vanmieu.hanoi.vn) Python-urllib/3.13'
}

out_dir = 'public/images/dishes'
os.makedirs(out_dir, exist_ok=True)

final_dish_map = {}

for did, item in DISH_IMAGES.items():
    name = item['name']
    out_file = os.path.join(out_dir, f"{did}.jpg")
    url = item['url']
    fallback = item['fallback']
    
    downloaded = False
    chosen_url = url
    
    for target in [url, fallback]:
        try:
            time.sleep(0.3)
            req = urllib.request.Request(target, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
                if resp.status == 200:
                    data = resp.read()
                    if len(data) > 10000: # at least 10KB
                        with open(out_file, 'wb') as f:
                            f.write(data)
                        downloaded = True
                        chosen_url = target
                        print(f"[{did}] {name}: SUCCESS ({len(data) // 1024} KB) from {target[:50]}...")
                        break
        except Exception as e:
            # print(f"  Failed {target[:50]}: {e}")
            pass
            
    if not downloaded:
        print(f"[{did}] {name}: FAILED BOTH URLS")
    
    final_dish_map[did] = {
        'name': name,
        'local_path': f"/images/dishes/{did}.jpg",
        'online_url': chosen_url,
        'downloaded': downloaded
    }

with open('scripts/dishes_downloaded.json', 'w', encoding='utf-8') as f:
    json.dump(final_dish_map, f, ensure_ascii=False, indent=2)

print("\n--- Summary ---")
succ = sum(1 for v in final_dish_map.values() if v['downloaded'])
print(f"Total downloaded: {succ} / {len(final_dish_map)}")

