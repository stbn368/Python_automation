from selenium import webdriver
from configuration import Config
import chromedriver_autoinstaller
from datetime import datetime
import os

def before_all(context):
    # Install automatically Chromedriver
    chromedriver_autoinstaller.install()
    
    # Set up driver
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(Config.IMPLICIT_WAIT)
    context.driver.maximize_window()

def before_scenario(context, scenario):
    """
    Navigate to the home page for each scenario
    """
    context.driver.get(Config.BASE_URL)

def after_scenario(context, scenario):     
    # Generate a custom report taking into account the datetime
    timestamp_report = datetime.now().strftime("%Y-%m-%d_%H-%M")
    timestamp_screenshot = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    scenario_name = scenario.name.replace(" ", "_")
    report_address = os.path.join(os.path.pardir, "reports", timestamp_report)
    screenshot_address = os.path.join(os.path.pardir, "screenshots")
    
    # Create a report directory if it does not exist
    os.makedirs(report_address, exist_ok=True)
    os.makedirs(screenshot_address, exist_ok=True)
    
    # Create or update the custom report
    with open(os.path.join(report_address, "custom_report.txt"), "a") as reporte:
        if scenario.status == "passed":
            reporte.write(f"Scenario '{scenario.name}' PASSED\n")
        else:
            reporte.write(f"Scenario '{scenario.name}' FAILED\n")
            
            # Take screenshot
            screenshot_filename = os.path.join(screenshot_address, f"{scenario_name}_{timestamp_screenshot}.png")
            context.driver.save_screenshot(screenshot_filename)

def after_all(context):
    # Close driver
    context.driver.quit()
