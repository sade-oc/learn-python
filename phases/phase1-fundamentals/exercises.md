# 🐍 Phase 1: Python Fundamentals – Hands-On Exercises

Each section includes **core exercises** and a few **stretch goals** to deepen your understanding.

---

## 🔹 1. Python Syntax & Dynamic Typing

### 🧪 Exercises

1. Write a function that adds two numbers and returns the result.
2. Call it with both integers and floats. Then try strings and see what happens.
3. Assign an integer to a variable, then reassign a string to it.

### 🧠 Stretch

- Write a function that accepts any two values and prints their type, value, and whether they're equal.

---

## 🔹 2. Variables & Expressions

### 🧪 Exercises

1. Create a temperature converter: Celsius ↔ Fahrenheit.
2. Write an expression that uses modulo, floor division, and exponentiation.

### 🧠 Stretch

- Create a BMI calculator using named variables and formatted output (e.g., f-strings).

---

## 🔹 3. `if`, `for`, `while`, and `with`

### 🧪 Exercises

1. Write a program that loops through numbers 1–100 and:
    - Prints "Fizz" if divisible by 3
    - "Buzz" if divisible by 5
    - "FizzBuzz" if divisible by both
2. Loop through a list of student scores and assign letter grades.
3. Use `while` to guess a random number between 1–10 (use `random.randint`).

### 🧠 Stretch

- Use a `with open()` block to read a file line-by-line and count the number of lines containing the word "Python".

---

## 🔹 4. Lists, Tuples, Sets, and Dictionaries

### 🧪 Exercises

1. Create a list of 10 numbers. Sort, reverse, slice, and calculate sum/average.
2. Store 3D coordinates as a tuple and write a function to calculate distance from origin.
3. Use a set to remove duplicates from a list of names.
4. Create a dictionary with names as keys and ages as values. Add, update, and delete entries.

### 🧠 Stretch

- Write a function that takes a list of dictionaries representing users and returns only users over age 30.

---

## 🔹 5. Functions (incl. *args and **kwargs)

### 🧪 Exercises

1. Write a function to find the factorial of a number.
2. Write a function that accepts any number of arguments and returns the largest one.
3. Write a function that takes keyword arguments and prints them nicely.

### 🧠 Stretch

- Create a function called `describe_pet(name, **traits)` that prints info like:  
  `"Buddy is a 3-year-old Golden Retriever who loves to run."`

---

## 🔹 6. String Manipulation

### 🧪 Exercises

1. Take a string input, reverse it, and print it.
2. Count the number of vowels in a string.
3. Remove all punctuation from a paragraph (use `string.punctuation`).

### 🧠 Stretch

- Parse a string of comma-separated email addresses and validate that each contains an `@`.

---

## 🔹 7. Basic File I/O

### 🧪 Exercises

1. Create a `.txt` file and write some lines to it.
2. Read the file back and print each line with line numbers.
3. Write a list of strings to a file, one per line.

### 🧠 Stretch

- Read a file and create a frequency counter for each word (bonus: ignore case and punctuation).

---

## 🔹 8. Exceptions (`try/except/finally`)

### 🧪 Exercises

1. Write a function that divides two numbers, with exception handling for `ZeroDivisionError`.
2. Ask a user to input a number. If input is invalid, catch the exception and re-prompt.
3. Open a file that doesn’t exist and handle the exception gracefully.

### 🧠 Stretch

- Wrap your temperature converter from earlier in try/except to handle invalid inputs.

---

## ✨ Bonus: Combined Mini Challenge

Write a CLI app that:

- Asks the user for a file path  
- Reads the file and counts word frequencies  
- Prints the top 5 most common words  
- Handles exceptions if the file doesn’t exist or isn't readable

---
