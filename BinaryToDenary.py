# Binary to Denary convertor
# @author: Junzhong Loo
# 19/5/2021

def main():
    user_input = input("Type in binary number: ")
    number_of_digits = list(user_input)
    length = len(number_of_digits)
    denary = 0
    for i in range(length):
        denary += int(number_of_digits[i]) * 2**(length-1)
        length -= 1
    
    print("Binary:", user_input)
    print("Denary:", denary)


if __name__ == "__main__":
    main()