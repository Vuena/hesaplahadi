from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        file_path = os.path.abspath("kdv-hesaplama.html")
        page.goto(f"file://{file_path}")

        # Take a screenshot of the top part of the page where the header is
        page.screenshot(path="verification/kdv_header_fix.png", clip={"x": 0, "y": 0, "width": 1280, "height": 600})

        browser.close()

if __name__ == "__main__":
    run()
