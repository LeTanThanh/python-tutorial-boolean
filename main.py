if __name__ == "__main__":
  # Introduction to Python Boolean data type
  is_active = True
  print(is_active)

  is_admin = True
  print(is_admin)

  print(20 > 10)
  print(20 < 10)

  print("a" < "b")
  print("a" > "b")

  # The bool() function

  print(bool("Hi"))
  print(bool(""))
  print(bool(100))
  print(bool(0))

  # Falsy and Truthy values

  """
  When a value evaluates to True, it's truthy.
  And if a value evaluates to Flase, it's falsy.

  The following are falsy values in Python:
  - A number zero
  - An empty string ""
  - Flase
  - None
  - An empty list []
  - An empty tuple ()
  - An empty dictionary {}

  The truthy values are the other values that aren't falsy
  """
