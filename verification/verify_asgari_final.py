from playwright.sync_api import sync_playwright, expect
import re

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/asgari-ucret-hesaplama.html?v=final")

        page.locator("button.btn-calc").click()

        result_div = page.locator("#res-asgari")
        expect(result_div).not_to_have_class("hidden")

        net_val = page.locator("#val-asgari")
        # Matches 28,500 or 28.500
        expect(net_val).to_have_text(re.compile(r"28[.,]500"))

        page.screenshot(path="verification/asgari_2026.png")
        print("Verification successful")
        browser.close()

if __name__ == "__main__":
    run()
