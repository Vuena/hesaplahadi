import os
import sys
from bs4 import BeautifulSoup

def update_layout(files_to_update):
    # 1. Parse index.html (Master Template)
    with open('index.html', 'r', encoding='utf-8') as f:
        master_soup = BeautifulSoup(f, 'html.parser')

    # Extract Master Components
    master_drawer_mask = master_soup.select_one('#drawer-mask')
    master_drawer = master_soup.select_one('#drawer')
    master_header = master_soup.select_one('header')
    master_footer = master_soup.select_one('footer')

    # Desktop Sidebar (Left) - Identifying by classes
    master_left_sidebar = None
    for nav in master_soup.find_all('nav'):
        classes = nav.get('class', [])
        if 'lg:col-span-3' in classes and 'hidden' in classes:
            master_left_sidebar = nav
            break

    # Right Sidebar - Identifying by classes
    master_right_sidebar = None
    for aside in master_soup.find_all('aside'):
        if aside.get('id') == 'drawer': continue
        classes = aside.get('class', [])
        if 'lg:col-span-3' in classes and 'col-span-1' in classes:
            master_right_sidebar = aside
            break

    # Scripts
    master_blog_script = master_soup.find('script', src='assets/js/blog-data.js')

    # Inline Script containing logic
    master_inline_script = None
    for script in master_soup.find_all('script'):
        if not script.get('src') and script.string and 'renderRecentBlog' in script.string:
            master_inline_script = script
            break

    if not all([master_drawer_mask, master_drawer, master_header, master_footer, master_left_sidebar, master_right_sidebar, master_blog_script, master_inline_script]):
        print("CRITICAL: Could not find all master components in index.html")
        return

    print("Master components loaded successfully.")

    count = 0
    for filename in files_to_update:
        if not os.path.exists(filename):
            print(f"Skipping {filename}, not found.")
            continue

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')

            print(f"Updating {filename}...")

            # A. UPDATE BODY START (Drawer & Mask)
            if soup.select_one('#drawer-mask'): soup.select_one('#drawer-mask').decompose()
            if soup.select_one('#drawer'): soup.select_one('#drawer').decompose()

            if soup.body:
                soup.body.insert(0, master_drawer)
                soup.body.insert(0, master_drawer_mask)

            # B. UPDATE HEADER
            if soup.header:
                soup.header.replace_with(master_header)
            else:
                if soup.body: soup.body.insert(2, master_header)

            # C. UPDATE GRID SIDEBARS
            main_grid = None
            for div in soup.find_all('div'):
                classes = div.get('class', [])
                if 'container' in classes and 'grid' in classes:
                    main_grid = div
                    break

            if main_grid:
                # 1. Left Sidebar
                existing_left = None
                for nav in main_grid.find_all('nav'):
                    classes = nav.get('class', [])
                    if 'lg:col-span-3' in classes:
                        existing_left = nav
                        break

                if existing_left:
                    existing_left.replace_with(master_left_sidebar)
                else:
                    main_grid.insert(0, master_left_sidebar)

                # 2. Right Sidebar
                existing_right = None
                for aside in main_grid.find_all('aside'):
                    if aside.get('id') == 'drawer': continue
                    classes = aside.get('class', [])
                    if 'lg:col-span-3' in classes:
                        existing_right = aside
                        break

                if existing_right:
                    existing_right.replace_with(master_right_sidebar)
                else:
                    main_grid.append(master_right_sidebar)

            # D. UPDATE FOOTER
            if soup.footer:
                soup.footer.replace_with(master_footer)
            else:
                if soup.body: soup.body.append(master_footer)

            # E. UPDATE SCRIPTS
            for s in soup.find_all('script'):
                if s.get('src') and 'blog-data.js' in s.get('src'):
                    s.decompose()
                elif not s.get('src') and s.string and ('renderRecentBlog' in s.string or 'toggleDrawer' in s.string):
                    s.decompose()

            calc_script = None
            for s in soup.find_all('script'):
                if s.get('src') and 'calculator.js' in s.get('src'):
                    calc_script = s
                    break

            if calc_script:
                calc_script.insert_after(master_inline_script)
                calc_script.insert_after(master_blog_script)
            else:
                if soup.body:
                    soup.body.append(master_blog_script)
                    soup.body.append(master_inline_script)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(str(soup))

            count += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print(f"Updated {count} files.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--limit', type=int, default=20)
    args = parser.parse_args()

    files = sorted([f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html'])

    # Process only the specific batch
    batch = files[args.start:args.start+args.limit]
    update_layout(batch)
