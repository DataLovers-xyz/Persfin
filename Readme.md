# Personal Finance Classifier 
## What is the Personal Finance Classifier?
- This package classifies bank transaction statements in categories according to the description of the transaction as provided by the bank in the statement.
- The package outputs files that then can be analyzed, also by the program, to see a breakdown of your expenses by category on a given period, filtered by year and grouped by month and category.
- The program operates locally in order the information never leaves the local environment.
- You can create your own classfying categories and populate them. 
    - Some classifiers are included but are heavily localized to the Netherlands.
    - Pull request on expanding the classifiers are welcomed. Follow contribution guidelines.
- Your custom classifiers should be declared in the config file.
## Installing
- clone these repository to your local machine.
- create a python virtual environment through python3 -m venv venv
    - the environment should be based in python 3.10
- activate the virtual environment
- pip install the dependencies on requirements.txt
### Configurations:
- All configurations are set in the config.toml file, the file includes the following values to configure.
    - Paths to:
        - Schema Mapper: 
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
        - Generates output file
        - Displays the classified file
        - Displays the breakdown of transactions by category.
    - Options
        - Comming soon
- persfin analyze [year] 
    - Analyses output files data per the input year
    - Collects data from all classified output files
    - Deduplicates data, if the same transaction is contained in several files it will be taken into account for analysis only once.
    presents the breakdown of transactions filtered by the corresponding year and grouped by month and class, it presents the aggregated number of type of transactions, the median value of each transaction class and the maximum value of each transaction class.




