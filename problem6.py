#QWERTY KEYBOARD
#26/10/2020

dict1={'W':'Q','E':'W','R':'E','T':'R','Y':'T','U':'Y','I':'U','O':'I','P':'O','[':'P','S':'A','D':'S','F':'D','G':'F','H':'G','J':'H','K':'J','L':'K',';':'L','X':'Z','C':'X','V':'C','B':'V','N':'B','M':'N',',':'M','.':',','/':'.'}
string=input()
final=""
for i in string:
    if i==" ":
        final+=" "
    else:
        final+=dict1[i]
print(final)

