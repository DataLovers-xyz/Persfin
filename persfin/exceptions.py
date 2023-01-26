class Unexpected_Input(Exception): 
    "Raised when incorrect amount of arguments was passed"
    def __init__(self):
        self.message = "You provided the wrong number of arguments, type persfin help to get help"
        super().__init__(self.message)

class Master_Schema_Error(Exception):
    "Raised when the columns of the loaded file don't match the defined schema"
    def __init__(self, master_schema_columns, data_columns ):
        self.message = f"Your provided canonical schema {master_schema_columns} doesn't match the data you are ingesting {data_columns} "
        super().__init__(self.message)

class Preprocess_Definition_Error(Exception):
    "Raised when the prprocesse defined in the configuration doesn't exist"
    def __init__(self, script_name):
        self.message = f"The preprocess defined as {script_name} does not exist in your preprocesses folder"
        super().__init__(self.message)


