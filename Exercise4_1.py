import pandas as pd
import matplotlib.pyplot as plt
from standardizer import standardizer

# Reading and Standardizing the file ==============================================================
df = pd.read_csv('data.csv')
df = standardizer(df)


# Mean and Median for Age, Weight =================================================================
mean_val = df[['Age', 'Weight']].mean()
median_val = df[['Age', 'Weight']].median()
print(f'MEAN =========\n{mean_val}\nMEDIAN =======\n{median_val}')


# Mode for Height, Gender, Education ==============================================================
mode_val = df[['Height', 'Gender', 'Education']].mode().iloc[0]
print(f'MODE ================\n{mode_val}')


# Range for Age, Height, Weight ===================================================================
range_val = df[['Age', 'Height', 'Weight']].max() - df[['Age', 'Height', 'Weight']].min()
print(f'RANGE ======\n{range_val}')


# Variance and Standard Deviation for Age, Height, Weight =========================================
var_val = df[['Age', 'Height', 'Weight']].var()
std_dev_val = df[['Age', 'Height', 'Weight']].std()
print(f'VARIANCE ======\n{var_val}')
print(f'STD-DEV ===========\n{std_dev_val}')


# Quartiles for Age, Height, Weight ===============================================================
quantiles = df[['Age', 'Height', 'Weight']].quantile([0.25, 0.5, 0.75])
quantiles.index = ['Q1', 'Q2', 'Q3']
print(f'QUANTILES ==============\n{quantiles}')


# IQR for Age, Height, Weight =====================================================================
quantiles = df[['Age', 'Height', 'Weight']].quantile([0.25, 0.5, 0.75])
quantiles.index = ['Q1', 'Q2', 'Q3']
iqr = quantiles.loc['Q3'] - quantiles.loc['Q1']
print(f'IQR ==========\n{iqr}')


# CHARTS ==========================================================================================
income_cols = ['January income', 'February income', 'March income', 'April income', 'May income', 'June income', 'July income', 'August income', 'September income', 'October income', 'November income', 'December income']
mean_incomes = df[income_cols].mean(axis=1)
df['Average Income'] = df[income_cols].mean(axis=1)
# print(df[['Name', 'Average Income']])

# Bar Chart -----------------------------------------------
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['Average Income'], color='blue')
plt.title('میانگین درآمد هر فرد')
plt.xlabel('نام')
plt.ylabel('میانگین درآمد')
plt.show()

# Plot Chart ----------------------------------------------
months_names = [col.split()[0] for col in income_cols]

for index, row in df.iterrows():
    plt.plot(months_names, row[income_cols], marker='o', label=row['Name'])

plt.title('روند تغییر درآمد هر فرد در ۱۲ ماه سال')
plt.xlabel('ماه‌های سال')
plt.ylabel('میزان درآمد')
plt.xticks(rotation=45)
plt.legend(title="افراد")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
