import unittest
from . import account


class AccountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account1 = account.Account("tola", "1234")

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        """
        GIVEN: An account class
        WHEN: when a deposit is made
        THEN: account balance should be reflected
        """

        account1 = account.Account("bola", "1234")

        account1.deposit(2000)

        self.assertEqual(2000, account1.balance)

    def test_that_negative_deposit_raises_error(self):
        account1 = account.Account("bola", "1234")
        account1.deposit(500)
        self.assertRaises(ValueError, account1.deposit, -2000)
        self.assertEqual(500, account1.balance)

    def test_that_withdrawal_can_be_made(self):
        account1 = account.Account("bola", "1234")
        account1.deposit(5000)
        account1.withdraw(3000)
        self.assertEqual(2000, account1.balance)

    def test_for_negative_withdraw(self):
        account1 = account.Account("bola", "1234")
        account1.deposit(5000)
        account1.withdraw(-3000)
        self.assertEqual(5000, account1.balance)

    def test_for_withdrawal_more_than_balance(self):
        account1 = account.Account("bola", "1234")
        account1.deposit(5000)
        account1.withdraw(7000)
        self.assertEqual(5000, account1.balance)

    def test_that_when_there_is_no_money_withdrawal_fails(self):
        account1 = account.Account("bola", "1234")
        account1.withdraw(7000)
        self.assertEqual(0, account1.balance)

    def test_for_transfer(self):
        account1 = account.Account("bola", "1234")
        account2 = account.Account("chi", "1234")
        account1.deposit(5000)
        account1.transfer(account2, 2000, "1234")
        self.assertEqual(3000, account1.balance)
        self.assertEqual(2000, account2.balance)


if __name__ == '__main__':
    unittest.main()
