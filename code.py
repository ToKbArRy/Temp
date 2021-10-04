from bs4 import BeautifulSoup
import re
 

# file reading
with open(r"C:\Users\janni\OneDrive\Paxisemester\Daten\quellen_content-fantin-scholderer\mws_quellen\fantin-scholderer/1858_03", "r",encoding='utf-8') as a:
    RawText = a.read()
    
RawSoupText = BeautifulSoup(RawText, 'html.parser')
a = RawSoupText

# set up data structure

Data = {"text":
            {"body":
                {"salute":0}                
             }
             }        
    
# support variabels

TempData = {}
structure = []
TempList = []
b = 0
c = int
   
# regex  
salute = RawSoupText.find(id="3").get_text()
Data["text"]["body"]["salute"] = salute

aftercomments = re.findall(r'(<\/span>.+<\/p>)|(<\/span>.+<spa)',RawText) 
textstrukture = re.findall('id=\"\d{1,2}\"|id=\"n\d{1,2}\"',RawText)
Test = re.findall(r"\[\d\d\]",RawText)


# preperate the struckture for future use

if len(Test) == 1:
    aftercomments = aftercomments[1:]
for x in aftercomments:
    for y in x:
        if y:
            TempList.append(y)
        
aftercomments = TempList 



# extract tex and save in data

for x in textstrukture:
    x = x[4:-1]
    try:
        structure.append(int(x))
    except:
        structure.append(x)

    


for x in structure[3:]:
    
    if isinstance(x, int):
        Temp2 = "p " + str(x-3) 
        Temp = RawSoupText.find(id=x).get_text()
        TempDic = {Temp2 :Temp}
        Data["text"]["body"].update(TempDic)
    if isinstance(x, str) and isinstance(c, int):
        b = b + 1
        Temp = RawSoupText.find(id=x).get_text()
        TempDic = { 'note place="foot" n="' + str(b) + ')"' :Temp}
        Data["text"]["body"][Temp2] = [Data["text"]["body"][Temp2],TempDic,(aftercomments[b-1])[7:-4]]
    if isinstance(x, str) and isinstance(c, str):
        b = b + 1
        Temp = RawSoupText.find(id=x).get_text()
        TempDic = { 'note place="foot" n="' + str(b) + ')"' :Temp}
        Data["text"]["body"][Temp2] = Data["text"]["body"][Temp2] + [TempDic,(aftercomments[b-1])[7:-4]]
        
    c = x