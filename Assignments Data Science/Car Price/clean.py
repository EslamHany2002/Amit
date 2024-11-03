import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns

class pre_processing():
    
    # This function get all the info about the dataset
    def data_info(data):
        col_names = data.columns
        datatypes = [data[col].dtype for col in col_names]
        nullcounts = [data[col].isnull().sum() for col in col_names]
        nullcountspersentage = [(data[col].isnull().sum()/len(data))*100 for col in col_names]
        numberunique = [data[col].nunique() for col in col_names]
        uniqueValue = [data[col].unique() for col in col_names]
        top_unique = [data[col].value_counts().head(10).index.to_list() for col in col_names]
        dupliacte = data.duplicated().sum()
        col_type = ['Numerical' if pd.api.types.is_numeric_dtype(data[col]) 
                else 'Categorical' if pd.api.types.is_categorical_dtype(data[col]) or data[col].dtype == 'object' 
                else 'Other' for col in col_names]
        return pd.DataFrame({"Names of columns":col_names , "Data Type":datatypes ,"Nan Counts":nullcounts,"Nan Counts Persentage":nullcountspersentage,"Number of Unique":numberunique,"Unique values":uniqueValue,"Top Unique":top_unique,"Number of Dupliacted":dupliacte , "Column Type":col_type})
    
    
    
    # This Function convert the data Type of the column in dictionary pass the column name and the data type you want to convert to it
    def convert_data(data , datatype):
        for name,data_type in datatype.items():
            data[name] = data[name].astype(data_type)
    
    
    
    # This Function plot categorical Columns only by pass the Data & Categorical Features
    def plot_categorical_features(data,features):
        total_cols = 3
        total_rows = math.ceil(len(features) / total_cols)
        plt.figure(figsize=(20, 5 * total_rows))
        plot_idx = 1
        for col in features:
            plt.subplot(total_rows,total_cols,plot_idx)
            sns.countplot(data=data,x=col,palette="rocket")
            plot_idx += 1
        plt.tight_layout()
        plt.show()
        
    
    # This Function plot categorical columns with Target column by pass the Data & Categorical Features & target Feature
    def plot_categorical_features_with_target_feature(data,features,target):
        total_cols = 3
        total_rows = math.ceil(len(features) / total_cols)
        plt.figure(figsize=(20, 5 * total_rows))
        plot_idx = 1
        for col in features:
            plt.subplot(total_rows,total_cols,plot_idx)
            sns.countplot(data=data,x=col,palette="rocket",hue=target)
            plot_idx += 1
        plt.tight_layout()
        plt.show()   
        
        
    # This Function plot Numerical Columns only by pass the Data & Categorical Features using (Histogram Plot)
    def plot_numerical_features(data,features):
        total_cols = 3
        total_rows = math.ceil(len(features) / total_cols)
        plt.figure(figsize=(20, 5 * total_rows))
        plot_idx = 1
        for col in features:
            plt.subplot(total_rows,total_cols,plot_idx)
            sns.histplot(data=data,x=col,kde=True,bins=20)
            plt.title(f"Distribution of {col} and skew {data[col].skew()}")
            plot_idx += 1
        plt.tight_layout()
        plt.show()
        
        
    def plot_categorical_features_with_target_featur_nume(data,features,target):
        total_cols = 3
        total_rows = math.ceil(len(features) / total_cols)
        plt.figure(figsize=(20, 5 * total_rows))
        plot_idx = 1
        for col in features:
            plt.subplot(total_rows,total_cols,plot_idx)
            sns.boxplot(data=data,y=col,x=target,palette="rocket")
            plot_idx += 1
        plt.tight_layout()
        plt.show()
        
    
    # This Function plot Numerical Columns with target column (this column is Categorical) by pass the Data & Categorical Features & target column using (barplot)
    def plot_numerical_features_with_target_feature(data,features,target):
        total_cols = 3
        total_rows = math.ceil(len(features) / total_cols)
        plt.figure(figsize=(20, 5 * total_rows))
        plot_idx = 1
        for col in features:
            plt.subplot(total_rows,total_cols,plot_idx)
            sns.barplot(data=data,y=col,x=target,palette="rocket")
            plt.title(f"Distribution of {col} and skew {data[col].skew()}")
            plot_idx += 1
        plt.tight_layout()
        plt.show()
        
 
    # This Function to Detecte Outliers for numerical Data by pass (data & numerical features)
    def detect_outliers(data,features):
        total_cols = 3
        total_rows = math.ceil(len(features) / total_cols)
        plt.figure(figsize=(20, 5 * total_rows))
        plot_idx = 1
        for col in features:
            plt.subplot(total_rows,total_cols,plot_idx)
            sns.boxplot(data=data,x=col,color="red")
            plot_idx += 1
        plt.tight_layout()
        plt.show()


    # This Function to Get the numbers of the NaN in the Dataset
    def data_nan(data):
        missing_data = data.isnull().sum()
        return pd.DataFrame({"Null":missing_data[missing_data>0],"Null %":(missing_data[missing_data>0]/len(data))*100})
    
    
    # This Function to remove the Outliers by pass (Data & numerical features)
    def remove_outliers(data,features):
        for col in features:
            Q1 = data[col].quantile(0.25)
            Q3 = data[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bounds = Q1 - 1.5* IQR
            upper_bounds = Q3 + 1.5* IQR
            outliers = data[(data[col]<lower_bounds)|(data[col]>upper_bounds)]
            print(f"Numbers of outliers in {col} : {len(outliers)}")
            data.drop(outliers.index,axis=0,inplace=True)
            
    
    # This Function to replace the Outliers by Pass (Data & numerical features)
    def replace_outliers(data,features):
        for col in features:
            Q1 = data[col].quantile(0.25)
            Q3 = data[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bounds = Q1 - 1.5* IQR
            upper_bounds = Q3 + 1.5* IQR
            outliers_lower = data[(data[col]<lower_bounds)][col].values
            outliers_upper = data[(data[col]>upper_bounds)][col].values
            print(f"Number of outliers in {col} : {len(outliers_lower)+len(outliers_upper)}")
            data[col].replace(outliers_lower,lower_bounds,inplace=True)
            data[col].replace(outliers_upper,upper_bounds,inplace=True)