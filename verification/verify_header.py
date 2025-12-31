
from playwright.sync_api import sync_playwright
import os

def verify_mobile_header():
    cwd = os.getcwd()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a mobile viewport
        context = browser.new_context(
            viewport={"width": 390, "height": 844},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
        )
        page = context.new_page()

        # 1. Check Homepage Header
        print("Checking Homepage...")
        page.goto(f"file://{cwd}/index.html")
        page.wait_for_load_state("networkidle")

        # Take screenshot of homepage header
        page.screenshot(path="verification/homepage_mobile.png", clip={"x": 0, "y": 0, "width": 390, "height": 300})

        # 2. Check Blog Page Header
        print("Checking Blog Page...")
        page.goto(f"file://{cwd}/blog/kredi-notu-nasil-yukseltilir.html")
        page.wait_for_load_state("networkidle")

        # Take screenshot of blog header
        page.screenshot(path="verification/blog_mobile.png", clip={"x": 0, "y": 0, "width": 390, "height": 300})

        # 3. Check a Tool Page Header (e.g. KDV)
        print("Checking Tool Page...")
        page.goto(f"file://{cwd}/kdv-hesaplama.html")
        page.wait_for_load_state("networkidle")

        # Take screenshot of tool header
        page.screenshot(path="verification/tool_mobile.png", clip={"x": 0, "y": 0, "width": 390, "height": 300})

        browser.close()

if __name__ == "__main__":
    verify_mobile_header()
