import requests
from time import time

def get_file(url):
    response = requests.get(url, allow_redirects=True)
    return response

def write_file(response):
    # https://loremflickr.com/cache/resized/65535_52482515227_0e5cd1ccd7_z_320_240_nofilter.jpg
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)

def main():
    t0 = time()
    url = 'https://loremflickr.com/320/240'

    for i in range(10):
        write_file(get_file(url))
    
    print(time() - t0)

if __name__ == '__main__':
    main()