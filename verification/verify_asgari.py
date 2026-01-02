from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/asgari-ucret-hesaplama.html")

        # Check if title contains '2026' (since we updated html text)
        # Note: HTML title might not have changed, but content has.

        # Check dropdown default
        dropdown = page.locator("#asgari-period")
        expect(dropdown).to_have_value("2026-1")

        # Click Calculate
        page.locator("button.btn-calc").click()

        # Wait for result
        result_div = page.locator("#res-asgari")
        expect(result_div).to_be_visible()

        # Check Net Salary Value (Should be ~28,500)
        net_val = page.locator("#val-asgari")
        # Format: "28.500 TL (Net)"
        expect(net_val).to_contain_text("28.500")

        page.screenshot(path="verification/asgari_2026.png")
        print("Verification successful")
        browser.close()

if __name__ == "__main__":
    run()
