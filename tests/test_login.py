import pytest

from constants import (
    STANDARD_USER,
    STANDARD_PASSWORD,
    INVALID_USER,
    INVALID_PASSWORD,
    LOCKED_USER,
    BASE_URL,
    INVENTORY_URL,
    INVALID_CREDENTIALS_ERROR,
    USERNAME_REQUIRED_ERROR,
    PASSWORD_REQUIRED_ERROR,
    LOCKED_USER_ERROR,
)


# =========================================================
# TC001 - Valid Login
# =========================================================

@pytest.mark.order(1)
def test_valid_login(login_page):

    login_page.verify_title()

    login_page.login(
        STANDARD_USER,
        STANDARD_PASSWORD
    )

    assert login_page.page.url == INVENTORY_URL


# =========================================================
# TC002 - TC007 - Invalid Login Scenarios
# =========================================================

@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            STANDARD_USER,
            INVALID_PASSWORD,
            INVALID_CREDENTIALS_ERROR,
        ),
        (
            INVALID_USER,
            STANDARD_PASSWORD,
            INVALID_CREDENTIALS_ERROR,
        ),
        (
            "",
            STANDARD_PASSWORD,
            USERNAME_REQUIRED_ERROR,
        ),
        (
            STANDARD_USER,
            "",
            PASSWORD_REQUIRED_ERROR,
        ),
        (
            "",
            "",
            USERNAME_REQUIRED_ERROR,
        ),
        (
            LOCKED_USER,
            STANDARD_PASSWORD,
            LOCKED_USER_ERROR,
        ),
    ],
    ids=[
        "TC002_invalid_password",
        "TC003_invalid_username",
        "TC004_empty_username",
        "TC005_empty_password",
        "TC006_both_fields_empty",
        "TC007_locked_user",
    ],
)
@pytest.mark.order(2)
def test_invalid_login(
    login_page,
    username,
    password,
    expected_error,
):

    login_page.login(
        username,
        password
    )

    login_page.verify_error(
        expected_error
    )

    login_page.verify_login_page(
        BASE_URL
    )
