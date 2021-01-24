# Graham
A simple pipeline to extract data from stock exchange websites, aggregate and analyse for insights.

## Current Working setup
- `pip install selenium`
- Download appropriate driver for [Chrome - click me](https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/)
- Place driver in root folder
- Create config.json in root folder with values as mentioned in next section but specific to your environment
- To run `python .\dataFetch\main.py`

## Config.json
`{ "root": "Location to your Graham folder" }`

## In development (Nice to have) setup
- `pip install scrapy`

## To Do
- [X] Setup selenium, load NSE homepage
- [ ] Add links of pages where data can be extracted
- [ ] Use selenium to download the files
- [ ] Process downloaded files

## Nice to have
- [ ] Go headless which is possible by replacing selenium with scrapy or beautiful soup and perform data fetch 

