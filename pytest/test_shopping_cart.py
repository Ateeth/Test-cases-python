from unittest.mock import Mock
import pytest
from item_database import ItemDatabase
from shopping_cart import ShoppingCart

# Fixture can be used to initialize items/objects and can be passed as arguments to test cases
# Fixtures are run once before each test case i.e new cart will be created for each test
@pytest.fixture
def cart():
    ## All setup for cart starts here...
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1
    
def test_when_item_added_then_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()
    
def test_when_add_more_than_max_items_should_fail(cart):
    for _ in range(5):
        cart.add("apple")
    with pytest.raises(OverflowError):
        cart.add("apple")
        
def test_can_get_total_price(cart):
    print("Testing can get price")
    cart.add("apple")
    cart.add("orange")
    
    # price_map = {
    #     "apple": 1.0,
    #     "orange": 2.0
    # }
    
    # assert cart.get_total_price(price_map) == 3.0

    item_database = ItemDatabase()
    
    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        
        if item == "orange":
            return 2.0
    
    item_database.get = Mock(side_effect = mock_get_item)
    
    assert cart.get_total_price(item_database) == 3.0

   
    pass