import os
import re

def update_mobile_header(filepath, is_blog_dir=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine relative path for links
    root_path = "../" if is_blog_dir else ""
    blog_path = "index.html" if is_blog_dir else "blog/index.html"
    index_path = "../index.html" if is_blog_dir else "index.html"
    ai_path = "../ai-asistan.html" if is_blog_dir else "ai-asistan.html"

    # New Header Structure
    new_header = f'''    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50 border-b border-slate-100">
        <!-- Desktop Header Content (Preserved somewhat, but unified for Mobile as per request) -->
        <div class="container mx-auto px-4 py-3">
             <div class="flex justify-between items-center">
                <!-- Logo (Left) -->
                <a href="{index_path}" class="flex items-center gap-2 group">
                    <div class="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold text-lg">H</div>
                    <span class="font-bold text-slate-800 text-lg tracking-tight">Hesapla<span class="text-blue-600">Hadi</span></span>
                </a>

                <!-- Right Actions -->
                <div class="flex items-center gap-2">
                    <!-- Desktop Nav -->
                    <div class="hidden md:flex items-center space-x-3 text-sm font-bold text-slate-600">
                        <a href="{blog_path}" class="hover:text-blue-600 px-3 py-2 transition">Blog</a>
                        <a href="{ai_path}" class="flex items-center gap-2 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 px-4 py-2 rounded-xl border border-indigo-100 transition duration-300">
                            <i class="fa-solid fa-wand-magic-sparkles"></i>
                            <span>AI Asistan</span>
                        </a>
                    </div>

                    <!-- Mobile Blog Button (Text) -->
                    <a href="{blog_path}" class="md:hidden mobile-blog-btn">
                        <span>Blog</span>
                        <i class="fa-solid fa-arrow-right text-[10px] opacity-50"></i>
                    </a>
                </div>
            </div>

            <!-- Mobile: Big "All Calculations" Bar (User Request) -->
            <div class="md:hidden mt-3">
                <button onclick="toggleDrawer()" class="mobile-big-btn group">
                    <i class="fa-solid fa-bars-staggered group-hover:rotate-180 transition duration-500"></i>
                    <span>Tüm Hesaplamalar</span>
                </button>
            </div>

            <!-- Mobile Search Bar (Below Header) -->
            <div class="md:hidden mt-3 relative">
                 <i class="fa-solid fa-search absolute left-3 top-3.5 text-slate-400 text-sm"></i>
                 <input type="text" id="mobile-tool-search" onkeyup="filterDrawerTools()" placeholder="Hesaplama aracı ara..." class="w-full pl-10 pr-4 py-3 bg-slate-50 border border-slate-200 rounded-xl text-sm focus:bg-white focus:border-blue-500 transition outline-none shadow-sm">
            </div>
        </div>
    </header>'''

    # Regex to find existing header
    # We look for <header ...> up to </header>
    pattern = re.compile(r'<header class="bg-white/90.*?<\/header>', re.DOTALL)

    if pattern.search(content):
        new_content = pattern.sub(new_header, content)

        # Add loading="lazy" to images
        new_content = re.sub(r'<img ((?!loading="lazy")[^>]+)>', r'<img loading="lazy" \1>', new_content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Header not found in {filepath}")

# Update Root Files
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        update_mobile_header(filename, is_blog_dir=False)

# NOTE: Not updating blog/* files as they have a different header structure/purpose.
