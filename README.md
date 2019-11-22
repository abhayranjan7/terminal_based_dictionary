# Log Reporting Tool

This tool generates log reporting data gathered from build server logs

## Getting Started

These instructions will get you tool ready for reporting data generation. The output of the data will be on command line.

### Prerequisites

In order to get satisfy the pre requisite install the pip dependency from requirements.txt. To install requirements execute the following command.

```
Python 3.7.4
```

### Installing

To install the pip dependency from requirements.txt. Execute the following command to install required packages.

```
pip install -r requirements.txt
```

## Running the tests

To run this tool get to the root level directory of the project. Make sure csv file from which reporting data has to be generated present there. 
Now execute the below command in the given format

```
python main.py -s <startdate_rfc-3339_format> -e <enddate_rfc-3339_format> -f CSV.csv
```
*Startdate : From this time calculations will be calculated  
*Enddate : Till this time calculations will be calculated  
*File : From this csv file data will be generated  
e.g of rfc-3339 format is : 2018-11-02T12:00:00+02:00  


