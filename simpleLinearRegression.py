def mean(values):
    return sum(values) / len(values)

def sl_regressor(x,y):
    n=len(x)
    mean_x=mean(x)
    mean_y=mean(y)
    numerator=sum((x[i]-mean_x)*(y[i]-mean_y) for i in range(n))
    denominator=sum((x[i]-mean_x)**2 for i in range(n))
    b1=numerator/denominator
    b0=mean_y-b1*mean_x

    print(f"Slope:{b1}")
    print(f"Intercept:{b0}")

    return b1,b0

x=list(map(float,input("Enter values for x:").split(',')))
y=list(map(float,input("Enter values for y:").split(',')))

print(f"x:{x}")
print(f"y:{y}")

b1,b0=sl_regressor(x,y)
print(f"Slope:{b1}")
print(f"Intercept:{b0}")
