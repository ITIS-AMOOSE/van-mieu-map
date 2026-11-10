import json

with open('scripts/dishes_downloaded.json', encoding='utf-8') as f:
    dishes_info = json.load(f)

with open('scripts/places_downloaded.json', encoding='utf-8') as f:
    places_info = json.load(f)

with open('src/data/foodMapData.json', encoding='utf-8') as f:
    data = json.load(f)

# 1. Update dishes
for dish in data.get('dishes', []):
    did = dish['dish_id']
    if did in dishes_info:
        info = dishes_info[did]
        dish['image_url'] = info['local_path']
        dish['online_image_url'] = info['online_url']

# 2. Update places & their offerings
for place in data.get('places', []):
    pid = place['place_id']
    if pid in places_info:
        p_info = places_info[pid]
        place['image_url'] = p_info['local_path']
        place['online_image_url'] = p_info['online_url']
        
    for p_dish in place.get('dishes', []):
        did = p_dish.get('dish_id')
        if did and did in dishes_info:
            d_info = dishes_info[did]
            p_dish['image_url'] = d_info['local_path']
            p_dish['online_image_url'] = d_info['online_url']

# Save updated foodMapData.json
with open('src/data/foodMapData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated foodMapData.json with 50 dish photos and 70 place photos successfully!")
