import os
import re

def update_ui(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Fix Logo Visibility on Mobile
    # Search for the logo container: <div class="block bg-gradient-to-br ...">
    # Replace 'block' with 'flex items-center justify-center' to ensure it's not hidden if block is manipulated by parent,
    # but more importantly, ensure the PARENT link or container doesn't have hidden.
    # Actually, the user said "En sol üstteki HesaplaHadi yazısının başına hesap makinası logomuzu tekrar koy."
    # and "mobilde gözükmüyor o ikon".
    # The provided file has `block`. We will change it to `flex items-center justify-center` to be safe and robust.

    logo_pattern = r'(<div class=")(block)( bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-2.5 rounded-xl group-hover:shadow-lg)'
    if re.search(logo_pattern, content):
        content = re.sub(logo_pattern, r'\1flex items-center justify-center\3', content)

    # Also ensure the icon is there
    # <i class="fa-solid fa-calculator text-lg"></i>
    # If the user says "tekrar koy", maybe it was removed? I'll assume it's there based on read_file.

    # 2. Fix Menu Button Clickability
    # <button class="md:hidden w-full mt-3 flex items-center justify-center gap-2 bg-gradient-to-r from-indigo-600 to-purple-700 text-white px-4 py-2.5 rounded-lg font-bold text-sm hover:from-indigo-700 hover:to-purple-800 transition shadow-sm" onclick="toggleDrawer()">
    # We want to add `relative z-30 cursor-pointer`

    btn_pattern = r'(<button class="md:hidden w-full mt-3 flex items-center justify-center gap-2 bg-gradient-to-r from-indigo-600 to-purple-700 text-white px-4 py-2.5 rounded-lg font-bold text-sm hover:from-indigo-700 hover:to-purple-800 transition shadow-sm)'
    if re.search(btn_pattern, content):
        content = re.sub(btn_pattern, r'\1 relative z-30 cursor-pointer', content)

    # 3. Fix Search Container Z-Index
    # <div class="md:hidden mt-3 relative group">
    # Change to <div class="md:hidden mt-3 relative group z-40">

    search_pattern = r'(<div class="md:hidden mt-3 relative group)'
    if re.search(search_pattern, content):
        # check if z-40 is already there
        if 'z-40' not in re.search(search_pattern, content).group(0):
             content = re.sub(search_pattern, r'\1 z-40', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes for {filepath}")

# Iterate all html files
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            update_ui(os.path.join(root, file))
