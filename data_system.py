
# coding: utf-8

def measure(strg):
    num = 0
    for i in strg:
        num += ord(i) #傳回其ASCII編碼或Unicode碼點
    return num

class node():
    def __init__(self,eng,chin):
        self.english = eng
        self.chinese = chin
        self.son = {}
    def clone(self):
        x = node(self.english,self.chinese)
        x.son = self.son
        return x
    def switch(self,a):
        self.english = a.english
        self.chinese = a.chinese
        self.son = a.son
    def push_in(self,eng,chin):
        self.switch(merge( node(eng,chin), self.clone() ))

        
def merge(a,b):
    if measure(a.english) > measure(b.english):
        x = a; a = b; b = x;
    if measure(a.chinese) > measure(b.chinese):
        if "left" in a.son:
            a.son["left"] = merge(a.son["left"],b)
        else:
            a.son["left"] = b
    else:
        if "right" in a.son:
            a.son["right"] = merge(a.son["right"],b)
        else:
            a.son["right"] = b
    return a
        
def transfer(a):
    x = {}
    x["english"] = a.english
    x["chinese"] = a.chinese
    if "left" in a.son:
        x["left"] = transfer(a.son["left"])
    if "right" in a.son:
        x["right"] = transfer(a.son["right"])
    return x

#Testing

a = node("1","一一一")
b = node("1","二二二")
x = merge(a,b)
print(transfer(x))

x.push_in("0","嘿嘿嘿")
print(transfer(x))

