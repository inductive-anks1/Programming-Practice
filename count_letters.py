def count_letters(mystr):
    import re
    new_str = re.findall("[a-zA-Z]", mystr)
    return (len(new_str))

