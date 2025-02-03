def find_minimum(numbers):
    """ ฟังก์ชันหาค่าต่ำสุดจาก list ขนาด 5 จำนวน """
    return min(numbers)  # ใช้ฟังก์ชัน min() เพื่อหาค่าต่ำสุด

# รับค่าจากผู้ใช้ 5 จำนวนและเก็บใน list
numbers = []
print("Enter 5 numbers:")
for i in range(5):
    num = float(input(f"Number {i+1}: "))  # รับค่าจากผู้ใช้
    numbers.append(num)  # เพิ่มค่าเข้า list

# เรียกใช้ฟังก์ชันหาค่าต่ำสุด
min_value = find_minimum(numbers)

# แสดงผลค่าต่ำสุด
print(f"The minimum value is: {min_value}")
