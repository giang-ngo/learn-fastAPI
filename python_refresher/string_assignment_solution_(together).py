'''
String Assignment we will do together:
(Bài tập chuỗi mà chúng ta sẽ làm cùng nhau:)

Ask the user how many days until their birthday
(Yêu cầu người dùng nhập số ngày còn lại cho đến sinh nhật của họ)

and print an approx number of weeks until their birthday
(và in ra số tuần ước tính còn lại cho đến sinh nhật của họ)

Weeks is = 7 days
(1 tuần = 7 ngày)

decimals within the return is allowed..
(phép tính cho phép kết quả có số thập phân)

'''

days = int(input("How many days until your birthday? "))

# Tính số tuần còn lại bằng cách chia số ngày cho 7 và làm tròn kết quả đến 2 chữ số thập phân
print(round(days / 7, 2))
