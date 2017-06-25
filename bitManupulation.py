# def bitManupulation:

a = 1023
count = 0
while a:
	count = count + (a&1)
	a = (a>>1)
	# print a
	

# print count

arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
dict = {}
for elm in arr:
	if( elm in dict):
		dict[elm] += 1
	else:
		dict[elm] = 1

for key in dict:
	if(dict[key] == 1):
		print key
		

print dict	