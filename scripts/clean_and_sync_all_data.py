import json
import os
import shutil

with open('src/data/foodMapData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. DISHES: Keep existing valid news source and online_image_url
for dish in data.get('dishes', []):
    did = dish['dish_id']
    dish['image_url'] = f"/images/dishes/{did}.jpg"
    if not dish.get('image_source'):
        dish['image_source'] = "Báo VnExpress (Ẩm thực & Đời sống)"

# 2. CLEAN PLACES AND OFFERINGS
for place in data.get('places', []):
    pid = place['place_id']
    place['image_url'] = f"/images/places/{pid}.jpg"
    
    if not place.get('image_source') or 'unsplash' in place.get('image_source', '').lower():
        place['image_source'] = f"Foody / Google Maps - {place['name']} ({place.get('address', '')})"
        
    if 'unsplash' in place.get('online_image_url', ''):
        place['online_image_url'] = f"/images/places/{pid}.jpg"

    for off in place.get('dishes', []):
        oid = off.get('offering_id')
        menu_name = off.get('menu_item_name_vi') or off.get('dish_name_vi')
        
        off['image_url'] = f"/images/offerings/{oid}.jpg"
        if not off.get('image_source'):
            off['image_source'] = f"{place['name']} - {menu_name}"
            
        if 'unsplash' in off.get('online_image_url', ''):
            off['online_image_url'] = f"/images/offerings/{oid}.jpg"

# Write cleaned foodMapData.json
with open('src/data/foodMapData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("foodMapData.json verified clean!")

# 3. SYNC IMAGES TO dist/images/
for folder in ['dishes', 'places', 'offerings']:
    src_dir = os.path.join('public', 'images', folder)
    dst_dir = os.path.join('dist', 'images', folder)
    os.makedirs(dst_dir, exist_ok=True)
    if os.path.exists(src_dir):
        count = 0
        for fname in os.listdir(src_dir):
            if fname.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                src_file = os.path.join(src_dir, fname)
                dst_file = os.path.join(dst_dir, fname)
                shutil.copy2(src_file, dst_file)
                count += 1
        print(f"Synced public/images/{folder} -> dist/images/{folder} ({count} files)")

print("Synchronization completely SUCCESSFUL!")
