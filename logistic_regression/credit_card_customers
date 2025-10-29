import pandas as pd # type: ignore
import numpy as np # type: ignore
from sklearn.linear_model import LogisticRegression # type: ignore
from sklearn.metrics import accuracy_score, classification_report # type: ignore

class Main:
    def __init__(self):
        self.csv_path = "BankChurners.csv"
        self.features = [
            "Customer_Age", 
            "Gender", 
            "Dependent_count", 
            "Education_Level",
            "Marital_Status", 
            "Income_Category", 
            "Card_Category", 
            "Months_on_book",
            "Total_Relationship_Count",
            "Months_Inactive_12_mon",
            "Contacts_Count_12_mon",
            "Credit_Limit",
            "Total_Revolving_Bal",
            "Avg_Open_To_Buy",
            "Total_Amt_Chng_Q4_Q1",
            "Total_Trans_Amt",
            "Total_Trans_Ct",
            "Total_Ct_Chng_Q4_Q1",
            "Avg_Utilization_Ratio"
        ]
        self.columns_to_drop = [
            "CLIENTNUM",
            "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
            "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"
        ]
        self.columns_to_convert_to_int = [
            "Attrition_Flag", 
            "Gender", 
            "Education_Level", 
            "Marital_Status", 
            "Income_Category", 
            "Card_Category"
        ]
        self.target = "Attrition_Flag"


    def load_data(self):
        df = pd.read_csv(self.csv_path)
        return df
    
    def print_df(self, df):
        print(df.head())
        print(f"Df shape: {df.shape}")
        print(f"Columns in df: {df.columns}")

    def drop_data(self, df):
        df = df.drop(columns=self.columns_to_drop)
        return df
    
    def convert_non_numeric_columns_to_numeric_columns(self, df):
        mapping_dict = {
            "Attrition_Flag": {"Existing Customer": 0, "Attrited Customer": 1},
            "Gender": {"M": 0, "F": 1},
            "Education_Level": {
                "Uneducated": 0,
                "High School": 1,
                "College": 2,
                "Graduate": 3,
                "Post-Graduate": 4,
                "Doctorate": 5,
                "Unknown": 6
            },
            "Marital_Status": {
                "Single": 0,
                "Married": 1,
                "Divorced": 2,
                "Unknown": 3
            },
            "Income_Category": {
                "Less than $40K": 0,
                "$40K - $60K": 1,
                "$60K - $80K": 2,
                "$80K - $120K": 3,
                "$120 +": 4,
                "Unknown": 5
            },
            "Card_Category": {
                "Blue": 0,
                "Silver": 1,
                "Gold": 2,
                "Platinum": 3
            }
        }

        for column, map_dict in mapping_dict.items():
            df[column] = df[column].map(map_dict)
        return df
    
    def fill_missing_values(self, df):
        for column in df.columns:
            if df[column].dtype in ["float64", "int64"]:
                df[column] = df[column].fillna(df[column].mean())
            else:
                df[column] = df[column].fillna(df[column].mode()[0])
        return df
    
    def prepare_model_data(self, df):
        train_percent = 80
        train_nums = int((len(df) / 100) * train_percent)
        train_df = df.sample(n=train_nums, random_state=42)
        test_df = df.drop(train_df.index)
        x_train = train_df.drop(columns=[self.target])
        y_train = train_df[self.target]
        x_test = test_df.drop(columns=[self.target])
        y_test= test_df[self.target]
        return x_train, y_train, x_test, y_test
    
    def train_model(self, x_train, y_train, x_test, y_test):
        model = LogisticRegression(solver="lbfgs", max_iter=1000, random_state=42)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
        print(classification_report(y_test, y_pred))



if __name__ == "__main__":
    main = Main()
    df = main.load_data()
    df = main.drop_data(df=df)
    df = main.convert_non_numeric_columns_to_numeric_columns(df=df)
    df = main.fill_missing_values(df=df)
    x_train, y_train, x_test, y_test = main.prepare_model_data(df=df)
    main.train_model(x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)
