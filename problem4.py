#9/10/2020
#kryptography

string="HELLO RUTUJA"
value=int(input("Enter the value by which you want to increment it:"))
new_string=""
for i in range(0, len(string)):
    if string[i]!=" ":
        new_string+=chr(ord(string[i])+value)
    else:
        new_string+=" "
print(new_string)
