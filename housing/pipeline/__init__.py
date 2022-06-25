"""
Machine Learing Pipeline :

Data ingestion - Bring data to system
                    Split dataset into train and test data.
Data validation - File name, Data type validation,
                  Schema validation(column name. column data type etc),
                  Null check, Duplicate data, outlier, imbalanced data set,
                  Domain value,  Data range, Anomolies
                  Data Drift.
perform EDA to understand Data:
Data Transformation / FE : EDA helps to uderstand, what Data Transformation is needed.
                            get the pickle for FE stage
Model Training : Model se;ection, hyper parameter tuning, 
                    get the pickle for model training.
                    model comparision - Compare with best model and minimum expectation

Model Evaluation : Use the test data to do model evaluation
                    model comparision

Model performance : 

Push Model ; 



Data drift :
wwhen the stats of the old dataset is no longer align with new dataset

"""