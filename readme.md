# Library Project

In this mini project, the data went through several key stages, starting from cleaning and preprocessing,
through exploratory data analysis (EDA), to model training for predicting the likelihood that books will 
not be returned on time.

## Data Cleaning and Preprocessing:
In the initial phase, the data was analyzed to identify missing or incorrect entries. Missing data was handled
appropriately, either through imputation or by removing certain records.
 
## Exploratory Data Analysis (EDA):
Exploratory data analysis helped identify key factors influencing the likelihood that books will not be returned on
time. Various aspects were analyzed, including demographic characteristics of users, types of books, seasonality,
and library characteristics. 
Visualizations such as histograms, boxplots, and correlations between different variables provided better insights into
the relationships between variables and potential data irregularities.

## Model Training:
Three models were trained (Logistic Regression, Random Forest and Gradient Boosting Classifier).
Categorical data was encoded using appropriate techniques, such as one-hot encoding for categorical variables like
‘gender’, ‘education’, ‘occupation’, ‘library name’, while numerical data (e.g., ‘price’ and ‘pages’)
was transformed into appropriate ranges and encoded by label encoder due to their natural ordinal relationship. 
Normalization or scaling of the data was not necessary, given the nature of the selected features and the model to be
used.
Using the selected features, the model was trained to predict the likelihood that books would not be returned on time. 
Additionally, tuning hyperparameters was performed for potential performance improvement.

### More detailed comments can be found in notebooks!!

## Project Structure:
CodeChallengeProject:
* **data/** - folder with all datasets (initial and processed)
* **notebooks/** - directory containing three notebooks used in this study
  * [part_1_data_preprocessing.ipynb](notebooks/part_1_data_preprocessing.ipynb)
  * [part_2_data_analysis.ipynb](notebooks/part_2_data_analysis.ipynb)
  * [part_3_model_training.ipynb](notebooks/part_3_model_training.ipynb)
* **src/** - Python scripts with custom designed functions
  * [basic_description_utils.py](src/basic_description_utils.py)
  * [date_correction_utils.py](src/date_correction_utils.py)
  * [geo_utils.py](src/geo_utils.py)
  * [customers_utils.py](src/customers_utils.py)
  * [nlp_utils.py](src/nlp_utils.py)
  * [regex_patterns.py](src/regex_patterns.py)
  * [model_training_utils.py](src/model_training_utils.py)




    