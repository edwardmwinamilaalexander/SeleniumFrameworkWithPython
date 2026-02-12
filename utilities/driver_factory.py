from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.settings import Config


def get_driver():
    browser = Config.BROWSER.lower()

    if browser == "chrome":
        options = Options()

        # Preferences to disable password manager and autofill/address prompts
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "profile.default_content_setting_values.automatic_downloads": 1,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.popups": 0,
            "profile.default_content_setting_values.ads": 2,
            "profile.default_content_setting_values.savable_form_data": 2,  # <-- disables autofill/address popups
            # Add these two lines for Save Address popup
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False,
        }
        options.add_experimental_option("prefs", prefs)

        # Chrome feature flags
        options.add_argument("--disable-features=PasswordLeakDetection")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-password-manager-reauthentication")
        options.add_argument("--disable-autofill-keyboard-accessory-view")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--no-first-run")
        # Add this line for Save Address popup
        options.add_argument("--disable-autofill-address-save-prompt")

        if Config.HEADLESS:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)

    else:
        raise ValueError(f"Unsupported browser: {Config.BROWSER}")

    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    return driver
