import time
import os
from playwright.sync_api import sync_playwright

def test_subpage_search():
    cwd = os.getcwd()
    # Test on KDV Hesaplama page
    file_path = f"file://{cwd}/kdv-hesaplama.html"
    print(f"Navigating to: {file_path}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Test Desktop View
        print("Testing Desktop View on Subpage...")
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        page.goto(file_path)

        # Check if desktop search exists
        search_input = page.locator('#desktop-tool-search')
        if search_input.count() > 0:
            print("SUCCESS: Desktop search input found.")
        else:
            print("ERROR: Desktop search input NOT found.")

        # Focus and check suggestions
        search_input.click()
        time.sleep(1)
        suggestions = page.locator('#desktop-search-suggestions')

        if suggestions.is_visible():
            print("SUCCESS: Desktop suggestions visible on focus.")
        else:
            print("ERROR: Desktop suggestions NOT visible on focus.")

        # Take screenshot
        page.screenshot(path="verification/subpage_search.png")
        print("Screenshot saved: subpage_search.png")

        browser.close()

if __name__ == "__main__":
    test_subpage_search()
