customer_name = input("กรุณากรอกชื่อ : ")
product_name = input("กรุณากรอกชื่อสินค้า : ")
product_price = float(input("กรุณากรอกราคาสินค้า (บาท): "))

vat = product_price *0.07

total_price = product_price + vat

print("\n-----ใบเสร็จ-----")
print("ชื่อลูกค้า:", customer_name)
print("ชื่อสินค้า:", product_name)
print("ราคาสินค้า: {:.2f} บาท".format(product_price))
print("ภาษีมูลค่าเพิ่ม (7%): {:.2f} บาท".format(vat))
print("ราคารวมทั้งหมด: {:.2f} บาท" .format(total_price))
