import re
import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.google.com/")

# Fill in the form
browser.select_form('form[action="/search"]')
browser["q"] = "MechanicalSoup"
browser.submit_selected(btnName="btnG")

# Display links
for link in browser.links():
    target = link.attrs['href']

    if(target.startswith('/url?') and not 
        target.startswith("/url?q=http://webcache.googleusercontent.com")):
        
        target = re.sub(r"^/url\?q=([^&]*)&.*", r"\1", target)
        print(target)