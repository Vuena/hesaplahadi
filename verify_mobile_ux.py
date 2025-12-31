from playwright.sync_api import sync_playwright
import os

def verify_mobile_header():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": 375, "height": 667},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1"
        )

        # 1. Verify Index Page (Hamburger, AI Btn, Search)
        print("Navigating to Index...")
        page.goto(f"file://{os.getcwd()}/index.html")
        page.wait_for_selector("header")

        # Check Hamburger
        hamburger = page.query_selector('button[onclick="toggleDrawer()"]')
        if hamburger and page.evaluate("el => getComputedStyle(el).display !== 'none'", hamburger):
            print("SUCCESS: Hamburger menu found.")
        else:
            print("FAILURE: Hamburger menu missing or hidden.")

        # Check AI Button (Mobile) - using attribute selector only
        ai_btn = page.query_selector('a[href="ai-asistan.html"].md\:hidden') # Escaping colon or use separate class check
        # Actually playwright selector engine supports CSS. :hidden is a pseudo-class.
        # The class name is "md:hidden". In CSS selector you must escape colon: .md\:hidden
        # Let's just use the href and check class in python.

        ai_btns = page.query_selector_all('a[href="ai-asistan.html"]')
        mobile_ai_found = False
        for btn in ai_btns:
            classes = btn.get_attribute("class")
            if "md:hidden" in classes:
                mobile_ai_found = True
                break

        if mobile_ai_found:
            print("SUCCESS: Mobile AI Button found.")
        else:
            print("FAILURE: Mobile AI Button missing.")

        # Check Search Bar (Mobile)
        search_bar = page.query_selector('input#mobile-tool-search')
        if search_bar and page.evaluate("el => el.offsetParent !== null", search_bar):
             print("SUCCESS: Mobile Search Bar found.")
        else:
             print("FAILURE: Mobile Search Bar missing.")

        page.screenshot(path="verification/mobile_index_header.png")

        # 2. Verify Blog Page (Araçlar Button)
        blog_path = f"file://{os.getcwd()}/blog/yapay-zeka-gelecegi.html"
        print(f"Navigating to Blog Page: {blog_path}")
        page.goto(blog_path)

        # Check "Araçlar" button
        # Look for link to index.html that is visible on mobile
        tools_btns = page.query_selector_all('a[href="../index.html"]')
        mobile_tools_found = False

        for btn in tools_btns:
            classes = btn.get_attribute("class")
            if "md:hidden" in classes:
                txt = btn.inner_text().strip()
                if "Araçlar" in txt:
                    mobile_tools_found = True
                    print(f"SUCCESS: Blog Header has '{txt}' button linking to index.")
                    break
                else:
                    print(f"WARNING: Found mobile index link but text is '{txt}'.")

        if not mobile_tools_found:
            print("FAILURE: Blog Header 'Back to Tools' button missing.")

        page.screenshot(path="verification/mobile_blog_header.png")

        browser.close()

if not os.path.exists("verification"):
    os.makedirs("verification")
verify_mobile_header()
