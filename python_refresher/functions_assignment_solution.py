"""
Bài tập về hàm
- Tạo một hàm nhận 3 tham số (firstname, lastname, age)
- Trả về một dictionary dựa trên các giá trị đó
"""


def user_dictionary(firstname, lastname, age):
    created_user_dictionary = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return created_user_dictionary


solution_dictionary = user_dictionary(firstname="Eric", lastname="Cartman", age=10)
print(solution_dictionary)
