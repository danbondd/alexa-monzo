import re

def pence_to_pounds(pence):
    pounds = pence / 100.00
    return "{0:.2f}".format(round(pounds,2))

def speakable_currency(pence):
    pounds = pence_to_pounds(pence)
    units = pounds.split(".")
    output = units[0]
    output = re.sub('-', '', output)

    if units[0] == "1":
        output += " pound and "
    else:
        output += " pounds and "

    output += "%s pence" % units[1]
    return output


