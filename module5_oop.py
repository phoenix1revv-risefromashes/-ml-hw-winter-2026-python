# module5_oop.py
#This is the OOPS style version of the assignment we previously did in module 4


# Class that handles reading numbers and searching
class NumberList:
    def __init__(self):
        self.numbers = []  # initialize an empty list

    # Method to read N numbers from user
    def read_numbers(self, N):
        print(f"Enter {N} numbers one by one (only positive numbers allowed):")
        for i in range(N):
            while True:
                try:
                    num = int(input(f"Enter number {i + 1}: "))
                    if num >= 0:
                        self.numbers.append(num)
                        break
                    else:
                        print("Oops! Only positive numbers are allowed. Try again.")
                except ValueError:
                    print("Oops! That’s not a number. Please type an integer.")

    # Method to search for X in the list
    def find_number(self, X):
        for i, num in enumerate(self.numbers):
            if num == X:
                return i + 1  # 1-based index
        return -1

# Main program
if __name__ == "__main__":
    while True:
        try:
            N = int(input("How many numbers do you want to enter? (N, must be positive): "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Oops! That’s not a number.")

    # Create an object of the NumberList class
    my_list = NumberList()
    my_list.read_numbers(N)

    # Ask for the number to search
    while True:
        try:
            X = int(input("Which number do you want to find? (X can be any integer): "))
            break
        except ValueError:
            print("Oops! That’s not a number.")

    # Search and print the result
    result = my_list.find_number(X)
    if result == -1:
        print(f"The number {X} was not found. Output: -1")
    else:
        print(f"The number {X} was found at position {result}.")
