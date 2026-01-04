from playwright.sync_api import sync_playwright
import os

def verify_static_sidebar():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine absolute path to index.html
        cwd = os.getcwd()
        path = f"file://{cwd}/index.html"

        print(f"Navigating to {path}")
        page.goto(path)

        # Wait for potential rendering (though we expect static)
        page.wait_for_timeout(1000)

        # Verify Sidebar Content
        # We expect a .cat-header for "Yapay Zeka" which is statically injected
        if page.locator("#sidebar-list .cat-header").first.is_visible():
            print("Sidebar category header visible!")
        else:
            print("Error: Sidebar category header NOT visible.")

        # Verify Tool Link
        # KDV link should be present
        if page.locator("a[href='kdv-hesaplama.html']").first.is_visible():
             print("KDV link visible!")
        else:
             print("Error: KDV link NOT visible.")

        # Take Screenshot
        os.makedirs("verification", exist_ok=True)
        screenshot_path = "verification/sidebar_check.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_static_sidebar()
