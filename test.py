from model_lin_reg import regression_model

RESULTS = regression_model()

for i in range(len(RESULTS[0])):
    print(RESULTS[0][i],RESULTS[1][i])


