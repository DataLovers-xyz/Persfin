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

def output_file(source_df,path):
    source_df.to_excel(path,index=False)

def get_analyzed_df(source_df):
    return source_df.groupby("Class").agg({"Amount":['sum','count','max']})

def get_hashed_df(source_df):
    working_df = source_df
    working_df["_signature"] = pandas.util.hash_pandas_object(source_df[["Date","Amount","Description"]], index=False)
    return(working_df)

def get_new_df():
    return pandas.DataFrame()

def get_concatenated_df(source, added):
    list = [source, added]
    return pandas.concat(list, ignore_index=True)

def get_deduplicated_df(source_df):
    return source_df.drop_duplicates(subset="_signature", ignore_index=True)

def get_analized_df_by_year(source_df,year):
    return (source_df[source_df["Date"].dt.year == year].groupby([source_df["Date"].dt.month,"Class"]).agg({"Amount":["count","sum","median","max"]}))
