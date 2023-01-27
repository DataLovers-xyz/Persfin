import pandas
from exceptions import Master_Schema_Error
from modules.utilities import classification_engine

def ingest_data(path):
    working_data = pandas.read_excel(path)
    return working_data

def get_canonical_df(working_df, canonical_schema):
    canonical_df = pandas.DataFrame()
    if verify_columns(working_df,canonical_schema):
        for key in canonical_schema["columns"].keys():
            canonical_df[key] = working_df[canonical_schema["columns"][key]]
        return canonical_df
    else:
        raise Master_Schema_Error(set(canonical_schema["columns"].values()),set((working_df.columns)))

def verify_columns(working_df, canonical_schema):
    return set(canonical_schema["columns"].values()).issubset(set(working_df.columns))

def get_custom_preprocessed_df(canonical_df, column, preprocess_func):
    preprocessed_df = canonical_df
    preprocessed_df[column] = canonical_df[column].map(preprocess_func)
    return preprocessed_df

def get_preprocessed_df(canonical_df):
    expenses_filtered_df = canonical_df[canonical_df["Amount"]<0].copy()
    expenses_filtered_df["Amount"] = expenses_filtered_df['Amount'].abs()
    return expenses_filtered_df

def get_classified_df(source_df,classification_set):
    classified_df = source_df.copy()
    classified_df["Class"] = classified_df["Description"].map(lambda entry:classification_engine(entry,classification_set))
    return classified_df

