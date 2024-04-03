import pandas as pd
import random
'''
Урок 10. Построение графиков
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''
#генерация data
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(pd.get_dummies(data['whoAmI']))
#генерация onehot data
unique_values = data['whoAmI'].unique()
out_data = pd.DataFrame(0, index = data.index, columns = unique_values)
for value in unique_values:
    out_data.loc[data['whoAmI'] == value, value] = 1
print(out_data)
