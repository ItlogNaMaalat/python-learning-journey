# DAY 3 — CONDITIONAL STATEMENTS

## PART 1 — CONCEPT
### What are Conditionals?
Conditionals allow your program to make decisions based on conditions

### Basic Syntax
    if condition:
        # code runs if TRUE

### Example
age = 18

if age >= 18:
    print("You are an adult")

## PART 2 — if, else, elif

### if - else
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

### if - elif - else
score = int(input("Enter score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")

## PART 3 — COMPARISON OPERATORS
 _______________________________
|Operator |Meaning
|---------|---------------------|
|==       |equal                |
|!=       |not equal            |
|>        |greater than         |
|<        |less than            |
|>=       |greter or equal than |
|<=       |less or equal than   |
 _______________________________

## PART 4 — LOGICAL OPERATORS

 ___________________________
|Operator |Meaning          |
|---------|-----------------|
|and      |both true        |
|or       |atleast one true |
|not      |opposite         |
 ___________________________

### Example
age = 20
is_student = True

if age >= 18 and is_student:
    print("Eligible student")

