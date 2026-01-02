from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/asgari-ucret-hesaplama.html?v=99")

        # Click Calculate
        page.locator("button.btn-calc").click()
        page.wait_for_timeout(3000)

        # Check result text presence directly
        text_content = page.content()
        if "28.500" in text_content:
            print("PASS: 28.500 found in page content")
        else:
            print("FAIL: 28.500 NOT found")

        page.screenshot(path="verification/asgari_2026.png")
        browser.close()

if __name__ == "__main__":
    run()
