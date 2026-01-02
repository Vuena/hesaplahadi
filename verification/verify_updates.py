from playwright.sync_api import sync_playwright
import os

def verify_headers():
    if not os.path.exists("verification"):
        os.makedirs("verification")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Define key files to check
        files_to_check = [
            'asgari-ucret-hesaplama.html',
            'mtv-hesaplama.html',
            'emekli-maas-hesaplama.html',
            'enflasyon-alim-gucu-hesaplama.html'
        ]

        # Base URL for static file loading (using file:// protocol in sandbox)
        cwd = os.getcwd()

        for file in files_to_check:
            url = f"file://{cwd}/{file}"
            print(f"Checking {url}")
            try:
                page.goto(url)

                # Check Title
                title = page.title()
                print(f"  Title: {title}")
                if "2026" in title:
                    print(f"  FAIL: Title contains 2026")

                # Check H1
                h1 = page.inner_text("h1")
                print(f"  H1: {h1}")
                if "2026" in h1:
                    print(f"  FAIL: H1 contains 2026")

                # Take Screenshot of the header area
                page.screenshot(path=f"verification/verify_{file.replace('.html', '')}.png")

            except Exception as e:
                print(f"  Error checking {file}: {e}")

        browser.close()

if __name__ == "__main__":
    verify_headers()
