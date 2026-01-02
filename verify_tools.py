import os
import re

def get_defined_functions():
    defined_funcs = set()
    js_files = ['assets/js/calculator.js', 'assets/js/tools-2026.js']

    # Regex to find function definitions: function myFunc() or myFunc = function() or const myFunc = () =>
    # Simplified for this project's style: function myFunc()
    pattern = re.compile(r'function\s+([a-zA-Z0-9_]+)\s*\(')

    for js_file in js_files:
        if os.path.exists(js_file):
            with open(js_file, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = pattern.findall(content)
                defined_funcs.update(matches)

    # Add common built-ins or globals if necessary
    defined_funcs.add('toggleDrawer')
    defined_funcs.add('filterDrawerTools')
    defined_funcs.add('acceptCookies')
    defined_funcs.add('copyResult')
    defined_funcs.add('window.location.href') # Logic in onclick
    return defined_funcs

def check_html_files(defined_funcs):
    issues = []
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and not f.startswith('ai-')]

    # Regex for onclick="funcName(...)"
    # We want to capture the function name before the parenthesis
    pattern = re.compile(r'onclick=["\']\s*([a-zA-Z0-9_]+)\s*\(')

    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = pattern.findall(content)
            for func_name in matches:
                if func_name not in defined_funcs:
                    # Ignore common safe calls or inline JS
                    if func_name in ['alert', 'console', 'window', 'location']:
                        continue
                    issues.append(f"{html_file}: Calls undefined function '{func_name}'")

    return issues

if __name__ == "__main__":
    funcs = get_defined_functions()
    problems = check_html_files(funcs)

    if problems:
        print("Found issues:")
        for p in problems:
            print(p)
    else:
        print("No broken onclick handlers found.")
