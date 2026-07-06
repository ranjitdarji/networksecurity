import yaml
import numpy as np
import pickle
import sys
import os

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise NetworkSecurityException(e, sys)


def save_numpy_array_data(file_path: str, array: np.array):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info("Entered save_object method")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

        logging.info("Exited save_object method")

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


def load_object(file_path: str) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"File does not exist: {file_path}")

        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)

    except Exception as e:
        raise NetworkSecurityException(e, sys) from e


def evaluate_models(
    X_train,
    y_train,
    X_test,
    y_test,
    models,
    param
):
    try:

        report = {}

        for model_name, model in models.items():

            para = param[model_name]

            gs = GridSearchCV(
                estimator=model,
                param_grid=para,
                cv=3,
                n_jobs=-1,
                verbose=0
            )

            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_

            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            train_score = accuracy_score(y_train, y_train_pred)
            test_score = accuracy_score(y_test, y_test_pred)

            logging.info(
                f"{model_name} --> Train Accuracy: {train_score:.4f} | Test Accuracy: {test_score:.4f}"
            )

            report[model_name] = test_score

        return report

    except Exception as e:
        raise NetworkSecurityException(e, sys)