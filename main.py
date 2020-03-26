from pprint import pprint
from algoritmo import AlgoritmoBarrido
from Punto import Punto
from Segmento import Segmento
from Vertice import Vertice
from Arista import Arista
from Cara import Cara

def main():

  s1 = Segmento(Punto(0,0), Punto(10,10))
  s2 = Segmento(Punto(2,1), Punto(1,2))
  segmentos = [s1,s2]
  for s in segmentos:
      print(s)
  barr = AlgoritmoBarrido(segmentos)
  
  barr.barrer()  
#  for e in barr:
#    print(e)
  print(barr.R)

if __name__=="__main__":
    main()



