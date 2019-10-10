from memoriaSwapping import Memoria 
from datetime import datetime

class MemoriaVirtual:
  def __init__(self,tamanhoMemoria):
    self.memoriaSwapping = Memoria()
    self.tamanhoMemoria = tamanhoMemoria
    self.memoriaVirtual = [] 
    self.contador=0
    self.ponteiro=0
    for i in range(0,tamanhoMemoria):
      self.memoriaSwapping.adicionarProcesso(str(i)+";"+str(int((self.memoriaSwapping.getTamanhoMemoria()+1)/self.tamanhoMemoria))+";0;-1")
    for i in range(0,tamanhoMemoria):
      self.memoriaSwapping.substituirProcesso(i,[0,0,0,0])  
      self.inserir([0,0,0,0]) 
    
#----------------------------------------------------------------------------------
  def organizarProcesso(self,dados):
    dadosSplit = dados.split(";")
    processo=[int(dadosSplit[0]),int(dadosSplit[1]),int(dadosSplit[2]),int(dadosSplit[3])] 
    tamanhoMaxPagina = int((self.memoriaSwapping.getTamanhoMemoria()+1)/self.tamanhoMemoria)
    processosRemovidos=[]
    while(processo[1]>tamanhoMaxPagina):
      processosRemovidos.append(self.inserir([processo[0],tamanhoMaxPagina,processo[2],processo[3]]))
      processo[1] = processo[1]-tamanhoMaxPagina    
    processosRemovidos.append(self.inserir(processo))
    return processosRemovidos

    
  def inserir(self,processo):
    now = datetime.now()
    pagina = [1,now.second,self.contador%self.tamanhoMemoria,processo]

    if(len(self.memoriaVirtual)<self.tamanhoMemoria):
      pagina[3] = pagina[3][0]
      self.memoriaVirtual.append(pagina)
      self.contador+=1 
      return  [0,0,0,0]
    else:
      return self.substituicao(pagina)

  def substituicao(self,pagina):

    while (True):
      if(self.memoriaVirtual[self.ponteiro%self.tamanhoMemoria][0]==0):
        
        self.memoriaVirtual.pop(self.ponteiro%self.tamanhoMemoria)
        processoSaiu = self.memoriaSwapping.substituirProcesso(self.contador%self.tamanhoMemoria,pagina[3])        
        print("Processo: ",pagina[3],"inserido na memória")
        pagina[3] = pagina[3][0]
        self.memoriaVirtual.insert(self.ponteiro%self.tamanhoMemoria,pagina)        
        self.contador+=1 
        self.ponteiro+=1 #O self.ponteiro deve andar sempre que a página mais antiga for trocada
        
      
        break
      else:
        self.memoriaVirtual[self.ponteiro%self.tamanhoMemoria][0]=0
        self.ponteiro+=1#Se a página mais antiga ainda foi referenciada, zera o bitR e anda o ponteiro   
    return processoSaiu
#--------------------------------------------------------------------------------------------------
  def printMemoriaVirtual(self):
    for i in self.memoriaVirtual:
      print(i)      
      
  def printMemoriaFisica(self):
    self.memoriaSwapping.print()

  def decrementaTempoExecutando(self):
    self.memoriaSwapping.decrementaTempoExecutando()
  
  def controleTempoBitR(self):
    now = datetime.now()
    for i in self.memoriaVirtual:
      segundosAgora = now.second
      if i[1]>= 55 and i[1] < 60:
        if abs(segundosAgora-i[1]) <= 55 and i[0] == 1:
          i[0] = 0
      else:
          if abs(segundosAgora-i[1]) >= 5 and i[0] == 1:
            i[0] = 0

  def esvazearMemorias(self):
    for i in range(0,len(self.memoriaVirtual)):
      self.memoriaVirtual[i][0]=0
      self.memoriaVirtual[i][3]=0
    self.memoriaSwapping.esvazear()  