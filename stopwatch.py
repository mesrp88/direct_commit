import datetime as dt

user_input = input("Enter your goal with deadline separated by colon:\n")
input_list = user_input.split(':')  #input looks like -> python:27.08.2021

goal = input_list[0]
deadline = input_list[1]

deadline_date=dt.datetime.strptime(deadline, "%d.%m.%Y")
today_date= dt.datetime.today()
time_remaining= deadline_date-today_date

print(f"Dear user you have {time_remaining.days} days before deadline of your goal ie {goal}")






