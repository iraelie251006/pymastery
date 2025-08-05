import pandas as pd
# [[30, 21]], columns=['Apples', 'Bananas']
dataset = {'Apples': [30], 'Bananas': [21]}
fruits = pd.DataFrame(dataset)

print(fruits)