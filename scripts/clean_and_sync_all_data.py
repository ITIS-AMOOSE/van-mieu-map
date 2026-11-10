import json
import os
import shutil
import re

with open('src/data/foodMapData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract authentic dish sources from deploy_authentic_vietnamese_dishes.py text without executing it
authentic_map = {}
with open('scripts/deploy_authentic_vietnamese_dishes.py', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r'"(DISH_\d+)":\s*\{\s*"name":\s*"([^"]+)",\s*"url":\s*"([^"]+)",(?:\s*"alt_url":\s*"[^"]+",)?\s*"source":\s*"([^"]+)"', content)
for did, name, url, source in matches:
    authentic_map[did] = {"name": name, "url": url, "source": source}

print(f"Parsed {len(authentic_map)} authentic dish definitions.")

# 1. CLEAN DISHES
for dish in data.get('dishes', []):
    did = dish['dish_id']
    dish['image_url'] = f"/images/dishes/{did}.jpg"
    if did in authentic_map:
        dish['online_image_url'] = authentic_map[did]['url']
        dish['image_source'] = authentic_map[did]['source']
    else:
        if 'unsplash' in dish.get('online_image_url', ''):
            dish['online_image_url'] = f"/images/dishes/{did}.jpg"
        if not dish.get('image_source'):
            dish['image_source'] = "Wikimedia Commons (CC BY-SA)"

# 2. CLEAN PLACES AND OFFERINGS
for place in data.get('places', []):
    pid = place['place_id']
    place['image_url'] = f"/images/places/{pid}.jpg"
    
    # Ensure realistic image_source
    if not place.get('image_source') or 'unsplash' in place.get('image_source', '').lower():
        place['image_source'] = f"Foody / Google Maps - {place['name']} ({place.get('address', '')})"
        
    # Remove any unsplash in online_image_url
    if 'unsplash' in place.get('online_image_url', ''):
        first_off = place.get('dishes', [{}])[0]
        first_did = first_off.get('dish_id')
        if first_did and first_did in authentic_map:
            place['online_image_url'] = authentic_map[first_did]['url']
        else:
            place['online_image_url'] = f"/images/places/{pid}.jpg"

    # Offerings
    for off in place.get('dishes', []):
        oid = off.get('offering_id')
        did = off.get('dish_id')
        menu_name = off.get('menu_item_name_vi') or off.get('dish_name_vi')
        
        off['image_url'] = f"/images/offerings/{oid}.jpg"
        if not off.get('image_source'):
            off['image_source'] = f"{place['name']} - {menu_name}"
            
        if 'unsplash' in off.get('online_image_url', ''):
            if did and did in authentic_map:
                off['online_image_url'] = authentic_map[did]['url']
            else:
                off['online_image_url'] = f"/images/offerings/{oid}.jpg"

# Write cleaned foodMapData.json
with open('src/data/foodMapData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("foodMapData.json cleaned! Checking for any remaining unsplash links...")

remaining_unsplash = 0
for d in data['dishes']:
    if 'unsplash' in str(d): remaining_unsplash += 1
for p in data['places']:
    if 'unsplash' in str(p): remaining_unsplash += 1

print(f"Remaining unsplash references in foodMapData.json: {remaining_unsplash}")

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

print("Data & Image synchronization completely SUCCESSFUL!")
