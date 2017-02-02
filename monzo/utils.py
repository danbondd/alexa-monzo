from __future__ import division

import re


def pence_to_pounds(pence):
    pounds = pence / 100
    return "{0:.2f}".format(round(pounds, 2))


def speakable_currency(pence):
    pounds = pence_to_pounds(pence)
    units = pounds.split(".")
    output = units[0]
    output = output.replace("-", "")

    if units[0] == "1":
        output += " pound and "
    else:
        output += " pounds and "

    if units[1][0] == "0":
        units[1] = units[1][1:]

    output += "%s pence" % units[1]
    return output


def singular(dur, word):
    if int(dur) > 1:
        word = word + "s"
    return "%s %s" % (dur, word)


# This is definitely not the most efficient way of doing this - lots of tests!
def duration_to_words(duration):
    if len(duration) == 0:
        return ""

    if duration[0] == "P":
        duration = duration[1:]

    t_off = duration.find("T")
    time = duration[t_off:]

    if t_off >= 0:
        duration = duration[:t_off]

    pattern = re.compile(r'[0-9]*[A-Z]')
    durs = pattern.findall(duration)
    words = []

    if len(durs) > 0:
        for d in durs:
            last = len(d) - 1
            if d[last] == "Y":
                period = "year"
            elif d[last] == "M":
                period = "month"
            elif d[last] == "W":
                period = "week"
            elif d[last] == "D":
                period = "day"
            words.append(singular(d[:last], period))

    if t_off >= 0:
        if time[0] == "T":
            time = time[1:]

        times = pattern.findall(time)

        for t in times:
            last = len(t) - 1
            if t[last] == "H":
                ts = "hour"
            elif t[last] == "M":
                ts = "minute"
            elif t[last] == "S":
                ts = "second"
            words.append(singular(t[:last], ts))

    i = 0
    output = ""
    for w in words:
        if i == len(words) - 1 and len(words) > 1:
            output = "%s and %s" % (output, w)
        elif i == 0:
            output = w
        else:
            output = "%s, %s" % (output, w)
        i += 1

    return output
