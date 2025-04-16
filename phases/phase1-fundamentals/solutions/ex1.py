
#Task 1
def add_two_numbers(a, b):

  return a + b

#Task 2
print(add_two_numbers(2, 3))
print(add_two_numbers(5.2, 7.4))

#Task 3
var1 = 10
print(var1)
var1 = "Hello"
print(var1)

#Stretch Task
def two_vals(val1, val2):
  val1Type = type(val1)
  val2Type = type(val2)
  print(val1Type)
  print(val2Type)
  if val1 == val2:
    return True
  else:
    return False
  
print(two_vals(1, 2))
print(two_vals(1, "2"))
print(two_vals("1", "2"))
print(two_vals(1, 1))
print(two_vals("1", "1")) 