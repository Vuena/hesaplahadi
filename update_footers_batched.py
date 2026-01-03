import os
import re
import argparse

# The new footer content with Blog and AI Asistan restored
NEW_FOOTER = """<footer class="bg-slate-900 text-slate-400 py-12 mt-auto border-t border-slate-800">
    <div class="container mx-auto px-4 text-center">
      <span class="text-2xl font-bold text-white tracking-tight">Hesapla<span class="text-blue-500">Hadi</span></span>
      <div class="flex justify-center flex-wrap gap-6 text-sm font-medium mt-6 text-slate-300">
        <a href="index.html" class="hover:text-white transition">Ana Sayfa</a>
        <a href="blog/index.html" class="hover:text-white transition">Blog</a>
        <a href="ai-asistan.html" class="hover:text-white transition">AI Asistan</a>
        <a href="hakkimizda.html" class="hover:text-white transition">Hakkımızda</a>
        <a href="gizlilik-politikasi.html" class="hover:text-white transition">Gizlilik Politikası</a>
        <a href="iletisim.html" class="hover:text-white transition">İletişim</a>
      </div>
      <div class="text-xs text-slate-600 mt-6">&copy; HesaplaHadi.</div>
    </div>
  </footer>"""

def update_footer(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find the footer block
        # matches <footer ... > ... </footer>
        footer_regex = re.compile(r'<footer.*?</footer>', re.DOTALL)

        if not footer_regex.search(content):
            print(f"Skipping {filepath}: Footer not found.")
            return False

        new_content = footer_regex.sub(NEW_FOOTER, content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
        return True
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Batch update footers.")
    parser.add_argument('--start', type=int, default=0, help='Start index')
    parser.add_argument('--end', type=int, default=20, help='End index')
    args = parser.parse_args()

    # Get all HTML files
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    files.sort() # Ensure deterministic order

    # Slice the list
    batch = files[args.start:args.end]

    print(f"Processing batch: {args.start} to {args.end} (Total files in batch: {len(batch)})")

    count = 0
    for f in batch:
        if update_footer(f):
            count += 1

    print(f"Batch complete. Updated {count} files.")

if __name__ == "__main__":
    main()
