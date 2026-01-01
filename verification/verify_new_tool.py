
from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Path to the file
    filepath = f"file://{os.getcwd()}/hangi-gun-hesaplama.html"
    page.goto(filepath)

    # Wait for page to load
    page.wait_for_load_state("networkidle")

    # Select date
    page.fill("#day-date", "2026-01-01")

    # Click Calculate
    page.click("button.btn-calc")

    # Wait for result
    page.wait_for_selector("#res-day", state="visible")

    # Take screenshot
    page.screenshot(path="verification/verify_hangi_gun.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
