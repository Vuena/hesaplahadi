from playwright.sync_api import sync_playwright, expect
import os
import re

def test_mobile_ux(page):
    # Load the KDV calculator page locally
    # Get current working directory
    cwd = os.getcwd()
    page.goto(f"file://{cwd}/kdv-hesaplama.html")

    # Set viewport to mobile size
    page.set_viewport_size({"width": 375, "height": 812})

    # 1. Verify Logo Visibility
    logo = page.locator(".fa-calculator").first
    expect(logo).to_be_visible()
    print("Logo is visible on mobile.")

    # 2. Verify Menu Toggle
    menu_btn = page.locator("button", has_text="Tüm Hesaplama Araçları")
    expect(menu_btn).to_be_visible()
    menu_btn.click()

    # Wait for drawer to appear
    drawer = page.locator("#drawer")
    expect(drawer).to_have_class(re.compile(r"drawer-open"))
    print("Drawer opened successfully.")

    # 3. Verify 'All Tools' link is REMOVED
    all_tools_link = drawer.locator("a", has_text="Tüm Hesaplamalar")
    expect(all_tools_link).to_have_count(0)
    print("'Tüm Hesaplamalar' link is correctly absent.")

    # 4. Verify AI Link in Results
    # Fill in the KDV form to trigger a result
    # Need to close drawer first or click outside, but logic might work if form is interactable
    # The mask covers the screen, so we must close the drawer.
    # Click the close button in the drawer
    drawer.locator("button").click()
    expect(drawer).not_to_have_class(re.compile(r"drawer-open"))

    page.locator("#kdv-amt").fill("1000")
    # Be more specific with the Calculate button
    calc_btn = page.locator("button.btn-calc", has_text="Hesapla")
    calc_btn.click()

    # Wait for result
    res_card = page.locator("#res-kdv")
    expect(res_card).to_be_visible()

    # Check for AI help link
    ai_link = res_card.locator("a", has_text="Bir hata olduğunu mu düşünüyorsunuz?")
    expect(ai_link).to_be_visible()
    print("AI help link appeared in results.")

    # Take screenshot
    page.screenshot(path="verification/mobile_ux_verified.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_mobile_ux(page)
        except Exception as e:
            print(f"Test failed: {e}")
            page.screenshot(path="verification/mobile_ux_failed.png")
            raise e
        finally:
            browser.close()
