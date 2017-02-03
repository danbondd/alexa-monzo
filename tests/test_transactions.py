import json

from monzo import transactions
from nose.tools import assert_equal


class TestTransactions(object):

    transactions

    def setUp(self):
        with open('./fixtures/transactions.json') as data:
            TestTransactions.transactions = json.load(data)


    def test_calculate_total(self):
        expected = 29099

        total = transactions.calculate_total(TestTransactions.transactions['transactions'], None)
        assert_equal(total, expected)


    def test_calculate_total_with_category(self):
        results = {
            "eating_out": 5355,
            "transport": 7833,
            "groceries": 6213,
            "shopping": 7698,
            "bills": 2000,
            "mondo": 0
        }

        for category, expected in results.iteritems():
            total = transactions.calculate_total(TestTransactions.transactions['transactions'], category)
            assert_equal(total, expected)
