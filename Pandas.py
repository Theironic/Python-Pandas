import pandas as pd
# exemplo de daata frame usando a biblioteca pandas do python


datatest = {
    'nome': ['joao','maria','jose'],
    'idade': [14,20,38],
    'pais': ['brazil','portugal','angola']
}

#dataframe

dataframe = pd.DataFrame(datatest)

dataframe