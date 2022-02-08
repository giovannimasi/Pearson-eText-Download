from asyncio.windows_events import NULL
import requests
import os
from PIL import Image

def Download(cookie, bookId, pagesNumber, folder):
    s = requests.Session()
    s.cookies.set('etext-cdn-token', cookie, domain = '.pearson-intl.com')
    for i in range(pagesNumber):
        if i != 0:
            url = f'https://etext-content.gls.pearson-intl.com/eplayer/pdfassets/prod1/{bookId}/pages/page{i}?password=&accessToken=null&formMode=true'
            r = s.get(url, allow_redirects=True)
            if not os.path.exists(folder):
                os.makedirs(folder)
            open(f'{folder}/{i}.png', 'wb').write(r.content)
    print('Done', end='\n')
    print('Converting to PDF', end='...')
    ToPdf(pagesNumber, folder)

def ToPdf(pagesNumber, folder):
    img1 = NULL
    imagelist = []
    for i in range(pagesNumber):
        if i == 1:
            image = Image.open(f'{folder}/1.png')
            img = image.convert('RGB')
            img1 = img
        elif i != 0:
            image = Image.open(f'{folder}/{i}.png')
            img = image.convert('RGB')
            imagelist.append(img)
    img1.save(f'{folder}/{folder}.pdf',save_all=True, append_images=imagelist)
    print('Done', end='\n')
    if input('Do you want to delete single pages files? (y) ') == 'y':
        for i in range(pagesNumber):
            if i != 0:
                os.remove(f'{folder}\{i}.png')
    print("The book has been extracted as a pdf. It's recommended to optimize it through a PDF editor.")

cookie = input('Enter etext-cdn-token: ')
bookId = input('Enter BookId: ')
pagesNumber = int(input('Enter pages number: ')) + 1
folder = input('Where to save: ')
if cookie!=NULL and bookId!=NULL and pagesNumber>0:
    print('Download in progress', end='...')
    Download(cookie, bookId, pagesNumber, folder)