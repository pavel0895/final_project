import datetime
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use")
    parser.addoption("--base_url", default="http://192.168.0.3:8081", help="Base URL")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")
    parser.addoption("--log_level", action="store", default="INFO", help="Log level")
    parser.addoption("--executor", action="store", default="localhost", help="Executor address")
    parser.addoption("--mobile", action="store_true", help="Enable mobile emulation")
    parser.addoption("--vnc", action="store_true", help="Enable VNC")
    parser.addoption("--logs", action="store_true", help="Enable logs")
    parser.addoption("--video", action="store_true", help="Enable video")
    parser.addoption("--bv", action="store", default=None, help="Browser version")
    parser.addoption("--selenium-manager", action="store_true", help="Use Selenium Manager for driver management")

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    mobile = request.config.getoption("--mobile")
    use_selenium_manager = request.config.getoption("--selenium-manager")

    executor_url = f"http://{executor}:4444/wd/hub"

    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(handler)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    options = None

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        if headless:
            options.add_argument("--headless")
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
    else:
        logger.error(f"Unrecognized browser name: {browser_name}")
        raise ValueError("Unrecognized browser name: %s" % browser_name)

    caps = {
        "browserName": browser_name,
        "acceptInsecureCerts": True,
    }

    if version:  # Добавляем версию браузера только если она указана
        caps["browserVersion"] = version

    for k, v in caps.items():
        options.set_capability(k, v)

    logger.info(f"Connecting to WebDriver at {executor_url}")

    try:
        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )
    except Exception as e:
        logger.error(f"Failed to connect to WebDriver: {e}")
        raise

    driver.maximize_window()
    driver.base_url = base_url
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser_name)

    if not mobile:
        driver.maximize_window()

    def fin():
        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
