class Disco:
  def __init__(self,nomeArquivo):
    self.nomeArquivo = nomeArquivo

  def retirarProcessoDisco(self,indice):
    arquivoLeitura = open(self.nomeArquivo, 'r')

    linhasFinal = "" 
    retornarLinha = ""
    for linha in arquivoLeitura:
      linhaSplit = linha.split(";")       
      if(linhaSplit[0]==str(indice)):  
        retornarLinha = linha
      else:
        linhasFinal += linha 
    arquivoEscrita = open(self.nomeArquivo, 'w')
    arquivoEscrita.write(linhasFinal)

    arquivoLeitura.close()
    arquivoEscrita.close()      
    return retornarLinha.replace("\n","")

  def retirarMaisUrgente(self):
    arquivoLeitura = open(self.nomeArquivo, 'r')
    menorTempo = 100000
    menorIndice = 0
    for linha in arquivoLeitura:
      linhaSplit = linha.split(";") 
      if(int(linhaSplit[3])<menorTempo):
        menorTempo = int(linhaSplit[3])
        menorIndice = int(linhaSplit[0])
    arquivoLeitura.close()

    return self.retirarProcessoDisco(menorIndice)
    

  def escreverProcessoDisco(self,processo,ultimo):
    arquivoEscrita = open(self.nomeArquivo, 'a')
    processoSplit = processo.split(";")
    if(processoSplit[2]==str(0)):
      print("Processo: "+processo+" Terminou a execução!")
    else:          
      if(ultimo==True):
        arquivoEscrita.write(processoSplit[0]+";"+processoSplit[1]+";"+processoSplit[2]+";"+processoSplit[3]) 
      else:
        arquivoEscrita.write(processoSplit[0]+";"+processoSplit[1]+";"+processoSplit[2]+";"+processoSplit[3]+"\n")
      print("Processo: "+processo+" voltou para o disco!")
      arquivoEscrita.close()    

  def decrementarTempoRestante(self):
    arquivoLeitura = open(self.nomeArquivo, 'r')  
    arquivoFinal = ""
    tempoFinal = 0
    for linha in arquivoLeitura:
      linhaSplit = linha.split(";")
      if(int(linhaSplit[3])>0):
        tempoFinal = int(linhaSplit[3])-1
      arquivoFinal += linhaSplit[0]+";"+linhaSplit[1]+";"+linhaSplit[2]+";"+str(tempoFinal)+"\n" 

    arquivoLeitura.close()
    arquivoEscrita = open(self.nomeArquivo, 'w')
    arquivoEscrita.write(arquivoFinal)

    arquivoEscrita.close()
    

  def existeProcessoPronto(self):
    arquivoLeitura = open(self.nomeArquivo, 'r')  
    for linha in arquivoLeitura:
      linhaSplit = linha.split(";")
      if(linhaSplit[3]=="0\n"): 
        arquivoLeitura.close()  
        return True     
    arquivoLeitura.close()      
    return False     
    
  
  def vazio(self):
    arquivoLeitura = open(self.nomeArquivo, 'r')  
    conteudo = ""
    for i in arquivoLeitura:
      conteudo+=i
    
    if(conteudo==""):
      arquivoLeitura.close()
      print(conteudo)
      return True      
    arquivoLeitura.close() 
    return False  
     

  def print(self):
    arquivoLeitura = open(self.nomeArquivo, 'r')  
    for linha in arquivoLeitura:
        print(linha)  
    arquivoLeitura.close()  