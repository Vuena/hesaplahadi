
from playwright.sync_api import sync_playwright
import os

def capture_final_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # 1. MOBILE CONTEXT
        context_mobile = browser.new_context(viewport={"width": 390, "height": 844})
        page_mobile = context_mobile.new_page()
        cwd = os.getcwd()
        page_mobile.goto(f"file://{cwd}/index.html")

        # Screenshot Mobile Home
        page_mobile.screenshot(path="verification/final_mobile_home.png")
        print("Mobile screenshot saved.")

        # 2. DESKTOP CONTEXT
        context_desktop = browser.new_context(viewport={"width": 1920, "height": 1080})
        page_desktop = context_desktop.new_page()
        page_desktop.goto(f"file://{cwd}/index.html")

        # Screenshot Desktop Home
        page_desktop.screenshot(path="verification/final_desktop_home.png")
        print("Desktop screenshot saved.")

        browser.close()

if __name__ == "__main__":
    capture_final_state()
