import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr_1d)

arr_2d = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])

print("2D Array:\n", arr_2d)
print("Shape of 2D Array:", arr_2d.shape) 
print("Data type of Array:", arr_2d.dtype)  
print("Number of dimensions:", arr_2d.ndim)  
arr_sum = arr_1d + 5
print("Add 5 to each element:", arr_sum)
arr_mul = arr_1d * 2
print("Multiply each element by 2:", arr_mul)

#slicing in 1d arrays:
print("Elements from index 1 to 3:", arr_1d[1:4])  # [2, 3, 4]

# Indexing and Slicing In 2D arrays:

sliced_2d = arr_2d[:2, :3]
print("Sliced 2D Array:\n", sliced_2d)
print("Answer:",arr_2d[0:3,1:3])

print("Answer1:",arr_2d[:3,1:4])


# Accessing elements
print("First element of 1D array:", arr_1d[0])
print("Element at row 1, column 2 of 2D array:", arr_2d[1, 2])
print(arr_2d[0,0])


array_3d = np.array([[[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12]],
                      [[13, 14, 15, 16],
                       [17, 18, 19, 20],
                       [21, 22, 23, 24]]])

slice_0 = array_3d[0] 
print("First Slice:\n", slice_0)
print("Second Row of First Slice:\n",array_3d[0, 1] )

sub_array = array_3d[0, :2, :3]
print("Sub-array:\n", sub_array)

print("Shape of the 3d Array:",array_3d.shape)



