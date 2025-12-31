
from playwright.sync_api import sync_playwright
import os

def check_features():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Check Index AI Placeholder
        print('Checking index.html...')
        page.goto('file://' + os.path.abspath('index.html'))
        placeholder = page.get_by_placeholder('Örn. 50.000 TL')
        if placeholder.count() > 0:
            print('SUCCESS: Placeholder updated.')
        else:
            print('FAIL: Placeholder not found.')

        # 2. Check Drawer on Tool Page
        print('Checking kidem-tazminati.html Drawer...')
        page.goto('file://' + os.path.abspath('kidem-tazminati.html'))
        drawer = page.locator('#drawer')
        if drawer.count() > 0:
            print('SUCCESS: Drawer exists.')
        else:
            print('FAIL: Drawer missing.')

        # 3. Check Result Promo (Simulate Calc)
        # We need to simulate a calc. KDV is easier.
        print('Checking KDV Calc Promo...')
        page.goto('file://' + os.path.abspath('kdv-hesaplama.html'))

        # Fill inputs
        page.locator('#kdv-amt').fill('1000')
        page.get_by_text('Hesapla', exact=True).click()

        # Check result
        # Wait for result to appear
        promo = page.locator('.ai-promo')
        try:
            promo.wait_for(timeout=2000)
            print('SUCCESS: AI Promo appeared.')
        except:
            print('FAIL: AI Promo did not appear.')

        page.screenshot(path='verification/check.png')
        browser.close()

if __name__ == '__main__':
    check_features()
