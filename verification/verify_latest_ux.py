from playwright.sync_api import sync_playwright
import os

def verify_latest_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        cwd = os.getcwd()

        # 1. MOBILE VERIFICATION
        context_mobile = browser.new_context(viewport={"width": 375, "height": 667})
        page_mobile = context_mobile.new_page()
        page_mobile.goto(f"file://{cwd}/index.html")

        # Check for NEW bottom drawer toggle text
        bottom_toggle = page_mobile.get_by_text("Tüm Hesaplama Araçları", exact=True)
        if bottom_toggle.is_visible():
            print("SUCCESS: Mobile 'Tüm Hesaplama Araçları' button found.")
        else:
            print("FAILURE: Mobile 'Tüm Hesaplama Araçları' button NOT found.")

        page_mobile.screenshot(path="verification/latest_mobile_ux.png")

        # 2. TOOL INPUT VERIFICATION
        page_tool = context_mobile.new_page()
        page_tool.goto(f"file://{cwd}/ags-puan-hesapla.html")

        # Check if input exists (means injection worked)
        input_el = page_tool.locator("#ags-nets")
        if input_el.is_visible():
             print("SUCCESS: AGS Tool input injected.")
        else:
             print("FAILURE: AGS Tool input NOT found.")

        browser.close()

if __name__ == "__main__":
    verify_latest_ux()
