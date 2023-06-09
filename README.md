# Tumblr Post Scraper

This is a Python script for scraping Tumblr posts based on a search query and extracting relevant information such as post links, authors, and dates. It uses the Pyppeteer library, which provides a high-level API for controlling a headless Chrome browser.

## Features

- Login to Tumblr: The script automates the login process to access restricted content and perform searches.
- Search Posts: It navigates to the search page and enters the desired query to fetch relevant posts.
- Scrolling and Loading: The script simulates scrolling to load more posts on the page dynamically.
- Extract Information: It extracts information such as post links, authors, and dates from the loaded posts.
- Filtering: The script filters the posts based on specific criteria (e.g., post date) and stores the filtered posts in a CSV file.
- Headless Mode: The script runs the browser in headless mode by default, but it can be configured to run in non-headless mode for debugging and visualization purposes.

## Getting Started

To get started with the Tumblr Post Scraper, follow these steps:

1. Install Python 3.x: Make sure you have Python 3.x installed on your machine.
2. Install Dependencies: Run `pip install -r requirements.txt` to install the required dependencies.
3. Update Credentials: Update the username and password fields in the script with your Tumblr login credentials.
4. Customize Search: Modify the search query and any other parameters as per your requirements.
5. Run the Script: Execute the script using `python scraper.py` and wait for it to complete.
6. Check Output: The filtered posts will be saved in a CSV file named `filtered_posts.csv` in the same directory.

## Customization

The script can be customized in several ways:

- Modify Search Query: Change the search query to search for different keywords or tags.
- Adjust Filtering Criteria: Update the filtering criteria to include or exclude posts based on specific requirements.
- Enable/Disable Headless Mode: Modify the script to run the browser in headless mode or non-headless mode as per your preference.

Feel free to explore the script code and make any necessary modifications to suit your needs.

## Limitations

- Rate Limits: Take into account Tumblr's rate limits and ensure that the script operates within the allowed limits to avoid any issues.
- Dynamic Website Changes: If Tumblr's website structure changes, some parts of the script may need to be updated to adapt to the changes.

## Contributions

Contributions, bug reports, and feature requests are welcome! If you encounter any issues or have ideas for improvements, please feel free to open an issue or submit a pull request on the project's GitHub repository.

