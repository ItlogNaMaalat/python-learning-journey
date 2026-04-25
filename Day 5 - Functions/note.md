# Day 5 - Functions

## Part 1: What is a Function?
    its a block of code that performs a specific task and can be reused.

### Example:
**without function:**

        print("Hello, World")
        print("Hello, World")
        print("Hello, World")

**With function:**

        def greet():
            Print("Hello, world")
        greet():

## part 2: Basic Syntax
    def function_name():
        # then you can write your code here.
    function_name()
    
**def**
    Used to define a function.

**Fucntion_name**
    its like the ID of the function.

**function_name()**
    its to call the fucntion and and execute the code inside it.

**Example:**

    def say_hello():
        print("Hello!")

    say_hello() #this is to call the funtion.

## Part 3: Parameters (input)
    def greet(name):
        print("Hello", name)
    
    greet("Ivan")


## Part 4: Return Value
    def add(a,b):
        return a + b

    result = add(5, 3)
    print(result)

**note:**
"return"
    sends value back 
    end the function