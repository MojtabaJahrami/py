#بخش اول
دستور نصب در سیستم 
pip install pandas

import pandas as pd

# ساخت دیتافریم
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# اضافه کردن یک ردیف جدید به دیتافریم
df = df.append({'A': 4, 'B': 5, 'C': 6}, ignore_index=True)

# تغییر نوع داده‌های یک ستون
df['A'] = df['A'].astype(float)

# تغییر نام ستون‌ها
df.columns = ['X', 'Y', 'Z']

# مقایسه دو دیتافریم و بازگرداندن تفاوت‌ها
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 10]})
df_diff = df1.compare(df2)

# کپی کردن دیتافریم
df_copy = df.copy()

# نمایش آماری از دیتافریم
df.describe()

# حذف یک ستون
df = df.drop('X', axis=1)

# حذف ردیف‌های تکراری
df = df.drop_duplicates()

# حذف ردیف‌هایی که دارای مقدار NaN هستند
df = df.dropna()

# بازگرداندن ردیف‌های تکراری
df[df.duplicated()]

# جایگزینی مقادیر NaN با یک مقدار خاص
df.fillna(0)

# نمایش چند ردیف اول دیتافریم
df.head()

# نمایش اطلاعات دیتافریم
df.info()

# ادغام دو دیتافریم بر اساس یک ستون مشترک
df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': [1, 2, 3, 4]})
df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value': [5, 6, 7, 8]})
df3 = pd.merge(df1, df2, on='key')

# محاسبه ماکسیمم یک ستون
df['Y'].max()

# محاسبه میانگین یک ستون
df['Y'].mean()

# محاسبه مد یک ستون
df['Y'].median()

# نمایش ابعاد دیتافریم
df.shape

# فیلتر کردن دیتافریم بر اساس یک شرط
df[df['Y'] > 3]







#بخش دوم
import pandas as pd
# Students Table
student_info = {
"Name": ['Amin', 'Ali', 'Reza', 'Zohre', 'Fateme', 'Sara'],
"Age": [19,       22,       33,    44,     55,      66],
"Ins":['BSc', 'BSc','BSc','MSc','BSc','BSc',],
"GPA":[11,12,13,14,15,16]
}

students_df = pd.DataFrame(student_info)

print(students_df)
print(students_df.info())
print("*" * 50)

print(students_df.head(3))
print("*" * 60)
print(students_df.tail(3))
