#Task 1
def fizbuzz():
   for i in range(1,101):
         if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
         elif i % 3 == 0:
            print("Fizz")
         elif i % 5 == 0:
            print("Buzz")
         else:
            print(i)

#Task 3
def guess_random():
   import random
   number = random.randint(1, 10)
   guess = None
   while guess != number:
         guess = int(input("Guess a number between 1 and 10: "))
         if guess < number:
            print("Too low!")
         elif guess > number:
            print("Too high!")
         else:
            print("Congratulations! You guessed it right.")


#Stretch Task
count = 0
with open('example.txt', 'r') as file:
   for line in file:
      if 'python' in line.lower():
         count += 1
print(f'The word "python" appears {count} times in the file.')   


#fizbuzz()
#guess_random()
 