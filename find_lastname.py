def find_lastname(first_name, names):
    
    first_name_list = []
    
    for i in range(len(names)):
        first_name_list.append(names[i].split(' ')[0])
        
    if first_name not in first_name_list:
        return (None)
    
    else:
        for i in range(len(first_name_list)):
            if first_name_list[i] == first_name:
                if len(names[i].split(' ')) >= 2:
                    return(names[i].split(' ')[-1])
                elif len(names[i].split(' ')) == 1:
                    return('')
        
##names = ['Betrtrand Russel', 'Kurt Godel', 'Peter Norvig', 'Srinivas Ramanujan', 'Kanad', 'Demosthenes']
##first_name = 'Kanad'

##print(find_lastname(names, first_name))