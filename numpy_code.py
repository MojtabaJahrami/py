import numpy as np

# تعداد ابعاد آرایه
arr = np.array([1, 2, 3, 4, 5])
print(arr.ndim)

# کپی کردن آرایه
arr_copy = arr.copy()

# ایجاد یک view از آرایه
arr_view = arr.view()

# ابعاد آرایه
arr_shape = arr.shape

# تغییر ابعاد آرایه
arr_reshape = arr.reshape(5, 1)

# ایتریت کردن روی آرایه
for x in np.nditer(arr):
  print(x)

# ایتریت کردن روی آرایه با شمارش اندیس ها
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# ادغام دو آرایه
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_concat = np.concatenate((arr1, arr2))

# ادغام دو آرایه در یک محور خاص
arr_concat_axis = np.concatenate((arr1, arr2), axis=1)

# تقسیم یک آرایه به n بخش
arr_split = np.array_split(arr, 2)

# جستجوی مقدار x در آرایه
x = 3
arr_where = np.where(arr == x)

# جستجوی مقادیری که بر 2 بخش پذیر هستند
arr_where_mod = np.where(arr%2 == 0)

# مرتب کردن آرایه
arr_sort = np.sort(arr)
