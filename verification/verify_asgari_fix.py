from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/asgari-ucret-hesaplama.html")

        # Check dropdown default
        dropdown = page.locator("#asgari-period")
        expect(dropdown).to_have_value("2026-1")

        # Fill nothing, just click calculate
        # Ensure #asgari-type is bn (Gross to Net is easier to verify)
        # But our function calc_asgari is:
        # if t==bn: showRes(net, tahmini brut)

        page.locator("button.btn-calc").click()

        # The result container is #res-asgari.
        # It has class 'hidden'. The JS removes 'hidden'.
        # We need to wait for that.
        result_div = page.locator("#res-asgari")
        expect(result_div).not_to_have_class("hidden")

        # Check Net Salary Value
        # Should be formatted: "28.500 TL (Net)"
        # Note: Depending on locale, might be 28.500 or 28,500. Using partial match.
        net_val = page.locator("#val-asgari")
        expect(net_val).to_contain_text("28.500")

        page.screenshot(path="verification/asgari_2026.png")
        print("Verification successful")
        browser.close()

if __name__ == "__main__":
    run()
