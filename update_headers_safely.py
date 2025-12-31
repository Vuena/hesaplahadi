
import os
import re

# Define the new header block for tool pages
# INCLUDES SEARCH BAR
new_header = """    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50 border-b border-slate-100">
        <div class="container mx-auto px-4 py-3">
            <div class="flex justify-between items-center">
                <!-- Left: Hamburger + Logo -->
                <div class="flex items-center gap-3">
                    <!-- Mobile Menu Button -->
                    <button class="md:hidden text-slate-600 hover:text-blue-600 transition p-2" onclick="toggleDrawer()">
                        <i class="fa-solid fa-bars text-xl"></i>
                     </button>

                     <a href="index.html" class="flex items-center space-x-2 group">
                        <div class="hidden md:block bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-2.5 rounded-xl group-hover:shadow-lg group-hover:shadow-blue-500/30 transition duration-300">
                            <i class="fa-solid fa-calculator text-lg"></i>
                        </div>
                        <div class="leading-tight">
                            <h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></h1>
                        </div>
                    </a>
                </div>

                <!-- Right: Actions -->
                <div class="flex items-center gap-3">
                    <!-- Desktop Nav -->
                    <div class="hidden md:flex items-center space-x-3 text-xs font-bold text-slate-600">
                        <a href="index.html" class="hover:text-blue-600 transition">Araçlar</a>
                        <a href="blog/index.html" class="hover:text-blue-600 transition">Blog</a>
                        <a href="ai-asistan.html" class="flex items-center gap-2 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 px-4 py-2 rounded-xl border border-indigo-100 transition duration-300">
                            <i class="fa-solid fa-wand-magic-sparkles"></i>
                            <span>AI Asistan</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Mobile Search Bar (Below Header) -->
            <div class="md:hidden mt-3 relative">
                 <i class="fa-solid fa-search absolute left-3 top-3 text-slate-400 text-sm"></i>
                 <input type="text" id="mobile-tool-search" onkeyup="filterDrawerTools()" placeholder="Hesaplama aracı ara..." class="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg text-sm focus:bg-white focus:border-blue-500 transition outline-none">
            </div>
        </div>
    </header>"""

# Regex to find the header block
# It looks for <!-- Header --> ... </header>
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

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

# List of files to process (exclude blog folder, include root html files)
files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']

for f in files:
    update_file(f)
