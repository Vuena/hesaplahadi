from playwright.sync_api import sync_playwright

def verify_kdv_page():
    with sync_playwright() as p:
        # Use a mobile viewport to test the drawer and responsive logo
        browser = p.chromium.launch(headless=True)
        # iPhone 12 viewport
        context = browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True)
        page = context.new_page()

        # Load the KDV page via Localhost
        page.goto("http://localhost:8000/kdv-hesaplama.html")

        # 1. Verify Logo Visibility
        # The logo is the calculator icon inside a gradient box in the header
        logo = page.locator("header .fa-calculator")
        if logo.is_visible():
            print("PASS: Calculator logo icon is visible.")
        else:
            print("FAIL: Calculator logo icon is NOT visible.")

        # Take a screenshot of the header
        page.screenshot(path="verification/mobile_header_logo.png", clip={"x":0, "y":0, "width":390, "height":100})

        # 2. Verify Drawer Menu Button
        # Click the "Tüm Hesaplama Araçları" button
        menu_btn = page.get_by_text("Tüm Hesaplama Araçları")
        if menu_btn.is_visible():
            print("PASS: Menu button is visible.")
            menu_btn.click()
            # Wait for drawer animation
            page.wait_for_timeout(500)

            # Check if drawer is open
            drawer = page.locator("#drawer")
            # Drawer open class is 'drawer-open' (transform 0)
            if "drawer-open" in drawer.get_attribute("class"):
                print("PASS: Drawer opened successfully.")
            else:
                print("FAIL: Drawer did not open.")

            # Check for "Tüm Hesaplamalar" link absence
            all_links_text = drawer.inner_text()
            if "Tüm Hesaplamalar" in all_links_text:
                print("FAIL: Found 'Tüm Hesaplamalar' text in drawer.")
            else:
                print("PASS: 'Tüm Hesaplamalar' link is NOT present in drawer.")

            # Take a screenshot of the open drawer
            page.screenshot(path="verification/mobile_drawer_open.png")

        else:
            print("FAIL: Menu button not found.")

        # 3. Verify AI Link in Results
        # Reset page or close drawer to interact with form
        # Reloading to reset state is easier
        page.reload()

        # Input KDV amount
        page.fill("#kdv-amt", "1000")

        # Click Calculate
        page.click("button:has-text('Hesapla')")

        # Wait for result
        res_card = page.locator("#res-kdv")
        res_card.wait_for(state="visible")

        # Check for AI link
        ai_link = res_card.locator(".ai-help-link")
        if ai_link.is_visible():
            print("PASS: AI Help Link is visible in results.")
            print("Text content:", ai_link.inner_text())
        else:
            print("FAIL: AI Help Link is NOT visible.")

        # Take a screenshot of the result card
        res_card.screenshot(path="verification/kdv_result_ai_link.png")

        browser.close()

import os
if __name__ == "__main__":
    verify_kdv_page()
