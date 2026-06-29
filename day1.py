import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def run_first_test():
    # 1. Initialize the Chrome WebDriver instance
    # Selenium Manager automatically handles the driver binaries behind the scenes
    driver = webdriver.Chrome()

    try:
        # 2. Maximize the window so elements aren't hidden in mobile views
        driver.maximize_window()

        # 3. Navigate to the target website
        target_url = "https://www.wikipedia.org/"
        print(f"Navigating to: {target_url}")
        driver.get(target_url)

        # 4. Extract data from the page using core driver properties
        page_title = driver.title
        current_url = driver.current_url

        print("\n--- Page Metadata Captured ---")
        print(f"Page Title : {page_title}")
        print(f"Verified URL: {current_url}")
        print("-----------------------------\n")

    except Exception as e:
        print(f"An error occurred during execution: {e}")

    finally:
        # 5. Crucial Step: Always close the browser window and terminate the driver process.
        # This prevents rogue chromedriver processes from eating up your system RAM.
        print("Closing the browser session...")
        driver.quit()

if __name__ == "__main__":
    run_first_test()