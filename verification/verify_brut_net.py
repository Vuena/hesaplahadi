from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the HTML file directly
        import os
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/brutten-nete-maas-hesaplama.html")

        # Select Year and Month (default is 2026/Jan)
        # Change to March for test
        page.select_option("#brut_net-month", "3")

        # Enter Gross Salary
        page.fill("#brut_net-brut", "40000")

        # Click Calculate - using ID or onclick attribute to be specific
        page.click("button[onclick='calc_brut_net()']")

        # Wait for result card
        page.wait_for_selector("#res-brut_net:not(.hidden)")

        # Take screenshot
        page.screenshot(path="verification/brut_net_result.png", full_page=True)

        # Verify result content (simple assertion)
        result_text = page.text_content("#val-brut_net")
        print(f"Result for 40000 TL in March: {result_text}")

        # Verify table existence
        table_rows = page.locator("#table-brut_net_container table tbody tr").count()
        print(f"Table rows count: {table_rows}")

        browser.close()

if __name__ == "__main__":
    run()
