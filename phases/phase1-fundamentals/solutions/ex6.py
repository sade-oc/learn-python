#Task 1 
def reverse(s):
   print("Reversed string:", s[::-1])
   return s[::-1]

reverse("Sade")

#Task 2
def count_vowels(s):
   vowels = "aeiouAEIOU"
   count = 0
   for char in s:
       if char in vowels:
           count += 1
   print("Number of vowels:", count)
   return count
count_vowels("Sade")

#Task 3
def remove_punctuation(s):
   import string
   return s.translate(str.maketrans("", "", string.punctuation))

print("String without punctuation:", remove_punctuation("Hello, world!"))

#Stretch Task
def is_email(*args):
   for s in args:
      if "@" not in s:
         print("Invalid email address")
      else:
         print("Valid email address")

is_email("shsbs@gmail.com", "shsbs.com", "shsbs@gmail", "jasjsjs", "shsbs@.com", "hshsis.com")