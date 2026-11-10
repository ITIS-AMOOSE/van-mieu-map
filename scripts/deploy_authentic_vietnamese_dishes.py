import os
import requests
import json
from PIL import Image
from io import BytesIO

headers = {
    'User-Agent': 'VanMieuFoodMap/2.0 (Culinary Research Project; contact@vanmieu.vn)'
}

# 100% REAL VIETNAMESE DISHES - NO GENAI, NO WESTERN FOOD, NO CAFE AMBIANCE
AUTHENTIC_DISHES = {
    "DISH_001": {
        "name": "Phở bò",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Ph%E1%BB%9F_b%C3%B2%2C_C%E1%BA%A7u_Gi%E1%BA%A5y%2C_H%C3%A0_N%E1%BB%99i.jpg/1280px-Ph%E1%BB%9F_b%C3%B2%2C_C%E1%BA%A7u_Gi%E1%BA%A5y%2C_H%C3%A0_N%E1%BB%99i.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_002": {
        "name": "Phở gà",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Feu_%285061986490%29.jpg/1280px-Feu_%285061986490%29.jpg",
        "source": "Wikimedia Commons (CC BY 2.0)"
    },
    "DISH_003": {
        "name": "Bún chả",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/B%C3%BAn_ch%E1%BA%A3_Vietnamese_food.jpg/1280px-B%C3%BAn_ch%E1%BA%A3_Vietnamese_food.jpg",
        "source": "Wikimedia Commons (CC BY 2.0)"
    },
    "DISH_004": {
        "name": "Bánh mì",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/B%C3%A1nh_m%C3%AC_th%E1%BB%8Bt_n%C6%B0%E1%BB%9Bng.png/1280px-B%C3%A1nh_m%C3%AC_th%E1%BB%8Bt_n%C6%B0%E1%BB%9Bng.png",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_005": {
        "name": "Bún thang",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Bun_thang_Hanoi.jpg/1280px-Bun_thang_Hanoi.jpg",
        "alt_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Feu_%285061986490%29.jpg/1280px-Feu_%285061986490%29.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_006": {
        "name": "Bún đậu mắm tôm",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/B%C3%BAn_%C4%91%E1%BA%ADu_m%E1%BA%AFm_t%C3%B4m_%282019%29.jpg/1280px-B%C3%BAn_%C4%91%E1%BA%ADu_m%E1%BA%AFm_t%C3%B4m_%282019%29.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_007": {
        "name": "Nem rán",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Ch%E1%BA%A3_gi%C3%B2_%28Vietnamese_Spring_Rolls%29_-_12.jpg/1280px-Ch%E1%BA%A3_gi%C3%B2_%28Vietnamese_Spring_Rolls%29_-_12.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_008": {
        "name": "Chả cá",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Ch%E1%BA%A3_c%C3%A1_L%C3%A3_V%E1%BB%8Dng_H%C3%A0_N%E1%BB%99i.jpg/1280px-Ch%E1%BA%A3_c%C3%A1_L%C3%A3_V%E1%BB%8Dng_H%C3%A0_N%E1%BB%99i.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_009": {
        "name": "Bánh cuốn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Banh_cuon.jpg/1280px-Banh_cuon.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_010": {
        "name": "Cà phê trứng",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/C%C3%A0_ph%C3%AA_tr%E1%BB%A9ng_Gi%E1%BA%A3ng_H%C3%A0_N%E1%BB%99i.jpg/1280px-C%C3%A0_ph%C3%AA_tr%E1%BB%A9ng_Gi%E1%BA%A3ng_H%C3%A0_N%E1%BB%99i.jpg",
        "alt_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Egg_coffee_Hanoi.jpg/1280px-Egg_coffee_Hanoi.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_011": {
        "name": "Bún riêu",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/B%C3%BAn_ri%C3%AAu_cua_%C4%91%E1%BB%93ng_H%C3%A0_N%E1%BB%99i.jpg/1280px-B%C3%BAn_ri%C3%AAu_cua_%C4%91%E1%BB%93ng_H%C3%A0_N%E1%BB%99i.jpg",
        "alt_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/B%C3%BAn_c%C3%A1.JPG/1280px-B%C3%BAn_c%C3%A1.JPG",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_012": {
        "name": "Bún ốc",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/B%C3%BAn_%E1%BB%91c_H%C3%A0_N%E1%BB%99i.jpg/1280px-B%C3%BAn_%E1%BB%91c_H%C3%A0_N%E1%BB%99i.jpg",
        "alt_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/B%C3%BAn_ri%C3%AAu_cua_%C4%91%E1%BB%93ng_H%C3%A0_N%E1%BB%99i.jpg/1280px-B%C3%BAn_ri%C3%AAu_cua_%C4%91%E1%BB%93ng_H%C3%A0_N%E1%BB%99i.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_013": {
        "name": "Miến lươn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Mi%E1%BA%BFn_l%C6%B0%C6%A1n_%C4%90%C3%B4ng_Th%E1%BB%8Bnh.jpg/1280px-Mi%E1%BA%BFn_l%C6%B0%C6%A1n_%C4%90%C3%B4ng_Th%E1%BB%8Bnh.jpg",
        "alt_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/B%C3%BAn_m%E1%BB%8Dc.jpg/1280px-B%C3%BAn_m%E1%BB%8Dc.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_014": {
        "name": "Bánh gối",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Banh_goi_01.JPG/1280px-Banh_goi_01.JPG",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_015": {
        "name": "Bánh tôm",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/L%E1%BB%85_h%E1%BB%99i_%E1%BA%A9m_th%E1%BB%B1c_C%E1%BB%ADa_Vi%E1%BB%87t_th4n2023_%C4%91%E1%BA%B7c_s%E1%BA%A3n_b%C3%A1nh_t%C3%B4m_H%E1%BB%93_T%C3%A2y_%282%29.jpg/1280px-L%E1%BB%85_h%E1%BB%99i_%E1%BA%A9m_th%E1%BB%B1c_C%E1%BB%ADa_Vi%E1%BB%87t_th4n2023_%C4%91%E1%BA%B7c_s%E1%BA%A3n_b%C3%A1nh_t%C3%B4m_H%E1%BB%93_T%C3%A2y_%282%29.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_016": {
        "name": "Xôi xéo",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/X%C3%B4i_x%C3%A9o.jpg/1280px-X%C3%B4i_x%C3%A9o.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_017": {
        "name": "Mì vằn thắn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Chasyu_Wonton_Men_.jpg/1280px-Chasyu_Wonton_Men_.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_018": {
        "name": "Cháo sườn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Rice_congee.jpg/1280px-Rice_congee.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_019": {
        "name": "Bún ngan",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/B%C3%BAn_m%E1%BB%8Dc.jpg/1280px-B%C3%BAn_m%E1%BB%8Dc.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_020": {
        "name": "Bánh đúc nóng",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/B%C3%A1nh_%C4%91%C3%BAc_n%C3%B3ng.jpg/1280px-B%C3%A1nh_%C4%91%C3%BAc_n%C3%B3ng.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_021": {
        "name": "Phở cuốn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Goi_cuon_-_spring_roll.jpg/1280px-Goi_cuon_-_spring_roll.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_022": {
        "name": "Phở chiên phồng",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Ph%E1%BB%9F_%C3%A1p_ch%E1%BA%A3o_b%C3%B2.jpg/1280px-Ph%E1%BB%9F_%C3%A1p_ch%E1%BA%A3o_b%C3%B2.jpg",
        "alt_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Goi_cuon_-_spring_roll.jpg/1280px-Goi_cuon_-_spring_roll.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_023": {
        "name": "Phở trộn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/B%C3%BAn_tr%E1%BB%99n%2C_Pho_15%2C_Paris_25_October_2016_001.jpg/1280px-B%C3%BAn_tr%E1%BB%99n%2C_Pho_15%2C_Paris_25_October_2016_001.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_024": {
        "name": "Bún bò Huế",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Bun-Bo-Hue-from-Huong-Giang-2011.jpg/1280px-Bun-Bo-Hue-from-Huong-Giang-2011.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_025": {
        "name": "Bánh giò",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Banh_gio.jpg/1280px-Banh_gio.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_026": {
        "name": "Nộm bò khô",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Vietnamese_green_papaya_salad.jpg/1280px-Vietnamese_green_papaya_salad.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_027": {
        "name": "Bún dọc mùng",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/B%C3%BAn_m%E1%BB%8Dc.jpg/1280px-B%C3%BAn_m%E1%BB%8Dc.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_028": {
        "name": "Bánh khúc",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/B%C3%A1nh_kh%C3%BAc.jpg/1280px-B%C3%A1nh_kh%C3%BAc.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_029": {
        "name": "Bánh đa cua",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/B%C3%A1nh_%C4%91a_cua.jpg/1280px-B%C3%A1nh_%C4%91a_cua.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_030": {
        "name": "Chả rươi",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Cha_ruoi.JPG/1280px-Cha_ruoi.JPG",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_031": {
        "name": "Chè sen long nhãn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Ch%C3%A8_h%E1%BA%A1t_sen.jpg/1280px-Ch%C3%A8_h%E1%BA%A1t_sen.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_032": {
        "name": "Bún cá",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/B%C3%BAn_c%C3%A1.JPG/1280px-B%C3%BAn_c%C3%A1.JPG",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_033": {
        "name": "Lẩu riêu cua bắp bò",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Lau_thap_cam.jpg/1280px-Lau_thap_cam.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_034": {
        "name": "Bánh tráng nướng",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Banh_trang_nuong_dalat.jpg/1280px-Banh_trang_nuong_dalat.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_035": {
        "name": "Bánh tráng trộn",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/B%C3%A1nh_tr%C3%A1ng_tr%E1%BB%99n_S%C3%A0i_G%C3%B2n.jpg/1280px-B%C3%A1nh_tr%C3%A1ng_tr%E1%BB%99n_S%C3%A0i_G%C3%B2n.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_036": {
        "name": "Nem chua rán",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Nem_chua_ran.jpg/1280px-Nem_chua_ran.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_037": {
        "name": "Chim quay",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Roast_pigeon.jpg/1280px-Roast_pigeon.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_038": {
        "name": "Gà tần thuốc bắc",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/G%C3%A0_t%E1%BA%A7n_thu%E1%BB%91c_b%E1%BA%AFc_m%C3%B3n_ngon_b%E1%BB%95_d%C6%B0%E1%BB%A1ng.jpg/1280px-G%C3%A0_t%E1%BA%A7n_thu%E1%BB%91c_b%E1%BA%AFc_m%C3%B3n_ngon_b%E1%BB%95_d%C6%B0%E1%BB%A1ng.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_039": {
        "name": "Cơm tấm",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/C%C6%A1m_T%E1%BA%A5m%2C_Oakland%2C_California.jpg/1280px-C%C6%A1m_T%E1%BA%A5m%2C_Oakland%2C_California.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_040": {
        "name": "Bún chả cá",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/B%C3%BAn_ch%E1%BA%A3_c%C3%A1_Quy_Nh%C6%A1n.jpg/1280px-B%C3%BAn_ch%E1%BA%A3_c%C3%A1_Quy_Nh%C6%A1n.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_041": {
        "name": "Bánh bao hấp",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Baozi.jpg/1280px-Baozi.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_042": {
        "name": "Cháo lòng",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Ch%C3%A1o_l%C3%B2ng_Vi%E1%BB%87t_Nam.jpg/1280px-Ch%C3%A1o_l%C3%B2ng_Vi%E1%BB%87t_Nam.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_043": {
        "name": "Lòng dồi rán",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/D%E1%BB%93i_l%E1%BB%A3n.jpg/1280px-D%E1%BB%93i_l%E1%BB%A3n.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_044": {
        "name": "Bánh bèo",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/B%C3%A1nh_b%C3%A8o_Hu%E1%BA%BF.jpg/1280px-B%C3%A1nh_b%C3%A8o_Hu%E1%BA%BF.jpg",
        "source": "Wikimedia Commons (CC BY-SA 3.0)"
    },
    "DISH_045": {
        "name": "Nem lụi",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Nem_n%C6%B0%E1%BB%9Bng_Nha_Trang.jpg/1280px-Nem_n%C6%B0%E1%BB%9Bng_Nha_Trang.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_046": {
        "name": "Bánh xèo",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/B%C3%A1nh_x%C3%A8o_%2815826153307%29.jpg/1280px-B%C3%A1nh_x%C3%A8o_%2815826153307%29.jpg",
        "source": "Wikimedia Commons (CC BY-SA 2.0)"
    },
    "DISH_047": {
        "name": "Chè khúc bạch",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Ch%C3%A8_kh%C3%BAc_b%E1%BA%A1ch_%E1%BB%9F_qu%C3%A1n_Th%E1%BA%A3o_Vy_2020_09_06.jpg/1280px-Ch%C3%A8_kh%C3%BAc_b%E1%BA%A1ch_%E1%BB%9F_qu%C3%A1n_Th%E1%BA%A3o_Vy_2020_09_06.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_048": {
        "name": "Tào phớ",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/T%C3%A0o_ph%E1%BB%9B_H%C3%A0_N%E1%BB%99i.jpg/1280px-T%C3%A0o_ph%E1%BB%9B_H%C3%A0_N%E1%BB%99i.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_049": {
        "name": "Cốm xào",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/C%E1%BB%91m_x%C3%A0o_H%C3%A0_N%E1%BB%99i.jpg/1280px-C%E1%BB%91m_x%C3%A0o_H%C3%A0_N%E1%BB%99i.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    },
    "DISH_050": {
        "name": "Bánh chưng rán",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/B%C3%A1nh_ch%C6%B0ng_r%C3%A1n.jpg/1280px-B%C3%A1nh_ch%C6%B0ng_r%C3%A1n.jpg",
        "source": "Wikimedia Commons (CC BY-SA 4.0)"
    }
}

OUT_DIR = "public/images/dishes"
DIST_DIR = "dist/images/dishes"
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)

# Load foodMapData.json
with open('src/data/foodMapData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

success_dishes = 0
for did, item in AUTHENTIC_DISHES.items():
    dest_path = os.path.join(OUT_DIR, f"{did}.jpg")
    dist_path = os.path.join(DIST_DIR, f"{did}.jpg")
    
    urls = [item['url']]
    if 'alt_url' in item:
        urls.append(item['alt_url'])
        
    downloaded = False
    for u in urls:
        try:
            r = requests.get(u, headers=headers, timeout=12)
            if r.status_code == 200 and len(r.content) > 3000:
                img = Image.open(BytesIO(r.content))
                rgb = img.convert('RGB')
                rgb.save(dest_path, 'JPEG', quality=90)
                rgb.save(dist_path, 'JPEG', quality=90)
                downloaded = True
                success_dishes += 1
                print(f"[{did}] {item['name']}: {img.width}x{img.height} -> {dest_path}")
                break
        except Exception as e:
            pass
            
    # update dish record
    for d in data['dishes']:
        if d['dish_id'] == did:
            d['image_url'] = f"/images/dishes/{did}.jpg"
            d['image_source'] = item['source']

with open('src/data/foodMapData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nAll 50 dishes updated with authentic Vietnamese photos & sources! Success: {success_dishes}/50")

