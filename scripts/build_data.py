import json
import os
import math

with open(r'E:\Demo Văn Miếu\Demo Văn Miếu\van_mieu_foods_combined.json', encoding='utf-8') as f:
    raw_data = json.load(f)

places = raw_data['relational_tables']['places']
dishes = raw_data['relational_tables']['dishes']
offerings = raw_data['relational_tables']['offerings']
ingredients = raw_data['relational_tables']['ingredients']
sources = raw_data['relational_tables']['sources']
guide = raw_data['hierarchical_food_guide']

# Create lookup
source_map = {s['source_id']: s for s in sources}
dish_map = {d['dish_id']: d for d in dishes}
place_map = {p['place_id']: p for p in places}

# Group ingredients by dish_id
dish_ing_map = {}
for ing in ingredients:
    did = ing['dish_id']
    dish_ing_map.setdefault(did, []).append(ing)

# Group offerings by place_id and dish_id
place_offerings_map = {}
dish_offerings_map = {}
for off in offerings:
    pid = off['place_id']
    did = off['dish_id']
    place_offerings_map.setdefault(pid, []).append(off)
    dish_offerings_map.setdefault(did, []).append(off)

# Category definitions
CATEGORY_META = {
    'noodle_soup': {'label': 'Phở & Bún nước', 'icon': '🍜', 'color': '#c2410c'},
    'grilled': {'label': 'Bún chả & Nướng', 'icon': '🍢', 'color': '#b45309'},
    'rolled': {'label': 'Món cuốn', 'icon': '🌯', 'color': '#059669'},
    'fried': {'label': 'Món chiên & Rán', 'icon': '🥟', 'color': '#d97706'},
    'steamed': {'label': 'Món hấp & Bánh giò', 'icon': '🥠', 'color': '#7c3aed'},
    'rice': {'label': 'Cơm & Xôi', 'icon': '🍚', 'color': '#ea580c'},
    'sandwich': {'label': 'Bánh mì', 'icon': '🥖', 'color': '#ca8a04'},
    'snack': {'label': 'Ăn vặt & Quà chiều', 'icon': '🍢', 'color': '#e11d48'},
    'sweet_soup': {'label': 'Chè & Tráng miệng', 'icon': '🍧', 'color': '#db2777'},
    'drink': {'label': 'Cà phê & Đồ uống', 'icon': '☕', 'color': '#9333ea'},
    'salad': {'label': 'Nộm & Gỏi', 'icon': '🥗', 'color': '#16a34a'},
    'hotpot': {'label': 'Lẩu', 'icon': '🍲', 'color': '#dc2626'},
    'other': {'label': 'Đặc sản khác', 'icon': '🥢', 'color': '#475569'},
}

# Process places
enriched_places = []
for p in places:
    pid = p['place_id']
    p_offs = place_offerings_map.get(pid, [])
    p_dishes = []
    seen_dids = set()
    for off in p_offs:
        did = off['dish_id']
        d_info = dish_map.get(did, {})
        d_entry = {
            'dish_id': did,
            'dish_name_vi': d_info.get('name_vi', ''),
            'dish_name_en': d_info.get('name_en', ''),
            'category': d_info.get('category', 'other'),
            'image_url': d_info.get('image_url', ''),
            'offering_id': off.get('offering_id'),
            'menu_item_name_vi': off.get('menu_item_name_vi'),
            'price_min_vnd': off.get('price_min_vnd'),
            'price_max_vnd': off.get('price_max_vnd'),
            'variant': off.get('variant'),
            'portion': off.get('portion')
        }
        p_dishes.append(d_entry)
        seen_dids.add(did)
    
    # Primary category
    primary_cat = p_dishes[0]['category'] if p_dishes else 'other'
    
    enriched_places.append({
        'place_id': pid,
        'name': p['name'],
        'branch_name': p.get('branch_name', ''),
        'address': p.get('address', ''),
        'lat': float(p['lat']),
        'lng': float(p['lng']),
        'distance_m': round(float(p.get('distance_m', 0)), 1),
        'rating': float(p.get('rating') or 4.5),
        'review_count': int(p.get('review_count') or 50),
        'opening_hours': p.get('opening_hours_raw') or '07:00 - 21:00',
        'price_min_vnd': p.get('venue_price_min_vnd'),
        'price_max_vnd': p.get('venue_price_max_vnd'),
        'primary_category': primary_cat,
        'dishes': p_dishes,
        'dish_ids': list(seen_dids),
        'image_url': p_dishes[0]['image_url'] if p_dishes and p_dishes[0].get('image_url') else 'https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=600'
    })

# Process dishes with rich details from hierarchical guide
enriched_dishes = []
for d in dishes:
    did = d['dish_id']
    guide_match = next((g for g in guide if g['dish_id'] == did), {})
    d_ings = dish_ing_map.get(did, [])
    d_offs = dish_offerings_map.get(did, [])
    
    serving_place_ids = list(set(off['place_id'] for off in d_offs))
    serving_places = [
        {
            'place_id': pid,
            'name': place_map[pid]['name'],
            'address': place_map[pid].get('address', ''),
            'lat': float(place_map[pid]['lat']),
            'lng': float(place_map[pid]['lng']),
            'distance_m': round(float(place_map[pid].get('distance_m', 0)), 1),
            'rating': float(place_map[pid].get('rating') or 4.5),
            'opening_hours': place_map[pid].get('opening_hours_raw', '')
        }
        for pid in serving_place_ids if pid in place_map
    ]
    # Sort serving places by distance from Van Mieu
    serving_places.sort(key=lambda x: x['distance_m'])
    
    enriched_dishes.append({
        'dish_id': did,
        'name_vi': d['name_vi'],
        'name_en': d.get('name_en', ''),
        'aliases': d.get('aliases', []),
        'category': d.get('category', 'other'),
        'short_description_vi': d.get('short_description_vi', ''),
        'description_vi': d.get('description_vi', ''),
        'how_to_eat_vi': d.get('how_to_eat_vi', ''),
        'ordering_phrase_vi': d.get('ordering_phrase_vi', ''),
        'meal_times': d.get('meal_times') or [],
        'taste_profile': d.get('taste_profile') or [],
        'image_url': d.get('image_url', ''),
        'recipe_video_url': d.get('recipe_video_url', ''),
        'recipe_video_embed_url': d.get('recipe_video_embed_url', ''),
        'recipe_video_creator': d.get('recipe_video_creator', ''),
        'allergens_by_recipe': d.get('allergens_by_recipe') or [],
        'ingredients': d_ings,
        'serving_places': serving_places,
        'serving_places_count': len(serving_places),
        'min_distance_m': serving_places[0]['distance_m'] if serving_places else 9999
    })

# Hanoi Boundary
with open(r'E:\Demo Văn Miếu\hanoi_boundary.geojson', encoding='utf-8') as f:
    hanoi_geo = json.load(f)

# Survey Circle 2000m
def create_circle(center_lng, center_lat, radius_meters=2000, points=64):
    coords = []
    R = 6378137.0
    lat_rad = math.radians(center_lat)
    lng_rad = math.radians(center_lng)
    d = radius_meters / R
    for i in range(points + 1):
        bearing = 2 * math.pi * i / points
        pt_lat = math.asin(math.sin(lat_rad) * math.cos(d) + math.cos(lat_rad) * math.sin(d) * math.cos(bearing))
        pt_lng = lng_rad + math.atan2(math.sin(bearing) * math.sin(d) * math.cos(lat_rad),
                                     math.cos(d) - math.sin(lat_rad) * math.sin(pt_lat))
        coords.append([math.degrees(pt_lng), math.degrees(pt_lat)])
    return {
        'type': 'FeatureCollection',
        'features': [{
            'type': 'Feature',
            'properties': {'name': 'Vùng khảo sát 2km Văn Miếu', 'radius_m': radius_meters},
            'geometry': {'type': 'Polygon', 'coordinates': [coords]}
        }]
    }

circle_geo = create_circle(105.835953, 21.02879, 2000)

output_bundle = {
    'metadata': {
        'title': 'Bản đồ ẩm thực Hà Nội - Vùng khảo sát Văn Miếu Quốc Tử Giám',
        'center': {'lat': 21.02879, 'lng': 105.835953, 'title': 'Văn Miếu – Quốc Tử Giám'},
        'radius_limit_m': 2000,
        'total_places': len(enriched_places),
        'total_dishes': len(enriched_dishes),
        'total_ingredients': len(ingredients),
        'total_sources': len(sources)
    },
    'category_meta': CATEGORY_META,
    'places': enriched_places,
    'dishes': enriched_dishes,
    'hanoi_boundary': hanoi_geo,
    'survey_circle': circle_geo
}

os.makedirs(r'E:\Demo Văn Miếu\src\data', exist_ok=True)
with open(r'E:\Demo Văn Miếu\src\data\foodMapData.json', 'w', encoding='utf-8') as f:
    json.dump(output_bundle, f, ensure_ascii=False, indent=2)

print('Successfully exported foodMapData.json with:')
print('  Places:', len(enriched_places))
print('  Dishes:', len(enriched_dishes))
print('  Hanoi features:', len(hanoi_geo['features']))
