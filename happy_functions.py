import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def adjusted_r_squared(r_squared, X):
    '''
        function calculates the adjusted r_squared for more than one feature
    '''
    adjusted_r2 = 1 - ((1 - r_squared) * (len(X) - 1) / (len(X) - X.shape[1] - 1))
    return adjusted_r2 


def train_model(ModelClass, X_train, Y_train, **kwargs):
    '''
        function trains a model with Train data and gives back this model
    '''
    model = ModelClass(**kwargs)
    model.fit(X_train, Y_train)

    return model

def scatter_mae_train_test_data(df_name):
    '''
        function shows a seaborn scatterplot from a special data frame 
        with mean absolute error from train and test data 
    '''
    sns.set_style('whitegrid', {'grid.linestyle': '--'})
    g = sns.scatterplot(data = df_name, x = 'model_name', y = 'test_mae', color = 'green')
    g = sns.scatterplot(data = df_name, x = 'model_name', y = 'train_mae', marker='+', color = 'green')
    g.set_xticklabels(g.get_xticklabels(), rotation=90)
    g.set(title = 'mean absolute error')
    g.legend(loc='upper right', labels=['test_mae', 'train_mae'] )
    plt.show();

