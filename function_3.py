def sum_of_squares(numbers):
    return sum([x ** 2 for x in numbers])
numbers = list(map(float, input("กรุณากรอกตัวเลขหลายๆ ตัว (คั่นด้วยช่องว่าง): ").split()))
result = sum_of_squares(numbers)
print(f"ผลบวกของกำลังสองของสมาชิกใน list คือ: {result}")
