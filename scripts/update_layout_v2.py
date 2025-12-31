
import os
import re

# Define the new header block
# CHANGES:
# 1. Logo (Icon) is now visible on mobile (removed 'hidden md:block').
# 2. "Tüm Hesaplamalar" Button moved from top-left to below the search bar (bottom of header).
# 3. "Tüm Hesaplamalar" Button has gradient style.
# 4. Mobile layout: Logo (Left) ... Actions (Right) -> Search -> Button

new_header = """    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50 border-b border-slate-100">
        <div class="container mx-auto px-4 py-3">
            <div class="flex justify-between items-center">
                <!-- Left: Logo -->
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

                    <!-- Mobile Stylized Blog Button -->
                    <a href="blog/index.html" class="md:hidden bg-gradient-to-r from-blue-600 to-blue-500 text-white text-[10px] font-bold px-3 py-1.5 rounded-full shadow-sm hover:shadow-md transition flex items-center gap-1">
                        <span>Blog</span> <i class="fa-solid fa-chevron-right text-[8px] opacity-70"></i>
                    </a>
                </div>
            </div>

            <!-- Mobile Search Bar -->
            <div class="md:hidden mt-3 relative">
                 <i class="fa-solid fa-search absolute left-3 top-3 text-slate-400 text-sm"></i>
                 <input type="text" id="mobile-tool-search" onkeyup="filterDrawerTools()" placeholder="Hesaplama aracı ara..." class="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg text-sm focus:bg-white focus:border-blue-500 transition outline-none">
            </div>

            <!-- Mobile "Tüm Hesaplamalar" Button (Moved to Bottom) -->
            <button class="md:hidden w-full mt-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-bold py-3 rounded-xl shadow-lg flex items-center justify-center gap-2 hover:shadow-xl transition transform active:scale-95" onclick="toggleDrawer()">
                <i class="fa-solid fa-bars"></i> Tüm Hesaplamalar
            </button>
        </div>
    </header>"""

# Regex to find the header block
header_regex = re.compile(r'<!-- Header -->.*?<header.*?>.*?</header>', re.DOTALL)

# Sidebar Fix: Ensure sidebar list has flex-col
sidebar_regex = re.compile(r'<div id="sidebar-list" class="([^"]*)">')

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Header
        if header_regex.search(content):
            content = header_regex.sub(new_header, content)
        else:
            print(f"Skipping Header for {filepath}: Header not found.")

        # Update Sidebar Class
        # We want to ensure it has 'flex flex-col'
        # Existing: "overflow-y-auto custom-scroll p-2 space-y-1"
        def sidebar_replacer(match):
            cls = match.group(1)
            if 'flex-col' not in cls:
                cls += ' flex flex-col'
            return f'<div id="sidebar-list" class="{cls}">'

        content = sidebar_regex.sub(sidebar_replacer, content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

# List of files to process
# Root html files + index.html
files = [f for f in os.listdir('.') if f.endswith('.html')]

# Also process blog files if they have headers
# Note: Blog files are in blog/ and use ../ assets.
# The header I constructed uses href="index.html".
# For blog pages, it should be href="../index.html".
# I'll handle blog folder separately with a slight modification to the header string.

for f in files:
    update_file(f)

# Blog Files
blog_files = [os.path.join('blog', f) for f in os.listdir('blog') if f.endswith('.html')]
blog_header = new_header.replace('href="index.html"', 'href="../index.html"').replace('href="blog/index.html"', 'href="index.html"').replace('href="ai-asistan.html"', 'href="../ai-asistan.html"')

def update_blog_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if header_regex.search(content):
            content = header_regex.sub(blog_header, content)

        # Blog might not have sidebar, but if it does...
        content = sidebar_regex.sub(lambda m: f'<div id="sidebar-list" class="{m.group(1)} flex flex-col">', content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

for f in blog_files:
    update_blog_file(f)
