def decodeString(s):
    repeat_str = []
    num = ''
    decoded_str = ''        

    for i in range(len(s)):
        if s[i] == '{' or s[i] == ')':
            continue
            
        if s[i].isdigit():
            num += s[i] 
            
        elif s[i] == '}':
            decoded_str = repeat_str.pop() + (decoded_str * int(num))
            num = ''
            
        elif s[i] == '(':
            repeat_str.append(decoded_str)
            decoded_str = ''

        else:
            decoded_str += s[i]            

    return decoded_str
    
decodeString("(a(c){31}){5}")