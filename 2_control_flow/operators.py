#!/usr/bin/env python3

a = 200
b = 42
c = 500
if a > b and c > a:
    print("Both true")

if a > b or a > c:
    print("At least 1 true")

if not a < b:
    print("a is NOT greater than b")

"""
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")
  """


# _ underscore character _ as the last case value to
# to execute when there are not other matches
day = 5
match day:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case 4:
        print("found")
    case _:
        print("other")


day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")
