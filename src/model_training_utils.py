import pandas as pd
from typing import Any
from sklearn.pipeline import Pipeline
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from IPython.display import display

def tune_hyperparameters(model: Any, parameters: dict[str, list[int|None|str]], x_train, y_train) -> Any:
    grid_search = RandomizedSearchCV(estimator=model,
                                     param_distributions=parameters,
                                     n_jobs=-1,
                                     cv=5,
                                     verbose=2,
                                     random_state=42
                                     )
    grid_search.fit(x_train, y_train)
    print("Best parameters: ", grid_search.best_params_)
    return grid_search.best_estimator_


def train_model(preprocessor: Any, model: Any, x_train, y_train) -> Any:
    pipeline = Pipeline(
        steps=[
            ('preprocessor', preprocessor),
            ('classifier', model)
        ]
    )
    pipeline.fit(x_train, y_train)
    return pipeline

def predict_and_display_performances(model, x_test, y_test):
    y_pred = model.predict(x_test)
    display(pd.DataFrame(classification_report(y_test, y_pred, output_dict=True)))
    display(pd.DataFrame(confusion_matrix(y_test, y_pred)))
    return y_pred