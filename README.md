# Mills and Boon Word Frequency Analysis

## About
Script to do word frequency analysis (WFA) on Mills and Boon book titles and descriptions, scraped from their [website](https://www.millsandboon.co.uk).

## Install requirements
```python
pip install -r requirements.txt
```

## Modify request headers
I'm not sure the best way of doing this other than going to the Mills and Boon listings page ([here](https://www.millsandboon.co.uk/c34/all-books.htm)) and looking at the cURL or network request in the dev tools for a page load. Replace the blank values in the `cookies` and `headers` dictionaries in the `_main_` method.

## Run
```python
python scrape.py
```
If you've not run the code before the results will be saved in a pkl file in the repo directory. Takes about 5 mins or so to perform the scraping, and a similar length of time to process the giant word lists.

## Results
The results presented here ignore common boring words like 'the' and 'a' using the nltk corpus. A limitation in these results is that I don't group different versions of the same word (e.g. 'Witch'/'Witches'). A total of 23,285 books were found and analysed, although some were missing descriptions.

### Book title

| Word        | Frequency           | 
| ------------- |:-------------:| 
|baby| 1081|
|christmas| 1069|
|secret| 692|
|marriage| 534|
|cowboy| 481|
|love| 481|
|night| 472|
|one| 467|
|wife| 466|
|mistress| 443|
|family| 386|
|wedding| 352|
|man| 341|
|heart| 334|
|child| 267|
|boss| 264|
|texas| 264|
|proposal| 256|
|seduction| 240|
|pregnant| 226|


### Book description

| Word        | Frequency           | 
| ------------- |:-------------:| 
|life| 1901|
|new| 1878|
|man| 1764|
|love| 1531|
|never| 1410|
|family| 1366|
|years| 1200|
|woman| 1086|
|baby| 967|
|home| 940|
|back| 879|
|night| 866|
|could| 836|
|two| 784|
|marriage| 780|
|time| 769|
|father| 766|
|would| 755|
|town| 743|
|christmas| 742|