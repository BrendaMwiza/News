import urllib.request, json
from .models import Sources, Articles


#get api key
api_key = None

#get the news base url
base_source_url = None
base_article_url = None

def config_request(app):
    global api_key, base_article_url, base_source_url
    api_key = app.config['NEWS_API_KEY']
    base_source_url = app.config['SOURCE_API_BASE_URL']
    base_article_url = app.config['ARTICLES_API_BASE_URL']

def get_sources():
    '''
    Function for getting the json response to the url request
    '''
    get_source_url = base_source_url.format(api_key)
    print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        
        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_source(source_results_list)

    return source_results


def process_source(source_list):
    '''
    Function  for processing the source results and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for sources_item in source_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

        sources_object = Sources(id, name, description, url, category, language, country)
        source_results.append(sources_object)
        
        

    return source_results




def get_article():
    '''
    Function for getting the json response to our url request
    '''
    get_articles_url = base_article_url.format('everything', api_key) + "&sources="

    with urllib.request.urlopen(get_articles_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            articles_results_list = get_article_response['articles']
            article_results = process_articles(articles_results_list)

    return article_results

def process_articles(articles_list):
    '''
    Function  that processes the articles results and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Returns :
        article_results: A list of articles objects
    '''
    article_results = []
    for article_item in articles_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        article_results.append(Article(id, name, author, title, description, url, urlToImage, publishedAt))

    return article_results