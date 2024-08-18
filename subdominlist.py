import requests

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_input = "google.com"

with open("subdomainlist.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()  # Boşluklardan kurtulduk
        my_url = "http://" + word + "." + target_input
        responce = make_request(my_url)
        print(responce)
        if responce:  # Eğer responce boş gelmiyorsa demek
            print("Found subdomain --->" + my_url)
