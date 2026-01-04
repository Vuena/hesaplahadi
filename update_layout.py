import os
import re
import sys

# --- CONFIGURATION ---
INDEX_FILE = 'index.html'

def get_outdated_files():
    outdated = []
    for f in sorted(os.listdir('.')):
        if f.endswith('.html') and f != 'index.html' and not f.startswith('blog/'):
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
                # Check for the marker of the updated layout
                if 'id="recent-blog-list"' not in content:
                    outdated.append(f)
    return outdated

def extract_master_components():
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    components = {}

    header_match = re.search(r'(<header.*?</header>)', content, re.DOTALL)
    if header_match:
        components['header'] = header_match.group(1)

    nav_match = re.search(r'(<nav class="hidden lg:block lg:col-span-3.*?</nav>)', content, re.DOTALL)
    if nav_match:
        components['nav'] = nav_match.group(1)

    aside_match = re.search(r'(<aside class="col-span-1 lg:col-span-3 space-y-6">.*?</aside>)', content, re.DOTALL)
    if aside_match:
        components['aside'] = aside_match.group(1)

    footer_match = re.search(r'(<footer.*?</footer >|<footer.*?</footer>)', content, re.DOTALL)
    if footer_match:
        components['footer'] = footer_match.group(1)

    drawer_mask = re.search(r'(<div id="drawer-mask".*?</div>)', content, re.DOTALL)
    drawer = re.search(r'(<aside id="drawer".*?</aside>)', content, re.DOTALL)
    if drawer_mask and drawer:
        components['drawer'] = drawer_mask.group(1) + '\n  ' + drawer.group(1)

    return components

def update_file(filepath, components):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    is_grid = 'class="col-span-1 lg:col-span-6' in content

    if is_grid:
        if 'header' in components:
            content = re.sub(r'<header.*?</header>', components['header'], content, flags=re.DOTALL)
        if 'nav' in components:
            content = re.sub(r'<nav class="hidden lg:block lg:col-span-3.*?</nav>', components['nav'], content, flags=re.DOTALL)
        if 'aside' in components:
             content = re.sub(r'<aside class="col-span-1 lg:col-span-3.*?</aside>', components['aside'], content, flags=re.DOTALL)
        if 'footer' in components:
            content = re.sub(r'<footer.*?</footer>', components['footer'], content, flags=re.DOTALL)
        if 'drawer' in components:
             if 'id="drawer-mask"' in content:
                 content = re.sub(r'<div id="drawer-mask".*?</div>', '', content, flags=re.DOTALL)
                 content = re.sub(r'<aside id="drawer".*?</aside>', '', content, flags=re.DOTALL)
                 content = re.sub(r'(<body.*?>)', r'\1\n  ' + components['drawer'], content, count=1)
             else:
                 content = re.sub(r'(<body.*?>)', r'\1\n  ' + components['drawer'], content, count=1)
        new_content = content
    else:
        # Scenario B
        head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
        head_content = head_match.group(1) if head_match else ""

        main_match = re.search(r'<main.*?>(.*?)</main>', content, re.DOTALL)
        tool_content = ""
        if main_match:
            raw_main = main_match.group(1)
            if 'class="max-w-4xl mx-auto' in raw_main:
                 raw_main = re.sub(r'<header.*?</header>', '', raw_main, flags=re.DOTALL)
                 tool_content = raw_main
            else:
                tool_content = raw_main
        else:
            print(f"Skipping {filepath}: No <main> tag.")
            return

        new_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
{head_content}
<style>
    .drawer-open {{ transform: translateX(0); }}
    .drawer-closed {{ transform: translateX(-100%); }}
    .mask-visible {{ opacity: 1; pointer-events: auto; }}
    .mask-hidden {{ opacity: 0; pointer-events: none; }}
  </style>
</head>
<body class="flex flex-col min-h-screen text-slate-800 bg-slate-50">

  {components['drawer']}

  {components['header']}

  <div class="container mx-auto px-4 py-6 md:py-8 grid grid-cols-1 lg:grid-cols-12 gap-8 flex-grow">

    {components['nav']}

    <main class="col-span-1 lg:col-span-6 space-y-6">
      {tool_content}
    </main>

    {components['aside']}

  </div>

  {components['footer']}

  <script src="assets/js/calculator.js?v=3"></script>
  <script src="assets/js/blog-data.js"></script>
  <script>
    // Drawer Logic
    function toggleDrawer() {{
      const d = document.getElementById('drawer');
      const m = document.getElementById('drawer-mask');
      if(d.classList.contains('drawer-closed')) {{
        d.classList.remove('drawer-closed');
        d.classList.add('drawer-open');
        m.classList.remove('mask-hidden');
        m.classList.add('mask-visible');
      }} else {{
        d.classList.remove('drawer-open');
        d.classList.add('drawer-closed');
        m.classList.remove('mask-visible');
        m.classList.add('mask-hidden');
      }}
    }}

    // Search in Drawer
    function filterDrawerTools() {{
      const q = document.getElementById('mobile-tool-search').value.toLowerCase();
      const drawerList = document.getElementById('drawer-list');
      const items = drawerList.querySelectorAll('a'); // Assuming links

      items.forEach(item => {{
        if(item.classList.contains('cat-header')) return; // skip headers
        const txt = item.innerText.toLowerCase();
        item.style.display = txt.includes(q) ? 'flex' : 'none';
      }});
    }}

    // Init
    window.addEventListener('load', () => {{
      renderRecentBlog();
    }});

    function renderRecentBlog() {{
      const container = document.getElementById('recent-blog-list');
      if(!container) return;
      const recent = [...blogPosts].reverse().slice(0, 3);
      container.innerHTML = "";
      recent.forEach(post => {{
        const a = document.createElement('a');
        a.href = `blog/${{post.slug}}`;
        a.className = "block group mb-3 last:mb-0";
        a.innerHTML = `
          <div class="flex items-start gap-3">
            <div class="shrink-0 mt-1"><i class="fa-solid ${{post.image || 'fa-file-lines'}} text-blue-300 group-hover:text-blue-500 transition"></i></div>
            <div>
              <p class="text-sm text-slate-700 font-bold group-hover:text-blue-600 transition leading-snug">${{post.title}}</p>
            </div>
          </div>
        `;
        container.appendChild(a);
      }});
    }}
  </script>
</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 update_layout.py <start_index> <count>")
        sys.exit(1)

    start_index = int(sys.argv[1])
    count = int(sys.argv[2])

    comps = extract_master_components()
    files = get_outdated_files()

    batch = files[start_index : start_index + count]
    print(f"Processing batch from {start_index} to {start_index+count}. Found {len(batch)} files.")

    for f in batch:
        update_file(f, comps)

if __name__ == "__main__":
    main()
