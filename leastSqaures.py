import numpy as np
import pandas as pd

data=pd.read_csv('/content/IceCreamData.csv')

x=data['Temperature']
y=data['Revenue']

print(data)

def least_squares(x,y):
  n=len(x)
  mean_x=np.mean(x)
  mean_y=np.mean(y)
  numerator=np.sum((x-mean_x)*(y-mean_y))
  denominator=np.sum((x-mean_x)**2)

  slope=numerator/denominator
  intercept=mean_y-slope*mean_x
  return slope,intercept

slope,intercept=least_squares(x,y)
print(f"Slope:{slope}")
print(f"Intercept:{intercept}")
