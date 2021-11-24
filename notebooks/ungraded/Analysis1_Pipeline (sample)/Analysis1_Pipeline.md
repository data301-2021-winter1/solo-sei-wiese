- [1. Load Data](#1-load-data)
- [2. Clean Data](#2-clean-data)
- [3. Process Data](#3-process-data)
- [4. Wrangle Data](#4-wrangle-data)

## 1. Load Data
    * Load data from "data" folder.
    * Check each data frame by using "head()".
    * Print to check the number of rows and columns.
    * Check the column names of each dataframe with ".columns".

## 2. Clean Data
  * df_AfricanDevelopment
      * Remove columns not being used
      * Check for missing values in the data frames by using "isnull().sum()" .
      * Deal with "inappropriate" data with "dropna()" to remove the row.
      * Visualizing the correlation between population of 2021 and HDI in the df_AfricanDevelopment data
  
  * df_country_variables
    * Load data. At that time, use "header=1" to eliminate the misalignment of column names.
    * Remove rows and columns not being used.
    * Use the variable "missing_columns" to remove unnecessary columns.
    * Remove all non-year elements from the column called "variable".
    * Replace "-" in the table by Nan.
    * Change each columns data type from "object" into "float64"
    * Deal with “incorrect” data.
      * Align the digits of the data by dividing the data from 2012 to 2015 by 10.

## 3. Process Data
  * df_country_variables
    * Identify any years in which the average trend in global CPI values has changed significantly.
  * df_AfricanDevelopment
    * Determine the country data to be used in the following steps by sorting df_AfricanDevelopment by "humanDevelopmentIndex".
    * Choose those with discrete values.
  * df_cpi_xxyyzz
    * Conduct data processing for the four selected countries to make it easier to visualize the data.
  
## 4. Wrangle Data
  * df_cpi_xxyyzz
    * Remove rows and columns not being used.
    * Use the variable "missing_columns_xxyyzz" to remove unnecessary columns.
    * Remove all-Nan row by using "dropna()".
    * Grasp the trend by visualizing the data that has been made easy to handle in the previous steps as a graph.