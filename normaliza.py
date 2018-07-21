import numpy as np
import pandas as pd

####  Z = (X - µ) / σ   ####
def zscore(data):
    (rows, cols) = data.shape
    media = np.zeros(shape=(cols), dtype=np.float32)
    sigma = np.zeros(shape=(cols), dtype=np.float32)
    
    # calcula a média e o desvio padrão
    for j in range(cols):
        media[j] = np.mean(data[:,j])
        sigma[j] = data[:,j].std()

    # faz o cálculo e a distribuição na nova tabela de dados
    result = np.copy(data)
    for i in range(rows):
        for j in range(cols):
            result[i,j] = ((data[i,j] - media[j]) / sigma[j])
    
    # retorna o novo dataset
    return (result)

###  Z = [Xi - min(X)]/[max(X) - min(X)] ####
def maxmin(data):
    (rows, cols) = data.shape
    mins = np.zeros(shape=(cols), dtype=np.int32)
    maxs = np.zeros(shape=(cols), dtype=np.int32)
    for j in range(cols):
        mins[j] = np.min(data[:,j])
        maxs[j] = np.max(data[:,j])
        
    result = np.copy(data)
    for i in range(rows):
        for j in range(cols):
            result[i,j] = (data[i,j] - mins[j]) / (maxs[j] - mins[j])
    return (result)