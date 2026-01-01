import time
import os
from playwright.sync_api import sync_playwright

def test_mobile_dynamic_search():
    cwd = os.getcwd()
    file_path = f"file://{cwd}/kdv-hesaplama.html"
    print(f"Navigating to: {file_path}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Mobile Viewport
        context = browser.new_context(viewport={'width': 390, 'height': 844}, user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1')
        page = context.new_page()
        page.goto(file_path)

        # 1. Test Initial Focus (Should show Popular Tools)
        print("1. Testing Mobile Focus...")
        page.locator('#mobile-tool-search').click()
        time.sleep(0.5)

        header = page.locator('#mobile-search-header').inner_text()
        print(f"Header on focus: {header}")
        if "POPÜLER" not in header:
            print("ERROR: Header should be POPÜLER ARAÇLAR")

        count = page.locator('#mobile-search-results-list a').count()
        print(f"Items found: {count}")
        if count == 0:
            print("ERROR: No popular items found")

        # 2. Test Typing 'kdv'
        print("2. Testing Search 'kdv'...")
        page.locator('#mobile-tool-search').fill('kdv')
        time.sleep(0.5)

        header = page.locator('#mobile-search-header').inner_text()
        print(f"Header on search: {header}")
        if "ARAMA" not in header:
            print("ERROR: Header should be ARAMA SONUÇLARI")

        kdv_item = page.locator('#mobile-search-results-list a:has-text("KDV Hesaplama")')
        if kdv_item.count() > 0:
            print("SUCCESS: Found 'KDV Hesaplama' in results")
        else:
            print("ERROR: 'KDV Hesaplama' not found")

        # 3. Test Typing 'xyz'
        print("3. Testing Search 'xyz'...")
        page.locator('#mobile-tool-search').fill('xyz')
        time.sleep(0.5)

        no_res = page.locator('#mobile-search-results-list div:has-text("Sonuç bulunamadı")')
        if no_res.count() > 0:
            print("SUCCESS: 'Sonuç bulunamadı' message shown")
        else:
            print("ERROR: 'Sonuç bulunamadı' message NOT shown")

        page.screenshot(path="verification/mobile_dynamic_search_verify.png")
        print("Screenshot saved")
        browser.close()

if __name__ == "__main__":
    test_mobile_dynamic_search()
