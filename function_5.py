def apply_discount(price, discount):
    discounted_price = price - (price * discount / 100)
    return discounted_price
price = float(input("กรุณากรอกราคาสินค้า: "))
discount = float(input("กรุณากรอกเปอร์เซ็นต์ส่วนลด: "))
final_price = apply_discount(price, discount)
print(f"ราคาสินค้าหลังจากได้รับส่วนลด {discount}% คือ: {final_price:.2f} บาท")
