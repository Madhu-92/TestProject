s = str(input())
char = ''
temp=''
found=''
for letter in s:
	if letter >= char:
		temp+= letter
	else:
		temp=letter
	if len(temp) > len(found):
		found = temp
	char = letter
print(found)
