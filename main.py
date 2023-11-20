import time 
from playwright.sync_api import Playwright, sync_playwright
from utils.scrolling import scroller
def runner(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = browser.new_page()
    page.goto("http://quotes.toscrape.com/scroll")
    scroller(page)
    context.close()
    browser.close()

with sync_playwright() as playwright:
    runner(playwright=playwright)