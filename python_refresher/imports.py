'''
Các mô-đun được sử dụng thường xuyên trong lập trình
Nó giúp tạo thêm nhiều file, với các mục đích riêng biệt, giúp viết code sạch và dễ bảo trì hơn
'''
import grade_average_service as grade_service

homework_assignment_grades = {
    'homework_1': 85,
    'homework_2': 100,
    'homework_3': 90,
}

grade_service.calculate_homework(homework_assignment_grades)
