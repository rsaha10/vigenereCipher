userInput = input("Please input text followed by your desired key and finally either True or False, True to encode and False to decode: ")

x = userInput.split()
txt = x[0].upper()
key = x[1].upper()
encodeDecode = None
if x[2] == "True":
    encodeDecode = True
else:
    encodeDecode = False

alphabet = "abcdefghijklmnopqrstuvwxyz"

expandedKey = ""
times = int(len(txt) / len(key))

for x in range(times):
    expandedKey = expandedKey + key

rem = int(len(txt) - len(expandedKey))

for x in range(rem):
    expandedKey = expandedKey + key[x]

def encode(str1, str2):
    encodedTXT = ""

    for x in range(len(str1)):
        y = (alphabet[(((ord(str1[x]) - 65) + (ord(str2[x]) - 65)) - 26)])
        encodedTXT = encodedTXT + y

    return (encodedTXT)

if encodeDecode == True:
    print (encode(txt, expandedKey))

def decode(str1,str2):
    decodedTXT = ""

    for x in range(len(str1)):
        if (ord(str1[x]) - 65) - (ord(str2[x]) - 65) < 0:
            y = (alphabet[(((ord(str1[x]) - 65) - (ord(str2[x]) - 65)) + 26)])
        else:
            y = (alphabet[((ord(str1[x]) - 65) - (ord(str2[x]) - 65))])

        decodedTXT = decodedTXT + y

    return (decodedTXT)

if encodeDecode == False:
    print (decode(txt, expandedKey))
