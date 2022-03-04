import numpy as np

if __name__ == '__main__':
    # x = np.array([1, 2, 3], dtype=np.int16)
    # print(x)
    # print(f'itemsize = {x.itemsize}')
    # print(f'x.dtype = {x.dtype}')
    # print(f'x.ndim = {x.ndim}')
    # print(f'x.size = {x.size}')

    # x = np.array([[1, 2, 3], [4, 5, 6]])
    # print(f'Dimesion = {x.ndim}\nShape = {x.shape}\nSize = {x.size}')
    # print(f'Content: \n{x}')

    # x = np.random.randint(10, 20)
    # print(x)
    # y = np.random.randint(1, 5, 10)
    # print(y)
    # z = np.random.randint(10, size=(3, 5))
    # print(z)

    # x = np.arange(0, 16, 1)
    # print(x)

    # y = np.arange(16)
    # print(y)
    # print(np.reshape(y, (-1, 8)))

    x = np.array([1, 2, 3])
    y = np.array([10, 20, 30])
    z= x * y
    print(f'{x}\n{y}\n{z}')