from monzo import utils 
from nose.tools import assert_equal

class TestUtils(object):
    def test_speakable_currency(self):
	money = {
	    100000: "1000 pounds and 0 pence",
	    10000: "100 pounds and 0 pence",
	    1000: "10 pounds and 0 pence",
	    100: "1 pound and 0 pence",
	    10: "0 pounds and 10 pence",
	    1: "0 pounds and 1 pence",
	    123456: "1234 pounds and 56 pence",
	    12345: "123 pounds and 45 pence",
	    1234: "12 pounds and 34 pence",
	    123: "1 pound and 23 pence",
	    12: "0 pounds and 12 pence",
	    00000: "0 pounds and 0 pence",
	    0000: "0 pounds and 0 pence",
	    000: "0 pounds and 0 pence",
	    00: "0 pounds and 0 pence",
	}

        for pence, expected in money.iteritems():
	    output = utils.speakable_currency(pence)
	    assert_equal(output, expected)

    def test_duration_to_words(self):
        durations = {
	    "P2M": "2 months",
	    "P3W": "3 weeks",
	    "P4D": "4 days",
	    "P5Y": "5 years",
	    "PT2H": "2 hours",
	    "PT3M": "3 minutes",
	    "PT4S": "4 seconds",
	    "P2DT3H": "2 days and 3 hours",
	    "P2WT3M": "2 weeks and 3 minutes",
	    "P2MT3S": "2 months and 3 seconds",
	    "P2Y3M4D": "2 years, 3 months and 4 days",
	    "P2Y3M4DT5H": "2 years, 3 months, 4 days and 5 hours",
	    "P2Y3M4DT5H6M": "2 years, 3 months, 4 days, 5 hours and 6 minutes",
	    "P2Y3M4DT5H6M7S": "2 years, 3 months, 4 days, 5 hours, 6 minutes and 7 seconds",
	    "P1M": "1 month",
	    "P1W": "1 week",
	    "P1D": "1 day",
	    "P1Y": "1 year",
	    "PT1H": "1 hour",
	    "PT1M": "1 minute",
	    "PT1S": "1 second"
	}

        for duration, expected in durations.iteritems():
    	    output = utils.duration_to_words(duration)
	    assert_equal(output, expected)
