
import json
import os
import re

def rebuild():
    # 1. Read the data from the JavaScript file
    try:
        with open('assets/js/blog-data.js', 'r', encoding='utf-8') as f:
            js_content = f.read()
    except FileNotFoundError:
        print("Hata: assets/js/blog-data.js dosyası bulunamadı.")
        return

    # Extract the array from the JS file using a more specific regex
    match = re.search(r'const blogPosts = (\s*\[.*?\]\s*);', js_content, re.DOTALL)
    if not match:
        print("Hata: blogPosts dizisi assets/js/blog-data.js içinde bulunamadı.")
        return

    # The captured group includes the semicolon, so we remove it for valid JSON
    json_str = match.group(1).rstrip(';')
    
    try:
        posts = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"Hata: JavaScript dosyasındaki veriler ayrıştırılamadı: {e}")
        # Print a snippet of the problematic string for debugging
        problematic_snippet = json_str[max(0, e.pos-25):e.pos+25]
        print(f"Sorunlu bölüm civarı: ...{problematic_snippet}...")
        return

    # 2. Read the HTML template for blog posts
    try:
        with open('blog/template.html', 'r', encoding='utf-8') as f:
            template_html = f.read()
    except FileNotFoundError:
        print("Hata: blog/template.html şablonu bulunamadı.")
        return

    # 3. Create the blog directory if it doesn't exist
    if not os.path.exists('blog'):
        os.makedirs('blog')

    # 4. Generate a static HTML file for each post
    for post in posts:
        if 'slug' not in post or 'title' not in post:
            continue

        post_html = template_html

        # Replace all placeholders with actual content
        post_html = post_html.replace('<title>Blog Detay - HesaplaHadi</title>', f'<title>{post.get("title", "Blog Yazısı")} - HesaplaHadi Blog</title>')
        post_html = post_html.replace('<meta name="description" content="HesaplaHadi Blog yazısı.">', f'<meta name="description" content="{post.get("summary", "")}">')
        post_html = post_html.replace('<link rel="canonical" href="https://hesaplahadi.com/blog/template.html" />', f'<link rel="canonical" href="https://hesaplahadi.com/blog/{post.get("slug", "")}" />')
        
        post_html = post_html.replace('<span class="text-slate-800" id="crumb-title">...</span>', f'<span class="text-slate-800" id="crumb-title">{post.get("title", "")}</span>')
        post_html = post_html.replace('<span id="post-cat" class="text-xs font-bold text-blue-600 bg-blue-50 px-3 py-1 rounded-full uppercase tracking-wider">...</span>', f'<span id="post-cat" class="text-xs font-bold bg-{post.get("color", "blue")}-50 text-{post.get("color", "blue")}-600 px-3 py-1 rounded-full uppercase tracking-wider">{post.get("category", "Genel")}</span>')
        post_html = post_html.replace('<h1 id="post-title" class="text-3xl md:text-4xl font-extrabold text-slate-900 mt-4 leading-tight">...</h1>', f'<h1 id="post-title" class="text-3xl md:text-4xl font-extrabold text-slate-900 mt-4 leading-tight">{post.get("title", "")}</h1>')
        post_html = post_html.replace('<p id="post-summary" class="text-lg text-slate-500 mt-4 leading-relaxed">...</p>', f'<p id="post-summary" class="text-lg text-slate-500 mt-4 leading-relaxed">{post.get("summary", "")}</p>')
        
        post_html = post_html.replace('<i id="post-icon" class="fa-solid fa-image text-8xl opacity-50"></i>', f'<i id="post-icon" class="fa-solid {post.get("image", "fa-file-alt")} text-8xl text-{post.get("color", "gray")}-300"></i>')
        
        post_html = post_html.replace('<p>İçerik yükleniyor...</p>', post.get("content", "<p>İçerik bulunamadı.</p>"))
        post_html = post_html.replace('İçerik korunamadı, lütfen kontrol edin.', post.get("content", "<p>İçerik bulunamadı.</p>"))

        # Remove the now-redundant scripts
        post_html = re.sub(r'<script src="../assets/js/blog-data.js"></script>\s*<script>.*?</script>', '', post_html, flags=re.DOTALL)
        
        file_path = os.path.join('blog', post['slug'])
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(post_html)
        
        print(f"Blog sayfası yeniden oluşturuldu: {file_path}")

    # 5. Update the blog index page
    try:
        with open('blog/index.html', 'r', encoding='utf-8') as f:
            index_html = f.read()
    except FileNotFoundError:
        print("Hata: blog/index.html bulunamadı.")
        return

    # Sort posts, maybe by title or another attribute if available
    sorted_posts = sorted(posts, key=lambda p: p.get('title', ''))

    grid_content = ""
    for post in sorted_posts:
        grid_content += f'''
            <a href="{post['slug']}" class="card-hover-effect bg-white rounded-2xl overflow-hidden flex flex-col group border border-slate-200">
                <div class="p-6 flex-grow">
                    <span class="text-xs font-bold bg-{post.get('color', 'blue')}-50 text-{post.get('color', 'blue')}-600 px-3 py-1 rounded-full uppercase tracking-wider">{post.get('category', 'Genel')}</span>
                    <h3 class="font-extrabold text-slate-900 text-lg mt-4 mb-2">{post.get('title', '')}</h3>
                    <p class="text-sm text-slate-500 leading-relaxed">{post.get('summary', '')}</p>
                </div>
                <div class="bg-slate-50 p-4 border-t border-slate-100 flex items-center justify-between text-xs font-bold text-slate-500">
                    <span>Devamını Oku</span>
                    <i class="fa-solid fa-arrow-right transform transition-transform group-hover:translate-x-1"></i>
                </div>
            </a>
        '''
    
    # This regex is now more robust to handle different spacing
    index_html = re.sub(
        r'(<div id="blog-grid"[^>]*>)[\s\S]*?(</div>)(?:\s*<script src="../assets/js/blog-data.js"></script>)?',
        f'\1{grid_content}\2',
        index_html,
        flags=re.DOTALL
    )

    # Also remove the dynamic script loader from the index
    index_html = re.sub(r'<script>\s*document.addEventListener.*?<\\/script>','', index_html, flags=re.DOTALL)


    with open('blog/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("\nBlog ana sayfası (index.html) başarıyla güncellendi.")

    print("\n\nTüm blog yazıları ve ana sayfa başarıyla statik HTML olarak yeniden oluşturuldu!")

if __name__ == "__main__":
    rebuild()
