def timeConversion(s):
    # h = s[:2]
    # m = s[3:5]
    # s = s[6:-2]
    #
    # h2m = int(h) * 60
    # h2m += int(m)
    # m2s = int(h2m) * 60
    # m2s += int(s)
    # convert_to_preferred_format(m2s)

    if s[-2:] == "PM":
        return f"{int(s[:2]) + int(0 if int(s[:2]) == 12 else 12)}{s[2:-2]}"
    else:
        if int(s[:2]) == 12:
            return f"00{s[2:-2]}"
        else:
            return f"{s[:-2]}"


def convert_to_preferred_format(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60

    print("seconds value in hours:", hour)
    print("seconds value in minutes:", min)
    print("seconds value in seconds:", sec)
    print(f'{hour:d}:{min:02d}:{sec:02d}')

    return "%02d:%02d:%02d" % (hour, min, sec)


# n = 100000000000
# print("Time in preferred format :-", convert_to_preferred_format(n))

s = "06:40:03AM"
# s = "07:05:45PM"
# s = "12:00:00AM"
# s = "12:05:39AM"
# s = "12:40:22AM"
# s = "12:45:54PM"
print(timeConversion(s))
