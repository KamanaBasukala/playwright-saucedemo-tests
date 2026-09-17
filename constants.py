# =========================================================
# URLs
# =========================================================

BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = BASE_URL + "inventory.html"


# =========================================================
# Page Titles
# =========================================================

EXPECTED_TITLE = "Swag Labs"
EXPECTED_PRODUCTS_TITLE = "Products"


# =========================================================
# Valid Credentials
# =========================================================

STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"


# =========================================================
# Invalid Credentials
# =========================================================

INVALID_USER = "invalid_user"
INVALID_PASSWORD = "wrong_password"


# =========================================================
# Locked User
# =========================================================

LOCKED_USER = "locked_out_user"


# =========================================================
# Expected Inventory Values
# =========================================================

EXPECTED_PRODUCT_COUNT = 6
EXPECTED_IMAGE_COUNT = 6
EXPECTED_ADD_TO_CART_BUTTON_COUNT = 6
EXPECTED_DESCRIPTION_COUNT = 6


# =========================================================
# Login Error Messages
# =========================================================

INVALID_CREDENTIALS_ERROR = (
    "Epic sadface: Username and password do not match any user in this service"
)

USERNAME_REQUIRED_ERROR = (
    "Epic sadface: Username is required"
)

PASSWORD_REQUIRED_ERROR = (
    "Epic sadface: Password is required"
)

LOCKED_USER_ERROR = (
    "Epic sadface: Sorry, this user has been locked out."
)


# =========================================================
# Products
# =========================================================

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"
BOLT_T_SHIRT = "Sauce Labs Bolt T-Shirt"
FLEECE_JACKET = "Sauce Labs Fleece Jacket"
ONESIE = "Sauce Labs Onesie"
RED_T_SHIRT = "Test.allTheThings() T-Shirt (Red)"


# =========================================================
# Product Prices
# =========================================================

BACKPACK_PRICE = "$29.99"
BIKE_LIGHT_PRICE = "$9.99"
BOLT_T_SHIRT_PRICE = "$15.99"
FLEECE_JACKET_PRICE = "$49.99"
ONESIE_PRICE = "$7.99"
RED_T_SHIRT_PRICE = "$15.99"


# =========================================================
# Sorting Options
# =========================================================

SORT_A_TO_Z = "az"
SORT_Z_TO_A = "za"
SORT_LOW_TO_HIGH = "lohi"
SORT_HIGH_TO_LOW = "hilo"