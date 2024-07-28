#! python3

import pyperclip, re

copyText = str(pyperclip.paste())

class Scraper:
    
    def emailFinder(self, text: str) -> None:
        self.matches = []
        self.email = re.compile(r'''( 
                ([a-zA-Z0-9._%+-]+) # Group[1] List Username
                @
                ([a-zA-Z-0-9.-]+)   # Group [2] List Domain name 
                ([.][a-zA-Z]{2,3})  # Group [3] List TLD 
                )''', re.VERBOSE)
        
        for groups in self.email.findall(text):
            self.matches.append(groups[0]) # Change zero to either 1, 2, or 3 to get different results
            
        return self.matches # Place return on the outside of the loop so it iterates all matching emails
    
    def phoneFinder(self, text: str) -> None:
        self.matches = []
        self.phone = re.compile(r'''( 
                (\([0-9]{3}\)|[0-9]{3}) # Group [1] Area Code
                [-\s]
                ([0-9]{3}) # Group[2] Exchange Code
                -
                ([0-9]{4}) # Group [3] Station Code
                )''', re.VERBOSE)
        
        for groups in self.phone.findall(text):
            self.matches.append(''.join(groups[0]).replace(' ', '').replace('(', '').replace(')', '-'))

        return self.matches
    
    def urlFinder(self, text: str) -> None:
        self.matches = []
        self.url = re.compile(r'''
                        (https?://\S+ | www.\S+)      
                              ''', re.VERBOSE)
        
        for groups in self.url.findall(text):
            self.matches.append(groups)
        
        return self.matches

scraper = Scraper()
emailList = scraper.emailFinder(copyText)
phoneList = scraper.phoneFinder(copyText)
urlList = scraper.urlFinder(copyText)

def loops(lists):
    for i in lists:
        print(i)

loops(emailList)
loops(phoneList)
loops(urlList)