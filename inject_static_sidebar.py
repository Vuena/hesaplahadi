import os
import glob
import re
import argparse
from layout_generator import get_tools_from_js, generate_sidebar_html, get_popular_tools_html

def inject_static_content(start=0, limit=None):
    # 1. Get Tools Data
    tools = get_tools_from_js()
    if not tools:
        print("Error: Could not load tools from calculator.js")
        return

    # 2. Find all HTML files
    root_files = sorted(glob.glob("*.html"))
    blog_files = sorted(glob.glob("blog/*.html"))

    all_files = root_files + blog_files
    total_files = len(all_files)

    # Slice batch
    if limit is None:
        batch_files = all_files
        print(f"Processing all {total_files} files.")
    else:
        end = start + limit
        batch_files = all_files[start:end]
        print(f"Processing batch: {start} to {start + len(batch_files)} (Total: {total_files})")

    for filepath in batch_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Determine context
            # If file path contains 'blog/', we assume it is one level deep.
            # Normalizing path separators just in case
            norm_path = filepath.replace('\\', '/')
            is_blog = "blog/" in norm_path
            link_prefix = "../" if is_blog else ""

            filename = os.path.basename(filepath)

            # 3. Generate Content
            sidebar_html = generate_sidebar_html(tools, current_page_link=filename, is_drawer=False, link_prefix=link_prefix)
            drawer_html = generate_sidebar_html(tools, current_page_link=filename, is_drawer=True, link_prefix=link_prefix)

            # 4. Inject Sidebar
            def replace_sidebar(match):
                opening_tag = match.group(1)
                closing_tag = match.group(3)
                return f"{opening_tag}{sidebar_html}{closing_tag}"

            content_new = re.sub(
                r'(<div[^>]*\bid="sidebar-list"[^>]*>)(.*?)(</div>)',
                replace_sidebar,
                content,
                flags=re.DOTALL
            )

            def replace_drawer(match):
                opening_tag = match.group(1)
                closing_tag = match.group(3)
                return f"{opening_tag}{drawer_html}{closing_tag}"

            content_new = re.sub(
                r'(<div[^>]*\bid="drawer-list"[^>]*>)(.*?)(</div>)',
                replace_drawer,
                content_new,
                flags=re.DOTALL
            )

            if content_new != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content_new)
                print(f"Updated {filepath}")
            else:
                print(f"No changes for {filepath}")

        except Exception as e:
            print(f"Failed to process {filepath}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    inject_static_content(start=args.start, limit=args.limit)
