def isValid(test_string):
    
    par_dict = {'(' : ')'}
    stack = []
    
    for char in test_string:
        
        if char in par_dict.keys():
            stack.append(char)
        elif char in par_dict.values():
            if stack == []:
                return False
            a = stack.pop()
            if char != par_dict[a]:
                return False
    return stack == []

print(isValid('hi(hi)()'))