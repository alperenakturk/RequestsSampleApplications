import requests
from bs4 import BeautifulSoup  # html ve xml ile işlem yapmak için kullanılan bir kütüphane

target_url = "https://atilsamancioglu.com/"
foundLinks = []  # Bulduğumuz linklerin bu dizinin içine koyacağız.


def make_request(url):
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")  # "html.parser" Bir hatanın çıkmaması için yazdık.
    return soup


def crawl(url):
    links = make_request(url)
    for link in links.find_all('a'):
        found_link = link.get('href')
        if found_link:  # found link boş değilse
            if "#" in found_link:
                found_link = found_link.split("#")[0]
                '''Üstteki kod şunu yapıyor --> found_link = https://atilsamancioglu.com/courses#python --> İşlemden 
                sonra --> ['https://atilsamancioglu.com/courses', 'python'] --> oluyor. Bu sayede halihazırda sayfa 
                içinde bulunan '#' ile gösterilen ve bizi ayrı bir sayfaya göndermeyen linkleri, asıl linkler ile 
                ayırmış bulunuyoruz.'''
            if target_url in found_link and found_link not in foundLinks:
                # Aynı linklerin tekrar tekrar gözükememesi için bu kontrolü yaptık.
                foundLinks.append(found_link)
                print(found_link)
                # recursive function
                crawl(found_link)
                '''linkin içindeki linkleri bulup onlarında içindeki linkler bitene kadar bulmak için recursive 
                function ile fonksiyonun içinde aynı fonksiyonu bir daha çağırdık bu sayede en sona kadar gidebilecek'''


crawl(target_url)
