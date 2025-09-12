import numpy as np

# Question 1
arr1 = np.arange(5, 26)
print(arr1)
arr2 = np.random.randint(10, 51, size=(3, 4))
print(arr2)

# Question 2
print(arr1.shape, arr1.size, arr1.dtype)
print(arr2.shape, arr2.size, arr2.dtype)

# Question 3
Array1 = np.array([2,4,6,8,10])
Array2 = np.array([1,3,5,7,9])
print(Array1 + Array2)
print(Array1 - Array2)
print(Array1 * Array2)
print(Array1 / Array2)

# Question 4
arr3 = np.arange(1, 10).reshape(3, 3)
print(arr3 * 5)

# Question 5
arr4 = np.arange(10, 26).reshape(4, 4)
print(arr4[1])
print(arr4[:, -1])
arr4[0] = 0
print(arr4)

# Question 6
arr5 = np.random.randint(20, 41, 10)
print(arr5[arr5 > 30])

# Question 7
arr6 = np.arange(11, 23)
print(arr6.reshape(3, 4))

# Question 8
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))
print(A.T)

# Question 9
arr7 = np.random.randint(10, 61, 15)
print(np.mean(arr7))
print(np.median(arr7))
print(np.std(arr7))

# Question 10
A10 = np.array([[2,1,3],[0,5,6],[7,8,9]])
print(np.linalg.det(A10))
print(np.linalg.inv(A10))
eigvals, eigvecs = np.linalg.eig(A10)
print(eigvals)
print(eigvecs)

# Question 11
robot_pos = np.array([[0,0],[2,3],[4,7],[7,10],[10,15]])
print(np.linalg.norm(robot_pos[-1] - robot_pos[0]))
print(np.sum(np.linalg.norm(np.diff(robot_pos, axis=0), axis=1)))