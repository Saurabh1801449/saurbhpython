import pandas as pd

a = [1,2,3,4]

sr = pd.Series(a)
print(sr)

# indexing 
print(sr[0])

# slicing
print(sr[0:2])

# sum
Total = sr.sum()
print(Total)