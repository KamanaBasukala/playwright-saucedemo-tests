import pytest
from playwright.sync_api import expect

from constants import (
    STANDARD_USER,
    STANDARD_PASSWORD,
    BACKPACK,
    SORT_A_TO_Z,
    SORT_Z_TO_A,
    SORT_LOW_TO_HIGH,
    SORT_HIGH_TO_LOW,
)
from pages.inventory_page import InventoryPage


# =========================================================
# Helper
# =========================================================

def open_inventory(login_page):

    login_page.login(
        STANDARD_USER,
        STANDARD_PASSWORD
    )

    return InventoryPage(
        login_page.page
    )


# =========================================================
# TC008 - Inventory page loads
# =========================================================

@pytest.mark.order(8)
def test_inventory_page_loads(login_page):

    inventory_page = open_inventory(
        login_page
    )

    inventory_page.verify_page_loaded()


# =========================================================
# TC009 - Product count
# =========================================================
@pytest.mark.order(9)
def test_product_count(login_page):

    inventory_page = open_inventory(
        login_page
    )

    inventory_page.verify_product_count()


# =========================================================
# TC010 - Product names
# =========================================================
@pytest.mark.order(10)
def test_product_names(login_page):

    inventory_page = open_inventory(
        login_page
    )

    inventory_page.verify_product_names()


# =========================================================
# TC011 - Product prices
# =========================================================
@pytest.mark.order(11)
def test_product_prices(login_page):

    inventory_page = open_inventory(
        login_page
    )

    inventory_page.verify_product_prices()


# =========================================================
# TC012 - Product images
# =========================================================
@pytest.mark.order(12)
def test_product_images(login_page):

    inventory_page = open_inventory(
        login_page
    )

    inventory_page.verify_product_images()


# =========================================================
# TC013 - Add to Cart buttons
# =========================================================
@pytest.mark.order(13)
def test_add_to_cart_buttons(login_page):

    inventory_page = open_inventory(
        login_page
    )

    inventory_page.verify_add_to_cart_buttons()


# =========================================================
# TC014 - Product descriptions
# =========================================================
@pytest.mark.order(14)
def test_product_descriptions(login_page):

    inventory_page = open_inventory(
        login_page
    )

    inventory_page.verify_product_descriptions()


# =========================================================
# TC015 & TC016 - Product name sorting
# =========================================================

@pytest.mark.parametrize(
    "sort_option, expected_first_product",
    [
        (
            SORT_A_TO_Z,
            BACKPACK,
        ),
        (
            SORT_Z_TO_A,
            "Test.allTheThings() T-Shirt (Red)",
        ),
    ],
    ids=[
        "TC015_sort_A_to_Z",
        "TC016_sort_Z_to_A",
    ],
)
@pytest.mark.order(15)
def test_sort_products_by_name(
    login_page,
    sort_option,
    expected_first_product,
):

    inventory_page = open_inventory(
        login_page
    )

    inventory_page.sort_by(
        sort_option
    )

    expect(
        inventory_page.product_names.nth(0)
    ).to_have_text(
        expected_first_product
    )


# =========================================================
# TC017 & TC018 - Price sorting
# =========================================================

@pytest.mark.parametrize(
    "sort_option, expected_first_price",
    [
        (
            SORT_LOW_TO_HIGH,
            "$7.99",
        ),
        (
            SORT_HIGH_TO_LOW,
            "$49.99",
        ),
    ],
    ids=[
        "TC017_price_low_to_high",
        "TC018_price_high_to_low",
    ],
)
@pytest.mark.order(17)
def test_sort_products_by_price(
    login_page,
    sort_option,
    expected_first_price,
):

    inventory_page = open_inventory(
        login_page
    )

    inventory_page.sort_by(
        sort_option
    )

    expect(
        inventory_page.product_prices.nth(0)
    ).to_have_text(
        expected_first_price
    )


# =========================================================
# TC019 - Add product to Cart
# =========================================================
@pytest.mark.order(19)
def test_add_product_to_cart(login_page):

    inventory_page = open_inventory(
        login_page
    )

    inventory_page.add_product_to_cart(
        BACKPACK
    )

    inventory_page.verify_cart_count(1)
