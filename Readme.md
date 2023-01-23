# Personal Finance Classifier 
## What is the Personal Finance Classifier?
- This package classifies bank transaction statements in categories according to the description of the transaction as provided by the bank.
- The package outputs a file that is classified according to the provided classifiers.
- The program operates locally in order the information never leaves the local environment.
- You can create your own classfying categories and populate them. 
    - Some classifiers are included but are heavily localized to the Netherlands.
    - Pull request on expanding the classifiers are welcomed. Follow contribution guidelines.
## Installing
## How to use?
### Configurations:
- All configurations are set in the config.toml file, the file includes the following values to configure.
    - Column mapper: 
        - The classifier assumes a canonical file structure. 
            - Date
            - Transaction class
            - Comment on transaction
            - Amount 
            - Description
        -  The column mappers maps the input columns, Date, Amount, and Description to the headings of the columns in your input files.
        - The column mapper is a Toml file in the configs directory.
        - Mapper for ABN AMRO is included and is the default that works with the sample file. 
    - Classifiers path:
        - Path to the JSON classifiers
        - This defaults to the NL classifiers.
    - Output files:
        Defaults to outputs
    - Path to master data:

    - Column preprocessing
        - Identify what columns need reprocessing. 
        - Testing file and ABN AMRO mapper requires preprocessing on date field.
### Commands:
- persfin classify [path to input file]
    - options
        - --analyze: Analyzes output produced and generates output file.
        - --add_to_master: Appends output to master
        - --complete_pending: Allows to manually classify unclassified transactions before generating output.
- persfin analyze [year] 
    -- Analyses master data per the input year


