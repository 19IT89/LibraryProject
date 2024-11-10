from typing import Any

from sklearn.model_selection import RandomizedSearchCV


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
