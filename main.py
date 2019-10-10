from disco import Disco
from memoriaSwapping import Memoria 
from memoriaVirtual import MemoriaVirtual 
import time
import threading
import sys

memoriaVirtual = MemoriaVirtual(5)
disco = Disco('arquivo.txt')

def controlaTempo():
  while(True):
    if(t2.isAlive()):
      disco.decrementarTempoRestante()
      memoriaVirtual.decrementaTempoExecutando()
      memoriaVirtual.controleTempoBitR()
      time.sleep(1) 
    else:
      sys.exit(0) #finalizar programa

def controlaRetidadaDisco():
    while(True):
      if(disco.existeProcessoPronto()):
        dados = disco.retirarMaisUrgente() 
        if(dados==""):
          continue
        else:   
          processosRetirados = memoriaVirtual.organizarProcesso(dados)             
          for processo in processosRetirados:
            if(processo!= [0,0,0,0]):
              disco.escreverProcessoDisco(str(processo[0])+";"+str(processo[1])+";"+str(processo[2])+";10",False)
          print("Memoria virtual:\nBitR|Tempo|Índice|Processo")
          memoriaVirtual.printMemoriaVirtual()
          print("Memoria fisica:\nMapa De Bits|Inicio|Fim|Processo")
          memoriaVirtual.printMemoriaFisica()   
          print("--------------------------------------------------------------")
          time.sleep(1) 

      elif(disco.vazio()):
        memoriaVirtual.esvazearMemorias()
        print("disco vazio, fim do programa! ")
        print("Memoria virtual:\nBitR|Tempo|Índice|Processo")
        memoriaVirtual.printMemoriaVirtual() 
        print("Memoria fisica:\nMapa De Bits|Inicio|Fim|Processo")
        memoriaVirtual.printMemoriaFisica()   
        print("--------------------------------------------------------------")
        break    
      else:
        print("Aguade os processos do HD ficarem prontos para executar")  
        time.sleep(1) 

    print("preenchendo novamente o disco para próxima execução")    
    for i in range (0,10):
      if(i==9):
        disco.escreverProcessoDisco(str(i+1)+";500;5;"+str(i+1),True)  
      else:
        disco.escreverProcessoDisco(str(i+1)+";500;5;"+str(i+1),False)    


    sys.exit(0)  
      
t1 = threading.Thread(target=controlaTempo)
t2 = threading.Thread(target=controlaRetidadaDisco)
t2.start()   
time.sleep(0.5) 
t1.start()