class Busz:
    file=open("helyjegy.txt" "r")
    jegyar:str
    tavolsag:str
    
    
    
    
    
    
    
def __init__(self, sor: str) -> None:
    adatok=sor.strip().split(' ')
    self.jegyar=adatok[0]
    self.tavolsag=adatok[1]
    