from playwright.sync_api import sync_playwright

def verify_mobile_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a mobile viewport
        context = browser.new_context(viewport={"width": 375, "height": 667})
        page = context.new_page()

        # Load local index.html
        import os
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # 1. Check for Hamburger Icon (should be visible in mobile)
        # There are two buttons with toggleDrawer, one in the drawer (close) and one in header (open)
        # The header one has fa-bars
        hamburger_btn = page.locator("header button[onclick='toggleDrawer()']")

        if hamburger_btn.is_visible():
             print("SUCCESS: Hamburger icon button is visible in header.")
        else:
             print("FAILURE: Hamburger icon button not found in header.")

        # 2. Check that "Tüm Hesaplamalar" text is NOT present in that button
        btn_text = hamburger_btn.inner_text()
        if "Tüm Hesaplamalar" not in btn_text:
             print(f"SUCCESS: 'Tüm Hesaplamalar' text is NOT present in the mobile menu button. Found text: '{btn_text}'")
        else:
             print(f"FAILURE: 'Tüm Hesaplamalar' text IS present: '{btn_text}'")

        # 3. Screenshot
        page.screenshot(path="verification/mobile_home_reverted.png")

        # Check Blog Page
        page.goto(f"file://{cwd}/blog/index.html")

        # The specific button we removed was in the header
        # Let's check if there is any button with text "Hesaplama Araçları" that is visible in mobile header

        # Note: Desktop might have a link "Araçlar" or similar.
        # We are looking for the specific one: <a ... class="md:hidden ...">Hesaplama Araçları</a>

        mobile_cta = page.locator("header .md\\:hidden").get_by_text("Hesaplama Araçları")
        if mobile_cta.count() == 0 or not mobile_cta.is_visible():
             print("SUCCESS: 'Hesaplama Araçları' mobile button is NOT visible in blog header.")
        else:
             print("FAILURE: 'Hesaplama Araçları' mobile button IS visible.")

        page.screenshot(path="verification/mobile_blog_reverted.png")

        browser.close()

if __name__ == "__main__":
    verify_mobile_ux()
