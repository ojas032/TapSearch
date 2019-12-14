import re


appearances_dict=dict()
class api:
    def __init__(self,txt):
        self.txt=txt

    def index(self,txt):
       
        while "\r\n\r\n" in txt: txt = txt.replace("\r\n\r\n", "\r\n")
       # txt= txt.replace("\r\n\r\n", "\r\n")
        txt=txt.split("\r\n")
        i=0
        for text in txt:
            i+=1
            clean_text = re.sub(r'[^\w\s\n]','',text)
            terms = clean_text.split(' ')
            for term in terms:
                term=term.lower()
                appearances_dict.setdefault(term,[])
                if(i not in appearances_dict[term] ):
                    appearances_dict[term].append(i)




    def index1(self,txt):
            while "\r\n" in txt: txt = txt.replace("\r\n", " ")
            txt=re.split('\s{4,}',txt)
            i=0
            for text in txt:
                i+=1
                clean_text = re.sub(r'[^\w\s\n]','',text)
                terms = clean_text.split(' ')
                for term in terms:
                    term=term.lower()
                    appearances_dict.setdefault(term,[])
                    if(i not in appearances_dict[term] ):
                        appearances_dict[term].append(i)    




    def search(self,src):
        try:
            l=[]
            print(appearances_dict[src])
            if(len(appearances_dict[src])>10):
                for j in range(0,10):
                    l.append(appearances_dict[src][j]) 
                print(l)    
                return l
            else:        
                return (appearances_dict[src])
        except:
            string="The word does not exist"
            l=[]
            l.append(string)
            return l

    def cleari(self):
        appearances_dict.clear()    






        

def search1(txt):
    call=api(txt)
    return call.search(txt)

def search2(txt):
    call=api(txt)
    return call.search(txt)    

def main(a,txt):
    call=api(txt)
    if(a==1):
        call.cleari()
        call.index(txt)

def main1(a,txt):
    call=api(txt)
    if(a==1):
        call.cleari()
        call.index1(txt)



        

