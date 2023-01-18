import seaborn as sns
import matplotlib.pyplot as plt

def optimumum_grid(x):
    i = 1
    
    def optimizer(x,i):
        j = x//i
        k = x%i
        return j, i, k
    
    j, i, k = optimizer(x,i)
    while j- i > k:
        i+=1
        k = x%i
        j, i, k = optimizer(x,i)
    if k == 0:
        return i, j
    else:
        return i, j+1

def outlier_treat(dataframe, column, i):
    upper_quartile = dataframe[column].quantile(i)
    dataframe = dataframe[dataframe[column] < upper_quartile]
    return dataframe

def outlier_graph(df, column, param):
    hori_cell, verti_cell = optimumum_grid(len(param))
    fig, axes = plt.subplots(hori_cell, verti_cell, figsize=(18, 10),constrained_layout = True)
    i = 0
    for j in range(hori_cell):
        for k in range(verti_cell):
            if i < len(param):
                dfg = outlier_treat(df, column, param[i]/100)
                sns.histplot(ax=axes[j, k], x = dfg[column],
                             kde=True).set(title = "Hist plot with {} outlier".format(param[i]/100))
                i+=1