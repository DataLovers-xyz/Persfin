# Personal Finance Classifier 
## What is the Personal Finance Classifier?
- This package classifies bank transaction statements in categories according to the description of the transaction as provided by the bank.
- The package outputs output files that then can be analyzed, also by the program, to see a breakdown of your expenses by category on a given period (month/year).
    - The program will process all input files in your provided data location.
- The program operates locally in order the information never leaves the local environment.
- You can create your own classfying categories and populate them. 
    - Some classifiers are included but are heavily localized to the Netherlands.
    - Pull request on expanding the classifiers are welcomed. Follow contribution guidelines.
## Installing
## How to use?
- You need to inform the program
    - The general structure of the files you will input.
        - The classifier assumes a canonical file structure with the following columns. 
                - Date
                - Amount 
                - Description
            -  The canonical headers, Date, Amount, and Description are mapped to the headings of the columns in your input files according to the master schema mentioned in your configuration file.
            - The canonical schema for ABN AMRO is included and is the default that works with the sample file. 
    - Where do you want the classified outputs to be stored.
    - The location of the classifiers you will use.
        - defaults to ./classifiers/NL
    - The classifiers that you will use and their respective tag (such as Groceries, Eat Out, etc.)
    - All of this is defined in configuration files.

### Configurations:
- All configurations are set in the config.toml file, the file includes the following values to configure.
    - Paths to:
        - Master Schema: 
        - Classifiers:
            - Path to the JSON classifiers
            - This defaults to the NL classifiers.
        - Desired location of output files:
            Defaults to ./outputs
    - Custom Preprocesses
        - Besides the regular pre-processes performed by the classifier, making sure only expenses are taken into account and that they are stated in their absolute value (not negatives), it is possible to include arbitrary functions to normalize or process any column in the canonical file (Date, Amount, Description). 
            - Input files of ABN Amro require that the date column is normalized to be read as a valid date.
            - The package includes the required preprocess for this. 
        - Preprocess are enabled by setting preprocess enabled to true in the config file.
        - The column to which the preprocess applies and the name of the preprocess module to apply to the column should be stated in the configuration file.
        - The module should be copied into the custom_preprocess directory and imported in the corresponding __init__.py in that folder. 

### Commands:
- persfin classify [path to input file]
    - Actions performed
        - Displays results and generates output file
    - Options
        - --analyze: Analyzes output produced and displays result.
        - --complete_pending: Allows to manually classify unclassified transactions before generating output. In development
- persfin analyze [year] 
    - Analyses master data per the input year


