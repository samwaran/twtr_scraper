# twtr_scraper

## Description
A tweets web scraper that even works in 2024. This uses an unofficial release of [ntscraper](https://github.com/bocchilorenzo/ntscraper), therefore, kindly use it for educational purpose only.

## Installation
In order to use this script to scrape data, we need two libraries:

- Pandas
- ntscraper

to install ntscraper, use:

```
pip install ntscraper
```

to install pandas, use:

```
pip install pandas@latest
```

Alternatively, you can use `-user` for only installing for current user and not globally.

## How to use

To use this script you have to cloe this repository to your local machine using

```
git clone https://github.com/samwaran/twtr_scraper.git
```
then use jupyter notebook to run the `.ipnyb` file or use cmd to run the python script. You have to `cd` into the exact loaction of the script where you can use,

```
python twtr_scraper.py
```
The script store a `data.csv`file within the same folder stored with the data requested. The script here use 4 parameters


- Username: a string to be entered with the username for which tweets are needed
- No. of tweets: number of tweets to be scraped (pls note this use a nitter instance which can be struck down shortly by twitter therefore might not be available to scrape huge amount of tweets)
- From date (YYYY-MM-DD): starting date in format YYYY-MM-DD
- To date (YYYY-MM-DD): End date in format YYYY-MM-DD

## Notes

Due to recent changes on Twitter's side, some Nitter instances may not work properly even if they are marked as "working" on Nitter's wiki. If you have trouble scraping with a certain instance, try changing it and check if the problem persists.



