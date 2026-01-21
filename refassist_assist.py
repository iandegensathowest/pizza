from playwright.sync_api import sync_playwright

#give your email adress
email=input("What is your email? ")
password=input("What is your password? ")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rbfa.refassist.com/RefereeApp")

    # login 
    page.wait_for_selector("#idp-discovery-username")
    page.fill("#idp-discovery-username", email)
    page.press("#idp-discovery-username", "Enter")

    page.wait_for_selector("#okta-signin-password", timeout=10000)
    page.fill("#okta-signin-password", password)
    page.press("#okta-signin-password", "Enter")

    # wait
    page.wait_for_selector("#upcoming .col-xl-6")

    # Make cards for each match 
    cards = page.locator("#upcoming .col-xl-6")

    count = cards.count()
    
    print(f"Found {count} upcoming matches\n")

    for i in range(count):
        card = cards.nth(i)
        # Date and time 
        date_time = card.locator("span.text-gray-600.d-block:not(.fs-7)").first.inner_text()

        # match info
        teams = card.locator(
            "label:has-text('Match') + span.text-gray-600.d-block.fs-7"
        ).inner_text()
        level = card.locator("label:has-text('Series') + span.text-gray-600.d-block.fs-7").inner_text()

        print(f"Match {i + 1}")
        print(" Date & time :", date_time)
        print(" Teams :", teams)
        print(" Niveau :", level)
        print("-" * 40)
    # close browser screen
    browser.close
    
