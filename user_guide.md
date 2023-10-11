# User Guide
Author: Tianji Rao

## Overview
Here we package the `main` function in `main.py` as a ETL query pipeline which can be used as a command line tool. This tool has three commands.

## Preparation
```
python setup.py develop
```

## Usage
Once the tool is installed, you can use it to perform various ETL and querying operations. Here's how to use it:

```
etl_query <action> [query]
```
**action**: Specifies the action you want to perform. It can be one of the following:

- extract: Extract data. 
- transform_load: Transform and load data. 
- general_query: Execute a general query (requires a query argument).

**query**: (Optional) A query to be executed when the action is general_query.

## Actions
### Extract Data
To extract data, use the extract action:

```
etl_query extract
```

This command will initiate the data extraction process.

### Transform and Load Data
To transform and load data, use the transform_load action:

```
etl_query transform_load
```

This command will initiate the data transformation and loading process.

### General Query
To execute a general query, use the general_query action and provide a query:

```
etl_query general_query 
```
"SELECT * FROM table_name WHERE condition;"
Replace "SELECT * FROM table_name WHERE condition;" with your SQL query. This command will execute the specified query on the data.

## Examples
Here are some examples of how to use the tool:

### Extract data:

```
etl_query extract
```


### Transform and load data:

```
etl_query transform_load
```

### Execute a general query:

```
etl_query general_query "SELECT * FROM alchoDB;"
```


