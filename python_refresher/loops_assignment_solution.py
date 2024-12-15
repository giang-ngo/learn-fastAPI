"""
Cho biến my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
- Tạo một vòng lặp while để in ra tất cả các phần tử trong my_list
- Khi in các phần tử, sử dụng một vòng lặp for để in từng phần tử
- Tuy nhiên, nếu phần tử trong vòng lặp for bằng "Monday", hãy in "------" và tiếp tục vòng lặp
"""

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

x = 0
while x < 3:
    x += 1
    for i in my_list:
        if i == "Monday":
            print("------")
            continue
        print(i)
