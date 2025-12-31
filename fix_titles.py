import glob
import re

def fix_titles():
    files = glob.glob('*.html')
    for filepath in files:
        if filepath == 'index.html':
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. Update <title> content
        # Regex to find <title>...</title>
        title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
        if title_match:
            title_text = title_match.group(1)
            # Check if it ends with "Hesaplama" or "Hesaplama..." (ignoring " - SiteName")
            # Usually format is "Tool Name - ... | HesaplaHadi"

            parts = title_text.split('|')
            main_title_part = parts[0].strip()

            # Simple heuristic: if "Hesaplama" is not in the first part, add it.
            # But be careful not to double it or make it "Netten Brüte Maaş Hesaplama 2026 Hesaplama"

            # Let's clean the main part. Remove " 2026", " - ...", etc temporarily?
            # User request: "örneğin bileşik faiz yazıyorsa bileşik faiz hesaplama olarak değiştir"

            # Strategy: Look for specific tool names or general patterns.
            # If the H1 is "KDV", make it "KDV Hesaplama".
            # It's safer to just check if "Hesaplama" word is present in the title close to the tool name.

            if "Hesaplama" not in main_title_part:
                # Need to be smart. "Kıdem Tazminatı" -> "Kıdem Tazminatı Hesaplama"
                # "Netten Brüte Maaş" -> "Netten Brüte Maaş Hesaplama"

                # Let's insert "Hesaplama" before " 2026" or " -" or "|"

                new_main_title = main_title_part
                if "2026" in new_main_title:
                    new_main_title = new_main_title.replace(" 2026", " Hesaplama 2026")
                elif " -" in new_main_title:
                     new_main_title = new_main_title.replace(" -", " Hesaplama -")
                else:
                    new_main_title = new_main_title + " Hesaplama"

                # Reconstruct
                new_title_text = title_text.replace(main_title_part, new_main_title)
                content = content.replace(f'<title>{title_text}</title>', f'<title>{new_title_text}</title>')
                print(f"Updated Title in {filepath}: {new_title_text}")

        # 2. Update <h1> content
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
        if h1_match:
            h1_full = h1_match.group(0)
            h1_text = h1_match.group(1) # This might contain spans.
            # Remove HTML tags for checking text
            clean_text = re.sub(r'<[^>]+>', '', h1_text).strip()

            if "HesaplaHadi" in clean_text: # Skip logo/header H1 if it's the main logo (usually in header)
                # Note: Tool pages usually have a second H1 or the main content H1.
                # In the current template, the header logo is H1 on tool pages?
                # Let's check kdv-hesaplama.html
                # Header: <h1 ...>Hesapla<span...>Hadi</span></h1>
                # Content: <h1 ...>KDV Hesaplama</h1>
                pass

            # Find the Content H1. It is usually inside <main>.
            # Let's use specific regex for the Content H1 which usually doesn't have "HesaplaHadi".

            content_h1_match = re.search(r'<main.*?(<h1[^>]*>.*?</h1>)', content, re.DOTALL)
            if content_h1_match:
                inner_h1 = content_h1_match.group(1)
                inner_h1_text = re.sub(r'<[^>]+>', '', inner_h1).strip()

                if "Hesaplama" not in inner_h1_text and "Asistan" not in inner_h1_text:
                    # Update it.
                    # We need to replace the text inside the H1 tag, preserving attributes.
                    # Warning: Regex replace on H1 content might be tricky if it has spans.
                    # But usually tool H1 is simple text.

                    new_h1_text = inner_h1_text + " Hesaplama"
                    new_inner_h1 = inner_h1.replace(inner_h1_text, new_h1_text)
                    content = content.replace(inner_h1, new_inner_h1)
                    print(f"Updated H1 in {filepath}: {new_h1_text}")

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == "__main__":
    fix_titles()
