
import os
import json
import re

BLOG_DATA_PATH = 'assets/js/blog-data.js'
BLOG_DIR = 'blog/'
TEMPLATE_PATH = 'blog_template.html'

CATEGORY_STYLES = {
    'Finans': {'color': 'green', 'icon': 'fa-chart-line'},
    'Eğitim': {'color': 'blue', 'icon': 'fa-book'},
    'Sağlık': {'color': 'teal', 'icon': 'fa-heart-pulse'},
    'Teknoloji': {'color': 'indigo', 'icon': 'fa-laptop-code'},
    'Astroloji': {'color': 'purple', 'icon': 'fa-star'},
    'Yaşam': {'color': 'orange', 'icon': 'fa-leaf'},
    'Hukuk': {'color': 'red', 'icon': 'fa-gavel'},
    'default': {'color': 'slate', 'icon': 'fa-file-alt'}
}

RELATED_TOOL_HTML = '''
<div class="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm">
    <h3 class="text-sm font-bold text-slate-800 uppercase tracking-wider mb-4">İlgili Araç</h3>
    <a href="/%%TOOL_SLUG%%" class="flex items-center gap-4 group bg-slate-50 p-4 rounded-xl border border-slate-100 hover:border-blue-200 hover:bg-blue-50 transition">
        <div class="flex items-center justify-center w-10 h-10 bg-white rounded-lg text-blue-600 shadow-sm border border-slate-100 text-xl">
            <i class="fa-solid %%TOOL_ICON%%"></i>
        </div>
        <div>
            <h4 class="font-bold text-slate-800 group-hover:text-blue-700 transition">%%TOOL_NAME%%</h4>
            <p class="text-xs text-slate-500">Hemen Hesapla</p>
        </div>
    </a>
</div>
'''

def get_blog_posts_data():
    try:
        with open(BLOG_DATA_PATH, 'r', encoding='utf-8') as f:
            js_content = f.read()
        match = re.search(r'const blogPosts\s*=\s*(\[.*\]);', js_content, re.DOTALL)
        if match:
            json_data = match.group(1)
            json_data = re.sub(r''',\s*([\}\]])''', r'\1', json_data)
            return json.loads(json_data)
    except Exception as e:
        print(f"Error reading or parsing {BLOG_DATA_PATH}: {e}")
    return None

def extract_content_from_html(html_string):
    # First, try to find a specific <article> tag
    article_match = re.search(r'<article[^>]*>(.*?)</article>', html_string, re.DOTALL)
    if article_match:
        # Check if this article contains a plausible content div
        article_html = article_match.group(1)
        prose_match = re.search(r'<div class="prose.*?>(.*?)</div>', article_html, re.DOTALL)
        if prose_match:
            return prose_match.group(1).strip()
        # Otherwise, return the whole article content, it's better than nothing
        return article_html.strip()

    # If no article, try to find the main content within the body
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html_string, re.DOTALL)
    if body_match:
        body_content = body_match.group(1)
        # A common pattern might be a main tag
        main_match = re.search(r'<main[^>]*>(.*?)</main>', body_content, re.DOTALL)
        if main_match:
            return main_match.group(1).strip()
    
    return None

def standardize_blog_posts():
    blog_posts = get_blog_posts_data()
    if not blog_posts:
        print("No blog posts data found. Aborting.")
        return

    try:
        with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"Template file not found at {TEMPLATE_PATH}. Aborting.")
        return

    updated_count = 0
    skipped_count = 0

    for post in blog_posts:
        slug = post.get('slug')
        if not slug or not slug.endswith('.html'):
            continue

        file_path = os.path.join(BLOG_DIR, slug)
        if not os.path.exists(file_path):
            print(f"File not found, skipping: {slug}")
            skipped_count += 1
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            old_content = f.read()
        
        post_content_html = extract_content_from_html(old_content)
        
        # If content extraction fails, we must not overwrite the file with an empty body.
        if not post_content_html or not post_content_html.strip():
            print(f"Could not extract valid content for {slug}. Skipping file modification.")
            skipped_count += 1
            continue

        # Populate template
        new_html = template_content
        new_html = new_html.replace('%%POST_TITLE%%', post.get('title', ''))
        new_html = new_html.replace('%%POST_DESCRIPTION%%', post.get('summary', ''))
        new_html = new_html.replace('%%POST_SLUG%%', slug)

        category = post.get('category', 'default')
        style = CATEGORY_STYLES.get(category, CATEGORY_STYLES['default'])
        new_html = new_html.replace('%%POST_CATEGORY%%', category)
        new_html = new_html.replace('%%POST_COLOR%%', style['color'])
        new_html = new_html.replace('%%POST_ICON%%', style['icon'])

        new_html = new_html.replace('%%POST_CONTENT%%', post_content_html)

        related_tool = post.get('related_tool')
        if related_tool and all(k in related_tool for k in ['slug', 'name', 'icon']):
            tool_block = RELATED_TOOL_HTML
            tool_block = tool_block.replace('%%TOOL_SLUG%%', related_tool['slug'])
            tool_block = tool_block.replace('%%TOOL_NAME%%', related_tool['name'])
            tool_block = tool_block.replace('%%TOOL_ICON%%', related_tool['icon'])
            new_html = new_html.replace('%%RELATED_TOOL_BLOCK%%', tool_block)
        else:
            new_html = new_html.replace('%%RELATED_TOOL_BLOCK%%', '')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        updated_count += 1
        print(f"Successfully standardized: {slug}")

    print(f"\nFinished. Standardized {updated_count} blog posts. Skipped {skipped_count} posts.")

if __name__ == '__main__':
    standardize_blog_posts()
