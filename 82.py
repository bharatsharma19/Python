import random
from xml.dom import WrongDocumentErr


def vivekMultiplication(number):
    wrong = random.randint(1, 10)
    table = [i*number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table


def isCorrect(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i

    return None


if __name__ == "__main__":
    number = int(input("Enter a number for multiplication table : "))
    # print(vivekMultiplication(number))
    myTable = vivekMultiplication(number)
    print(myTable)
    wrongIndex = isCorrect(myTable, number)
    print(f"The table is wrong at index {wrongIndex}")
