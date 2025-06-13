#Write a algorithm to accept an integer array (two dimensional) as the parameter and find the min, max, each row, column min and max elements of the given array.
def find_min_max(arr):
    #Find the max and min of the array
	max_value = float('-inf')
	min_value = float('inf')
	row_max = []
	row_min = []
	col_max = []
	col_min = []

	for i in range(len(arr)):
		row_max.append(max(arr[i]))
		row_min.append(min(arr[i]))

		for j in range(len(arr[i])):
			if arr[i][j] > max_value:
				max_value = arr[i][j]
			if arr[i][j] < min_value:
				min_value = arr[i][j]

	# Find column-wise max and min
	for j in range(len(arr[0])):
		col_values = [arr[i][j] for i in range(len(arr))]
		col_max.append(max(col_values))
		col_min.append(min(col_values))

	return {
		'Max': max_value,
		'Min': min_value,
		'Row Wise Max': row_max,
		'Row Wise Min': row_min,
		'Col Wise Max': col_max,
		'Col Wise Min': col_min
	}

arr = [[0, 1, 2, 3],
	  [3, 4, 5, 5],
	  [6, 7, 8, 8],
	  [9, 0, 1, 9]]
result = find_min_max(arr)
print("Max:", result['Max'])
print("Min:", result['Min'])
print("Row Wise Max:", result['Row Wise Max'])
print("Row Wise Min:", result['Row Wise Min'])
print("Col Wise Max:", result['Col Wise Max'])
print("Col Wise Min:", result['Col Wise Min'])