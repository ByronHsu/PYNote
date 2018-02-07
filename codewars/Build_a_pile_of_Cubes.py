def find_nb(m):
    # your code
    sum = 0
    i = 0
    while(True):
    	sum += i ** 3
    	if(sum == m):
    		return i
    	if(sum > m):
    		return -1
    	i = i + 1

print(find_nb(1071225))
