# Conditional statements

## Learning objectives

After this section you will:

- Understand what a **conditional statement** is and how it affects program flow  
- Know how to use the `if` statement in Python  
- Be able to use **comparison operators** to express conditions  

---

## Introduction

Up to now, every line of code in our programs has been executed **in order**, from top to bottom.  
However, in real-world programs, we often want to **run certain parts of code only under specific conditions**.  
This is where **conditional statements** come in.

For example, the following code checks if a user is old enough to watch a movie:

```python
age = int(input("How old are you? "))

if age >= 18:
    print("You are allowed to watch the movie.")

print("Thank you for visiting!")
```

If the user is 18 or older, the program prints both lines:

## Sample output
```
How old are you? 20
You are allowed to watch the movie.
Thank you for visiting!
```

If the user is younger, only the second line appears:

## Sample output
```
How old are you? 12
Thank you for visiting!
```

Notice how the part inside the `if` block is only executed when the condition is true.  
This allows programs to make decisions based on user input or other data.

---

## The `if` statement and indentation

A conditional statement begins with the keyword `if`, followed by a **condition** — usually a comparison between two values.  
If the condition is true, the indented code block underneath is executed.
```python
number = 5

if number > 0:
    print("The number is positive.")
```

⚠️ The colon (`:`) at the end of the `if` line is mandatory. Python uses indentation (spaces or a tab) to determine which lines belong to the conditional block.

For example, this would cause an error:
```python
if number > 0
    print("The number is positive.")
```

Output:
```
SyntaxError: invalid syntax
```

Make sure to always include the colon and use consistent indentation. Most editors (including Codespaces) will automatically indent for you after typing `:` and pressing Enter.

## Comparison operators

Conditions often compare two values. Here are the most common comparison operators in Python:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<` | Less than | `a < b` |
| `<=` | Less than or equal to | `a <= b` |
