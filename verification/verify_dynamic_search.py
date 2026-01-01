import time
import os
from playwright.sync_api import sync_playwright

def test_dynamic_search():
    cwd = os.getcwd()
    file_path = f"file://{cwd}/kdv-hesaplama.html"
    print(f"Navigating to: {file_path}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        page.goto(file_path)

        # 1. Test Initial Focus (Should show Popular Tools)
        print("1. Testing Focus...")
        page.locator('#desktop-tool-search').click()
        time.sleep(0.5)

        # Check header text
        header = page.locator('#desktop-search-header').inner_text()
        print(f"Header on focus: {header}")
        if "POPÜLER" not in header:
            print("ERROR: Header should be POPÜLER ARAÇLAR on empty focus")

        # Check if items exist
        count = page.locator('#desktop-search-results-list a').count()
        print(f"Items found: {count}")
        if count == 0:
            print("ERROR: No popular items found")

        # 2. Test Typing 'kdv' (Should show KDV)
        print("2. Testing Search 'kdv'...")
        page.locator('#desktop-tool-search').fill('kdv')
        time.sleep(0.5)

        header = page.locator('#desktop-search-header').inner_text()
        print(f"Header on search: {header}")
        if "ARAMA" not in header:
            print("ERROR: Header should be ARAMA SONUÇLARI")

        # Check specifically for KDV
        kdv_item = page.locator('#desktop-search-results-list a:has-text("KDV Hesaplama")')
        if kdv_item.count() > 0:
            print("SUCCESS: Found 'KDV Hesaplama' in results")
        else:
            print("ERROR: 'KDV Hesaplama' not found in results")

        # 3. Test Typing 'xyz' (Should show nothing/message)
        print("3. Testing Search 'xyz'...")
        page.locator('#desktop-tool-search').fill('xyz')
        time.sleep(0.5)

        no_res = page.locator('#desktop-search-results-list div:has-text("Sonuç bulunamadı")')
        if no_res.count() > 0:
            print("SUCCESS: 'Sonuç bulunamadı' message shown")
        else:
            print("ERROR: 'Sonuç bulunamadı' message NOT shown")

        page.screenshot(path="verification/dynamic_search_verify.png")
        print("Screenshot saved")
        browser.close()

if __name__ == "__main__":
    test_dynamic_search()
