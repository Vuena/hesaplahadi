import os
import glob
import re

DRAWER_HTML = """
    <!-- Mobile Sidebar Drawer -->
    <div id="drawer-mask" class="fixed inset-0 bg-black/50 z-[60] transition-opacity duration-300 mask-hidden" onclick="toggleDrawer()"></div>
    <aside id="drawer" class="fixed top-0 left-0 w-64 h-full bg-white z-[70] shadow-2xl transition-transform duration-300 drawer-closed overflow-y-auto">
        <div class="p-4 border-b border-slate-100 flex justify-between items-center">
             <span class="font-bold text-lg text-slate-800">Hesaplama Araçları</span>
             <button onclick="toggleDrawer()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-times text-xl"></i></button>
        </div>
        <div id="drawer-list" class="p-3 space-y-1">
            <!-- Populated by JS -->
        </div>
    </aside>
"""

def inject_drawer():
    files = glob.glob('*.html')
    for filepath in files:
        if filepath == 'index.html':
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'id="drawer"' in content:
            print(f"Skipping {filepath} (Drawer already exists)")
            continue

        # Inject after <body ...>
        # Regex to find <body ...> tag
        match = re.search(r'<body[^>]*>', content)
        if match:
            print(f"Injecting drawer into {filepath}")
            body_tag = match.group(0)
            new_content = content.replace(body_tag, body_tag + "\n" + DRAWER_HTML)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        else:
            print(f"Warning: Could not find <body> tag in {filepath}")

if __name__ == "__main__":
    inject_drawer()
