# convert time into integers. Divide minutes and hours
# calculate the time: add minutes until 60 after that calculate plus one hour
# calculate the change from PM to AM and viceversa, if the hour is 11 PM plus one will be 0 AM
# if day is provided, the day must change if the hour has crossed the bounduary from PM to AM

import math
import re

day_names = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]
timeday_am = ["PM", "AM"] * 100
timeday_pm = ["AM", "PM"] * 100


def result_printer(new_hour, new_minute, new_am_pm, day_count, weekday):

    day = None

    if new_hour == 12 and new_am_pm == "AM":
        new_hour = 0

    if new_minute < 10:
        new_minute = f"0{new_minute}"

    if day_count != 0:
        if day_count == 1:
            day = "(next day)"

        else:
            day = f"({day_count} days later)"

    if weekday is not None:
        weekday = weekday.capitalize()

    if weekday is None and day_count == 0:
        print(f"{new_hour}:{new_minute} {new_am_pm}")

    elif weekday is None:
        print(f"{new_hour}:{new_minute} {new_am_pm} {day}")

    elif day_count is None:
        print(f"{new_hour}:{new_minute} {new_am_pm}, {weekday}")

    else:
        print(f"{new_hour}:{new_minute} {new_am_pm}, {weekday} {day}")


def adjust_weekday(
    day_count,
    new_hour,
    new_minute,
    new_am_pm,
    weekday,
):  # this is to adjust the weekday index if it is more than 6
    weekday_index = (len(weekday)) - 6
    weekday = day_names[weekday_index]
    print(weekday)

    result_printer(new_hour, new_minute, new_am_pm, day_count, weekday)


def weekday_calculator(
    day_count, new_hour, new_minute, new_am_pm, weekday
):  # this function calculates the right weekday for the new time

    # weekday = weekday

    print(f"starting weekday:{weekday}")
    weekday = weekday.lower()
    starting_day_index = day_names.index(weekday)
    print(f"This is the starting day of the week's index: {starting_day_index}")
    print(f"This is the day count {day_count}")

    weekday_calculate = starting_day_index + day_count

    if weekday_calculate <= 6:
        new_weekday = day_names[weekday_calculate]  # to be fixed
        print(f"This is the new weekday {new_weekday}")
        result_printer(new_hour, new_minute, new_am_pm, day_count, new_weekday)

    elif weekday_calculate > 6:
        print("let's adjust the weekday")
        adjust_weekday(day_count, new_hour, new_minute, new_am_pm, weekday)


def day_calculator(
    new_hour, new_minute, new_am_pm, am_pm, weekday, day_count
):  # this function calculates the right AM PM of the new hour, and the number of days between times (if applicable)

    if am_pm == 1:
        am_pm = 0

    if new_am_pm == "AM":
        print("AM")
        new_am_pm = timeday_am[am_pm]
        print(f"This is the new time of the day list {new_am_pm}")

        day_new = timeday_am[:am_pm]
        print(f"this is the new day {day_new}")

        day_count = day_new.count(
            "AM"
        )  # this is to count how many days have passed from the starting day
        print(f"this is the day count {day_count}")

    elif new_am_pm == "PM":
        print("PM")
        new_am_pm = timeday_pm[am_pm]
        print(f"This is the new time of the day {new_am_pm}")

        day_new = timeday_pm[:am_pm]
        print(f"this is how it is calculated {day_new}")

        day_count = day_new.count("AM")

        if len(day_new) == 0:  # this adds the day when the list day_new is empty
            day_count = 1
        print(f"this is the day count {day_count}")

    if weekday is not None:
        print(weekday)
        print("Let's calculate the weekday")
        weekday_calculator(day_count, new_hour, new_minute, new_am_pm, weekday)

    else:
        result_printer(new_hour, new_minute, new_am_pm, day_count, weekday)


def time_calculator(init_time: str, add_time: str, weekday: str = None):

    day_count = 0

    new_am_pm = init_time.split(" ")[1]

    init_hour = int(init_time.split(":")[0])
    init_minute = init_time.split(":")[1]
    init_minute = int(
        init_minute.split(" ")[0]
    )  # this is to avoid to include AM/PM in the string #this results in problem when python cannot convert string to integer because of formatting ex 00:

    add_hour = int(add_time.split(":")[0])
    add_minute = int(add_time.split(":")[1])

    print(
        f"1. This is the hour to be added: {init_hour} and this is the  minute: {init_minute}"
    )  # @ control string

    new_minute = init_minute + add_minute
    new_hour = init_hour + add_hour

    if new_minute >= 60:
        new_minute -= 60
        new_hour = new_hour + 1

    # calculate am or pm
    am_pm = (
        new_hour // 12
    )  # this starts the process to calculate the right time of the day and day of the week, floor division rounds the number down
    print(f"This is {am_pm} am pm coefficent")  # @control string

    # adapt new hour to hour format 0-12

    if new_hour > 12:
        new_hour = new_hour - (am_pm * 12)
        print(new_hour)

    print(
        f"This is the new hour: {new_hour} and this is the new minute: {new_minute}"
    )  # @ control string

    print(am_pm)

    if am_pm >= 1:
        day_calculator(new_hour, new_minute, new_am_pm, am_pm, weekday, day_count)

    elif am_pm == 0:
        am_pm = new_am_pm
        result_printer(new_hour, new_minute, new_am_pm, day_count, weekday