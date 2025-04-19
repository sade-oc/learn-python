import math

# Task 1
# Create a list called myList of random integers between 1 and 100
myList = [1, 8, 25, 13, 49, 99, 100, 2,2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 10, 49]

sortedList = myList.sort(reverse=True)
reversedList = myList.reverse()
sliceList = myList[2:5] # slicing the list from index 2 to 5 exlusive
sumList = sum(myList) # sum of all elements in the list
averageList = sum(myList) / len(myList) # average of all elements in the list

print("Sorted List:", myList)
print("Reversed List:", myList)
print("Sliced List:", sliceList)
print("Sum of List:", sumList)
print("Average of List:", averageList)

# Task 2
point = (3, 4, 5)

def distanceFromOrigin(p):
   x, y, z = p
   return math.sqrt(x**2 + y**2 + z**2)

print("Distance from origin:", distanceFromOrigin(point))

# Task 3
mySet = set(myList) #Type casting the list to a set to remove duplicates
print(mySet)

# Task 4
people = {
    "alice": {
        "age": 25,
        "city": "London"
    },
    "bob": {
        "age": 30,
        "city": "Manchester"
    },
      "charlie": {
         "age": 35,
         "city": "Bristol"
      },
      "dave": {
         "age": 40,
         "city": "Liverpool"
      }
}
print(people) # Printing the dictionary
print(people["alice"]["age"]) # Accessing the age of alice
print(people["bob"]["city"]) # Accessing the city of bob

# Stretch Task 
users = {
      "alice": {
         "age": 25,
         "city": "London",
         "hobbies": ["reading", "swimming"]
      },
      "bob": {
         "age": 30,
         "city": "Manchester",
         "hobbies": ["gaming", "cooking"]
      },
         "charlie": {
            "age": 35,
            "city": "Bristol",
            "hobbies": ["traveling", "photography"]
         },
         "dave": {
            "age": 40,
            "city": "Liverpool",
            "hobbies": ["sports", "music"]
         }
   }

def averageAge(users):
   total_age = 0
   for user in users.values():
      total_age += user["age"]
   return total_age / len(users)
print("Average age of users:", averageAge(users))
