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
| Bride | 1181 |
| Her | 1091 |
| Baby | 1073 |
| His | 1063 |
| Christmas | 1061 |
| Secret | 693 |
| Marriage | 530 |
| Cowboy | 481 |
| Love | 480 |
| Night | 477 |
| Wife | 466 |
| One | 461 |

### Book description

| Word        | Frequency           | 
| ------------- |:-------------:| 
| Her | 12001 |
| His | 6928 |
| She | 6382 |
| He | 5116 |
| But | 4714 |
| One | 2541 |
| Life | 1902 |
| New | 1847 |
| Man | 1759 |
| Love | 1531 |
| All | 1485 |
| After | 1413 |
| Never | 1411 |