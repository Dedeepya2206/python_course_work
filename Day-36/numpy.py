import numpy as np
arr1=np.array([1,2,3,4,5])
print("1-dim",arr1,sep='\n',end='\n\n')

import numpy as np
arr2=np.array ([[1,2,3,4,5],[6,7,8,9,0]])
print("mult",arr2,sep='\n',end='\n\n')

import numpy as np
arr3=np.array([[[1,2,3,4,5],[6,7,8,9,0]],[[5,8,9,0,6],[1,7,0,8,8]]])
print("multi-dim",arr3,sep='\n')

zeros=np.zeros((3,3))
print(zeros)
ones=np.ones((3,3))
print(ones)
identity=np.eye(4)
print(identity)
arr=np.full((10,2),20)
print(arr)

import numpy as np
range_arr=np.arange(2,51,2) #genertae numbers in a range
print(range_arr)


lin_space=np.linspace(0,100,5) #divide it into equal parts
print(lin_space)

np.random.seed(40)
rand_arr=np.random.randint(100)
print(rand_arr)

rand_float=np.random.rand()
print(rand_float)

rand_float=np.random.rand(4)
print(rand_float)

rand_int=np.random.randint(1,6,(4,3))
print(rand_int)

rand_int=np.random.randint(1,6,8)
print(rand_int)

l=['html','css','javascript','python','mysql']
rand_choice=np.random.choice(l, 2)
print(rand_choice)

arr=np.array([[1,2],[4,5],[6,7],[8,7],[1,2],[4,5]])
print(arr.shape)

reshaped=arr.reshape(3,4)
print(reshaped)

a=np.array([[1,2,3,4],[1,2,3,4]])
flattend=a.flatten()
print(flattend)

transposed=arr.T
print(transposed)

arr=np.array([10,20,30,40,50])
print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[:3])
print(arr[::2])

import numpy as np
matrix=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(matrix[0:3,1])
print(matrix[1:3,2])
print(matrix[0:2,0:2])
print(matrix[1:3,1:3])


arr=np.array([4,9,16,25,36])

print(arr+10)
print(arr*2)
print(arr**0.5)

print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))

a=np.array([1,2,3,4,5])
print(np.mean(a))
print(np.var(a))
print(np.std(a))

arr=np.array([1,2,3,4,5])
print(np.cumsum(arr))
print(np.cumprod(arr))

arr=np.array([1,2,3,4,5,6,7,8,8,3])
print(arr%2==0)
print(arr[arr%2!=0])


arr=np.array([3,1,4,5,9,2,6])
sorted_arr=np.sort(arr)
print(sorted_arr)

unique_vals=np.unique(arr)
print(unique_vals)

arr=np.array([10,20,30])
view_arr=arr.view()
view_arr[0]=100
print(arr,view_arr)

copy_arr=arr.copy()
copy_arr[0]=200
print(arr,copy_arr)

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.dot(a,b))

print(np.linalg.det(a))

print(np.linalg.inv(a))

eigenvalues,eigenvectors=np.linalg.eig(a)
print(eigenvalues)

print(eigenvectors)

c=np.array([5,11])
sol=np.linalg.solve(a,c)
print(sol)

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
v_s=np.vstack((a,b))
h_s=np.hstack((a,b))
print(v_s)
print(h_s)

split_arr=np.split(np.array([1,2,3,4,5,6]),3)
print(split_arr)

