import re
import os

def get_tools_from_js(js_path="assets/js/calculator.js"):
    """
    Parses the tools array from calculator.js to ensure single source of truth.
    """
    if not os.path.exists(js_path):
        # Fallback if file doesn't exist (e.g. running in a different context)
        # Try finding it relative to current script if needed, or just fail gracefully
        if os.path.exists("../assets/js/calculator.js"):
            js_path = "../assets/js/calculator.js"
        else:
            return []

    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the tools array
    # Looking for: const tools = [ ... ];
    match = re.search(r'const tools = \[(.*?)\];', content, re.DOTALL)
    if not match:
        print("Could not find tools array in calculator.js")
        return []

    tools_str = match.group(1)

    tools = []

    # Iterate over lines to extract tool objects
    for line in tools_str.split('\n'):
        line = line.strip()
        if not line or line.startswith('//'):
            continue

        try:
            tool = {}
            # Extract fields using regex
            id_match = re.search(r"id:\s*['\"](.*?)['\"]", line)
            cat_match = re.search(r"cat:\s*['\"](.*?)['\"]", line)
            name_match = re.search(r"name:\s*['\"](.*?)['\"]", line)
            link_match = re.search(r"link:\s*['\"](.*?)['\"]", line)

            if id_match and cat_match and name_match and link_match:
                tool['id'] = id_match.group(1)
                tool['cat'] = cat_match.group(1)
                tool['name'] = name_match.group(1)
                tool['link'] = link_match.group(1)
                tools.append(tool)
        except Exception as e:
            continue

    return tools

def generate_sidebar_html(tools, current_page_link=None, is_drawer=False, link_prefix=""):
    """
    Generates the HTML for the sidebar/drawer matching calculator.js renderSidebar logic.
    """

    # Get unique categories maintaining order
    categories = []
    seen_cats = set()
    for tool in tools:
        if tool['cat'] not in seen_cats:
            categories.append(tool['cat'])
            seen_cats.add(tool['cat'])

    html_parts = []

    for cat in categories:
        # Header
        html_parts.append(f'<div class="cat-header">{cat}</div>')

        # Tools in this category
        cat_tools = [t for t in tools if t['cat'] == cat]

        for tool in cat_tools:
            # Check for drawer filter: remove "Tüm Hesaplamalar"
            if is_drawer:
                if 'tüm hesaplama' in tool['name'].lower() or 'tum hesaplama' in tool['name'].lower():
                    continue

            # Determine Icon
            icon = '<span class="w-1.5 h-1.5 rounded-full bg-slate-300"></span>'
            if tool['cat'] == 'Yapay Zeka':
                icon = '<i class="fa-solid fa-wand-magic-sparkles text-indigo-500"></i>'
            elif tool['cat'] == 'E-Ticaret':
                icon = '<i class="fa-solid fa-shop text-orange-500"></i>'

            # Active State
            active_class = ""
            # Check if current_page matches.
            # current_page_link is typically just the filename (e.g. 'index.html')
            if current_page_link and current_page_link == tool['link']:
                active_class = " nav-active bg-blue-50 text-blue-600"

            # Construct Link
            href = link_prefix + tool['link']

            html_parts.append(
                f'<a href="{href}" class="w-full text-left px-4 py-3 rounded-xl text-xs font-medium transition flex items-center nav-item gap-3 mb-1 text-slate-500 hover:bg-slate-50 hover:text-blue-600 block{active_class}">'
                f'{icon} {tool["name"]}'
                f'</a>'
            )

    return "".join(html_parts)

def get_popular_tools_html(link_prefix=""):
    """
    Generates the HTML for the popular tools widget (Right Sidebar).
    """
    popular_links = [
        ('KDV Hesaplama', 'kdv-hesaplama.html'),
        ('Tevkifat Hesapla', 'tevkifat-hesaplama.html'),
        ('Kredi Hesaplama', 'kredi-hesaplama.html'),
        ('Netten Brüte Maaş', 'netten-brute-maas-hesaplama.html'),
        ('Vücut Kitle İndeksi', 'vucut-kitle-i̇ndeksi-bmi-hesaplama.html')
    ]

    html = '<h4 class="font-bold text-xs text-slate-500 mb-4 uppercase tracking-wider border-b border-slate-100 pb-2 flex items-center gap-2"><i class="fa-solid fa-fire text-orange-500"></i> Popüler Araçlar</h4>'
    html += '<ul class="text-sm space-y-2 text-slate-600 font-medium">'

    for name, link in popular_links:
        href = link_prefix + link
        # Note: JS onclick uses window.location.href.
        # For static SEO friendliness, we should preferably use <a> tags, but the existing design uses <li> with onclick.
        # The user requested "statik linkli" for sidebar. Right sidebar is "nice to have".
        # I will keep the existing structure but update the href in onclick if needed,
        # OR better, convert to <a> tags inside <li> to be truly SEO friendly if I can without breaking layout.
        # The current layout: <li ... onclick="...">...</li>
        # Converting to <a class="block ...">...</a> inside <li> or just <a> might change display.
        # I'll stick to the requested text for now but ensure path is correct.

        html += f'''
          <li class="cursor-pointer hover:text-blue-600 hover:bg-blue-50 p-2.5 rounded-lg transition flex items-center justify-between group" onclick="window.location.href='{href}'">
            <span>{name}</span> <i class="fa-solid fa-chevron-right text-xs opacity-30"></i>
          </li>'''

    html += '</ul>'
    return html

if __name__ == "__main__":
    tools = get_tools_from_js()
    print(f"Found {len(tools)} tools.")
