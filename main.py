import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error,root_mean_squared_error
import pickle
import warnings
warnings.filterwarnings("ignore")
class SPR:
    def __init__(self,path):
        try:
            #Data understanding and Exploration
            self.df=pd.read_csv(path)
            self.df['Extracurricular Activities']=self.df['Extracurricular Activities'].map({'Yes':1,'No':0}).astype(int)
            print(self.df.head())
            print(self.df.shape)
            print(self.df.isnull().sum())
            print(self.df.info())
            #Data Preprocessing
            self.X=self.df.iloc[:,:-1]
            self.y=self.df.iloc[:,-1]
            print(self.X)
            print(self.y)
            #Train-Test Split
            self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(self.X,self.y,test_size=0.2,random_state=42)
            print(self.X_train.shape)
            print(self.y_train.shape)
            print(self.X_test.shape)
            print(self.y_test.shape)
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f"Error found in line number {er_line.tb_lineno} due to {er_type} and the reason was {er_msg}")
    def training_data(self):
        try:
            #Model Building
            self.reg=LinearRegression()
            self.reg.fit(self.X_train,self.y_train)
            #Evaluation of training data
            self.train_predictions=self.reg.predict(self.X_train)
            print(f"The Accuracy of training data:{r2_score(self.y_train,self.train_predictions)}")
            print(f"The Mean Squared Error of training data:{mean_squared_error(self.y_train,self.train_predictions)}")
            print(f"The Root Mean Squared Error of training data:{root_mean_squared_error(self.y_train,self.train_predictions)}")
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f"Error found in line number {er_line.tb_lineno} due to {er_type} and the reason was {er_msg}")
    def testing_data(self):
        try:
            #Evaluation of testing data
            self.test_predictions=self.reg.predict(self.X_test)
            print(f"The Accuracy of testing data:{r2_score(self.y_test,self.test_predictions)}")
            print(f"The Mean Squared Error of testing data:{mean_squared_error(self.y_test,self.test_predictions)}")
            print(f"The Root Mean Squared Error of testing data:{root_mean_squared_error(self.y_test,self.test_predictions)}")
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f"Error found in line number {er_line.tb_lineno} due to {er_type} and the reason was {er_msg}")
    def eda(self):
        plt.figure(figsize=(15,13))
        plt.title("Multiple Linear Regression")
        plt.scatter(self.X_train['Hours Studied'],self.y_train,c="blue")
        plt.plot(self.X_train['Hours Studied'],self.train_predictions,c="red")
        plt.show()
    def model_saving(self):
        try:
            #Saving the pickle file
            with open("SPR.pkl","wb") as f:
                pickle.dump(self.reg,f)
            #Loading the pickle file
            with open("SPR.pkl","rb") as f:
                m=pickle.load(f)
                hrs_studied=4
                previous_scores=90
                extra_curricular_activities=1
                sleep=8
                qp_practice=4
                features=np.array([[hrs_studied,previous_scores,extra_curricular_activities,sleep,qp_practice]])
                result=m.predict(features)[0]
                print(f"The result of sample input is {result}")
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f"Error found in line number {er_line.tb_lineno} due to {er_type} and the reason was {er_msg}")
if __name__=="__main__":
    try:
        dataset="Student_Performance.csv"
        obj=SPR(dataset)
        obj.training_data()
        obj.testing_data()
        obj.model_saving()
        obj.eda()
    except Exception as e:
        er_type,er_msg,er_line=sys.exc_info()
        print(f"Error found in line number {er_line.tb_lineno} due to {er_type} and the reason was {er_msg}")
