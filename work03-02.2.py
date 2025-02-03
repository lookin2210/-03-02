def find_minimum(numbers):
    """ ฟังก์ชันหาค่าต่ำสุดจาก list ขนาด 5 จำนวน """
    return min(numbers) 
numbers = []
print("Enter 5 numbers:")
for i in range(5):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)
min_value = find_minimum(numbers)
print(f"The minimum value is: {min_value}")
