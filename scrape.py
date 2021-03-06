import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pickle
from pathlib import Path
import sys
sys.setrecursionlimit(100000)
import re
from collections import Counter
import datetime
import nltk
nltk.download('stopwords')
stopwords = set(nltk.corpus.stopwords.words('english'))

def get_soup(response):
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
    except:
        print('could not parse html')
    return soup

def get_desc_wrapper_list(soup):
    try:
        desc_wrapper = soup.find_all(class_='desc-wrapper')
    except:
        print('could not find description wrapper elements')
    return desc_wrapper


def get_author(el):
    try:
        author = el.find_all(class_='author')[0].contents[0]
    except:
        print('could not find author in element')
        return ""
    return author


def get_published_date(el):
    try:
        date_string = el.find_all(text="Published:")[
            0].parent.parent.contents[1]
        date_object = parse_date_from_string(date_string)
    except:
        print('could not find date string in element')
        return ""
    return date_object

def parse_date_from_string(date):
    try:
        date = datetime.datetime.strptime(date, '%b %Y')
    except:
        print('could not parse date string')
    return date

def get_description(el):
    try:
        description = el.find_all(class_='edition-desc')[0].contents[0]
    except:
        print('could not get description from element')
        return ""
    return description

def get_title(el):
    try:
        title = el.find_all(class_='title group')[0].contents[1].contents[0]
    except:
        print('could not get title from element')
        return ""
    return title

def request_params(page_number):
    params = (('mode', 'all'),
              ('CategoryID', '34'),
              ('HeaderCatID', '34'),
              ('pageenumsize', '12'),
              ('pubfrom', '2005-1-01'),
              ('pubto', '2018-5-31'),
              ('ratings', '0'),
              ('pagesort', 'pubdateDESC'),
              ('pageno', str(page_number)),
              ('_', '1524771903406'))
    return params

def analyse_word_frequency_in_dict_list(dict_list, key):
    list_of_vals = [str(d[key]).lower() for d in dict_list]
    try:
        joined_list_of_vals = ' '.join(set(list_of_vals))
        split_string_from_vals = re.findall(r"[\w']+|[.,!?;]", joined_list_of_vals)
        word_list_alnum = [i for i in split_string_from_vals if i.isalnum()]
        word_list_alnum_no_stopwords = [i for i in word_list_alnum if not i in stopwords]
    except TypeError:
        import ipdb; ipdb.set_trace()
    return Counter(word_list_alnum_no_stopwords).most_common()

def save_data(list_of_dicts, filename):
    with open(filename, 'wb') as f:
        pickle.dump(list_of_dicts, f)

def check_if_data_exists(filename):
    my_file = Path(filename)
    if my_file.is_file():
        return True
    else:
        return False

def load_data(filename):
    with open(filename,'rb') as f:
        list_of_dicts = pickle.load(f)
    return list_of_dicts

def get_list_of_items_in_date(dict_list,month_int,year):
    list_of_items_in_date = []
    try:
        list_of_items_in_date = [item for item in dict_list if item['published_date'] == datetime.datetime(year,month_int,1,0,0)]
    except:
        print('could not get items in that date')
    return list_of_items_in_date

def get_word_freq_by_date(dict_list):
    month_range = range(1,13)
    year_range = range(2007,2018+1)
    output_dict_list_title = []
    output_dict_list_description = []

    for year in year_range:
        for month in month_range:
            wfa_list = get_list_of_items_in_date(dict_list,month,year)
            if len(wfa_list) > 0:
                wfa_list_by_title = analyse_word_frequency_in_dict_list(wfa_list, 'title')
                temp_dict = {}
                temp_dict['published_date'] = datetime.datetime(year,month,1,0,0)
                temp_dict['wfa_list'] = wfa_list_by_title
                output_dict_list_title.append(temp_dict)

                wfa_list_by_description = analyse_word_frequency_in_dict_list(wfa_list, 'description')
                temp_dict = {}
                temp_dict['published_date'] = datetime.datetime(year,month,1,0,0)
                temp_dict['wfa_list'] = wfa_list_by_description
                output_dict_list_description.append(temp_dict)
    return output_dict_list_title, output_dict_list_description


if __name__ == "__main__":
    filename = 'results.pkl'
    if check_if_data_exists(filename):
        print('loading pre-existing data')
        list_of_dicts = load_data(filename)
    else:
        cookies = {'ASP.NET_SessionId': '',
                'SessionId': '',
                'affno': '',
                'firstvisit': '',
                'sentisum_session': ''}

        headers = {'Accept': 'text/html, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Referer': 'https://www.millsandboon.co.uk/c34/all-books.htm',
                'User-Agent': '',
                'X-Requested-With': 'XMLHttpRequest'}

        page_numbers = range(1,1941+1)

        list_of_dicts = []
        for i in page_numbers:
            print('analysing page {} of 1941'.format(i))
            params = request_params(i)
            response = requests.get('https://www.millsandboon.co.uk/CategoryResults.aspx', headers=headers, params=params, cookies=cookies)
            soup = get_soup(response)
            desc_wrapper = get_desc_wrapper_list(soup)
            for el in desc_wrapper:
                temp_dict = {}
                temp_dict['author'] = get_author(el)
                temp_dict['published_date'] = get_published_date(el)
                temp_dict['description'] = get_description(el)
                temp_dict['title'] = get_title(el)
                list_of_dicts.append(temp_dict)
                #pprint(temp_dict)

        save_data(list_of_dicts, 'results.pkl')

    print('found {} books'.format(len(list_of_dicts)))

    title_wfa = analyse_word_frequency_in_dict_list(list_of_dicts,'title')
    for s in title_wfa[0:21]: print(str(s))
    save_data(title_wfa, 'title_data.pkl')    

    description_wfa = analyse_word_frequency_in_dict_list(list_of_dicts,'description')
    for s in description_wfa[0:21]: print(str(s))
    save_data(description_wfa, 'description_data.pkl')    

    title_date_wfa, description_date_wfa = get_word_freq_by_date(list_of_dicts)
