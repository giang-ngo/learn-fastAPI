"""
- Bạn có $50
- Bạn mua một món hàng trị giá $15
- Với thuế là 3%
- In ra số tiền bạn còn lại
"""

money = 50
item = 15
tax = .03

money_left = money - item - (item * tax)

print(money_left)

print(50 - 15 - (15 * .03))
