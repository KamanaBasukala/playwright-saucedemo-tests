from playwright.sync_api import Page, expect

from constants import EXPECTED_TITLE


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    # =====================================================
    # Actions
    # =====================================================

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    # =====================================================
    # Assertions
    # =====================================================

    def verify_title(self):
        expect(self.page).to_have_title(EXPECTED_TITLE)

    def verify_error(self, expected_message: str):
        expect(self.error_message).to_have_text(
            expected_message
        )

    def verify_login_page(self, expected_url: str):
        expect(self.page).to_have_url(
            expected_url
        )