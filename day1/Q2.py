
file_path = 'Q2.txt'

with open(file_path, 'r') as file:
    file_contents = file.read()

lines = file_contents.split('\n')


res = []
digits = []
for str_ in lines :
    each_res = []
    words = { "one" : 1 , "two" : 2 , "three" : 3 , "four" : 4 , "five" : 5 , "six" : 6 , "seven" : 7 , "eight" : 8 , "nine" : 9 } 

    for index, letter in enumerate(str_):
        for num, value in words.items():
            if str_[index:].startswith(num):
                str_ = str_[:index] + str(value) + str_[index + 1:]
    
    print(str_)
    each_line_digits = []
    for line in str_ :
        if line.isdigit() : 
            each_line_digits.append(line)
    digits.append(each_line_digits)        

print(digits)
summation = 0
for i in digits :
    whole_num = str(i[0]) + str(i[-1])
    summation += int(whole_num)

print(summation)
                

# if key in i :
#     ind = i.find(key)
#     remind.append(ind)
#     if (ind,value) not in each_res :
#         each_res.append((ind,value))

# if str(value) in i :
#     ind = i.find(str(value))
#     remind.append(ind)
#     if (ind,value) not in each_res :
#         each_res.append((ind,value))

# for k in remind :
        #     i = list(i)
        #     i[int(k)] = " "
        #     i = ''.join(i)
