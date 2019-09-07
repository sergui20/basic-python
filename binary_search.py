numbers = [-40, 1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

def binary_search(number, low, high):
    if low > high:
        return False

    mid_number = (low + high) / 2

    if numbers[mid_number] == number:
        return True
    elif numbers[mid_number] > number:
        return binary_search(number, low, mid_number - 1)
    elif numbers[mid_number] < number:
        return binary_search(number, mid_number + 1, high)

if __name__ == "__main__":
    num_to_search = input("Enter a number: ")
    result = binary_search(num_to_search, 0, len(numbers) - 1)

    if result is True:
        print("The number IS in the list")
    else:
        print("The number IS NOT in the list")    