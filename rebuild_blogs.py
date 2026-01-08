
import json
import os
import re

def get_blog_posts_from_js(js_path="assets/js/blog-data.js"):
    """
    Parses the blogPosts array from blog-data.js to be used as the source of truth.
    """
    if not os.path.exists(js_path):
        # Fallback for running from root directory
        if os.path.exists("assets/js/blog-data.js"):
            js_path = "assets/js/blog-data.js"
        else:
            print(f"Error: Cannot find {js_path}")
            return []

    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Use regex to extract the array content
    match = re.search(r'const blogPosts =\s*(\[[\s\S]*?\]);', content)
    if not match:
        print("Could not find blogPosts array in blog-data.js")
        return []

    json_str = match.group(1)
    
    # The string is almost JSON, but keys are not quoted. We need to fix that.
    # Add quotes around keys
    json_str = re.sub(r'([{,])\s*([a-zA-Z0-9_]+)\s*:', r'\1"\2":', json_str)
    
    # Replace single quotes with double quotes for string values
    json_str = json_str.replace("\'", '"')
    json_str = re.sub(r':\s*null', ': "null" ', json_str)

    
    try:
        # Final cleanup for any weirdness
        # Remove trailing commas before closing braces or brackets
        json_str = re.sub(r',\s*([]}])', r'\1', json_str)
        
        data = json.loads(json_str)
        return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from blog-data.js: {e}")
        # Find the problematic part
        line_number = e.lineno
        col_number = e.colno
        lines = json_str.split('\n')
        if line_number <= len(lines):
            print(f"Problematic line ({line_number}): {lines[line_number-1]}")
            print(" " * (col_number - 1) + "^")
        return []

BLOG_POSTS = get_blog_posts_from_js()

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="[[SUMMARY]]">
    <title>[[TITLE]] - HesaplaHadi Blog</title>
    <link rel="canonical" href="https://hesaplahadi.com/blog/[[SLUG]]" />
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="../assets/css/style.css" rel="stylesheet">
    <style>
        .prose h2 { font-size: 1.5rem; font-weight: 700; color: #1e293b; margin-top: 2rem; margin-bottom: 1rem; }
        .prose h3 { font-size: 1.25rem; font-weight: 600; color: #334155; margin-top: 1.5rem; margin-bottom: 0.75rem; }
        .prose p { margin-bottom: 1.25rem; line-height: 1.8; color: #334155; }
        .prose ul { list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1.25rem; }
        .prose li { margin-bottom: 0.5rem; }
        .prose strong { color: #1e293b; font-weight: 700; }
    </style>
    <link rel="icon" type="image/svg+xml" href="../assets/img/favicon.svg">
</head>
<body class="flex flex-col min-h-screen text-slate-800 bg-slate-50">

    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50 border-b border-slate-100">
        <div class="container mx-auto px-4 py-3">
            <div class="flex justify-between items-center">
                <a href="../index.html" class="flex items-center space-x-2 group">
                    <div class="flex items-center justify-center bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-2.5 rounded-xl group-hover:shadow-lg group-hover:shadow-blue-500/30 transition duration-300">
                        <i class="fa-solid fa-calculator text-lg"></i>
                    </div>
                    <div class="leading-tight">
                        <h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></h1>
                    </div>
                </a>
                <a href="../index.html" class="bg-gradient-to-r from-blue-600 to-blue-500 text-white text-xs font-bold px-4 py-2 rounded-full shadow-sm hover:shadow-md transition flex items-center gap-2">
                    <span>Tüm Araçlar</span> <i class="fa-solid fa-arrow-right text-xs opacity-70"></i>
                </a>
            </div>
        </div>
    </header>

    <div class="container mx-auto px-4 py-8 lg:py-12 flex-grow">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12">
            <!-- Main Content -->
            <main class="lg:col-span-8">
                <!-- Breadcrumb -->
                <nav class="flex text-xs text-slate-500 mb-6 uppercase tracking-wide font-bold">
                    <a href="../index.html" class="hover:text-blue-600">Anasayfa</a>
                    <span class="mx-2">/</span>
                    <a href="index.html" class="hover:text-blue-600">Blog</a>
                    <span class="mx-2">/</span>
                    <span class="text-slate-800" id="crumb-title">[[TITLE]]</span>
                </nav>

                <article>
                    <div class="mb-8">
                        <span id="post-cat" class="text-xs font-bold text-[[COLOR]]-600 bg-[[COLOR]]-50 px-3 py-1 rounded-full uppercase tracking-wider">[[CATEGORY]]</span>
                        <h1 id="post-title" class="text-3xl md:text-4xl font-extrabold text-slate-900 mt-4 leading-tight">[[TITLE]]</h1>
                        <p id="post-summary" class="text-lg text-slate-500 mt-4 leading-relaxed">[[SUMMARY]]</p>
                    </div>

                    <!-- Featured Image / Icon Area -->
                    <div class="bg-slate-100 rounded-2xl h-64 md:h-80 flex items-center justify-center mb-10 text-slate-300 overflow-hidden relative">
                         <div class="absolute inset-0 bg-gradient-to-br from-[[COLOR]]-50 to-slate-100 opacity-50"></div>
                         <i id="post-icon" class="fa-solid [[IMAGE]] text-9xl opacity-20 text-[[COLOR]]-500 transform scale-110"></i>
                    </div>

                    <!-- Content Body -->
                    <div class="prose max-w-none" id="content-body">
                        [[CONTENT]]
                    </div>
                </article>
            </main>

            <!-- Sidebar -->
            <aside class="lg:col-span-4">
                <div class="sticky top-24 space-y-8">
                    <div class="bg-white rounded-2xl shadow-sm border border-slate-200 p-6">
                        <h4 class="font-bold text-slate-900 mb-4 border-b pb-2 flex items-center gap-2">
                            <i class="fa-solid fa-list-ul text-blue-600"></i> İçindekiler
                        </h4>
                        <nav id="toc" class="text-sm space-y-2 text-slate-600"></nav>
                    </div>

                    <div id="cta-widget" class="hidden bg-gradient-to-br from-indigo-600 to-blue-700 rounded-2xl shadow-lg p-6 text-white text-center relative overflow-hidden">
                        <div class="absolute top-0 right-0 p-4 opacity-10">
                            <i class="fa-solid fa-calculator text-9xl transform rotate-12 translate-x-4 -translate-y-4"></i>
                        </div>
                        <div class="relative z-10">
                            <h3 class="text-xl font-bold mb-2">Hemen Hesaplayın!</h3>
                            <p class="text-blue-100 text-sm mb-6">Bu konuyla ilgili hesaplamalarınızı ücretsiz aracımızla saniyeler içinde yapın.</p>
                            <a href="#" id="cta-link" class="inline-block w-full bg-white text-blue-700 font-bold py-3 px-6 rounded-xl shadow-md hover:bg-blue-50 transition transform hover:scale-105">
                                Araca Git <i class="fa-solid fa-arrow-right ml-2"></i>
                            </a>
                        </div>
                    </div>
                </div>
            </aside>
        </div>
    </div>

    <footer class="bg-slate-900 text-slate-400 py-12 mt-auto border-t border-slate-800">
        <div class="container mx-auto px-4 text-center">
            <span class="text-2xl font-bold text-white tracking-tight">Hesapla<span class="text-blue-500">Hadi</span></span>
            <div class="text-xs text-slate-600 mt-6">&copy; 2026 HesaplaHadi.</div>
        </div>
    </footer>

    <script src="../assets/js/blog-data.js"></script>
    <script>
        function loadPostData() {
            const post = getCurrentPost();
            if(!post) return;

            if(post.relatedTool && post.relatedTool !== "null") {
                const cta = document.getElementById('cta-widget');
                const btn = document.getElementById('cta-link');
                let link = `../index.html#btn-${post.relatedTool}`;
                const standaloneMap = {
                    'kdv': '../kdv-hesaplama.html',
                    'tevkifat': '../tevkifat-hesaplama.html',
                    'kredi': '../kredi-hesaplama.html',
                    'ai_asistan': '../ai-asistan.html',
                    'bmi': '../vucut-kitle-i̇ndeksi-bmi-hesaplama.html',
                    'net_brut': '../netten-brute-maas-hesaplama-2026.html'
                };
                if(standaloneMap[post.relatedTool]) link = standaloneMap[post.relatedTool];
                btn.href = link;
                cta.classList.remove('hidden');
            }
        }

        function generateTOC() {
            const content = document.getElementById('content-body');
            const tocNav = document.getElementById('toc');
            const headers = content.querySelectorAll('h2, h3');
            if(headers.length === 0) {
                tocNav.parentElement.classList.add('hidden');
                return;
            }
            headers.forEach((header, index) => {
                if(!header.id) header.id = `section-${index}`;
                const link = document.createElement('a');
                link.href = `#${header.id}`;
                link.innerText = header.innerText;
                link.className = `block toc-link hover:text-blue-600 transition truncate ${header.tagName === 'H3' ? 'pl-4 text-xs' : ''}`;
                link.onclick = (e) => {
                    e.preventDefault();
                    document.getElementById(header.id).scrollIntoView({behavior: 'smooth'});
                };
                tocNav.appendChild(link);
            });
        }

        window.onload = function() {
            loadPostData();
            setTimeout(generateTOC, 100);
        };
    </script>
</body>
</html>
"""

BLOG_INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog - HesaplaHadi</title>
    <meta name="description" content="Finans, sağlık, vergi ve daha birçok konuda en güncel hesaplama yöntemleri ve ipuçları HesaplaHadi blogunda.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="../assets/css/style.css" rel="stylesheet">
    <link rel="icon" type="image/svg+xml" href="../assets/img/favicon.svg">
</head>
<body class="flex flex-col min-h-screen text-slate-800 bg-slate-50">
    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-md shadow-sm sticky top-0 z-50 border-b border-slate-100">
        <div class="container mx-auto px-4 py-3">
            <div class="flex justify-between items-center">
                <a href="../index.html" class="flex items-center space-x-2 group">
                    <div class="flex items-center justify-center bg-gradient-to-br from-blue-600 to-indigo-700 text-white p-2.5 rounded-xl group-hover:shadow-lg group-hover:shadow-blue-500/30 transition duration-300">
                        <i class="fa-solid fa-calculator text-lg"></i>
                    </div>
                    <div class="leading-tight">
                        <h1 class="text-xl md:text-2xl font-extrabold tracking-tight text-slate-900">Hesapla<span class="text-blue-600">Hadi</span></h1>
                    </div>
                </a>
                <a href="../index.html" class="bg-gradient-to-r from-blue-600 to-blue-500 text-white text-xs font-bold px-4 py-2 rounded-full shadow-sm hover:shadow-md transition flex items-center gap-2">
                    <span>Tüm Araçlar</span> <i class="fa-solid fa-arrow-right text-xs opacity-70"></i>
                </a>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="container mx-auto px-4 py-8 lg:py-12 flex-grow">
        <div class="text-center max-w-3xl mx-auto mb-12">
            <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tighter">HesaplaHadi Blog</h1>
            <p class="mt-4 text-lg text-slate-600">Finans, sağlık, vergi ve daha birçok konuda en güncel hesaplama yöntemleri ve ipuçları.</p>
        </div>

        <!-- Blog Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            [[BLOG_CARDS]]
        </div>
    </main>

    <footer class="bg-slate-900 text-slate-400 py-12 mt-auto border-t border-slate-800">
        <div class="container mx-auto px-4 text-center">
            <span class="text-2xl font-bold text-white tracking-tight">Hesapla<span class="text-blue-500">Hadi</span></span>
            <div class="text-xs text-slate-600 mt-6">&copy; 2026 HesaplaHadi.</div>
        </div>
    </footer>
</body>
</html>
"""

BLOG_CARD_TEMPLATE = """<a href="[[SLUG]]" class="block bg-white rounded-2xl shadow-sm border border-slate-200/80 overflow-hidden group transition hover:shadow-lg hover:-translate-y-1 hover:border-blue-300">
    <div class="h-40 bg-[[COLOR]]-50 flex items-center justify-center text-[[COLOR]]-300 relative">
        <i class="fa-solid [[IMAGE]] text-6xl"></i>
        <div class="absolute top-2 right-2 bg-white/80 text-[[COLOR]]-700 text-[10px] font-bold uppercase px-2 py-0.5 rounded-full">[[CATEGORY]]</div>
    </div>
    <div class="p-6">
        <h3 class="font-bold text-slate-900 text-lg mb-2 leading-tight">[[TITLE]]</h3>
        <p class="text-sm text-slate-600 leading-relaxed">[[SUMMARY]]</p>
    </div>
</a>"""

def generate_blog_index():
    """Generates the main blog listing page (index.html) from all posts."""
    cards_html = []
    for post in BLOG_POSTS:
        card = BLOG_CARD_TEMPLATE.replace("[[SLUG]]", post.get("slug", "#"))
        card = card.replace("[[TITLE]]", post.get("title", "Başlık Yok"))
        card = card.replace("[[SUMMARY]]", post.get("summary", ""))
        card = card.replace("[[CATEGORY]]", post.get("category", "Genel"))
        card = card.replace("[[IMAGE]]", post.get("image", "fa-file-alt"))
        card = card.replace("[[COLOR]]", post.get("color", "slate"))
        cards_html.append(card)

    final_html = BLOG_INDEX_TEMPLATE.replace("[[BLOG_CARDS]]", "\n".join(cards_html))
    
    filepath = os.path.join("blog", "index.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"Blog index page '{filepath}' rebuilt successfully.")

def rebuild_blog_posts():
    """Rebuilds individual blog post HTML files based on the source of truth."""
    if not BLOG_POSTS:
        print("No blog posts found to rebuild. Exiting.")
        return

    if not os.path.exists("blog"):
        os.makedirs("blog")

    for post in BLOG_POSTS:
        slug = post.get('slug')
        if not slug:
            print(f"Skipping post with missing slug: {post.get('title')}")
            continue

        filepath = os.path.join("blog", slug)
        
        content_body = ""
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                existing_html = f.read()
                match = re.search('<div class=\"[^\"]*prose[^\"]*\">([\s\S]*?)<\/div>', existing_html, re.DOTALL)
                if match:
                    content_body = match.group(1).strip()
                else:
                    content_body = f"<p>İçerik korunamadı, lütfen kontrol edin.</p>"
        else:
            content_body = f"<h2>{post.get('title')}</h2><p>{post.get('summary')}</p><p>Bu içerik yakında güncellenecektir.</p>"

        html = HTML_TEMPLATE.replace("[[TITLE]]", post.get("title", "Başlık Yok"))\
                           .replace("[[SUMMARY]]", post.get("summary", ""))\
                           .replace("[[SLUG]]", slug)\
                           .replace("[[CATEGORY]]", post.get("category", "Genel"))\
                           .replace("[[COLOR]]", post.get("color", "slate"))\
                           .replace("[[IMAGE]]", post.get("image", "fa-file-alt"))\
                           .replace("[[CONTENT]]", content_body)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

    print(f"{len(BLOG_POSTS)} blog posts processed.")


if __name__ == "__main__":
    rebuild_blog_posts()
    generate_blog_index()
