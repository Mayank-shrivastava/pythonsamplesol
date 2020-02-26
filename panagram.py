alphabets="abcdefghijklmnopqrstuvwxyz"
def ispanagram(s):
    for i in alphabets:
        if i not in s.lower():
            return False
        return True
s=input()
if ispanagram(s)==True:
    print("yes panagram")
else:
    print("no panagram")
