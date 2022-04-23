"""
this program a calculator
"""
__author__ = "lee bernard"
# lee bernard
# calculator
import test


def list_for_selection():
    print("\n")
    print("welcome to lee's simple calculator")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    print("^ for power")
    print("% for whole number and remainder")
    print("list for list option")
    print("type the word [stop] to stop ")
    print("\n")


def main():
    loop_for_main = 0
    multi_and_div_for_stupid = 1
    holder_for_if_number_is_a_number = 0
    while loop_for_main == 0:
        list_for_selection()
        operation = input("what operation do you want to do: ")
    # addition
        if operation == "+":
            add_number_1 = None
            add_number_2 = None
            print("this part does addition")
            while holder_for_if_number_is_a_number == 0:
                try:
                    add_number_1 = float(input("first number you want to add: "))
                    holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")
            while holder_for_if_number_is_a_number == 1:
                try:
                    add_number_2 = float(input("second number you want to add: "))
                    holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")

            def add_par(num1, num2):
                num3 = num1 + num2
                print(format(num1).rstrip("0").rstrip("."), "+", format(num2).rstrip("0").rstrip("."),
                      "is", format(num3).rstrip("0").rstrip("."))
                if num3 == 42069 or num3 == 420 or num3 == 69:
                    print("stop" * 100)

            add_par(add_number_1, add_number_2)
            holder_for_if_number_is_a_number -= 2
        # subtraction

        elif operation == "-":
            sub_real_number_1 = None
            sub_real_number_2 = None
            print("this part does subtraction")
            while holder_for_if_number_is_a_number == 0:
                try:
                    sub_real_number_1 = float(input("first number you want to subtract: "))
                    holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")

            while holder_for_if_number_is_a_number == 1:
                try:
                    sub_real_number_2 = float(input("second number you want to subtract: "))
                    holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")

            subtraction = sub_real_number_1 - sub_real_number_2
            print(format(sub_real_number_1).rstrip("0").rstrip("."), "-",
                  format(sub_real_number_2).rstrip("0").rstrip("."), "is", format(subtraction).rstrip("0").rstrip("."))
            holder_for_if_number_is_a_number -= 2
        # multiplication
        elif operation == "*":
            multi_real_number_1 = None
            multi_real_number_2 = None
            print("this part does multiplication")
            while holder_for_if_number_is_a_number == 0:
                try:
                    multi_real_number_1 = float(input("first number you want to multiply: "))
                    holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")

            while holder_for_if_number_is_a_number == 1:
                try:
                    multi_real_number_2 = float(input("second number you want to multiply: "))
                    holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")

            if multi_real_number_2 == multi_and_div_for_stupid:
                print("the answer is what you" + " put in the first input but if you really need the answer it's",
                      format(multi_real_number_1).rstrip("0").rstrip("."))
            else:
                multiplication = multi_real_number_1 * multi_real_number_2
                print(format(multi_real_number_1).rstrip("0").rstrip("."), "*", format(multi_real_number_2).rstrip("0")
                      .rstrip("."), "is", format(multiplication).rstrip("0").rstrip("."))
            holder_for_if_number_is_a_number -= 2
        # division
        elif operation == "/":
            divide_real_number_1 = None
            divide_real_number_2 = None
            print("this part does division")
            while holder_for_if_number_is_a_number == 0:
                try:
                    divide_real_number_1 = float(input("first number you want to divide: "))
                    holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")

            while holder_for_if_number_is_a_number == 1:
                try:
                    divide_real_number_2 = float(input("second number you want to divide: "))
                    if divide_real_number_2 == 0:
                        print("can't do that")
                    else:
                        holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")

            if divide_real_number_2 == multi_and_div_for_stupid:
                print("the answer is what you put in the first input but if you can't "
                      "do basic division it's", format(divide_real_number_1).rstrip("0").rstrip("."))
            else:
                division = divide_real_number_1 / divide_real_number_2
                print(format(divide_real_number_1).rstrip("0").rstrip("."), "/", format(divide_real_number_2)
                      .rstrip("0").rstrip("."), "is", format(division).rstrip("0").rstrip("."))
            holder_for_if_number_is_a_number -= 2
        # power
        elif operation == "^":
            pow_real_number_1 = None
            pow_real_number_2 = None
            print("this part allows you to power numbers")
            while holder_for_if_number_is_a_number == 0:
                try:
                    pow_real_number_1 = float(input("the number you want to be powered: "))
                    holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")

            while holder_for_if_number_is_a_number == 1:
                try:
                    pow_real_number_2 = float(input("how much power do you want: "))
                    holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")

            power = pow_real_number_1 ** pow_real_number_2
            print(format(pow_real_number_1).rstrip("0").rstrip("."), "to he power of",
                  format(pow_real_number_2).rstrip("0").rstrip("."), "is", format(power).rstrip("0").rstrip("."))

            power_number_for_easter_egg = 20

            if pow_real_number_2 >= power_number_for_easter_egg:
                print("no one man should have all that power "*2)
            # lyric from Kanye West - POWER
            holder_for_if_number_is_a_number -= 2
        # whole number and remainder

        elif operation == "%":
            whole_real_number_1 = None
            whole_real_number_2 = None
            print("this part tell you how many times the first "
                  "number can go into the second number and what the remainder is")
            while holder_for_if_number_is_a_number == 0:
                try:
                    whole_real_number_1 = float(input("the first number you want to divide: "))
                    holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")

            while holder_for_if_number_is_a_number == 1:
                try:
                    whole_real_number_2 = float(input("the second number you want to divide: "))
                    if whole_real_number_1 < whole_real_number_2:
                        print("first number needs to be greater than the second one")
                    else:
                        holder_for_if_number_is_a_number += 1
                except ValueError:
                    print("please input a valid number")

            whole_number = whole_real_number_1 // whole_real_number_2
            rest_number = whole_real_number_1 % whole_real_number_2

            if rest_number == 0:
                print(format(whole_real_number_1).rstrip("0").rstrip("."), "can be " + "divided by",
                      format(whole_real_number_2).rstrip("0").rstrip("."), "a grand total of",
                      format(whole_number).rstrip("0").rstrip("."), "times and there isn't any remainder")
            else:
                print(format(whole_real_number_1).rstrip("0").rstrip("."), "can be " + "divided by",
                      format(whole_real_number_2).rstrip("0").rstrip("."), "a grand total of",
                      format(whole_number).rstrip("0").rstrip("."), "times" + " and the remainder is",
                      format(rest_number).rstrip("0").rstrip("."))
            holder_for_if_number_is_a_number -= 2
        elif operation == "stop":
            loop_for_main += 1
        elif operation == "list":
            kut = 45
            while kut == 45:
                print("> to find the greatest in a list with a known length")
                print("< to find the smallest in a list with a known length")
                print(">? to find the greatest in a list with a unknown length")
                print("<? to find the smallest in a list with a unknown length")
                print("type the word [stop] to stop ")
                operation = input("what operation do you want to do: ")
                if operation == ">":
                    test.known_great()
                    kut += 1
                elif operation == "<":
                    test.known_small()
                    kut += 22
                elif operation == ">?":
                    test.unknown_great()
                    kut += 54
                elif operation == "<?":
                    test.unknown_small()
                    kut += 75
                elif operation == "stop":
                    kut += 765
                    loop_for_main -= -1
                else:
                    print("please read carefully and pick again")

        else:
            print("please read carefully ", end="")
            print("choose a valid option", " or make sure you only put the symbol in the list above", sep="")
            print("\n")


main()
