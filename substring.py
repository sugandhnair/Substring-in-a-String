def count_substring(string, sub_string):
    lst = list()
    new_str = ''
    for i in range(0,len(string)):
        new_str += string[i]
    for i in range(0,len(sub_string)-1):
        new_str += ' '
    for i in range(0,len(string)):
        temp = ''
        for j in range(0,len(sub_string)):
            temp = temp + new_str[i+j]
        lst.append(temp)
    total = 0
    for i in lst:
        if i == sub_string:
            total += 1
    return total
    

string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)