
# Conditional Statements in Python

Conditional statements let a program **make decisions**.  
They control which parts of code are executed depending on certain conditions.

---

## 🧠 The idea
When we want a program to behave differently based on some rule (for example, a number being positive or negative, or an age being over 18),  
we use an `if` statement.

```python
age = int(input("How old are you? "))

if age >= 18:
    print("You are of age!")
````

If the condition (`age >= 18`) is **true**, the indented code inside the `if` block runs.
If it’s **false**, Python skips that block.

---

## 🔹 Syntax of `if`

An `if` statement always has:

1. The keyword `if`
2. A **condition** (a Boolean expression that is True or False)
3. A **colon (`:`)**
4. One or more **indented lines** of code

Example:

```python
if condition:
    # code that runs if the condition is True
```

If the colon or indentation is missing, you’ll get a `SyntaxError`.

---

## 🔸 Adding `else`

Use `else` when you want to specify what happens if the condition is **not true**.

```python
if age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")
```

➡️ Only **one** of these two blocks runs — never both.

---

## 🔸 Multiple conditions: `elif`

When there are **more than two possible outcomes**, use `elif` ("else if").

```python
if number < 0:
    print("Negative")
elif number == 0:
    print("Zero")
else:
    print("Positive")
```

Python checks conditions **in order**:

* If the first one is true, it runs that block and skips the rest.
* If not, it tries the next one (`elif`), and so on.
* If none are true, it runs the `else` block (if it exists).

---

## 🔸 Logical operators in conditions

You can combine conditions using `and`, `or`, and `not`:

```python
if temperature > 0 and temperature < 30:
    print("Nice weather!")

if grade < 50 or attendance < 70:
    print("You failed the course.")

if not is_raining:
    print("Let’s go outside!")
```

---

## 🔹 Indentation matters

Code that belongs to the same block must be **indented equally**:

```python
if x > 0:
    print("Positive")
    print("Greater than zero")
print("Always printed")  # outside the if
```

---

## 🔸 Comparison operators

Conditions often compare two values:

| Operator | Meaning          | Example  |
| -------- | ---------------- | -------- |
| `==`     | Equal to         | `x == 5` |
| `!=`     | Not equal to     | `x != 5` |
| `>`      | Greater than     | `x > 5`  |
| `<`      | Less than        | `x < 5`  |
| `>=`     | Greater or equal | `x >= 5` |
| `<=`     | Less or equal    | `x <= 5` |

---

## ⚠️ Common mistakes

❌ Forgetting the colon:

```python
if x > 0
    print("Positive")
```

✅ Correct:

```python
if x > 0:
    print("Positive")
```

❌ Forgetting to convert input to int:

```python
number = input("Enter a number: ")  # string!
if number > 10:  # ERROR: comparing str and int
    print("Too big!")
```

✅ Correct:

```python
number = int(input("Enter a number: "))
```

❌ Wrong indentation:

```python
if x > 0:
print("Positive")  # ERROR: expected indent
```

✅ Correct:

```python
if x > 0:
    print("Positive")
```

---

### Summary

* `if` runs code when a condition is true.
* `else` runs code when it’s false.
* `elif` allows multiple branches.
* Conditions use comparison and logical operators.
* Blocks are defined by indentation, not braces.
* Always end `if`, `elif`, and `else` with a colon `:`.

With these tools, you can build programs that **make decisions**, such as checking ages, comparing numbers, or printing different messages depending on user input.

# Combining Conditions in Python

## 🎯 Learning objectives
After this section, you will be able to:
- Use the logical operators **and**, **or**, and **not** in conditions  
- Write and understand **nested and combined conditionals**  

---

## 🔹 Logical operators
Python allows you to combine multiple conditions into one expression using logical operators:

| Operator | Meaning | True if… |
|----------|---------|----------|
| `and` | both conditions are true | both parts are True |
| `or` | at least one condition is true | one or both are True |
| `not` | reverses the truth value | the condition is False |

---

### 🧩 Example: `and`
`and` means **all conditions must be true** at the same time.
```python
number = int(input("Please type in a number: "))

if number >= 5 and number <= 8:
    print("The number is between 5 and 8")
```

This condition only passes if the number is 5, 6, 7, or 8.

---

### 🧩 Example: `or`
`or` means at least one condition must be true.
```python
number = int(input("Please type in a number: "))

if number < 5 or number > 8:
    print("The number is not within the range of 5 to 8")
```

This checks whether the number is outside the range 5–8.

---

### 🧩 Example: `not`
`not` reverses a condition.
```python
if not (number >= 5 and number <= 8):
    print("The number is not within the range of 5 to 8")
```

This means exactly the same thing as the previous example — just written differently.

---

## 🧮 Truth tables

| a | b | `a and b` | `a or b` |
|---|---|-----------|----------|
| False | False | False | False |
| True | False | False | True |
| False | True | False | True |
| True | True | True | True |

| a | `not a` |
|---|---------|
| True | False |
| False | True |

---

## ✨ Simplified notation
Python allows a mathematical shorthand for range checks.

Instead of:
```python
if x >= 5 and x <= 8:
```

you can write:
```python
if 5 <= x <= 8:
```

Both versions are valid and mean the same thing. The chained version is cleaner and closer to mathematical notation.

---

## 🧠 Nested and combined conditionals
Conditions can be chained or placed inside one another. For example, finding the greatest of four numbers:
```python
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    greatest = n1
elif n2 > n3 and n2 > n4:
    greatest = n2
elif n3 > n4:
    greatest = n3
else:
    greatest = n4

print(f"{greatest} is the greatest of the numbers.")
```

This works because:
* The first condition is true only if n1 is greater than all others.
* If not, the program continues checking other conditions.
* Finally, exactly one branch executes.

---

## ✅ Summary
* Use `and` when all conditions must be true.
* Use `or` when any condition can be true.
* Use `not` to invert a condition.
* Combine comparisons for clean range checks (`5 <= x <= 10`).
* Always use parentheses for clarity when combining several conditions.
* Combined conditionals make your programs more expressive and powerful.

