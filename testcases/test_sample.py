from playwright.sync_api import *

def test_sample_login(page:Page):
    page.goto("https://playwright.dev/python/")
    page.get_by_role('link', name='Get started').click()