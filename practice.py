def get_input():
    num = int(input("Please enter a positive number: "))
    bitsize = int(input("Please enter the bit amount: "))
    return num, bitsize

def decimal_to_binary(number, bits):
    
    binary_str = bin(number)[2:]
    # משלימים באפסים משמאל אם צריך כדי להגיע לאורך שביקשתי
    return binary_str.zfill(bits)

def two_complement(binary_num):
    #הופכת את כל הסיביות
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary_num)
    
    # המרה לעשרוני, הוספת 1, ואז חזרה לבינארי
    inverted_int = int(inverted, 2) + 1
    result = bin(inverted_int)[2:]

    # לוודא שהתוצאה עדיין באותו אורך ביטים (לחתוך אם ארוך מדי)
    return result.zfill(len(binary_num))[-len(binary_num):]

def main():
    num, bitsize = get_input()
    
    # שלב ההמרה לבינארי
    binary = decimal_to_binary(num, bitsize)
    print(f"Binary representation: {binary}")
    
    # החזרת המשלים לשתיים
    twos_comp = two_complement(binary)
    print(f"Two's complement (negative representation): {twos_comp}")

if __name__ == "__main__":
    main()
