def concatenate_strings(STR1, STR2, STR3):
    return STR1 + STR2 + STR3
STR1 = input("กรุณากรอกสตริงตัวแรก: ")
STR2 = input("กรุณากรอกสตริงตัวที่สอง: ")
STR3 = input("กรุณากรอกสตริงตัวที่สาม: ")
result = concatenate_strings(STR1, STR2, STR3)
print(f"ผลลัพธ์ของการต่อสายอักขระ: {result}")
