number = float(input())

if number == 0:
  print("zero")
elif number > 0 and number < 1:
  print("small positive")
elif number > 0 and number > 1000000:
  print("large positive")
elif number > 0:
  print("positive")

if number < 0 and number > -1:
  print("small negative")
elif number < 0 and number < -1000000:
  print("large negative")
elif number < 0:
  print("negative")

#1 000 000