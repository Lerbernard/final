"""
this file is just a file with some function for project.py
"""
__author__ = "lee bernard"
# for loop with the largest number from list


def known_great():
    k = None
    loop_variable_1 = 3
    print("this will tell you what item on your list is the greatest")
    while loop_variable_1 == 3:
        try:
            k = int(input("enter the amount of item on your list: "))
            loop_variable_1 += 1
        except ValueError:
            print("please enter a whole number and try again")
    list_1 = []
    loop_inner = 0
    counter_loop = 1
    for xex in range(k):
        loop_inner += 1
        while loop_inner == counter_loop:
            try:
                f = float(input("enter the items on your list: "))
                list_1.append(f)
                loop_inner += 1
                counter_loop += 2
            except ValueError:
                print("please enter a valid number and try again")
    list_1.sort()
    list_12 = list_1[-1]
    print("the greatest item on this list is", format(list_12).rstrip("0").rstrip("."))


# for loop with the smallest number from list
def known_small():
    w = None
    loop_variable_2 = 0
    print("this will tell you what item on your list is the smallest")
    while loop_variable_2 == 0:
        try:
            w = int(input("enter the amount of item on your list: "))
            loop_variable_2 += 1
        except ValueError:
            print("please enter a whole number and try again")
    counter_loop_2 = 1
    loop_inner_2 = 0
    pep8_is_stupid = []

    for pep8_is__stupid in range(w-1+1):
        loop_inner_2 += 1
        while loop_inner_2 == counter_loop_2:
            try:
                v = float(input("enter the items on your list: "))
                pep8_is_stupid.append(v)
                loop_inner_2 += 1
                counter_loop_2 += 2
            except ValueError:
                print("please enter a valid number and try again")
    pep8_is_stupid.sort()
    listed_13 = pep8_is_stupid[0]
    print("the smallest item on this list is", format(listed_13).rstrip("0").rstrip("."))


# while loop with the greatness number from list
def unknown_great():
    print("this will tell you what item on your list is the greatest")
    print("to stop", "just don't enter anything and press enter")
    holder_for_great = 0
    hold = []
    while holder_for_great != 1:
        variable_for = input("enter the items on your list: ")
        try:
            if variable_for == "" and hold != []:
                holder_for_great += 1
            variable_for_try = float(variable_for)
            hold.append(variable_for_try)
        except ValueError:
            if variable_for == "":
                pass
            else:
                print("please enter a valid number and try again")

    hold.sort()
    hold_221 = hold[-1]
    print("the greatest item on this list is", format(hold_221).rstrip("0").rstrip("."))


# while loop with the smallest number from list
def unknown_small():
    print("this will tell you what item on your list is the smallest")
    print("to stop just don't enter anything and press enter")
    for_great_1 = 42
    hold_1 = []
    while for_great_1 != 42:
        st = input("enter the items" + "on your list: ")
        try:
            if st == "" and hold_1 != []:
                for_great_1 += 1
            variable_for_try_1 = float(st)
            hold_1.append(variable_for_try_1)
        except ValueError:
            if st == "":
                pass
            else:
                print("please enter a valid number and try again")
    hold_1.sort()
    hold_344 = hold_1[0]
    print("the smallest item on this list is", format(hold_344).rstrip("0").rstrip("."))
