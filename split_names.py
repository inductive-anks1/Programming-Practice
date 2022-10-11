def split_names(names):
    
    first_names = []
    last_names = []
    
    for i in range(0, len(names)):
        if len(names[i].split(' ')) == 1:
            first_names.append(names[i].split(' ')[0])
            last_names.append('')
        else:
            first_names.append(names[i].split(' ')[0])
            last_names.append(names[i].split(' ')[-1])
            
    return (first_names, last_names)

names = ['Betrtrand Russel', 'Kurt Godel', 'Peter Norvig', 'Srinivas Ramanujan', 'Kanad', 'Demosthenes']
first_names, last_names = split_names(names)
print(first_names)
print(last_names)


