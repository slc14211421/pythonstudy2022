# -*- coding: utf-8 -*-
"""
Create Time: 2022/4/30 18:37
Author: Lison Song
"""
import datetime


def time_till_deadline(goal, deadline):
    deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
    today_date = datetime.datetime.today()
    time_till = deadline_date - today_date
    return f"Dear user! Time remaining for your goal: {goal} is {time_till.days} days"


if __name__ == '__main__':
    user_input = input("enter you goal with a deadline separated by colon\n\r")
    input_list = user_input.split(":")
    goal = input_list[0]
    deadline = input_list[1]

    print(time_till_deadline(goal, deadline))
