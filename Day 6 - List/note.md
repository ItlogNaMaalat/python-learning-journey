# Day 6 - List

## What is a list? 

A list stores multiple values in one variable.

**Lists are used to:**

        store multiple values
        organize data
        loop through items
        build real applications
Almost EVERY real program uses lists.

Example:

    fruits = ["apple", "banana", "orange"]

Instead of:

    fruit1 = "apple"
    fruit2 = "banana"
    fruit3 = "orange"

we use ONE list.

## List Syntax
    variable_name = [item1, item2, item3]

Example:

    numbers = [1, 2, 3, 4, 5]

## Lists Can Store Different Data Type
    data = ["Ivan", 20, 5.8, True]

## Accessing List Items
Lists use indexes.

IMPORTANT:

    indexing starts at 0

Example:

    fruits = ["apple", "banana", "orange"]

    print(fruits[0])

Output:

    apple

## Index Guide
| Index | Value  |
| ----- | ------ |
| 0     | apple  |
| 1     | banana |
| 2     | orange |

## Changing List Values
    fruits = ["apple", "banana", "orange"]

    fruits[1] = "grape"

    print(fruits)

Output:

    ['apple', 'grape', 'orange']

## Adding Items
**append()**

Adds item at the end.

    fruits = ["apple", "banana"]

    fruits.append("orange")

    print(fruits)

Output:

    ['apple', 'banana', 'orange']

## Removing Items
**remove()**

    fruits.remove("banana")

## List Length
**len()**

    numbers = [1, 2, 3, 4]

    print(len(numbers))

Output:

    4

## Looping Through Lists
    fruits = ["apple", "banana", "orange"]

    for fruit in fruits:
        print(fruit)

Output:

    apple
    banana
    orange


