from playwright.sync_api import sync_playwright
import time

def verify_drawer(page):
    # Load index.html
    page.goto('file:///app/index.html')

    # Set viewport to mobile to see drawer button
    page.set_viewport_size({"width": 375, "height": 667})

    # Click the "Tüm Hesaplama Araçları" button
    # The user said it is a button with that text
    drawer_btn = page.locator('button:has-text("Tüm Hesaplama Araçları")')
    drawer_btn.wait_for()
    drawer_btn.click()

    # Wait for drawer to open
    drawer = page.locator('#drawer')
    # Check if it has 'drawer-open' class
    expect_drawer_open = drawer.evaluate("el => el.classList.contains('drawer-open')")

    if expect_drawer_open:
        print("Drawer opened successfully.")
    else:
        print("ERROR: Drawer did not open (missing class drawer-open).")

    # Check content of drawer
    # It should have links populated by JS
    drawer_list = page.locator('#drawer-list')
    links = drawer_list.locator('a')
    count = links.count()
    print(f"Found {count} links in drawer.")

    # Verify "Tüm Hesaplamalar" link is NOT present (strict cleanup requirement)
    all_calcs_link = drawer_list.locator('a:has-text("Tüm Hesaplamalar")')
    if all_calcs_link.count() > 0:
        print("ERROR: 'Tüm Hesaplamalar' link found in drawer (should be removed).")
    else:
        print("SUCCESS: 'Tüm Hesaplamalar' link correctly removed from drawer.")

    # Screenshot
    page.screenshot(path='verification/drawer_verification.png')

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        verify_drawer(page)
        browser.close()
