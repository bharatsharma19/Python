# Author: Bharat Sharma

print("This code is designed by Bharat Sharma\n")

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    n = int(input("Enter the number of test cases : "))
    numbers = []
    for i in range(n):
        number = int(input("Enter the numbers\n"))
        numbers.append(number)

    for i in range(n):
        print(
            f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
