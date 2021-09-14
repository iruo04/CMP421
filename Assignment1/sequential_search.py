def search (list1,key):
	list2 = [ ]
	flag = False  
	for i in range(len(list)):
		if key == list1[i]:
			flag = True
			list2.append(i)
			
			
	if flag == True:
		print('element is found')
		for i in list2:
			print(i)
			
	else:
		print('key is not found')

list1 = [ 34, 23,5,6,7,1,23,8]
print(list1 )
key = int (input("enter the key element: "))
search (list1,key)
