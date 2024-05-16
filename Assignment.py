from selenium import webdriver

# Create a new instance of the Firefox driver (you can use other drivers like Chrome as well)
driver = webdriver.Firefox()

try:
    # Your test case code goes here

    # For example, navigating to a website
    driver.get("https://www.example.com")

    # Asserting a condition that might fail
    assert "Example" in driver.title

except AssertionError:
    # If the assertion fails, take a screenshot
    driver.save_screenshot("screenshot_on_fail.png")

finally:
    # Quit the browser in the finally block to ensure it is closed even if the test fails
    driver.quit()
