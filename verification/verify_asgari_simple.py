from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/asgari-ucret-hesaplama.html")

        # Manually wait a bit for JS to bind
        page.wait_for_timeout(1000)

        # Click Calculate
        page.locator("button.btn-calc").click()

        # Wait 2 seconds for JS execution
        page.wait_for_timeout(2000)

        # Take screenshot regardless of failure logic to inspect
        page.screenshot(path="verification/asgari_2026.png")

        # Print content of result
        val = page.locator("#val-asgari").inner_text()
        print(f"Result Value: '{val}'")

        browser.close()

if __name__ == "__main__":
    run()
