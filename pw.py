from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(proxy={
        'server': 'http://192.168.31.133:8080',  # your phone’s IP and port
    })
    page = browser.new_page()
    page.goto('https://httpbin.org/ip')
    print(page.content())
    browser.close()