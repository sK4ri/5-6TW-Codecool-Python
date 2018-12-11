from random import randint


def get_random_numbers(random_range):
    rand_nums = []
    for number in range(10):
        rand_nums.append(randint(1, random_range))
    return rand_nums


def get_guess(random_range, ranges, rand_nums):
    for i in range(ranges):
        while True:
            guess = int(input("Enter an integer from 1 to %d : " % random_range))
            if guess < rand_nums[i]:
                print("guess is low")
            elif guess > rand_nums[i]:
                print("guess is high")
            else:
                print("you guessed it!")
                break


def main():
    get_guess(99, 1, get_random_numbers(99))
    get_guess(49, 10, get_random_numbers(49))


if __name__ == "__main__":
    main()
