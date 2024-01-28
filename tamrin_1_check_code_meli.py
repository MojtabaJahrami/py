def check_code_meli(code):
    L = len(code)
  
    if L < 8 or int(code) == 0: 
        return False
    code = ('0000' + code)[-10:]
    if int(code[3:9]) == 0: 
        return False
    c = int(code[9])
    s = sum([int(code[i]) * (10 - i) for i in range(9)]) % 11
    return (s < 2 and c == s) or (s >= 2 and c == (11 - s))

code = input("add code:")
print(check_code_meli(code))
