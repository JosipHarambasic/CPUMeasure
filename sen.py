from urllib.request import urlopen

try:
    urlopen("https://www.google.com", timeout=2)
    print("worked")
except:
    print("failed")