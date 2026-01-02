import os
import re

def audit_site():
    print("Starting Site Audit...")
    errors = []
    warnings = []

    files = []
    for root, dirs, filenames in os.walk("."):
        if "node_modules" in root or ".git" in root:
            continue
        for f in filenames:
            if f.endswith(".html"):
                files.append(os.path.join(root, f))

    print(f"Found {len(files)} HTML files.")

    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check Title
        if "<title>" not in content:
            errors.append(f"{filepath}: Missing <title>")
        elif "<title></title>" in content:
             errors.append(f"{filepath}: Empty <title>")

        # Check Description
        if 'meta name="description"' not in content and "meta name='description'" not in content:
             errors.append(f"{filepath}: Missing meta description")

        # Check Canonical
        if 'link rel="canonical"' not in content:
             warnings.append(f"{filepath}: Missing canonical link")

        # Check H1
        if "<h1>" not in content:
            warnings.append(f"{filepath}: Missing <h1> tag")

        # Check Character Set
        if 'charset="UTF-8"' not in content and "charset='UTF-8'" not in content:
            errors.append(f"{filepath}: Missing charset definition")

    if errors:
        print("\nERRORS FOUND:")
        for e in errors:
            print(f"- {e}")
    else:
        print("\nNo critical errors found.")

    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f"- {w}")
    else:
        print("\nNo warnings.")

if __name__ == "__main__":
    audit_site()
