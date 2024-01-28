#1.فراخوانی کتابخانه های مورد نظر
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



#2.	خواندن dataset درون یک data frame
file_path = 'glass.csv'  
df = pd.read_csv(file_path)

#3.	استخراج اطلاعات dataset از قبیل سایز، تعداد و نام ستونها، ستونهای دارای missed value.
# data_size = df.shape
# print(num_columns = df.shape[1])
# print(column_names = df.columns.tolist())
# print( missing_values = df.isnull().sum())
# print(df.info())
# print(df.shape)
# print(df.columns)


# 4.	بررسی رکوردهای دارای فیلدهای خالی
mis_val = df.isnull().sum()
print(mis_val[mis_val > 0])
print(df.describe())
print(df.isnull().sum())


# 5.	بررسی رکوردهای دارای فیلدهای دارای دیتا با فرمت اشتباه
# 6.	بررسی رکوردهای دارای فیلدهای دارای دیتای اشتباه
df_cleaned = df.dropna()
# print(df_cleaned)
string_rows = df.applymap(lambda x: isinstance(x, str))
df_string_data = df[string_rows.any(axis=1)]
# print(df_string_data)

# 7.	بررسی رکوردهای دارای فیلدهای دارای دیتای پر
# 8.	جایگزینی فیلدهای خالی با مقدار میانگین
# 9.	تصحیح فیلدهای دارای دیتا با فرمت اشتباه
# 10.	تصحیح فیلدهای دارای دیتای اشتباه
# 11.	تصحیح فیلدهای دارای دیتای پرت(جایگزینی با مقدار میانه)
for column in df_string_data.columns:
    for index, value in df_string_data[column].items():
        if isinstance(value, (int, float)):
            print(f"Column: {column}, Row {index}: {value}")



numeric_df = df.apply(pd.to_numeric, errors='coerce')
# print(numeric_df)

for column in df.columns:
    median_value = numeric_df[column].median()
    print(f"column = {column}, median_value = {median_value}")
    df[column] = numeric_df[column][numeric_df[column] <= median_value]

column_means = df.mean()
df_clean_non = df.apply(lambda col: col.fillna(column_means[col.name]))
print(df_clean_non)

# 12.	حذف رکوردهای دارای بیش از 3 فیلد خالی
df = df.dropna(thresh=df.shape[1]-3)

# 13.	(اختیاری با امتیاز اضافه)نمایش اطلاعات دیتاست در یک نمودار دلخواه

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()

