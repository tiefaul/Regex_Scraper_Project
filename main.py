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
                )''', re.VERBOSE)   # Group [0] Lists all
        
        for groups in self.email.findall(text):
            self.matches.append(groups[0])
            
        return self.matches # Place return on the outside of the loop so it iterates all matching emails

scraper = Scraper()
print(scraper.emailFinder(copyText))




# Create a phone number scraper


# Create a website scraper


# Create a email scraper

