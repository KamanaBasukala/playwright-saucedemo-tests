from playwright.sync_api import Page, expect

from constants import (
    EXPECTED_PRODUCTS_TITLE,
    EXPECTED_PRODUCT_COUNT,
    EXPECTED_IMAGE_COUNT,
    EXPECTED_ADD_TO_CART_BUTTON_COUNT,
    EXPECTED_DESCRIPTION_COUNT,
)


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        # =================================================
        # Locators
        # =================================================

        self.page_title = page.locator(".title")

        self.products = page.locator(
            ".inventory_item"
        )

        self.product_names = page.locator(
            ".inventory_item_name"
        )

        self.product_prices = page.locator(
            ".inventory_item_price"
        )

        self.product_images = page.locator(
            ".inventory_item_img img"
        )

        self.add_to_cart_buttons = page.locator(
            "button[id^='add-to-cart']"
        )

        self.product_descriptions = page.locator(
            ".inventory_item_desc"
        )

        self.cart_badge = page.locator(
            ".shopping_cart_badge"
        )

        self.sort_dropdown = page.locator(
            "[data-test='product-sort-container']"
        )

    # =================================================
    # Page Assertions
    # =================================================

    def verify_page_loaded(self):
        expect(
            self.page_title
        ).to_have_text(
            EXPECTED_PRODUCTS_TITLE
        )

    def verify_product_count(self):
        expect(
            self.products
        ).to_have_count(
            EXPECTED_PRODUCT_COUNT
        )

    # =================================================
    # Product Assertions
    # =================================================

    def verify_product_names(self):
        expect(
            self.product_names
        ).to_have_count(
            EXPECTED_PRODUCT_COUNT
        )

    def verify_product_prices(self):
        expect(
            self.product_prices
        ).to_have_count(
            EXPECTED_PRODUCT_COUNT
        )

    def verify_product_images(self):
        expect(
            self.product_images
        ).to_have_count(
            EXPECTED_IMAGE_COUNT
        )

    def verify_add_to_cart_buttons(self):
        expect(
            self.add_to_cart_buttons
        ).to_have_count(
            EXPECTED_ADD_TO_CART_BUTTON_COUNT
        )

    def verify_product_descriptions(self):
        expect(
            self.product_descriptions
        ).to_have_count(
            EXPECTED_DESCRIPTION_COUNT
        )

    # =================================================
    # Cart Actions
    # =================================================

    def add_product_to_cart(self, product_name: str):

        product = self.products.filter(
            has_text=product_name
        )

        product.get_by_role(
            "button",
            name="Add to cart"
        ).click()

    def verify_cart_count(self, expected_count: int):

        expect(
            self.cart_badge
        ).to_have_text(
            str(expected_count)
        )

    # =================================================
    # Sorting
    # =================================================

    def sort_by(self, option: str):

        self.sort_dropdown.select_option(option)