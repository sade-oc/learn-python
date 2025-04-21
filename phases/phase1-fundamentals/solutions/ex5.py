#Task 1 
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    
print(fact(5))  # Output: 120

#Task 2
def largest(*args):
      return max(args)
print(largest(1, 2, 3, 4, 5))  # Output: 5

#Task 3
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)


fun(name="Alice", age=25, city="London")  # Output: name Alice, age 25, city London

#Stretch Task

def describe_pet(name, **traits):
    # Pull specific traits (with defaults if missing)
    age = traits.get("age", "unknown age")
    breed = traits.get("breed", "unknown breed")
    hobby = traits.get("hobby", "do fun things")

    # Format the output
    print(f"{name} is a {age}-year-old {breed} who loves to {hobby}.")
describe_pet("Buddy", age=5, breed="Golden Retriever", hobby="play fetch")  # Output: Buddy is a 5-year-old Golden Retriever who loves to play fetch.