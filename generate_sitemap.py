import os
from datetime import datetime

def generate_sitemap():
    base_url = "https://hesaplahadi.com"
    paths_to_scan = ['.', 'blog']
    excluded_files = ['404.html', 'template.html', 'index.html']
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    # Add the homepage separately with higher priority
    sitemap_content += '  <url>\n'
    sitemap_content += f'    <loc>{base_url}/</loc>\n'
    sitemap_content += f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n'
    sitemap_content += '    <priority>1.0</priority>\n'
    sitemap_content += '  </url>\n'

    # Scan for other html files
    for dir_path in paths_to_scan:
        for file in os.listdir(dir_path):
            if file.endswith(".html") and file not in excluded_files:
                
                if dir_path == '.':
                    url_path = f"{base_url}/{file}"
                    priority = 0.8 # Main tools
                else:
                    url_path = f"{base_url}/{dir_path}/{file}"
                    priority = 0.7 # Blog posts

                sitemap_content += '  <url>\n'
                sitemap_content += f'    <loc>{url_path}</loc>\n'
                sitemap_content += f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n'
                sitemap_content += f'    <priority>{priority}</priority>\n'
                sitemap_content += '  </url>\n'

    sitemap_content += '</urlset>'

    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

    print("sitemap.xml generated successfully.")

if __name__ == '__main__':
    generate_sitemap()
