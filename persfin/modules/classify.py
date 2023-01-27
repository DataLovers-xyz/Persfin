from .pandas_services import ingest_data, get_canonical_df, get_custom_preprocessed_df, get_preprocessed_df, get_classified_df
import custom_preprocesses
from exceptions import Preprocess_Definition_Error
import json


def main(execution_params, configurations, canonical_schema):
    working_df = get_working_df(execution_params["path"])
    canonical_df = get_canonical_df(working_df, canonical_schema)
    preprocessed_df = preprocess(canonical_df,configurations)
    classification_set = get_classifiers(configurations)
    classified_df = get_classified_df(preprocessed_df,classification_set)
    print(classified_df)

def preprocess(canonical_df, configurations):
    if configurations["custom_preprocess"]["enabled"]:
        custom_preprocess_func = get_custom_preprocess_func(configurations)
        custom_preprocess_column = configurations["custom_preprocess"]["column"]
        temp_df = get_custom_preprocessed_df(canonical_df, custom_preprocess_column,custom_preprocess_func)
        preprocessed_df = get_preprocessed_df(temp_df)
    else:
        preprocessed_df = get_preprocessed_df(canonical_df)
    return preprocessed_df

def get_custom_preprocess_func(configurations):
    if verify_custom_preprocess(configurations):
        preprocess_func = getattr(custom_preprocesses,configurations["custom_preprocess"]["script"])
        return preprocess_func.main
    else:
        raise Preprocess_Definition_Error(configurations["custom_preprocess"]["script"])

def classify():
    pass

def get_classifiers(configurations):
    classification_set = []
    for classifier in configurations["classifiers"].keys():
        data = json.loads(open_classifier(configurations["paths"]["classifiers"]+"/"+configurations["classifiers"][classifier]))
        classification_set.append((data[classifier],classifier))
    return classification_set

def open_classifier(path):
    with open(path, "r") as json_file:
        data=json_file.read()
    return data

def get_working_df(path):
    return(ingest_data(path))

def verify_custom_preprocess(configurations):
    return configurations["custom_preprocess"]["script"] in set(dir(custom_preprocesses))
