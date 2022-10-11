string = "ankit008"
stack = []
a = list(string)
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in string:
    
    if i == '0':
        continue
    
    elif i in digits:
        stack.append(i)
        a.remove(i)
        
number = int(''.join(stack))
new_num = (number + 1)
a.append(str(new_num))
new_string = (''.join(a))
print(new_string)

        