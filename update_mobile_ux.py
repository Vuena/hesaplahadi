import os
import re

def update_mobile_header(filepath, is_blog_dir=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine relative path for links
    root_path = "../" if is_blog_dir else ""
    blog_path = "index.html" if is_blog_dir else "blog/index.html"
    index_path = "../index.html" if is_blog_dir else "index.html"

    # New Header Structure
    new_header = f'''    <!-- Mobile Header -->
    <header class="lg:hidden bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40">
        <div class="px-4 py-3 flex items-center justify-between">
            <!-- Logo -->
            <a href="{index_path}" class="flex items-center gap-2">
                <div class="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold text-lg">H</div>
                <span class="font-bold text-slate-800 text-lg tracking-tight">Hesapla<span class="text-blue-600">Hadi</span></span>
            </a>

            <!-- Action Buttons -->
            <div class="flex items-center gap-3">
                <!-- Blog Button (Text) -->
                <a href="{blog_path}" class="mobile-blog-btn">
                    <span>Blog</span>
                    <i class="fa-solid fa-arrow-right text-xs opacity-50"></i>
                </a>
            </div>
        </div>

        <!-- Full Width Drawer Toggle Bar -->
        <div class="px-4 pb-3">
            <button onclick="toggleDrawer()" class="mobile-big-btn group">
                <i class="fa-solid fa-bars-staggered group-hover:rotate-180 transition duration-500"></i>
                <span>Tüm Hesaplamalar</span>
            </button>
        </div>

        <!-- Search Bar -->
        <div class="px-4 pb-3">
             <div class="relative">
                 <i class="fa-solid fa-search absolute left-3 top-3.5 text-slate-400 text-sm"></i>
                 <input type="text" id="mobile-tool-search" onkeyup="filterDrawerTools()" placeholder="Hesaplama aracı ara..." class="w-full pl-10 pr-4 py-3 bg-slate-50 border border-slate-200 rounded-xl text-sm focus:bg-white focus:border-blue-500 transition outline-none shadow-sm">
            </div>
        </div>
    </header>'''

    # Regex to find existing header
    # We look for <header class="lg:hidden ..."> up to </header>
    pattern = re.compile(r'<header class="lg:hidden[^>]*>.*?</header>', re.DOTALL)

    if pattern.search(content):
        new_content = pattern.sub(new_header, content)

        # Also remove any "Mobile Search Bar (Below Header)" if it exists outside the header but usually it was inside or just below.
        # In the previous cat output, the search bar was INSIDE the header div but at the end.
        # My regex match includes it if it's inside <header>...</header>.

        # Add loading="lazy" to images
        new_content = re.sub(r'<img ((?!loading="lazy")[^>]+)>', r'<img loading="lazy" \1>', new_content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Header not found in {filepath}")

# Update Root Files
for filename in os.listdir('.'):
    if filename.endswith('.html') and filename != 'index.html': # Handle index separately or same? Same logic applies.
        update_mobile_header(filename, is_blog_dir=False)

# Update Blog Files (Only if they share the structure, but wait!)
# Blog files have a DIFFERENT header structure (saw in `cat blog/kdv...`).
# Blog files have "Hesaplama Araçları" button instead of Blog button (makes sense).
# User said: "Sağ üstteki blog simgesi yazıyla Blog olarak yazsın... dediklerim mobil için geçerli."
# User also said: "Mobilde tüm hesaplamalar çubuğunu biraz büyük..."
# This likely applies to the Tool pages where the user navigates.
# For Blog pages, the "Hesaplama Araçları" button is already text.
# BUT, maybe I should apply the "Big Bar" concept to the Blog pages too?
# "Mobilde tüm hesaplamalar çubuğunu..." -> Likely refers to the drawer toggle.
# Blog pages DO NOT have a drawer toggle currently?
# Let's check `blog/kdv-tevkifati...` header again.
# It has `href="../index.html"` as a button. It does NOT have a hamburger menu.
# So I should PROBABLY NOT touch the Blog files' header unless I want to add the drawer there too.
# The user instruction seems focused on the main "app" experience.
# I will skip `blog/` folder for the header update to avoid breaking the "Back to Tools" flow which is specific to blog.
# However, I will check if `index.html` needs update. Yes.

update_mobile_header('index.html', is_blog_dir=False)
