# Quy đổi điểm thành các loại sau:
# A = 90 - 100
# B = 80 - 89
# C = 70 - 79
# D = 60 - 69
# F = 0 - 59

grade = 63  # Gán điểm là 63

if grade >= 90:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
else:
    print("F")
