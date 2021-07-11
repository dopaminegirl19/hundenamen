# hundenamen
 
## What does it do? ##
This code takes a .csv file where the first entry of each row is a word in the form '"Word"' and returns all the unique entries with a Levenshtein distance = 1.

## How to run ##
1. Clone the repo: ```git clone https://github.com/dopaminegirl19/hundenamen.git``` 
1. ```cd hundenamen```
1. ```python levenshtein.py```
   - optional flag ```--csvname``` string to csv file input. Default is '20210103_hundenamen.csv' (provided in repo)
1. The output is a list, separated by commas.
