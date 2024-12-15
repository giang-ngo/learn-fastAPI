'''
Functions
'''


def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate


final_cost = buy_item(50)
print(final_cost)

# def print_list(list):
#     for i in list:
#         print(i)
#
#
# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print_list(numbers_list)

# def multiply_numbers(a, b):
#     return a * b
#
#
# solution = multiply_numbers(2, 3)
# print(solution)

# def print_numbers(highest_number, lowest_number):
#     print(highest_number)
#     print(lowest_number)
#
#
# print_numbers(lowest_number=10, highest_number=20)

# def print_color_red():
#     color = 'red'
#     print(color)
#
#
# color = "Blue"
# print(color)
# print_color_red()


# def print_my_name(first_name, last_name):
#     print(f"Hello {first_name} {last_name}!")
#
#
# print_my_name("Steve", "Jobs")
