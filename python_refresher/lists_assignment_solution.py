# Tạo một danh sách gồm 5 con vật gọi là zoo
# Xóa con vật tại chỉ số thứ 3
# Thêm một con vật mới vào cuối danh sách
# Xóa con vật ở đầu danh sách
# In ra tất cả các con vật
# Chỉ in ra 3 con vật đầu tiên

zoo = ["Monkey", "Zebra", "Gorilla", "Lion", "Tiger"]
zoo.pop(3)
zoo.append("Lizard")
zoo.pop(0)
print(zoo)
for x in zoo:
    print(x)
print(zoo[0:3])
