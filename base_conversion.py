
def is_number(number):
    # checks if the value is an integer number
    try:
        int(number)
        return True
    except ValueError:
        return False


def verify_input(base_ten):
    # checks if input is number and that it is not negative and gives feedback to user
    if not is_number(base_ten):
        print("Value entered was not a number. Please enter only integer numbers in base 10")
        return False
    elif int(base_ten) < 0:
        print("Value entered is negative. Please enter a positive base 10 integer")
        return False

    return True


def convert_to_base(base_ten, target_base):
    # convert the base ten number to the target base
    current_number = base_ten
    base_number = []

    while current_number > 0:
        remainder = current_number % target_base
        current_number = current_number / target_base
        base_number.append(get_base_16_value(remainder))

    return "".join(str(e) for e in base_number[::-1])


def get_base_16_value(number):
    # get base sixteen values for numbers over 9
    base_16_specials = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    if number > 9:
        return base_16_specials[number]
    else:
        return number


def run_test_cases():
    # run the test cases for the user and display
    test_numbers = [
        100,
        500,
        1300,
        42
    ]

    results_100 = [
        "1100100",
        "144",
        "64"
    ]

    results_500 = [
        "111110100",
        "764",
        "1F4"
    ]

    results_1300 = [
        "10100010100",
        "2424",
        "514"
    ]

    results_42 = [
        "101010",
        "52",
        "2A"
    ]

    print "\nThe table shows the original number the base being converted to and the result you should see"

    for number in test_numbers:
        if number == 100:
            print_test(number, results_100)
        elif number == 500:
            print_test(number, results_500)
        elif number == 1300:
            print_test(number, results_1300)
        elif number == 42:
            print_test(number, results_42)


def print_test(number, results):
    # prints the cases for bases 2, 8, 16
    bases = [
        2,
        8,
        16
    ]

    for base, result in zip(bases, results):
        print "\n{: <5} => base {: <2} {:_>30}".format(number, base, result)


def instructions(instruction):
    # return instruction requested
    instruction_dict = {
        "welcome": "Welcome this program will convert a base 10 number into a target base between 2 and 16\n",
        "test": "enter #test at prompt to view test cases",
        "base_ten": "Please enter a base 10 number to convert: ",
        "target_base": "Please enter a target base to convert to: ",
    }

    return instruction_dict[instruction]


def main():
    # print instructions
    print instructions("welcome")

    # try to get the input
    try:
        # get user input
        user_input = raw_input(instructions("base_ten"))

        # keep going until exit is entered
        while user_input:
            # special cases
            if user_input == "exit":
                exit(0)
            elif user_input == "#test":
                run_test_cases()
            # regular input
            elif verify_input(user_input):
                print "{: <5} => base {: <2} {:_>30}".format(user_input, "2", convert_to_base(int(user_input), 2))
                print "{: <5} => base {: <2} {:_>30}".format(user_input, "8", convert_to_base(int(user_input), 8))
                print "{: <5} => base {: <2} {:_>30}".format(user_input, "16", convert_to_base(int(user_input), 16))

            # rinse and repeat
            user_input = raw_input(instructions("base_ten"))

    # fail gracefully if serious error occurs
    except ValueError:
        print "Something has gone wrong. Shutting down"
        exit(1)
    except KeyboardInterrupt:
        print "Keyboard interrupt detected. Shutting down"
        exit(1)


main()
