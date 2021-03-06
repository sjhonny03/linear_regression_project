from greyatomlib.linear_regression.q01_load_data.build import load_data
from greyatomlib.linear_regression.q02_data_splitter.build import data_splitter
from sklearn.linear_model import LinearRegression

dataframe = load_data('data/house_prices_multivariate.csv')
res = data_splitter(dataframe)
xinp=res[0]
yinp=res[1]

def linear_regression(x,y):
    regressor = LinearRegression()
    lm=regressor.fit(x, y)
    return lm
