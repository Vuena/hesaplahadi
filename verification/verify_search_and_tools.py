import time
import os
from playwright.sync_api import sync_playwright

def test_search_and_tools():
    cwd = os.getcwd()
    file_path = f"file://{cwd}/index.html"
    print(f"Navigating to: {file_path}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # 1. Test Mobile View (iPhone 12)
        print("Testing Mobile View...")
        context_mobile = browser.new_context(viewport={'width': 390, 'height': 844}, user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1')
        page_mobile = context_mobile.new_page()
        page_mobile.goto(file_path)

        # Check z-index of mobile search
        search_container = page_mobile.locator('.md\:hidden.relative.group')
        z_index = search_container.evaluate("el => getComputedStyle(el).zIndex")
        print(f"Mobile Search z-index: {z_index}")
        if z_index != '50':
             print("ERROR: Mobile search z-index is not 50!")

        # Focus on mobile search to show suggestions
        page_mobile.locator('#mobile-tool-search').click()
        time.sleep(1) # Wait for UI
        page_mobile.screenshot(path="verification/mobile_search_focused.png")
        print("Screenshot saved: mobile_search_focused.png")

        # 2. Test Desktop View (1920x1080)
        print("Testing Desktop View...")
        context_desktop = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page_desktop = context_desktop.new_page()
        page_desktop.goto(file_path)

        # Check tool name updates in Sidebar (e.g., "Kıdem Tazminatı Hesaplama")
        # Wait for sidebar population (it's JS driven)
        page_desktop.wait_for_selector('#sidebar-list a')

        kidem_link = page_desktop.locator('#sidebar-list a:has-text("Kıdem Tazminatı Hesaplama")')
        if kidem_link.count() > 0:
            print("SUCCESS: 'Kıdem Tazminatı Hesaplama' found in sidebar.")
        else:
            print("ERROR: 'Kıdem Tazminatı Hesaplama' NOT found in sidebar.")

        # Focus on Desktop Search
        page_desktop.locator('#desktop-tool-search').click()
        time.sleep(1)
        # Check if suggestion box is visible
        suggestions = page_desktop.locator('#desktop-search-suggestions')
        if suggestions.is_visible():
            print("SUCCESS: Desktop suggestions visible on focus.")
        else:
            print("ERROR: Desktop suggestions NOT visible on focus.")

        page_desktop.screenshot(path="verification/desktop_search_focused.png")
        print("Screenshot saved: desktop_search_focused.png")

        browser.close()

if __name__ == "__main__":
    test_search_and_tools()
