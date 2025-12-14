# import urllib
# import urllib.request to get the data form the url
# write a function that takes a url and returns 
# returns a response

import urllib.request as urllib

def main(url):
    print("Checking connectivity")
    response = urllib.urlopen(url)
    print(f"Connected to {url} successfully")
    print(f"The response code was: {response.getcode()}") 

print("This is a site connectibity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)
