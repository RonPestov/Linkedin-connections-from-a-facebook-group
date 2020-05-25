import time, random
import facebook
import json
import re
from selenium import webdriver

def main():
    i = 0
    j = 0
    filtered = []
    link_list = []
    text = 'www.linkedin.com'
    
    token = {"insert access token"}   #Enter access token between quotation marks
    graph = facebook.GraphAPI(token)
    fields = ['feed{link}']
    
    profile = graph.get_object('insert group id', fields = fields) #Enter group id between tick marks
    results = json.dumps(profile)
    #print(json.dumps(profile, indent = 4))
    parse = json.loads(results)
    #print(parse["feed"]["data"][0]["link"])
    links = parse["feed"]["data"]
    #print(links[0]["link"])
    
    try:
        for i in range(len(links)):     #loop to fill a list with only links
            #print(links[i]["link"])
            filtered.append(links[i]["link"])
        #print(filtered)
    except:
        pass
    
        for fil in filtered:            #filters to Linkedin links only
            if re.search(text, fil):    #look for specific text inside fil variable
                #print('match found!')
                #print(fil)
                link_list.append(fil)
        #print(link_list)
        
        browser = webdriver.Chrome('folder_path/chromedriver.exe')
        browser.get('https://www.linkedin.com/uas/login') #open chrome to linkedin website
        
        file = open('config.txt')   #open file containing login credentials
        lines = file.readlines()
        username = lines[0]
        password = lines[1]
        
        elementID = browser.find_element_by_id('username')
        elementID.send_keys(username)   #enters username
        elementID = browser.find_element_by_id('password')
        elementID.send_keys(password)   #enters password
        elementID.submit()  #signs in
        
        print('Connection request sent to the following links:')
        try:
            for j in range(len(link_list)):
                browser.get(link_list[j])   #browser opens each url in the list
                browser.find_element_by_class_name('pv-s-profile-actions').click()  #browser clicks on Connect button
                browser.find_element_by_class_name('ml1').click()   #browser clicks send now
                print(link_list[j])
                time.sleep(random.uniform(3, 7))    #waiting in between requests
        except:
            pass
        browser.close() #closes browser when done
    
if __name__ == "__main__":
    main()  
