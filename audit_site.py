
import os
from bs4 import BeautifulSoup

def audit_page(path):
    print(f"\n--- Auditing: {path} ---")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # 1. Check Title
        title = soup.find('title')
        if not title or not title.string:
            print("  [FAIL] Missing or empty <title> tag.")
        elif len(title.string) < 10:
            print(f"  [WARN] Title is too short: \"{title.string}\"")
        else:
            print(f"  [PASS] Title: \"{title.string}\"")

        # 2. Check Meta Description
        description = soup.find('meta', attrs={'name': 'description'})
        if not description or not description.get('content'):
            print("  [FAIL] Missing or empty meta description.")
        elif len(description.get('content', '')) < 50:
            print(f"  [WARN] Meta description is too short: \"{description.get('content', '')}\"")
        else:
            print(f"  [PASS] Meta description is good.")

        # 3. Check H1 Tag
        h1_tags = soup.find_all('h1')
        if len(h1_tags) == 0:
            print("  [FAIL] No <h1> tag found.")
        elif len(h1_tags) > 1:
            print(f"  [WARN] Found {len(h1_tags)} <h1> tags. Should only be one.")
            for i, h1 in enumerate(h1_tags):
                print(f"     - H1 #{i+1}: \"{h1.string.strip()}\"")
        else:
            print(f"  [PASS] Single <h1> tag: \"{h1_tags[0].string.strip()}\"")

    except Exception as e:
        print(f"  [ERROR] Could not audit file: {e}")


def main():
    for root, _, files in os.walk('.'):
        # Ignore files in 'tests' and '__pycache__'
        if 'tests' in root or '__pycache__' in root or '.idx' in root or 'verification' in root:
            continue

        for file in files:
            if file.endswith('.html'):
                audit_page(os.path.join(root, file))

if __name__ == "__main__":
    main()

