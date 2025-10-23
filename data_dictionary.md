—
name: “Data dictionary”
Descriptions: “Description of variables in CSV file”
—

## Data dictionary

This file contains an explanation of the variables in the “ICU_Mortality.csv” file. The data are a simulation of patients admitted to a Intensive Care Unit.

## Response variable

### Mortality

The “Mortality” column is a nominal categorical variable with sample space elements “Died” and “Survived”. “Died” indicates that the subject died and “Survived” indicates that the subject survived.

## Explanatory variables

### Age

The “Age” column is a numerical variable and indicates the integer age of the patients measured in years on admission to the Intensive Care Unit.

### WCC

The “WCC” columns is a numerical variables and indicates the floating point value of a patient’s white cell count measured in 10 to the power of 9 cells per liter on admission to the Intensive Care Unit.

### HB

The “HB” column is a numerical variable and indicates the floating point value of a patient’s hemoglobin value measured in gram percentage on admission to the Intensive Care Unit.

### Diabetes

The “Diabetes” column is a nominal categorical variables with sample space elements “None”, “Type I”, and “Type II”. “None” indicates that the patient does not have diabetes mellitus. “Type I” indicates that the patient has insulin-dependent diabetes mellitus.”Type II” indicates that the patient has non-insulin-dependent diabetes mellitus.

### Class

The “Class” column is a categorical variable with sample space elements “Non-infectious” and “Infectious”. These categories indicates the type of disease on admission to the Intensive Care Unit. “Non-infectious” indicates that a patient was admitted with a non-infectious disease and “Infectious” indicates that a patient was admitted with an infectious disease.