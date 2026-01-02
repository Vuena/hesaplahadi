from playwright.sync_api import sync_playwright

def verify_kdv():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine absolute path to the HTML file
        import os
        cwd = os.getcwd()
        url = f"file://{cwd}/kdv-hesaplama.html"

        print(f"Navigating to {url}")
        page.goto(url)

        # Verify Title
        print("Verifying Title...")
        assert "KDV Hesaplama 2026" in page.title()

        # Test Case 1: KDV Dahil (Included)
        # Select "KDV Dahil" (value="include")
        page.select_option("#kdv-type", "include")
        # Set Amount to 118
        page.fill("#kdv-amt", "118")
        # Set Rate to 18% (Custom)
        page.select_option("#kdv-rate", "custom")
        page.fill("#kdv-custom-rate", "18")

        # Click Calculate
        page.click("button.btn-calc")

        # Wait for results
        page.wait_for_selector("#res-kdv:not(.hidden)")

        # Check Values (118 Total -> 100 Net + 18 Tax)
        net_text = page.locator("#kdv-res-net").inner_text()
        tax_text = page.locator("#kdv-res-tax").inner_text()
        total_text = page.locator("#kdv-res-total").inner_text()

        print(f"Result Included: Net={net_text}, Tax={tax_text}, Total={total_text}")

        # Take Screenshot
        page.screenshot(path="verification/kdv_verification.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    verify_kdv()
