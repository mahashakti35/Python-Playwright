import time

from playwright.sync_api import Playwright,expect

from utils.api import ApiUtils

def test_e2e_web_api(playwright:Playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()


    api_uitls = ApiUtils()
    api_uitls.createOrder(playwright)
    
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("mahashakti@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Sonusanu@1")
    page.get_by_role("button", name = "Login").click()
    page.get_by_role("button", name = "Orders").click()
    # page.get_by_role("button", name = "View").first.click()
    expect(page.get_by_text(api_uitls.orderID)).to_be_visible()
    orderRow = page.locator("tr").filter(has_text= api_uitls.orderID)
    orderRow.get_by_role("button", name = "View").click()
    expect(page.locator('.tagline')).to_have_text("Thank you for Shopping With Us")
    