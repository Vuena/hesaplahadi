from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/asgari-ucret-hesaplama.html?v=cachebust")

        # Check IDs
        has_period = page.locator("#asgari-period").count() > 0
        has_type = page.locator("#asgari-type").count() > 0
        has_res = page.locator("#res-asgari").count() > 0
        has_val = page.locator("#val-asgari").count() > 0

        print(f"IDs present: period={has_period}, type={has_type}, res={has_res}, val={has_val}")

        browser.close()

if __name__ == "__main__":
    run()
