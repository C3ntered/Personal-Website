from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8000/Mywebsite/index.html")

    # Wait for the projects section
    page.wait_for_selector("#projects")

    # Take a screenshot of the full page
    page.screenshot(path="verification/full_page.png", full_page=True)

    # Take a screenshot of the projects section specifically
    element = page.locator("#projects")
    element.screenshot(path="verification/projects_section.png")

    # Take a screenshot of the navigation to show "Projects" link
    nav = page.locator("header")
    nav.screenshot(path="verification/navigation.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
