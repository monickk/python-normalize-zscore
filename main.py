import numpy as np
import pandas as pd
from scipy import stats
from normaliza import zscore

def main():
    np.set_printoptions(suppress=True, precision=4)
    # carrega os dados do arquivo
    dados = pd.read_csv('./dados2.csv', sep=',', skiprows=0, header=None, dtype=np.float32).values

    X = dados[:,0: -1]
    Y = dados[:, -1]
    
    m = np.size(X, 0)
    n = np.size(X, 1)

    print(zscore(X)); print("")

if __name__ == "__main__":
    main()