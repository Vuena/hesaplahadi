from playwright.sync_api import sync_playwright

def verify_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Open Home Page (via file protocol)
        page.goto("file:///app/index.html")
        page.wait_for_selector("body")

        # 2. Check Sidebar for new tools
        # We need to click "Tüm Hesaplamalar" if on mobile, or check sidebar on desktop
        # Since headless is desktop default size (1280x720 usually), sidebar should be visible.
        # But `renderSidebar` populates it.
        page.wait_for_selector("#sidebar-list")

        # 3. Take Screenshot of Home/Sidebar
        page.screenshot(path="verification/home.png")

        # 4. Navigate to a New Tool (e.g. Altın Hesaplama)
        # We can navigate directly
        page.goto("file:///app/altin-hesaplama.html")
        page.wait_for_selector("#altin-amt")

        # 5. Perform Calculation
        page.fill("#altin-amt", "10")
        page.fill("#altin-rate", "3000")
        page.click("button.btn-calc")

        # 6. Verify Result
        page.wait_for_selector("#res-altin:not(.hidden)")
        result_text = page.inner_text("#val-altin")
        print(f"Altin Result: {result_text}")

        # 7. Take Screenshot of Result
        page.screenshot(path="verification/altin_result.png")

        # 8. Check Kidem Cap (Existing tool update)
        page.goto("file:///app/kidem-tazminati-hesaplama.html")
        page.wait_for_selector("#kidem-start")
        page.fill("#kidem-start", "2020-01-01")
        page.fill("#kidem-end", "2021-01-01")
        # Enter high salary to test cap (55k)
        page.fill("#kidem-salary", "100000")
        page.click("button.btn-calc")

        page.wait_for_selector("#res-kidem:not(.hidden)")
        kidem_res = page.inner_text("#val-kidem")
        print(f"Kidem Result (Cap Check): {kidem_res}")
        # Logic: 1 year * 55000 * 0.99241 = 54582.55 approx

        page.screenshot(path="verification/kidem_result.png")

        browser.close()

if __name__ == "__main__":
    verify_site()
