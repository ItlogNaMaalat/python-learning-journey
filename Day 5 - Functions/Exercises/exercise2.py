# 🧪 Exercise 2 — Grade Function

# task: def get_grade(score): return A,B,C,D, and F

def get_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    elif score <= 60:
        return "F"

number = int(input("Enter your score: "))
print(get_grade(number)) 