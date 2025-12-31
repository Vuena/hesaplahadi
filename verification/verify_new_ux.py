from playwright.sync_api import sync_playwright
import os

def verify_new_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        cwd = os.getcwd()

        # 1. MOBILE VERIFICATION
        context_mobile = browser.new_context(viewport={"width": 375, "height": 667})
        page_mobile = context_mobile.new_page()
        page_mobile.goto(f"file://{cwd}/index.html")

        # Check for TOP-LEFT hamburger (should be gone)
        top_hamburger = page_mobile.locator("header .flex.items-center.gap-3 button.md\\:hidden")
        # In our new code, we removed the button from the top-left div.
        # But wait, did we? The regex replaced the entire header.
        # Let's check if the specific button with "toggleDrawer()" exists in the top left container.
        # The new header structure has:
        # <div class="flex items-center gap-3">
        #    <!-- Left: Logo (No Hamburger) -->
        # ...

        # So looking for a button inside that first div should fail or return 0.
        # Be careful with selectors.

        # Let's check for the NEW bottom drawer toggle
        bottom_toggle = page_mobile.get_by_text("Menü", exact=True)
        if bottom_toggle.is_visible():
            print("SUCCESS: Mobile 'Menü' button found below search.")
        else:
            print("FAILURE: Mobile 'Menü' button NOT found.")

        # Check that top left hamburger is GONE
        # The old one was just an icon <i class="fa-bars"></i> inside a button.
        # The new bottom one also has fa-bars.
        # Let's check for a button in the top left area.
        top_area_btn = page_mobile.locator("header > div > div > div:first-child button")
        if top_area_btn.count() == 0:
             print("SUCCESS: Top-left hamburger button is gone.")
        else:
             print("FAILURE: Top-left hamburger button might still be there.")

        # Check for Mobile Search Suggestions
        mobile_search = page_mobile.locator("#mobile-tool-search")
        mobile_search.click()
        mobile_suggestions = page_mobile.locator("#mobile-search-suggestions")
        if mobile_suggestions.is_visible():
             print("SUCCESS: Mobile search suggestions appeared on focus.")
             # Check content
             if "KDV Hesaplama" in mobile_suggestions.inner_text():
                 print("SUCCESS: Suggestions contain expected tools.")
        else:
             print("FAILURE: Mobile search suggestions did not appear.")

        page_mobile.screenshot(path="verification/new_mobile_ux.png")


        # 2. DESKTOP VERIFICATION
        context_desktop = browser.new_context(viewport={"width": 1280, "height": 800})
        page_desktop = context_desktop.new_page()
        page_desktop.goto(f"file://{cwd}/index.html")

        # Check for Desktop Search Bar
        desktop_search = page_desktop.locator("#desktop-tool-search")
        if desktop_search.is_visible():
            print("SUCCESS: Desktop search bar is visible.")
            desktop_search.click()
            desktop_suggestions = page_desktop.locator("#desktop-search-suggestions")
            if desktop_suggestions.is_visible():
                print("SUCCESS: Desktop search suggestions appeared on focus.")
            else:
                print("FAILURE: Desktop search suggestions did not appear.")
        else:
            print("FAILURE: Desktop search bar NOT found.")

        page_desktop.screenshot(path="verification/new_desktop_ux.png")

        browser.close()

if __name__ == "__main__":
    verify_new_ux()
