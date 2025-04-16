# Dynamic Typing in Python

## Table of Contents
1. [What is Dynamic Typing?](#what-is-dynamic-typing)
2. [Example Code](#example-code)
3. [Python String Formatting with f-Strings](#python-string-formatting-with-f-strings)
   - [Basic Syntax](#basic-syntax)

---

## What is Dynamic Typing?

In dynamically typed languages, the **type of a variable is determined at runtime**, not in advance. This means:
- You can assign a value of any type to a variable.
- You can reassign that variable to a different type later.
- The interpreter handles type changes without explicit declarations.

---

## Example Code

```python
# Task 3
var1 = 10        # var1 is assigned an integer
print(var1)      # Output: 10

var1 = "Hello"   # var1 is now assigned a string
print(var1)      # Output: Hello
```

---

## Python String Formatting with f-Strings

**f-strings** (formatted string literals) were introduced in **Python 3.6**. They're a powerful, readable, and efficient way to embed expressions inside string literals.

### Basic Syntax

```python
name = "Alice"
age = 30

# Using f-string
print(f"My name is {name} and I'm {age} years old.")
```
---

## User Input

In Python, you can use the `input()` function to get input from the user. The input is always returned as a string, so you may need to convert it to the desired type.

### Example: Getting User Input

```python
# Prompt the user for their name
name = input("What is your name? ")

# Prompt the user for their age and convert it to an integer
age = int(input("How old are you? "))

# Print a message using the input
print(f"Hello, {name}! You are {age} years old.")
```

### Key Points:
- The `input()` function displays a prompt and waits for the user to type something.
- Use type conversion functions like `int()`, `float()`, etc., to convert the input to the desired type.
- Always handle user input carefully to avoid errors (e.g., invalid type conversions).