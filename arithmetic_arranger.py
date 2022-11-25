import re


# define error messages
MSG_ERROR0 = "Error: Too many problems"
MSG_ERROR1 = "Error: Numbers must contain only digits"
MSG_ERROR2 = "Error: Operation must be + or -"
MSG_ERROR3 = "Error: Number cannot be more than four digits"

# ----------------------------------------------------------------------------------------------
# define the functions
# -----------------------------------------------------------------------------------------------------

# define the last function that prints all operations side by side

width = 5
space = "    "


def arithmetic_arranger_true(
    arit_op: list, calculate: bool = False
):  # display the arranged op if condition false

    lst = list(zip(*[op.split(" ") for op in arit_op]))
    lines = [
        [s.rjust(width) for s in lst[0]],
        [f"{op}{val.rjust(width-1)}" for op, val in zip(lst[1], lst[2])],
        ["-" * (width)] * len(lst[0]),
        [str(eval(op)).rjust(width) for op in arit_op],
    ]

    for l in lines:
        print("   ".join(l))


def arithmetic_arranger_false(
    arit_op: list, calculate: bool = False
):  # display and calculate the arranged op if condition true

    lst = list(zip(*[op.split(" ") for op in arit_op]))  # zip is to yield a tuple
    lines = [
        [s.rjust(width) for s in lst[0]],
        [f"{op}{val.rjust(width-1)}" for op, val in zip(lst[1], lst[2])],
        ["-" * (width)] * len(lst[0]),
    ]

    for l in lines:
        print("   ".join(l))


# define the functions


def arithmetic_arranger(
    arit_op: list, calculate: bool = False
):  # sets the default value

    if len(arit_op) > 4:
        print(MSG_ERROR0)
    else:

        check_errors = " ".join(arit_op)

        match_letters = re.search("[A-Za-z]+", check_errors)
        match_divmult = re.search("[//**]+", check_errors)
        match_numlen = re.search("[0-9]{4,}", check_errors)

        if match_divmult is not None:
            print(MSG_ERROR2)
            exit()

        elif match_letters is not None:
            print(MSG_ERROR1)
            exit()

        elif match_numlen is not None:
            print(MSG_ERROR3)
            exit()

        else:
            arithmetic_arranger_calculate(arit_op, calculate)


def arithmetic_arranger_calculate(arit_op: list, calculate: bool):

    if (calculate) == True:
        arithmetic_arranger_true(arit_op, calculate)

    else:

        arithmetic_arranger_false(arit_op, calculate)
