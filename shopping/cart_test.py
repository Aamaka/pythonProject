import unittest
import cart


class CartTest(unittest.TestCase):
    def test_that_cart_has_been_created(self):
        cart1 = cart.Cart
        self.assertIsNotNone(cart1)

    def test_that_cart_can_have_item(self):
        cart1 = cart.Cart(3)
        self.assertEqual([], cart1.item)

    def test_that_cart_can_add_item(self):
        cart1 = cart.Cart(3)
        cart1.add_item("bread")
        cart1.add_item("egg")
        self.assertEqual(["bread", "egg"], cart1.item)

    def test_that_cart_have_limit(self):
        cart1 = cart.Cart(3)
        cart1.add_item("bread")
        cart1.add_item("egg")
        cart1.add_item("milk")
        cart1.add_item("butter")
        self.assertEqual(["butter", "egg", "milk"], cart1.item)

    def test_that_cart_will_not_be_more_than_limit(self):
        cart1 = cart.Cart(3)
        cart1.add_item("bread")
        cart1.add_item("egg")
        cart1.add_item("milk")
        cart1.add_item("butter")
        self.assertEqual(["butter", "egg", "milk"], cart1.item)
