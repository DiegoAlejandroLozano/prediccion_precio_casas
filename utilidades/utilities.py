from sklearn.metrics import r2_score, mean_squared_error
from math import sqrt

def evaluar_modelo(modelo, x_train, x_test, y_train,y_test)->None:
    y_pred_train = modelo.predict(X=x_train)
    y_pred_test = modelo.predict(X=x_test)

    r2_sc_train = r2_score(y_true=y_train, y_pred=y_pred_train)
    r2_sc_test = r2_score(y_true=y_test, y_pred=y_pred_test)

    RMSR_train = sqrt(mean_squared_error(y_true=y_train, y_pred=y_pred_train))
    RMSR_test = sqrt(mean_squared_error(y_true=y_test, y_pred=y_pred_test))

    print("R^2 train: {}".format(r2_sc_train))
    print("R^2 test: {}".format(r2_sc_test))

    print("\nRMSR train: {}".format(RMSR_train))
    print("RMSR test: {}".format(RMSR_test))
