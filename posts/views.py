from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
posts = [
    {
        'name' : 'Mont blac',
        'user' : 'Luisa Daza',
        'timestamp': datetime.now().strftime('%d-%m-%Y'),
        'picture': 'https://picsum.photos/id/237/200/300'
    },
    {
        'name' : 'Mont blac',
        'user' : 'Luisa Daza',
        'timestamp': datetime.now().strftime('%d-%m-%Y'),
        'picture': 'https://picsum.photos/id/237/200/300'
    },
    {
        'name' : 'Mont blac',
        'user' : 'Luisa Daza',
        'timestamp': datetime.now().strftime('%d-%m-%Y'),
        'picture': 'https://picsum.photos/id/237/200/300'
    },
    {
        'name' : 'Mont blac',
        'user' : 'Luisa Daza',
        'timestamp': datetime.now().strftime('%d-%m-%Y'),
        'picture': 'https://picsum.photos/id/237/200/300'
    }
]


def list_posts(request):
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><strong>{user}</strong></p>
        <p><strong>{timestamp}</strong></p>
        <figure><img src="{picture}"</figure>        
        """.format(**post))
    return HttpResponse('<br>'.join(content))