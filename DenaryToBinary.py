# Denary to Binary program
# @author: Junzhong Loo
# 19/5/2021

import math

def main():
    BASE = 2

    user_input = int(input("Type denary number:"))
    
    # b**c = a 
    # c = math.log(a,b), b = base
    max_binary_bits = math.ceil(math.log(user_input, BASE))   
    remaining = user_input - BASE**(max_binary_bits - 1) 
    arr = [1]
    max_binary_bits -= 1
       
    while max_binary_bits > 0:
        if (remaining - BASE**(max_binary_bits - 1)) >= 0:
            arr.append(1)
            remaining -= BASE**(max_binary_bits - 1)

        else: 
            arr.append(0)

        max_binary_bits -= 1

    binary = ''.join(map(str,arr))

    print("Denary:", user_input)
    print("Binary:", binary)

if __name__ == "__main__":
    main() 

