# Day 4 - Loops

## PART 1 — WHAT IS A LOOP?
    a way to repeat code multiple times

## Example 
Without a Loop
    print("Hello")
    print("Hello")
    print("Hello")

With a Loop
    for i in range(3):
    print("Hello")

Output: 
    Hello
    Hello
    Hello

## PART 2 — TYPES OF LOOPS
1. FOR LOOP (Most common)
    Used when you know how many time to repeat.

    ex.)
        for i in range(5):
            print(i)
    Output:
        0 1 2 3 4

### Understanding the Range()
 ________________________________
|Code             |Output        |
------------------|--------------|
|Range(5)         |0 to 4        |
|range(1,6)       |1 to 5        |
|range(1, 10, 2)  |1, 3, 5, 7, 9 |
 ________________________________

 2. WHILE LOOP
    Used when condition controls repetition
    
        ex.)
            x = 0

            while x < 5:
                print(x)
                x += 1
    ⚠️ important note:
        if you get "x += 1", it runs forever(infinite loop)

## PART 3 — BREAK & CONTINUE
    🔹break → stop loop

        ex.) 
        for i in range(10):
                if i == 5:
                    break
                print(i)

    🔹continue → skip

        ex.)
        for i in range(5):
            if i == 2:
                continue
            print(i)