import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from math import log

# Generate sample data
x = np.arange(1, 11)
y = np.array([1, 3, 8, 15, 28, 45, 66, 91, 120, 153])

# Fit a linear regression model
lr_model = LinearRegression()
lr_model.fit(x.reshape(-1, 1), y)

# Fit an exponential model
exp_model = Pipeline([('poly', PolynomialFeatures(degree=2)), ('linear', LinearRegression(fit_intercept=False))])
exp_model.fit(np.array(x).reshape(-1, 1), np.log(y))

# Fit a logarithmic model
log_model = Pipeline([('poly', PolynomialFeatures(degree=1)), ('linear', LinearRegression())])
log_model.fit(np.log(np.array(x)).reshape(-1, 1), y)

# Plot the data and models
plt.scatter(x, y)
plt.plot(x, lr_model.predict(x.reshape(-1, 1)), label='Linear')
plt.plot(x, np.exp(exp_model.predict(np.array(x).reshape(-1, 1))), label='Exponential')
plt.plot(x, log_model.predict(np.log(np.array(x)).reshape(-1, 1)), label='Logarithmic')
plt.legend()
plt.show()

# Evaluate the models using R-squared
print("Linear R-squared:", r2_score(y, lr_model.predict(x.reshape(-1, 1))))
print("Exponential R-squared:", r2_score(y, np.exp(exp_model.predict(np.array(x).reshape(-1, 1))))) 
print("Logarithmic R-squared:", r2_score(y, log_model.predict(np.log(np.array(x)).reshape(-1, 1))))

