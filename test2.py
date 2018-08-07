#from  default import spy_name,spy_age,spy
#print(spy_name)
#print(spy_age)
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)/2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found
item_list = [10,20,30,40,50,60,70]
item = input("Enter no. u want to search: ")
print(binary_search(item_list,item))
