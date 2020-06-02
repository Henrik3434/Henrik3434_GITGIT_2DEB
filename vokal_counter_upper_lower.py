f = open("input.txt", "r")
f_out = open ("output.txt", "w")
file_content = f.read()

vokal_array = ['a', 'e', 'i', 'o', 'u', 'y']
n = len(vokal_array)
telle_array = [0]*n

for i in file_content:
    index = 0
    for k in vokal_array:
        if (i.lower() == k) :
            telle_array[index] = telle_array{index] + 1 
        index = index + 1

index = 0
for k in vokal_array:
    f_out.write(k)
    f_out.write(": ")
    f_out.write(str(telle_array[index]))
    f_out.write("\n")
    index = index + 1

f.close()
f_out.close()
print("Successful")