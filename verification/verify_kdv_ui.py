from playwright.sync_api import sync_playwright

def verify_kdv(page):
    # Load the KDV calculator file directly
    page.goto('file:///app/kdv-hesaplama.html')

    # Check if the title is correct
    assert "KDV Hesaplama" in page.title()

    # Check for new design elements (gradient header)
    header = page.locator('h1')
    print(f"Header text: {header.inner_text()}")

    # Perform a calculation
    page.fill('#kdv-amt', '1000')
    page.select_option('#kdv-rate', '20')

    # Click Calculate
    page.click('button:has-text("Hesapla")')

    # Wait for result
    result = page.locator('#kdv-res-total')
    result.wait_for()

    print(f"Result Total: {result.inner_text()}")

    # Screenshot
    page.screenshot(path='verification/kdv_verification.png', full_page=True)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        verify_kdv(page)
        browser.close()
