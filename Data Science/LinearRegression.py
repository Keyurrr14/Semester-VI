import pandas as pd

def linear_regression(df, x):
    n = df.shape[0]
    df['x^2'] = df['x'] * df['x']
    df['xy'] = df['x'] * df['y']
    df.loc['total'] = df.sum()
    
    xbar = df['x']['total'] / n
    ybar = df['y']['total'] / n
    xsquarebar = df['x^2']['total'] / n
    xybar = df['xy']['total'] / n
    
    a1 = (xybar - (xbar * ybar)) / (xsquarebar - (xbar * xbar))
    a0 = ybar - (a1 * xbar)
    y = a0 + (a1 * x)
    return y

data = [[0, 2], [1, 3], [2, 5], [3, 4], [4, 6]]
columns = ['x', 'y']
index = ['A', 'B', 'C', 'D', 'E']
df = pd.DataFrame(data=data, columns=columns, index=index)
x = 10
y = linear_regression(df, x)
print(df)
print(f"\nValue of x: {x}")
print(f"Value of y: {y}")