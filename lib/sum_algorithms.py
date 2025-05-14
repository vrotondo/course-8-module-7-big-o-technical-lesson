"""
Algorithms for summing lists with different time complexities.
"""

def sum_list(numbers):
	total = 0
	for num in numbers:
    	total += num
	return total

def sum_list_nested(numbers):
	total = 0
	count = 0  # Count iterations
    
	for i in range(len(numbers)):
    	total += numbers[i]
    	for j in range(len(numbers)):
        	count += 1  # Increment every inner loop iteration
       	 
	print(f"Total iterations for nested loops: {count}")
	return total
