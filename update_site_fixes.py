import os
import re

# Define the logo replacement block
# Uses 'flex-shrink-0' on the icon wrapper and ensures standard visibility classes
NEW_LOGO_BLOCK = """
                <!-- Left: Logo -->
                <div class="flex items-center gap-3">
                     <a href="index.html" class="flex items-center space-x-2 group">
                        <div class="flex items-center justify-center bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-2.5 rounded-xl group-hover:shadow-lg group-hover:shadow-blue-500/30 transition duration-300 flex-shrink-0">
                            <i class="fa-solid fa-calculator text-lg"></i>
                        </div>
                        <div class="leading-tight">
                            <h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></h1>
                        </div>
                    </a>
                </div>
"""

# Regex to find the logo section
# Matches from '<!-- Left: Logo -->' to the closing </div> of the outer wrapper
LOGO_REGEX = re.compile(r'<!-- Left: Logo -->\s*<div class="flex items-center gap-3">.*?</div>\s*</a>\s*</div>', re.DOTALL)
# Actually, the regex needs to be more precise based on the file content I saw earlier
# Earlier file content:
# <!-- Left: Logo -->
# <div class="flex items-center gap-3">
#      <a href="index.html" class="flex items-center space-x-2 group">
#         <div ...>
#             <i ...></i>
#         </div>
#         <div class="leading-tight">
#             ...
#         </div>
#     </a>
# </div>

# Let's use a simpler replace strategy: Identify the block by commented start and end tags if possible, or fuzzy match
# Since the format is consistent, we can target the inner content.

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Update Logo
    # We will search for the specific structure.
    # Pattern: <!-- Left: Logo --> ... <div class="leading-tight"> ... </div> ... </a> ... </div>
    # Using a broad regex
    pattern = r'<!-- Left: Logo -->.*?<div class="leading-tight">.*?</h1>\s*</div>\s*</a>\s*</div>'

    # We need to construct the replacement carefully.
    # The read_file showed indentation.

    # Let's try to just find the specific line with "div class=... bg-gradient..." and add flex-shrink-0 if missing
    # And ensure no 'hidden' class is present.

    # Actually, replacing the whole block is safer to guarantee structure.
    # regex match
    match = re.search(pattern, content, re.DOTALL)
    if match:
        # print(f"Found logo in {filepath}")
        content = content.replace(match.group(0), NEW_LOGO_BLOCK.strip())

    # 2. Update Mobile Menu Button Z-Index
    # Find the button with "Tüm Hesaplama Araçları"
    # Update z-30 to z-40 (or check if it needs to be higher).
    # Current plan says ensure it has high z-index.
    # Search for: class="... z-30 cursor-pointer"
    # Replace with: class="... z-40 cursor-pointer"

    # We can do a direct string replace for the specific class string if it matches
    # "relative z-30 cursor-pointer" -> "relative z-40 cursor-pointer"
    if "relative z-30 cursor-pointer" in content:
        content = content.replace("relative z-30 cursor-pointer", "relative z-40 cursor-pointer")

    # 3. Cache Busting
    # src="assets/js/calculator.js" -> src="assets/js/calculator.js?v=2"
    if 'src="assets/js/calculator.js"' in content:
        content = content.replace('src="assets/js/calculator.js"', 'src="assets/js/calculator.js?v=2"')
    elif 'src="assets/js/calculator.js?v=1"' in content:
         content = content.replace('src="assets/js/calculator.js?v=1"', 'src="assets/js/calculator.js?v=2"')


    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

def main():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in files:
        update_file(file)

    # Also check blog/ directory
    if os.path.exists('blog'):
        blog_files = [os.path.join('blog', f) for f in os.listdir('blog') if f.endswith('.html')]
        for file in blog_files:
            update_file(file)

if __name__ == "__main__":
    main()
