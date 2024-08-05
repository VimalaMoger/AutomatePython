from unittest.mock import Mock

import pytest

from shopping_cart.item_database import ItemDatabase
from shopping_cart.shopping_cart import ShoppingCart


#use cases for unittests
#running unittests with pytest
#set up fixtures in pytest
#shopping cart initialization into fixtures for refactoring my code in enchance
#writing less lines of code(reducing boilerplate overhead)
#mock dependency-fake behavior of classes, fake data that unittest can use it

@pytest.fixture
def cart():
    #all set up for the cart here, runs as new for every test
    return ShoppingCart(5)


def test_addItemToCart(cart):
    #cart = ShoppingCart(5)
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    #cart = ShoppingCart(5)
    cart.add("apple")
    assert cart.get_items() == ["apple"]
    assert "apple" in cart.get_items()


#asserRaises implementation
def test_when_add_more_than_max_items_should_fail(cart):
    #cart = ShoppingCart(3)
    for i in range(5):
        cart.add("apple")
    #test fails when added 4th item
    with pytest.raises(OverflowError):
        cart.add("apple")


def test_can_get_totalPrice(cart):
    #cart = ShoppingCart(2)
    cart.add("apple")
    cart.add("Orange")
    #cart.add("Banana")
    item_database = ItemDatabase()

    #item_database.get = Mock(return_value=1.0)
    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "Orange":
            return 2.0

    #using side effect

    item_database.get = Mock(side_effect=mock_get_item)
    '''price_map = {
        "apple": 1.0,
        "Orange": 2.0
    }'''
    assert cart.get_total_price(item_database) == 3.0