# value = input('Enter the cost : ')

# if int(value) >= 100:
#     print('too much price')
# else:
#     print('no more price')


# number = input('Enter the number : ')

# if int(number) > 0:
#     print(f'received Positive {number}')
# elif int(number) == 0:
#     print(f'received Zero {number}')
# else:
#     print(f'received Negative {number}')


# number = input('Enter the number : ')

# if int(number) > 0:
#     print(f'received Positive {number}')
# if int(number) == 0:
#     print(f'received Zero {number}')
# else:
#     print(f'received Negative {number}')

# find maximum highest number

# marks = [90, 40, 99, 50, 80, 95, 99.5]
# highest = marks[0]

# for i in marks:
#     if highest < i:
#         highest = i
# print(f'this is highest marks : {highest}')


# Grading System


def grading_system():
    percentage = int(input('Enter Percentage : '))

    if percentage > 100 or percentage < 0:
        print('Please Enter Valid Percentage!')
        grading_system()
        return

    if percentage >= 90 and percentage <= 100:
        print('Congratulation you have got [A] Grade')
    elif percentage >= 80 and percentage <= 89:
        print('Congratulation you have got [B] Grade')
    elif percentage >= 70 and percentage <= 79:
        print('Congratulation you have got [c] Grade')
    elif percentage >= 50 and percentage <= 69:
        print('Congratulation you have got [A] Grade')
    else:
        print('You are failed')


grading_system()