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
The results presented here ignore common boring words like 'the' and 'a'. A limitation in these results is that I don't group different versions of the same word (e.g. 'Witch'/'Witches'). A total of 23,285 books were found and analysed, although some were missing descriptions.

### Book title

| Word        | Frequency           | 
| ------------- |:-------------:| 
| Bride | 1151 |
| Her | 1101 |
| His | 1095 |
| Christmas | 1009 |
| Baby | 1006 |
| Secret | 702 |
| Marriage | 513 |
| Cowboy | 490 |
| Wife | 445 |
| Cowboy | 490 |
| One | 429 |
| Night | 406 |
| Mistress | 398 |
| Family | 388 |
| Love | 375 |

### Book description

| Word        | Frequency           | 
| ------------- |:-------------:| 
| Bride | 1151 |
| Her | 1101 |
| His | 1095 |
| Christmas | 1009 |
| Baby | 1006 |
| Secret | 702 |
| Marriage | 513 |
| Cowboy | 490 |
| Wife | 445 |
| Cowboy | 490 |
| One | 429 |
| Night | 406 |
| Mistress | 398 |
| Family | 388 |
| Love | 375 |