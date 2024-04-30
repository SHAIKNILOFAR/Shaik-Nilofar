def determinant(matrix):
	if len(matrix)!=2 or len(matrix[1])!=2:
		raise ValueError("input matrix must be a 2*2 matrix")
matrix_2=[[1,2],[3,4]]
result=determinant(matrix_2)
print("determinant of 2*2matrix",result)

