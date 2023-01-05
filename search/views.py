from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        url = 'https://www.ask.com/web?q=' + search
        response = requests.get(url)
        soup = bs(response.text, 'lxml')

        # grab all the links
        results = soup.find_all('div', class_='PartialSearchResults-item')

        final_result = []

        # loop through the results
        for result in results:
            title = result.find(class_ = 'PartialSearchResults-item-title').text
            link = result.find('a').get('href')
            description = result.find(class_ = 'PartialSearchResults-item-abstract').text
            final_result.append((title, link, description))
        
        context = {
            'final_result': final_result
        }

        return render(request, 'search.html', context)
    
    else:
        return render(request, 'search.html')