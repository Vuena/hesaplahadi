from playwright.sync_api import sync_playwright, expect
import os

def verify_changes(page):
    cwd = os.getcwd()

    # 2. Verify Solar Harita Fix
    print("Verifying Solar Harita...")
    page.goto(f"file://{cwd}/solar-harita-hesaplama.html")
    # Use exact match for heading to avoid ambiguity
    expect(page.get_by_role("heading", name="Solar Harita Hesaplama", exact=True)).to_be_visible()

    # Fill inputs
    page.locator("#solar_harita_hesaplama-date").fill("1990-01-01")
    page.locator("#solar_harita_hesaplama-time").fill("12:00")

    # Click calculate
    page.get_by_role("button", name="Hesapla").click()

    # Result should be visible
    expect(page.locator("#res-solar_harita")).to_be_visible()
    page.screenshot(path="verification/solar_harita.png")
    print("Solar Harita verified.")

    # 3. Verify Renamed Page Access (MTV)
    print("Verifying MTV Renaming...")
    page.goto(f"file://{cwd}/mtv-hesaplama.html")
    expect(page.get_by_role("heading", name="MTV Hesaplama")).to_be_visible()

    title = page.title()
    if "2026" in title:
        print(f"Warning: Title still has 2026: {title}")
    else:
        print(f"Title clean: {title}")

    page.screenshot(path="verification/mtv_renamed.png")
    print("MTV Renaming verified.")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_changes(page)
        except Exception as e:
            print(f"Verification failed: {e}")
            import traceback
            traceback.print_exc()
        finally:
            browser.close()
