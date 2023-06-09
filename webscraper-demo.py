import asyncio
import csv
from pyppeteer import launch
import re


async def search_tumblr():  # Main function
    # Launch browser in non-headless mode
    browser = await launch({"headless": False, "args": ["--start-maximized"]})
    page = await browser.newPage()

    # Sign-in code
    await page.goto('https://www.tumblr.com/login')

    # Username input
    login_input = await page.querySelector('input[name="email"]')
    # Add username email here
    await login_input.type('example@gmail.com')

    # Password input
    pass_input = await page.querySelector('input[name="password"]')
    await pass_input.type('examplepassword')  # Add password here

    # Log-in button
    await page.waitForSelector('button[aria-label="Log in"]')
    login_button = await page.querySelector('button[aria-label="Log in"]')
    await login_button.click()
    await asyncio.sleep(1)

    # Redirecting to desired page that will be scraped (example page here)
    await page.goto('https://www.tumblr.com/search/throne%20of%20glass/text')

    # Scrolling code
    prev_scroll_position = 0

    while True:
        await page.evaluate('window.scrollBy(0, window.innerHeight*10)')
        await asyncio.sleep(2)

        curr_scroll_position = await page.evaluate('window.scrollY')
        if curr_scroll_position == prev_scroll_position:
            print("Reached the bottom of the page. Stopping scrolling.")
            break

        prev_scroll_position = curr_scroll_position

    await asyncio.sleep(1)

    # Combines all article tags (posts) to an array to iterate through
    posts = await page.querySelectorAll('article')

    filtered_posts = []  # Posts that match criteria

    # Iterating through every post on the page
    for post in posts:
        # Makes sure to skip adverts
        if not (await post.querySelector('div.UGqjE.KmE3L')):
            # Post text stored for filtering
            div_element = await post.querySelector('div.GzjsW')
            text_content = await page.evaluate('el => el.textContent', div_element)

            # Filters for desired text, if desired text found continue
            # Here we are looking for fanfics using words like 'k words' and 'word count' as indicators
            if re.search(r'\d+(\.\d+)?[kK]\b|\b(k words|word count)\b', text_content):
                # Click the three dots for checking date of post
                button = await post.querySelector('button[aria-label="More options"]')
                await button.click()

                await asyncio.sleep(0.2)

                # Reads date through appropriate tag
                await page.waitForSelector('span.cwYO_')
                date_element = await page.querySelector('span.cwYO_')
                post_date = await date_element.getProperty("textContent")

                # Store date
                date = await post_date.jsonValue()

                # Filter for desired date, if matches then store post details
                if ('2020') in date:

                    # Storing post author
                    author_element = await post.querySelector('div.vGkyT.vYL8Z')
                    author = await author_element.getProperty("textContent")
                    auth_name = await author.jsonValue()

                    # Storing post link
                    await page.waitForSelector('a.X1uIE.XOf8k.qYCWv.v_1X3')
                    copy_link = await page.querySelector("a.X1uIE.XOf8k.qYCWv.v_1X3")

                    # Get the clipboard contents and assign it to the post_link variable
                    post_link = await page.evaluate('el => el.href', copy_link)

                    # Save to criteria-matching posts array
                    filtered_posts.append({
                        'Author': auth_name,
                        'Link': post_link,
                        'Date': date
                    })

    # Close browser after scraping has concluded
    await browser.close()

    # Write the filtered posts to a CSV file
    with open('filtered_posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Author', 'Link', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(filtered_posts)

# Prints output to confirm scraping has begun
print("Starting...")

# Run the asyncio event loop
asyncio.get_event_loop().run_until_complete(search_tumblr())

# Confirms program has successfully concluded
print("Program has concluded")
