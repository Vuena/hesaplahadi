
import os
import json
import re

BLOG_DATA_PATH = 'assets/js/blog-data.js'
BLOG_DIR = 'blog/'

def get_blog_posts_data():
    try:
        with open(BLOG_DATA_PATH, 'r', encoding='utf-8') as f:
            js_content = f.read()
        match = re.search(r'const blogPosts\s*=\s*(\[.*\]);', js_content, re.DOTALL)
        if match:
            json_data = match.group(1)
            # Remove trailing commas that are invalid in JSON
            json_data = re.sub(r''',\s*([\}\]])''', r'\1', json_data)
            return json.loads(json_data)
    except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
        print(f"Error reading or parsing {BLOG_DATA_PATH}: {e}")
    return None

def save_blog_posts_data(posts):
    try:
        js_output = "const blogPosts = "
        js_output += json.dumps(posts, ensure_ascii=False, indent=4)
        js_output += ";\\n\\n"
        
        js_output += "function getCurrentPost() {\\n"
        js_output += "    const path = window.location.pathname;\\n"
        js_output += "    const filename = path.split('/').pop();\\n"
        js_output += "    const post = blogPosts.find(p => p.slug === filename);\\n"
        js_output += "    if (post) {\\n"
        js_output += "        return post;\\n"
        js_output += "    }\\n"
        js_output += "    return null;\\n"
        js_output += "}\\n"

        with open(BLOG_DATA_PATH, 'w', encoding='utf-8') as f:
            f.write(js_output)
        print(f"Successfully updated {BLOG_DATA_PATH}")
    except Exception as e:
        print(f"Error writing to {BLOG_DATA_PATH}: {e}")

def cleanup_weak_content():
    blog_posts = get_blog_posts_data()
    if blog_posts is None:
        print("Could not retrieve blog posts. Aborting cleanup.")
        return

    posts_to_keep = []
    files_to_delete = []
    
    weak_summary = 'Blog Detay aracı ile hızlı ve kolayca hesaplama yapın. En doğru ve güncel sonuçlar için HesaplaHadi'
    weak_title = 'Blog Detay - HesaplaHadi'

    for post in blog_posts:
        title = post.get('title', '').strip()
        summary = post.get('summary', '').strip()
        slug = post.get('slug')

        if not slug or title == weak_title or summary == weak_summary or not summary:
            if slug:
                files_to_delete.append(slug)
        else:
            posts_to_keep.append(post)

    deleted_count = 0
    for slug in files_to_delete:
        file_path = os.path.join(BLOG_DIR, slug)
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
                deleted_count += 1
            except OSError as e:
                print(f"Error deleting file {file_path}: {e}")
        else:
            print(f"File not found, but removing entry: {file_path}")
            # Also count if the file is not there but the entry is weak
            deleted_count += 1

    if deleted_count > 0:
        save_blog_posts_data(posts_to_keep)
        print(f"\\nRemoved {len(files_to_delete)} weak content entries and associated files.")
    else:
        print("\\nNo weak content found to remove.")

if __name__ == '__main__':
    cleanup_weak_content()
