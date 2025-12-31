from playwright.sync_api import sync_playwright
import os

def verify_mobile_ux():
    with sync_playwright() as p:
        # Use a mobile viewport
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 375, "height": 667}) # iPhone SE size
        page = context.new_page()

        # Load local file (Use absolute path correctly)
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # 1. Verify Header Elements
        print("Checking Header...")
        # Check for the new "Blog" text button
        blog_btn = page.locator("a.mobile-blog-btn")
        if blog_btn.is_visible():
            print("SUCCESS: Mobile Blog Button is visible.")
        else:
            print("FAIL: Mobile Blog Button not found.")

        # Check for the Big "All Calculations" Bar
        calc_btn = page.locator("button.mobile-big-btn")
        if calc_btn.is_visible():
            print("SUCCESS: 'Tüm Hesaplamalar' Big Button is visible.")
            # Verify text inside
            if "Tüm Hesaplamalar" in calc_btn.inner_text():
                 print("SUCCESS: Button text is correct.")
            else:
                 print(f"FAIL: Button text is '{calc_btn.inner_text()}'")
        else:
             print("FAIL: 'Tüm Hesaplamalar' Big Button not found.")

        # 2. Verify Functionality (Click to Open Drawer)
        print("Testing Drawer Toggle...")
        calc_btn.click()
        # Wait for drawer animation class or visibility
        # The drawer has id="drawer" and adds class "drawer-open"
        drawer = page.locator("#drawer")

        # Wait a bit for transition
        page.wait_for_timeout(500)

        if "drawer-open" in drawer.get_attribute("class"):
             print("SUCCESS: Drawer opened after click.")
        else:
             print(f"FAIL: Drawer did not open. Classes: {drawer.get_attribute('class')}")

        # Take Screenshot
        page.screenshot(path="verification/mobile_ux_verified.png")
        print("Screenshot saved to verification/mobile_ux_verified.png")

        browser.close()

if __name__ == "__main__":
    verify_mobile_ux()
