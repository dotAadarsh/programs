import tomli
ts = tomli.loads("ts = 2_459_772.084027777777778")["ts"]

print(ts) # 2459772.084027778

seconds = (ts - int(ts)) * 86_400
print(seconds) # 7260.000009834766


'''
You first use tomli to parse your Julian date, pick out the value, and name it ts. 
You can see that the value of ts has been truncated by several decimal places. 
To figure out how bad the effect of the truncation is, you calculate the number of seconds represented by the fractional part of ts and compare it to 7260
'''

seconds = seconds - 7260
print(seconds) # 9.834766387939453e-06


'''
An integer Julian date represents noon on some day. 
2:01pm is two hours and one minute after noon, and two hours and one minute equals 7260 seconds, 
so seconds - 7260 shows you how big of an error is introduced by your parsing.
'''

# you can fix it by using Python’s Decimal class, which provides arbitrary-precision decimal numbers.
from decimal import Decimal
ts = tomli.loads("ts = 2_459_772.084027777777778", parse_float=Decimal)["ts"]
print(ts)

seconds = (ts - int(ts)) * 86_400
print(seconds) # 7260.000000000019200

seconds = seconds - 7260
print(seconds) # '1.9200E-11

'''
Now, the small error that’s left comes from your original representation and is about nineteen picoseconds, 
which translates to subcentimeter errors at the speed of light.
'''