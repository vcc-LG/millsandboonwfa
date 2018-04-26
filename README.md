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

## Results
The results presented here ignore common boring words like 'the' and 'a'. A limitation in these results is that I don't group different versions of the same word (e.g. 'Witch'/'Witches').

### Book title

| Word        | Frequency           | 
| ------------- |:-------------:| 
|          |               |