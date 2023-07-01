def extracting_numbers(Input):
    numbers = []
    current_number = ''
    for char in Input:
        if char.isdigit() or char == '-' and not current_number:
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ''
    if current_number:
        numbers.append(int(current_number))
    return numbers


def third_large_and_smallest(numbers_list):
    if len(numbers_list) < 3:
        return "Need at  least 3 numbers."

    unique = list(set(numbers_list))
    unique.sort()

    if len(unique) < 3:
        return "Kindly provide a proper input"

    third_large = unique[-3]
    third_small = unique[2]

    return third_large, third_small


if __name__ == "__main__":
    Input = input()
    numbers_list = extracting_numbers(Input)
    third_large, third_small= third_large_and_smallest(numbers_list)

    print(f"Third Largest Number: {third_large}")
    print(f"Third Smallest Number: {third_small}")