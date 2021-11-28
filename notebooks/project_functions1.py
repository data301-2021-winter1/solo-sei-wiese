def load_and_process():
    import numpy as np
    import pandas as pd
    from pandas import DataFrame, Series
    import matplotlib.pyplot as plt
    import seaborn as sns

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    
    df_AfricanDevelopment_mc = pd.read_csv('../data/raw/AfricanDevelopment.csv').dropna().to_csv("../data/processed/df_AfricanDevelopment.cs")
    
    
    missing_columns = ['10/50 Ratio', 'Pop', 'Unnamed: 12']
    df_country_variables_mc = pd.read_csv('../data/raw/cpi_variable_data/country_variable.csv', header=1).drop(missing_columns, axis=1, inplace=True)

    df_country_variables = df_country_variables[df_country_variables['Variable'].astype(str).str.isdecimal()]
    df_country_variables.to_csv("../data/processed/df_country_variables.csv")
    
    
    df_data = pd.read_csv('../data/raw/archive/data.csv')
    df_data = df_data.replace(['-'], np.nan)
    df_data_f = df_data.astype({'1998': 'float64', '1999': 'float64', 
                                '2000': 'float64', '2001': 'float64', 
                                '2002': 'float64', '2003': 'float64', 
                                '2004': 'float64', '2005': 'float64', 
                                '2006': 'float64', '2007': 'float64', 
                                '2008': 'float64', '2009': 'float64', 
                                '2010': 'float64', '2011': 'float64', 
                                '2012': 'float64', '2013': 'float64', 
                                '2014': 'float64', '2015': 'float64', })

    df_data_f['2012'] =  df_data_f.apply(lambda x : (x['2012'] /10), axis=1)
    df_data_f['2013'] =  df_data_f.apply(lambda x : (x['2013'] /10), axis=1)
    df_data_f['2014'] =  df_data_f.apply(lambda x : (x['2014'] /10), axis=1)
    df_data_f['2015'] =  df_data_f.apply(lambda x : (x['2015'] /10), axis=1)

    df_data_f_float_only = df_data_f[df_data_f.columns[df_data_f.columns != 'Jurisdiction']]


    df_data_f_float_only.to_csv("../data/processed/df_data_f_float_only.csv")
    
def AfDev_plot():
    import numpy as np
    import pandas as pd
    from pandas import DataFrame, Series
    import matplotlib.pyplot as plt
    import seaborn as sns

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    
    df_AfricanDevelopment = pd.read_csv('../data/raw/AfricanDevelopment.csv')

    pop_and_hdi = sns.scatterplot(x='humanDevelopmentIndex', y='pop2021', data=df_AfricanDevelopment)
    pop_and_hdi.set(title = "The Correlation between Population of 2021 and HDI")
    pop_and_hdi
    
    pop_and_hdi_REG = sns.regplot(x='humanDevelopmentIndex', y='pop2021', data=df_AfricanDevelopment)
    pop_and_hdi_REG.set(title = "The Correlation between Population of 2021 and HDI")
    pop_and_hdi_REG
    

def AfDev_sort():
    import numpy as np
    import pandas as pd
    from pandas import DataFrame, Series
    import matplotlib.pyplot as plt
    import seaborn as sns

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    df_AfricanDevelopment_SORTED_by_HDI = df_AfricanDevelopment.sort_values('humanDevelopmentIndex', ascending=False).to_csv("../data/processed/df_AfricanDevelopment_SORTED_by_HDI.csv")
    

def cpi_nigeria():
    import numpy as np
    import pandas as pd
    from pandas import DataFrame, Series
    import matplotlib.pyplot as plt
    import seaborn as sns

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    missing_columns_nigeria = ['CPI', '10/50 Ratio', 'Pop', 'Unnamed: 12']
    
    df_cpi_nigeria =pd.read_csv('../data/raw/00cpi_xxxx/cpi_nigeria.csv',header=1).drop(missing_columns_nigeria, axis=1, inplace=True).dropna()

def cpi_congo():
    import numpy as np
    import pandas as pd
    from pandas import DataFrame, Series
    import matplotlib.pyplot as plt
    import seaborn as sns

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    missing_columns_congo = ['CPI', '10/50 Ratio', 'Pop', 'Unnamed: 12']
    
    df_cpi_congo =pd.read_csv('../data/raw/00cpi_xxxx/cpi_congo.csv',header=1).drop(missing_columns_congo, axis=1, inplace=True).dropna()


def cpi_mauritius(fnc):
    import numpy as np
    import pandas as pd
    from pandas import DataFrame, Series
    import matplotlib.pyplot as plt
    import seaborn as sns

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
        
    missing_columns_mauritius = ['CPI', '10/50 Ratio', 'Pop', 'Unnamed: 12']
    
    fnc =pd.read_csv('../data/raw/00cpi_xxxx/cpi_mauritius.csv',header=1)
    return fnc

def my_sum(x,y):
    z = x + y
    return z