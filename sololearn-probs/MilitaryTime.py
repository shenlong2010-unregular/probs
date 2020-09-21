# 5:00 AM - 5:00
# 11:00 AM - 11:00
# 12:00 AM - 00:00
# 12:30 AM - 00:30

# 12:00 PM - 12:00
# 12:30 PM - 12:30
# 1:00 PM - 13:00
# 8:00 PM - 20:00
def militaryTime(s):
    # AM time
    if s.endswith("AM"):
        if s[:2] == "12":
            return "00" + s[2:s.find("AM")]
        else:
            return '0' + s[:2] + s[2:s.find("AM")] if s.find(':') == 1 else s[:2] + s[2:s.find("AM")]

    # PM time
    elif s.endswith("PM"):
        # print(s.find(":"))
        if s[:2] == "12":
            return "12" + s[2:s.find("PM")]
        else:
            if s.find(":") == 2:
                return str(int(s[:s.find(":")]) + 12) + s[2:s.find("PM")]
            elif s.find(":") == 1:
                return str(int(s[:1]) + 12) + ":" + s[2:s.find("PM")]
print(militaryTime('11:58 AM'), '11:58')
print(militaryTime('11:59 AM'), '11:59')
print(militaryTime('12:00 PM'), '12:00')
print(militaryTime('12:01 PM'), '12:01')
print(militaryTime('11:58 PM'), '23:58')
print(militaryTime('11:59 PM'), '23:59')
print(militaryTime('12:00 AM'), '00:00')
print(militaryTime('12:01 AM'), '00:01')
print(militaryTime('9:00 AM'), '09:00')