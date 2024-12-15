# Tạo một vòng lặp for để in ra tất cả các khóa và giá trị
# Tạo một biến mới vehicle2, là một bản sao của my_vehicle
# Thêm một khóa mới 'number_of_tires' vào biến vehicle2 với giá trị là 4
# Xóa khóa và giá trị 'mileage' khỏi vehicle2
# In ra chỉ các khóa từ vehicle2

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x, y in my_vehicle.items():
    print(x, y)

vehicle2 = my_vehicle.copy()
vehicle2["number_of_tires"] = 4

# del vehicle2["mileage"]
vehicle2.pop('mileage')

for i in vehicle2.keys():
    print(i)
