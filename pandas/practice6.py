import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(5, 2), columns=["A", "B"])
print(df)
print(df["A"] < 0.5)

print(df[(df["A"] < 0.5) & (df["B"] > 0.3)])

print(df.query("A < 0.5 and B > 0.3"))
print("\n")


df = pd.DataFrame({
  'Animal' : ['Dog', 'Cat', 'Cat', 'Pig', 'Cat'],
  'Name' : ['Happy', 'Sam', 'Toby', 'Mini', 'Rocky']
})

print(df['Animal'].str.contains("Cat"))
print(df.Animal.str.match("Cat"))