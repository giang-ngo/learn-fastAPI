"""
For & While Loops
"""

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger or equal to 5")

# my_list = [1, 2, 3, 4, 5]
#
# # print(my_list[0])
# # print(my_list[1])
# # print(my_list[2])
# # print(my_list[3])
# # print(my_list[4])
#
# sum_of_for_loop = 0
#
# for x in my_list:
#     sum_of_for_loop += x
#
# print(sum_of_for_loop)
