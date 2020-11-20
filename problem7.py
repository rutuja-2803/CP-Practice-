#20/11/2020  CORPORATE RENAMING
import re
text = "Anderson Accounting begat Anderson Consulting, which offered advice to Enron before it DECLARED bankruptcy, which made Anderson Consulting quite happy it changed its name in the first place!"
before=["Anderson Consulting","Enron", "DEC", "TWA"]
after=["Accenture","Dynegy","Compaq","American"]
a=0
for i in before:
        text=re.sub(i,after[a],text)
        a+=1
print(text)
