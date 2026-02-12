import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Framework configuration"""

    # Environment URL
    BASE_URL = os.getenv("BASE_URL")

    # Browser Configuration
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", 10))

    # Test Credentials
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
