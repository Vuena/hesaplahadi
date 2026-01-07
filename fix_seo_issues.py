
import re
import os

def fix_seo_for_file(path):
    print(f"--- Fixing SEO for: {path} ---")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Replace the first h1 and /h1 tags with p tags.
        content = content.replace('<h1>', '<p>', 1)
        content = content.replace('</h1>', '</p>', 1)
        print("  [FIX] Converted first H1 to P tag.")

        # Check for meta description
        desc_match = re.search(r'<meta[^>]+name=(["\'])description\1', content, re.IGNORECASE)

        if not desc_match:
            print("  [INFO] Meta description not found. Adding one.")
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if title_match:
                title_text = title_match.group(1).strip().split('|')[0].strip()
                new_desc_content = f"{title_text} aracıyla hızlı ve doğru hesaplamalar yapın. HesaplaHadi, tüm finansal ve günlük ihtiyaçlarınız için yanınızda."
                new_desc_tag = f'\n<meta name="description" content="{new_desc_content}" />'
                # Insert before </head>
                head_end_match = re.search(r'</head>', content, re.IGNORECASE)
                if head_end_match:
                    insertion_point = head_end_match.start()
                    content = content[:insertion_point] + new_desc_tag + '\n' + content[insertion_point:]
                    print(f"  [FIX] Added meta description based on title.")
            else:
                print("  [WARN] Could not find title tag to generate meta description.")
        else:
            print("  [PASS] Meta description already exists.")

        # Clean up duplicate drawer templates
        drawer_template_str = '''<div class="fixed inset-0 bg-black/50 z-[60] transition-opacity duration-300 mask-hidden" id="drawer-mask" onclick="toggleDrawer()"></div><aside class="fixed top-0 left-0 w-64 h-full bg-white z-[70] shadow-2xl transition-transform duration-300 drawer-closed overflow-y-auto" id="drawer">\n<div class="p-4 border-b border-slate-100 flex justify-between items-center">\n<span class="font-bold text-lg text-slate-800">Hesaplama Araçları</span>\n<button class="text-slate-400 hover:text-slate-600" onclick="toggleDrawer()"><i class="fa-solid fa-times text-xl"></i></button>\n</div>\n<div class="p-3 space-y-1" id="drawer-list"></div>'''
        occurrences = content.count(drawer_template_str)
        if occurrences > 1:
            first_pos = content.find(drawer_template_str)
            start_of_second = first_pos + len(drawer_template_str)
            content = content[:start_of_second] + content[start_of_second:].replace(drawer_template_str, '')
            print(f"  [CLEAN] Removed {occurrences - 1} duplicate template sections.")

        if content != original_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [SUCCESS] File '{path}' has been updated.")
        else:
            print(f"  [INFO] No changes needed for '{path}'.")

    except Exception as e:
        print(f"  [ERROR] Could not process file {path}: {e}")

def main():
    ignored_dirs = {'.git', '.vscode', 'node_modules', '__pycache__', 'assets', '.idx', 'verification', 'tests'}
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for file in files:
            if file.endswith(('.html', '.htm')):
                fix_seo_for_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
