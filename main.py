#! python3

import pyperclip, re

copyText = str(pyperclip.paste())

class Scraper:
    
    def emailFinder(self, text: str) -> None:
        self.email_matches = []
        self.email = re.compile(r'''( 
                ([a-zA-Z0-9._%+-]+) # Group[1] List Username
                @
                ([a-zA-Z-0-9.-]+)   # Group [2] List Domain name 
                ([.][a-zA-Z]{2,3})  # Group [3] List TLD 
                )''', re.VERBOSE)
        
        for groups in self.email.findall(text):
            self.email_matches.append(groups[0]) # Change zero to either 1, 2, or 3 to get different results
            
        return self.email_matches # Place return on the outside of the loop so it iterates all matching emails
    
    def phoneFinder(self, text: str) -> None:
        self.phone_matches = []
        self.phone = re.compile(r'''( 
                (\([0-9]{3}\)|[0-9]{3}) # Group [1] Area Code
                [-\s]
                ([0-9]{3}) # Group[2] Exchange Code
                -
                ([0-9]{4}) # Group [3] Station Code
                )''', re.VERBOSE)
        
        for groups in self.phone.findall(text):
            self.phone_matches.append(''.join(groups[0]).replace(' ', '').replace('(', '').replace(')', '-'))

        return self.phone_matches
    
    def urlFinder(self, text: str) -> None:
        self.url_matches = []
        self.url = re.compile(r'''
                        (https?://\S+ | www.\S+)      
                              ''', re.VERBOSE)
        
        for groups in self.url.findall(text):
            self.url_matches.append(groups)
        
        return self.url_matches

scraper = Scraper()
email_list = scraper.emailFinder(copyText)
phone_list = scraper.phoneFinder(copyText)
url_list = scraper.urlFinder(copyText)

def print_list(lists):
    for i in lists:
        print(i)

print_list(email_list)
print_list(phone_list)
print_list(url_list)