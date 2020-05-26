f = open("input.txt", "r")
f_out = open ("ouput.txt", "w")

file_content = f.read()

count_a = 0

for i in file_content:
	if (i == 'a') or (i == 'A'):
		count_a = count_a + 1; 
        
f_out.write("A or a: ")
f_out.write(str(count_a))

f.close()
f_out.close()