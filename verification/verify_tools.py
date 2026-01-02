import os
import re

def verify_tools_array():
    # Read calculator.js
    with open('assets/js/calculator.js', 'r') as f:
        content = f.read()

    # Extract tools array content (simple regex approach)
    match = re.search(r'const tools = \[(.*?)\];', content, re.DOTALL)
    if not match:
        print("ERROR: Could not find tools array in calculator.js")
        return False

    tools_content = match.group(1)

    # Find all link properties
    links = re.findall(r"link:\s*['\"]([^'\"]+)['\"]", tools_content)
    print(f"Found {len(links)} tools configured in calculator.js")

    # List all .html files in root
    files = [f for f in os.listdir('.') if f.endswith('hesaplama.html') or f in ['ai-asistan.html', 'ai-diyetisyen.html', 'cekilis-araci.html', 'kidem-tazminati.html']]

    missing = []
    for f in files:
        if f not in links:
            # Ignore some known exceptions or duplicates if any
            if f == 'kidem-tazminati.html' and 'kidem-tazminati-hesaplama.html' in links: continue
            missing.append(f)

    if missing:
        print(f"WARNING: The following {len(missing)} files are not in the tools array:")
        for m in missing:
            print(f" - {m}")
        return False

    print("SUCCESS: All tool files appear to be registered in calculator.js")
    return True

if __name__ == "__main__":
    verify_tools_array()
