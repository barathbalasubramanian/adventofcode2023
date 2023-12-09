
file_path = 'q1.txt'

with open(file_path, 'r') as file:
    file_contents = file.read()

lines = file_contents.split('\n')


digits = []
for lines in lines :
    each_line_digits = []
    for line in lines :
        if line.isdigit() : 
            each_line_digits.append(line)
    digits.append(each_line_digits)

summation , res = 0 , 0
for index , digits in enumerate(digits) :
    print(digits , index)
    print(int(digits[0]) , int(digits[-1]))
    print()
    summation = int(str(digits[0]) + str(digits[-1]))
    
    res += summation
    
print(res)