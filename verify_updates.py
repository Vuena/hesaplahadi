from playwright.sync_api import sync_playwright
import os

def verify_updates():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": 375, "height": 667},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1"
        )

        # 1. Verify Mobile Drawer
        print("Navigating to Index for Drawer Check...")
        page.goto(f"file://{os.getcwd()}/index.html")

        # Click Hamburger (Header button)
        page.click('header button[onclick="toggleDrawer()"]')
        page.wait_for_timeout(500)

        # Check if list is populated
        drawer_content = page.inner_html("#drawer-list")
        if "KDV Hesaplama" in drawer_content and "Tüm Hesaplamalar" in drawer_content:
            print("SUCCESS: Mobile Drawer populated correctly.")
        else:
            print("FAILURE: Mobile Drawer is empty or missing items.")
            print(f"Content Sample: {drawer_content[:100]}...")

        # 2. Verify Percentage Calculator
        print("Navigating to Yuzde Hesaplama...")
        page.goto(f"file://{os.getcwd()}/yuzde-hesaplama-araci.html")

        # Check inputs
        mode_select = page.query_selector("select#yuzde-mode")
        if mode_select:
            print("SUCCESS: Percentage Mode Select found.")
            # Test Calculation: 500, 20% -> 100 (Mode 0)
            page.select_option("select#yuzde-mode", "0")
            page.fill("input#yuzde-a", "500")
            page.fill("input#yuzde-b", "20")
            page.click("button.btn-calc")

            page.wait_for_selector("#res-yuzde", state="visible")
            res_text = page.inner_text("#val-yuzde")

            if "100" in res_text:
                print(f"SUCCESS: Percentage Calc (Mode 0) Correct: {res_text}")
            else:
                print(f"FAILURE: Percentage Calc (Mode 0) Incorrect: {res_text}")
        else:
            print("FAILURE: Percentage Mode Select NOT found.")

        page.screenshot(path="verification/final_verification.png")
        browser.close()

if not os.path.exists("verification"):
    os.makedirs("verification")
verify_updates()
