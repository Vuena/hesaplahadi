from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify Gizlilik Politikası
        page.goto(f"file://{os.getcwd()}/gizlilik-politikasi.html")
        page.screenshot(path="verification/gizlilik.png", full_page=True)
        print("Captured gizlilik.png")

        # Verify Hakkımızda
        page.goto(f"file://{os.getcwd()}/hakkimizda.html")
        page.screenshot(path="verification/hakkimizda.png", full_page=True)
        print("Captured hakkimizda.png")

        # Verify İletişim
        page.goto(f"file://{os.getcwd()}/iletisim.html")
        page.screenshot(path="verification/iletisim.png", full_page=True)
        print("Captured iletisim.png")

        # Verify Index Footer
        page.goto(f"file://{os.getcwd()}/index.html")
        # Scroll to bottom
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.screenshot(path="verification/index_footer.png")
        print("Captured index_footer.png")

        browser.close()

if __name__ == "__main__":
    run()
