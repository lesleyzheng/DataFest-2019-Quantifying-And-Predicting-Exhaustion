import pickle
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_log_error

class modelSelection(object):

    def __init__(self):

        self.X_tr = None
        self.y_tr = None
        self.X_valid = None
        self.y_valid = None

    def start(self):

        #load in
        pickle_in = open("./data/data_v1.pkl", "rb") #v1
        (info, X, y), desc = pickle.load(pickle_in) #info
        print(desc)
        print("loading of v2 complete")

        print(X)

        #preprocess
        X = np.array(self.scaleMatrix(X))
        y = np.array(y)

        #shuffle
        rs = np.random.RandomState(seed=1234)
        inds = [i for i in range(len(y))]
        rs.shuffle(inds)
        X = X[inds,:]
        y = y[inds]

        num_points = len(y)
        print(num_points)

        #delegate data
        num_train = int(num_points*0.8)
        self.X_tr = X[:num_train]
        self.y_tr = y[:num_train]
        self.X_valid = X[num_train:num_points]
        self.y_valid = y[num_train:num_points]

        #check data
        # print(np.where(np.isnan(X)))
        # print(X[14][5])

        #model fitting

        # Decision Tree Grid Search
        print("Random Forest Grid Search")
        x_train_predicts, x_test_predicts = self.runGridSearch_dt()
        self.error(x_train_predicts, x_test_predicts)

        # kNN Grid Search
        print("kNN Grid Search")
        x_train_predicts, x_test_predicts = self.runGridSearch_knn()
        self.error(x_train_predicts, x_test_predicts)

        # Random Forest Grid Search
        print("Random Forest GS")
        x_train_predicts, x_test_predicts = self.runGridSearch_random_forest()
        self.error(x_train_predicts, x_test_predicts)

        # Gradient Boosting Regressor
        print("Gradient Boosting Regressor")
        x_train_predicts, x_test_predicts = self.gradient_boosting_regressor()
        self.error(x_train_predicts, x_test_predicts)

        # Linear Regression
        print("Linear Regression")
        x_train_predicts, x_test_predicts = self.linear_regression()
        self.error(x_train_predicts, x_test_predicts)

        print("completo!")

    def scaleMatrix(self, matrix):
        scaler = StandardScaler()
        scaler.fit(matrix)
        matrix_s = scaler.transform(matrix)
        return matrix_s

    def runGridSearch_dt(self):

        params = [{'splitter': ['best', 'random'], 'max_depth': [None, 1, 3, 5, 7, 9, 11]}]

        learner = DecisionTreeRegressor()
        gs = GridSearchCV(learner, params, 'explained_variance', cv=3, n_jobs=15)
        gs.fit(self.X_tr, self.y_tr)

        print("The best parameters for latitude were: ")
        print(gs.best_params_)
        print(gs.get_params())

        # means = gs.cv_results_['mean_test_score']
        # stds = gs.cv_results_['std_test_score']
        # for mean, std, params in zip(means, stds, gs.cv_results_['params']):
        #     print("%0.3f (+/-%0.03f) for %r"
        #           % (mean, std * 2, params))
        # print()

        train_preds = gs.predict(self.X_tr)
        test_preds = gs.predict(self.X_valid)

        return train_preds, test_preds

    def runGridSearch_knn(self):

        params = {'n_neighbors': [1,3,5,7,9], 'weights' : ['uniform', 'distance'], 'algorithm' : ['ball_tree', 'kd_tree', 'brute'], 'p' : [1,2]}

        learner = KNeighborsRegressor(n_jobs = 15)
        gs = GridSearchCV(learner, params, 'explained_variance', cv=5, n_jobs = 15)
        gs.fit(self.X_tr, self.y_tr)
        print("The best parameters found were: ")
        print(gs.best_params_)
        print(gs.get_params())

        train_preds = gs.predict(self.X_tr)
        test_preds = gs.predict(self.X_valid)

        return train_preds, test_preds

    def runGridSearch_random_forest(self):

        params = [{'n_estimators': [10, 30, 50, 70, 90, 100], 'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None], 'n_jobs': [17]}]

        learner = RandomForestRegressor(n_jobs=17)

        gs = GridSearchCV(learner, params, 'explained_variance', cv=5, n_jobs = 15)
        gs.fit(self.X_tr, self.y_tr)

        print("The best lat parameters found were: ")
        print(gs.best_params_)
        print(gs.get_params())

        # means = gs.cv_results_['mean_test_score']
        # stds = gs.cv_results_['std_test_score']
        # for mean, std, params in zip(means, stds, gs.cv_results_['params']):
        #     print("%0.3f (+/-%0.03f) for %r"
        #           % (mean, std * 2, params))
        # print()

        train_preds = gs.predict(self.X_tr)
        test_preds = gs.predict(self.X_valid)

        return train_preds, test_preds

    def gradient_boosting_regressor(self):

        learner = GradientBoostingRegressor()
        learner.fit(self.X_tr, self.y_tr)

        train_preds = learner.predict(self.X_tr)
        test_preds = learner.predict(self.X_valid)

        return train_preds, test_preds

    def linear_regression(self):

        learner = LinearRegression(n_jobs=17)
        learner.fit(self.X_tr, self.y_tr)

        train_preds = learner.predict(self.X_tr)
        test_preds = learner.predict(self.X_valid)

        return train_preds, test_preds

    def error(self, train, test):

        mse_tr = mean_squared_error(self.y_tr, train)
        mae_tr = mean_absolute_error(self.y_tr, train)
        msle_tr = mean_squared_log_error(self.y_tr, train)

        mse_te = mean_squared_error(self.y_valid, test)
        mae_te = mean_absolute_error(self.y_valid, test)
        msle_te = mean_squared_log_error(self.y_valid, test)

        print(f"Training: mse {mse_tr}, mae {mae_tr}, msle {msle_tr}")
        print(f"\tTest: mse {mse_te}, mae {mae_te}, msle {msle_te}")
        print()

if __name__ == "__main__":

    myModelSelection = modelSelection()
    myModelSelection.start()