
import os
import re

# Define the new header block for tool pages
# - Replaced "Menü" with "Tüm Hesaplama Araçları"
# - Gradient for mobile button
# - "Hesaplama Araçları" link in blog header logic (handled separately or shared if template allows)
# - Desktop search bar
# - Ensuring desktop view works (md:block hidden logic)

new_header = """    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50 border-b border-slate-100">
        <div class="container mx-auto px-4 py-3">
            <div class="flex justify-between items-center">
                <!-- Left: Logo (No Hamburger) -->
                <div class="flex items-center gap-3">
                    <a href="index.html" class="flex items-center space-x-2 group">
                        <div class="bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-2 rounded-lg group-hover:shadow-lg transition">
                            <i class="fa-solid fa-calculator text-base"></i>
                        </div>
                        <div class="leading-tight">
                            <h1 class="text-lg md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></h1>
                        </div>
                    </a>
                </div>

                <!-- Desktop Search -->
                <div class="hidden md:block relative w-96 mx-4">
                    <i class="fa-solid fa-search absolute left-3 top-3 text-slate-400 text-sm"></i>
                    <input type="text" id="desktop-tool-search" placeholder="Hesaplama aracı ara..." class="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg text-sm focus:bg-white focus:border-blue-500 transition outline-none">
                    <div id="desktop-search-suggestions" class="absolute top-full left-0 w-full bg-white border border-slate-200 shadow-lg rounded-xl mt-1 z-50 hidden"></div>
                </div>

                <!-- Right: Actions -->
                <div class="flex items-center gap-3">
                    <!-- Desktop Nav -->
                    <div class="hidden md:flex items-center space-x-3 text-xs font-bold text-slate-600">
                        <a href="blog/index.html" class="hover:text-blue-600 px-2 py-2 transition">Blog</a>
                        <a href="ai-asistan.html" class="flex items-center gap-2 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 px-4 py-2 rounded-xl border border-indigo-100 transition duration-300">
                            <i class="fa-solid fa-wand-magic-sparkles"></i>
                            <span>AI Asistan</span>
                        </a>
                    </div>

                    <!-- Mobile AI Button -->
                    <a href="ai-asistan.html" class="md:hidden flex items-center justify-center w-8 h-8 rounded-full bg-indigo-50 text-indigo-600 border border-indigo-100 hover:bg-indigo-100 transition">
                        <i class="fa-solid fa-wand-magic-sparkles text-sm"></i>
                    </a>

                    <!-- Mobile Stylized Blog Button (Changes to Home Link in Blog pages) -->
                    <!-- This generic template is for tool pages, so it links to Blog -->
                    <a href="blog/index.html" class="md:hidden bg-gradient-to-r from-blue-600 to-blue-500 text-white text-[10px] font-bold px-3 py-1.5 rounded-full shadow-sm hover:shadow-md transition flex items-center gap-1">
                        <span>Blog</span> <i class="fa-solid fa-chevron-right text-[8px] opacity-70"></i>
                    </a>
                </div>
            </div>

            <!-- Mobile Search Bar (Below Header) -->
            <div class="md:hidden mt-3 relative">
                 <i class="fa-solid fa-search absolute left-3 top-3 text-slate-400 text-sm"></i>
                 <input type="text" id="mobile-tool-search" onkeyup="filterDrawerTools()" placeholder="Hesaplama aracı ara..." class="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg text-sm focus:bg-white focus:border-blue-500 transition outline-none">
                 <div id="mobile-search-suggestions" class="absolute top-full left-0 w-full bg-white border border-slate-200 shadow-lg rounded-xl mt-1 z-50 hidden"></div>
            </div>

            <!-- Mobile Drawer Toggle (Below Search) - UPDATED -->
            <div class="md:hidden mt-3">
                <button onclick="toggleDrawer()" class="w-full bg-gradient-to-r from-slate-700 to-slate-600 text-white rounded-lg py-3 flex items-center justify-center gap-2 hover:opacity-90 transition shadow-sm">
                    <i class="fa-solid fa-bars"></i>
                    <span class="font-bold text-sm">Tüm Hesaplama Araçları</span>
                </button>
            </div>
        </div>
    </header>"""

# Regex to find the header block
header_regex = re.compile(r'<!-- Header -->.*?<header.*?>.*?</header>', re.DOTALL)

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has header
    if not header_regex.search(content):
        print(f"Skipping {filepath}: Header not found.")
        return

    # Replace header
    new_content = header_regex.sub(new_header, content)

    # Site Icon Injection
    if '<link rel="icon"' not in new_content:
        # Try to find an icon
        icon_path = 'assets/img/favicon.png'
        # Insert before </head>
        new_content = new_content.replace('</head>', f'    <link rel="icon" type="image/png" href="{icon_path}">\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

# List of files to process (exclude blog folder, include root html files)
files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

for f in files:
    update_file(f)

# Also update index.html specifically
update_file('index.html')
