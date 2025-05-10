def main():
    input_numbers = input("Введите числа через запятую: ")
    numbers = [int(x.strip()) for x in input_numbers.split(',')]

    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Четные числа:", even_numbers)

    max_number = numbers[0]
    min_number = numbers[0]
    for num in numbers[1:]:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num
    print("Максимальное число:", max_number)
    print("Минимальное число:", min_number)

    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print("Отсортированный список:", numbers)

if __name__ == "__main__":
    main()