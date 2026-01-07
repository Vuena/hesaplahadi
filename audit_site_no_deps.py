
import os
import re

def audit_page(path):
    print(f"\n--- Auditing: {path} ---")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Check Title using regex
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if not title_match or not title_match.group(1).strip():
            print("  [FAIL] Missing or empty <title> tag.")
        elif len(title_match.group(1).strip()) < 10:
            print(f'  [WARN] Title is too short: \"{title_match.group(1).strip()}\"')
        else:
            print(f'  [PASS] Title: \"{title_match.group(1).strip()}\"')

        # 2. Check Meta Description using regex
        # Corrected regex to handle quotes properly and fix the syntax error.
        desc_match = re.search(r'''<meta[^>]+name=["']description["'][^>]+content=["'](.*?)["']''', content, re.IGNORECASE)
        if not desc_match or not desc_match.group(1).strip():
            print("  [FAIL] Missing or empty meta description.")
        elif len(desc_match.group(1).strip()) < 50:
            print(f'  [WARN] Meta description is too short: \"{desc_match.group(1).strip()}\"')
        else:
            print("  [PASS] Meta description is good.")

        # 3. Check H1 Tag using regex
        h1_matches = re.findall(r'<h1[^>]*>', content, re.IGNORECASE)
        if len(h1_matches) == 0:
            print("  [FAIL] No <h1> tag found.")
        elif len(h1_matches) > 1:
            print(f"  [WARN] Found {len(h1_matches)} <h1> tags. Should only be one.")
        else:
            h1_content_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
            if h1_content_match:
                # Strip tags from the content to get clean text
                h1_text = re.sub(r'<[^>]+>', '', h1_content_match.group(1)).strip()
                print(f'  [PASS] Single <h1> tag found: \"{h1_text}\"')
            else:
                 print("  [PASS] Single <h1> tag found, but content could not be extracted.")

    except Exception as e:
        print(f"  [ERROR] Could not audit file: {e}")

def main():
    ignored_dirs = {'.git', '.vscode', 'node_modules', '__pycache__', 'assets', '.idx', 'verification', 'tests'}
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for file in files:
            if file.endswith(('.html', '.htm')):
                audit_page(os.path.join(root, file))

if __name__ == "__main__":
    main()
