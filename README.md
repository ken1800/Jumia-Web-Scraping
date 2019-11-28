# Jumia-Web-Scraping
Scraping The famous Jumia E-commerce using Django and Scrapy

## Installation

jumia E-commerce Link [jumia](http://jumia.co.ke/).

```bash
clone the project
make sure the following are installed
    Django 2.0 +
    Scrapy
    Postgres
    Scrapyd
    
```

## Usage

```python


cd Jumia-Scraper # migrating to the root directory 'iCrawler'
python manage.py runserver # starts the django server 'localhost:8000'
scrapyd # use this command when you are in the perfecto directory 'starting the scrapyd daemon'
curl http://localhost:6800/schedule.json -d project=default -d spider=jumia #open another tab in the perfecto directory
```
##Screenshots
![scrapy](https://user-images.githubusercontent.com/50213124/69782599-7cc49c00-117f-11ea-9eb9-87e9a5d23443.png)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
