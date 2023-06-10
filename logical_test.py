def int_to_thai_text(number):
    thai_digits = {
        0: 'ศูนย์',
        1: 'หนึ่ง',
        2: 'สอง',
        3: 'สาม',
        4: 'สี่',
        5: 'ห้า',
        6: 'หก',
        7: 'เจ็ด',
        8: 'แปด',
        9: 'เก้า'
    }

    thai_units = {
        1: 'สิบ',
        2: 'ร้อย',
        3: 'พัน',
        4: 'หมื่น',
        5: 'แสน',
        6: 'ล้าน'
    }

    thai_text = ''
    digits = []

    # Convert the number to a list of digits
    while number > 0:
        digits.append(number % 10)
        number //= 10

    digits.reverse()

    # Convert each digit to Thai text
    for i, digit in enumerate(digits):
        if digit != 0:
            thai_text += thai_digits[digit]

        if digit != 0 and i < len(digits) - 1:
            thai_text += thai_units[len(digits) - i - 1]

    return thai_text


# Example usage
number = int(input("Enter your value !not over 10Million : "))
if int(number)<10000000:

    thai_text = int_to_thai_text(number)
    print(thai_text)  # Output: หนึ่งร้อยยี่สิบสามล้านสี่แสนห้าหมื่นหกพันเจ็ดร้อยแปดสิบเก้า
else:
    print("Your input value greater than 10Million")