import pytest
from playwright.sync_api import Page, expect


def test_homepage(page: Page):
    """Test the React app homepage."""
    # 1. Open the homepage
    page.goto("http://localhost:3000")

    # 2. Take a screenshot
    page.screenshot(path="homepage_screenshot.png")

    # 3. Check if the React logo is visible
    react_logo = page.locator("img.App-logo, img[alt*='logo'], .App-logo, svg.App-logo")
    expect(react_logo.first).to_be_visible()

    # 4. Check if "Learn React" text exists on the page
    learn_react_text = page.get_by_text("Learn React")
    expect(learn_react_text).to_be_visible()
