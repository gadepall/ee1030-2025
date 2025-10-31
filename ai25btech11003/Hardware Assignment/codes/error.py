import numpy as np
import pandas as pd


#Loading Data
data = pd.read_csv("../data/test.csv")
V = data["V"]
T_pt = data["T_pt"]
T = data["T"]

#Calculating Mean Absolute Error(M.A.E)
E1 = (T_pt-T).abs().mean()
print("M.A.E =", E1)

#Calculating Root Mean Square Error(RMSE)
E2 = np.sqrt(((T_pt-T)**2).mean())

print("RMSE =", E2)

#Calculating Max Error
E3 = abs(T_pt-T).max()

print("Max Error =", E3)
