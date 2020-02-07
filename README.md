# NMR Clock
## Preliminaries

Install Python version 3.7;
Install pip;
Install numpy;
Install scipy.

Click "Clone or download" on this site (top page) to transfer this package to your local machine. Unzip.

## Input

The clock takes a CSV input containing a list of positions identified by `<CONTIG>:<POSITION>` for each sample e.g.

|Positions|Sample 1|Sample 2|
|---|---|---|
|JH602136:8746439|0.9|0.6|
|JH602136:8746449|0.5|0.5|

Place the input file in the downloaded and unzipped NMRAgePrediction folder.

## To run the clock
In a terminal window start Python and run the clock, changing "FILENAME" to your data filename


```python3
import run_clock
prediction = run_clock.run_clock("FILENAME.csv")
print(prediction)
```

returns sample and age estimate in weeks in two blocks of figures. Executing the following will output a results file in the working folder called "prediction.csv" sorted into columns.

```python3
import run_clock
import csv
prediction = run_clock.run_clock("FILENAME.csv")

with open('prediction.csv', 'w', newline='') as csvfile:
    fieldnames = ['Sample', 'Output']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0, len(prediction[0])):
	    writer.writerow({'Sample': prediction[0][i], 'Output': prediction[1][i]})
```
