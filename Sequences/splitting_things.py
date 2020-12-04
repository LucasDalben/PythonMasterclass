panagram = "The quick brown fox jumps over the lazy dog"

print(panagram.split())

numbers =  "934, 198, 82, 824, 2948, 193"
new_numbers = numbers.split(',')
print(new_numbers)

#values = "".join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '3', '2', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '9', '2', ' ',
                  '1', '9', '7', ' ']
values = "".join(generated_list)
print(values)                 

values_list = values.split()

for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(values_list)    

integer_values = []
for value in values_list:
    integer_values.append(int(value))

print(integer_values)    