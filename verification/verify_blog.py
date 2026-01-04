from playwright.sync_api import sync_playwright, expect

def verify_blog_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file directly since it is static HTML
        # We need absolute path
        import os
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/blog/kredi-notu-nasil-yukseltilir.html")

        print("Page loaded.")

        # 1. Verify Subtitle is REMOVED
        # The subtitle was a span with text "Finansal & Pratik Araçlar" under the logo
        subtitle = page.get_by_text("Finansal & Pratik Araçlar")
        if subtitle.count() == 0:
            print("PASS: Subtitle 'Finansal & Pratik Araçlar' is NOT found.")
        else:
            # Check visibility, might be hidden?
            if not subtitle.is_visible():
                print("PASS: Subtitle exists but is not visible.")
            else:
                print("FAIL: Subtitle is still visible.")

        # 2. Verify Footer Links
        footer = page.locator("footer")
        links = ["Ana Sayfa", "Hakkımızda", "Gizlilik Politikası", "İletişim", "Blog", "AI Asistan"]
        for link_text in links:
            link = footer.get_by_role("link", name=link_text)
            if link.is_visible():
                print(f"PASS: Footer link '{link_text}' is visible.")
            else:
                print(f"FAIL: Footer link '{link_text}' is MISSING.")

        # 3. Verify Sticky Sidebar
        # We expect the wrapper div to have 'sticky' class.
        # It's hard to verify 'sticky' behavior in headless without scrolling and checking position,
        # but we can check if the class exists on the sidebar wrapper.
        # The sidebar is an 'aside' element. The wrapper is the first child div.
        sidebar_wrapper = page.locator("aside.lg\:col-span-4 > div")
        class_attr = sidebar_wrapper.get_attribute("class")
        if "sticky" in class_attr and "top-24" in class_attr:
             print(f"PASS: Sidebar wrapper has sticky classes: {class_attr}")
        else:
             print(f"FAIL: Sidebar wrapper missing sticky classes. Found: {class_attr}")

        # Screenshot
        page.screenshot(path="verification/blog_verification.png", full_page=True)
        print("Screenshot saved to verification/blog_verification.png")

        browser.close()

if __name__ == "__main__":
    verify_blog_page()
