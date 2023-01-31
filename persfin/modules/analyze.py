import exceptions
import os 
import glob
from modules.pandas_services import ingest_data, get_hashed_df, get_new_df, get_concatenated_df, get_deduplicated_df, get_analized_df_by_year

def main(execution_params, configurations, canonical_schema):
    filter = int(execution_params["filter"])
    file_list = get_file_list(configurations)
    master_data = get_consolidated_df(file_list)
    print(get_analized_df_by_year(master_data,filter))

def get_file_list(configurations):
    path = configurations["paths"]["output_files"]
    if not os.path.isdir(path):
        raise exceptions.Configuration_Directory_Not_Present
    else:
        result = glob.glob(path+"/*.xlsx")
    return result

def verify_file(extracted_df):
    return (set(extracted_df.columns)) == set({"Date","Amount","Description","Class"})

def get_consolidated_df(file_list):
    consolidated_df = get_new_df()
    for file in file_list:
        working_df = ingest_data(file)
        if verify_file(working_df):
            consolidated_df = get_concatenated_df(consolidated_df,get_hashed_df(working_df))
        else:
            print(f"the {file} does not comply with the canonical schema")
    return get_deduplicated_df(consolidated_df)


