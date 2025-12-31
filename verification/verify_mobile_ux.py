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
        # The hamburger icon is usually <i class="fa-solid fa-bars"></i> inside a button
        # The button usually has an onclick="toggleDrawer()"
        hamburger_btn = page.locator("button[onclick='toggleDrawer()'] i.fa-bars")
        if hamburger_btn.is_visible():
             print("SUCCESS: Hamburger icon is visible.")
        else:
             print("FAILURE: Hamburger icon not found.")

        # 2. Check that "Tüm Hesaplamalar" text is NOT present in that button
        # The button text should just be the icon, or at least not the specific text "Tüm Hesaplamalar"
        btn_text = page.locator("button[onclick='toggleDrawer()']").inner_text()
        if "Tüm Hesaplamalar" not in btn_text:
             print(f"SUCCESS: 'Tüm Hesaplamalar' text is NOT present in the mobile menu button. Found text: '{btn_text}'")
        else:
             print(f"FAILURE: 'Tüm Hesaplamalar' text IS present: '{btn_text}'")

        # 3. Screenshot
        page.screenshot(path="verification/mobile_home_reverted.png")

        # Check Blog Page
        page.goto(f"file://{cwd}/blog/index.html")
        # Check that "Hesaplama Araçları" button is NOT in the header in the specific mobile spot
        # In the reverted version, the mobile header usually just has "Araçlar" link or similar, but NOT the specific styled button
        # The styled button had class "bg-blue-600 text-white ... Hesaplama Araçları"

        header_btn = page.get_by_text("Hesaplama Araçları", exact=True)
        # It might exist in the sidebar or footer, but we are looking for the mobile header one.
        # Let's just check if the specific mobile button we added is gone.
        # It was: <a href="../index.html" class="md:hidden ...">Hesaplama Araçları</a>

        mobile_cta = page.locator("header .md\\:hidden").get_by_text("Hesaplama Araçları")
        if not mobile_cta.is_visible():
             print("SUCCESS: 'Hesaplama Araçları' mobile button is NOT visible in blog header.")
        else:
             print("FAILURE: 'Hesaplama Araçları' mobile button IS visible.")

        page.screenshot(path="verification/mobile_blog_reverted.png")

        browser.close()

if __name__ == "__main__":
    verify_mobile_ux()
