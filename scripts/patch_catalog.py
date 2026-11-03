with open(r'E:\Demo Văn Miếu\Demo Văn Miếu\preview_catalog.html', 'r', encoding='utf-8') as f:
    c = f.read()

btn_html = '''                <a href="food_map_preview.html" target="_blank" class="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold rounded-lg bg-rose-700 hover:bg-rose-800 text-white shadow-sm transition">
                    <span>🗺️</span> Mở Bản Đồ Ẩm Thực (MapLibre)
                </a>\n'''

pos = c.find('<!-- Quick Action Buttons -->')
if pos != -1:
    div_pos = c.find('<div class="flex items-center gap-2">', pos)
    if div_pos != -1:
        insert_at = div_pos + len('<div class="flex items-center gap-2">\n')
        # Check if CRLF
        if c[div_pos + len('<div class="flex items-center gap-2">'):].startswith('\r\n'):
            insert_at = div_pos + len('<div class="flex items-center gap-2">\r\n')
        c = c[:insert_at] + btn_html + c[insert_at:]
        with open(r'E:\Demo Văn Miếu\Demo Văn Miếu\preview_catalog.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated preview_catalog.html successfully!")
    else:
        print("div not found")
else:
    print("comment not found")
