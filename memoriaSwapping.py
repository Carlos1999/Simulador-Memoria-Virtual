class Memoria:
  def __init__(self):
    self.tamanhoMemoria = 1999 #Kilo Bites      
    memoria = [[0,0,self.tamanhoMemoria,[]]]  
    self.memoria = memoria

  def adicionarProcesso(self,dados):
    
    dadosSplit = dados.split(";")
    processo=[int("0"+dadosSplit[0]),int("0"+dadosSplit[1]),int("0"+dadosSplit[2]),int(dadosSplit[3])] 
        
    contador = 0
    for espaco in self.memoria:
      if((espaco[0]==0) and espaco[2]-espaco[1]+1 >= processo[1]):
        espaco[0]=1
        espaco[2]= processo[1] + espaco[1]-1
        espaco[3]=(processo)                
        if((len(self.memoria)==contador+1) and self.memoria[contador][2]<self.tamanhoMemoria):
          self.memoria.insert(contador+1,[0,espaco[2]+1,self.tamanhoMemoria,[0,0,0,0]])
        return True
      contador+=1
    return False    
  
  def substituirProcesso(self,indice,processo):
    processoSaiu = self.memoria[indice][3]
    if(processo== [0,0,0,0]):
      self.memoria[indice][0]=0        
    else:         
      self.memoria[indice][0]=1
    self.memoria[indice][3] = processo
    return processoSaiu  

  def decrementaTempoExecutando(self):
    contador =0
    for espaco in self.memoria:
      if(espaco[0]==1 and espaco[3][2]>0):
        espaco[3][2]=espaco[3][2]-1 
      
      contador+=1
  def removerProcesso(self,processo):
    for espaco in self.memoria:
      if(espaco[0] ==0 and espaco[3]==processo):
        espaco[0]=0
        print("Processo:"+str(espaco[3][0])+" Finalizado!")
        espaco[3]=[0,0,0,0]
        break
  
  def juntarEspacosVazios(self):
    i = 0 
    for espaco in self.memoria:
      if(espaco[0]==0):
        j=i+1   
        while(j < len(self.memoria) and self.memoria[j][0]==0 ):
          self.memoria[j-1][2] = self.memoria[j][2]
          self.memoria.pop(j)      
      i+=1

  def colocarEspacosFim(self):
    i=0
    for espaco in self.memoria: 
      if(i>0 and self.memoria[i][0]==1 and self.memoria[i-1][0]==0):
        self.memoria[i-1][0]=1
        self.memoria[i-1][2]= self.memoria[i][1]-1
        self.memoria[i-1][3]= self.memoria[i][3]

        self.memoria[i][0] = 0
        self.memoria[i][3] = []  
      i+=1

  def organizar(self):     
    self.colocarEspacosFim() 
    self.juntarEspacosVazios()

  def esvazear(self):
    for i in range(0,len(self.memoria)):
      if(self.memoria[i][3][2]>0):
        print("Processo:",self.memoria[i][3]," Finalizado!")
      self.substituirProcesso(i,[0,0,0,0])   

  def print(self):
    for espaco in self.memoria:
      print(espaco)    

  def getTamanhoMemoria(self):
    return self.tamanhoMemoria