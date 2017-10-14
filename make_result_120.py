"""Question: You are given only 5 zeros, apply any mathematical operator(s)
             any number of times make the result 120.
"""

def factorial(num):
    """Calculating factorial of num"""
    if num < 0:
        print "Factorial cannot be calculated!"
    elif num == 0:
        print "Factorial = 1"
    else:
        factorial = 1
        for i in range(1, num+1):
            factorial = factorial * i
        print factorial


if __name__ == "__main__":
    zeros = [0, 0, 0, 0, 0]
    """Convert all zeros to 1 by using bitwise operator and
       calculate their sum.
    """
    num = sum(map(lambda a: ~a, zeros))
    """Calculate factorial of the sum."""
    factorial(abs(5))
