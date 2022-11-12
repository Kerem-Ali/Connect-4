class Connect4():
    def __init__(self,col=7,row=6,con=4):
        self.col=col
        self.row=row

        self.legal_moves=col*row

        self.moves=0
        self.connect=con
        
        self.platform=platform={a:[0 for x in range(1,row+1)]  for a in range(1,col+1)}
        
        self.sira="A"

    def reset(self):
        self.platform=platform={a:[0 for x in range(1,self.row+1)]  for a in range(1,self.col+1)}
        
    def start(self):
        self.platform_goster()
        while True:
            
            print("Sira {} numaralı oyunucuda".format(self.sira))
            col=int(input("Seciminizi yapınız (1-8) :"))
            while self.check_full(col):
                col=int(input("Seciminizi yapınız (1-8) :"))
                if col<1 or col>8:
                    break

            self.play(col)
            self.platform_goster()
                            
            self.sira_degistir()


            if self.check_win():
                print("Winner is ",self.check_win())
                break
        
    def platform_goster(self):
        print("-".join([str(x) for x in range(1,self.col+1)]))
        for x in range(self.row):
            qaw=""
            for b in [self.platform[a][x] for a in range(1,self.col+1)]:
                qaw+=str(b)+" "
            print(qaw)
        
    def check_full(self,col):
        return self.platform[col][0]!=0

    def check_win(self):
        col=self.col
        row=self.row
        platform=self.platform
        winner=""
        for sutun in range(1,col+1):
            for a in range(0,row-self.connect+1):
                dikeyleme=[platform[sutun][a+x] for x in range(self.connect)]
                if len(list(filter(lambda x:x!=0,dikeyleme)))==self.connect and len(set(list(filter(lambda x:x!=0,dikeyleme))))==1:#dikeyleme
                    return platform[sutun][a]#basarili


        for q in range(row):
            for b in range(1,col+1-(self.connect-1)):
                yataylama=[platform[b+x][q] for x in range(self.connect)]
                if len(list(filter(lambda x:x!=0,yataylama)))==self.connect and len(set(list(filter(lambda x:x!=0,yataylama))))==1:#yataylama
                    return platform[b][q]#basarili

        for a in range(1,col-self.connect+2):
            for b in range(0,row-self.connect+1):
                caprazlama=[platform[a+x][b+x] for x in range(self.connect)]
                if len(list(filter(lambda x:x!=0,caprazlama)))==self.connect and len(set(list(filter(lambda x:x!=0,caprazlama))))==1:
                    return platform[a][b]


        for a in range(1,col-self.connect+2):
            for b in range(-1,(-row+self.connect-2),-1):
                caprazlama=[platform[a+x][b-x] for x in range(self.connect)]
                if len(list(filter(lambda x:x!=0,caprazlama)))==self.connect and len(set(list(filter(lambda x:x!=0,caprazlama))))==1:
                    return platform[a][b]

    def play(self,col):
        for x in range(self.row+1):
            if x<self.row:
                if self.platform[col][x]=="A" or self.platform[col][x]=="B" :
                    self.platform[col][x-1]=self.sira
                    break
            else:
                self.platform[col][x-1]=self.sira
                break
                    
                
                    
                    
    def sira_degistir(self):
        self.moves+=1
        if self.sira=="A":
            self.sira="B"
        elif self.sira=="B":
            self.sira="A"
        
#a=Connect4()
#a.start()
