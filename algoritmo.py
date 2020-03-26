from Eventos import Eventos
from LineaBarrido import LineaBarrido
from Evento import Evento

class AlgoritmoBarrido():
  def __init__(self, segmentos):
    self.Q=Eventos()
    self.T=LineaBarrido()
    self.R = []
    for s in segmentos:
      p1,p2= s.puntos
      e = Evento(p1)
      e.I.add(s)
      self.Q.add(e)
      e= Evento(p2)
      e.T.add(s)
      self.Q.add(e)

  def __next__(self):
    try:
       e = next(self.Q)
       self.procesar(e)
       return e
    except StopIteration:
      raise StopIteration()
  def __iter__(self):
    return self
  def procesar(self, evento):
    evento=evento[1]
    if not evento: return 
    print(f"Procesando evento {evento}")
    p = evento.coord
    if len(evento.I|evento.T|evento.C) > 1:
      self.R+= (p, evento.I|evento.T|evento.C)
    for s in list(evento.T|evento.C):
      del self.T[s]
    for s in list(evento.I|evento.C):
      self.T.add(s,p.y)
    for s in self.T.segmentos:
      s.calcularX(p.y)
    self.T.ordenar()
    print(f"Linea de barrido {self.T.segmentos}")
    if not evento.I|evento.C:
      si = self.T.izquierda(p.x)
      sd = self.T.derecha(p.x)
      self.encontrarEvento(si,sd,p)
    else:
      sp= sorted(list(evento.I|evento.C), key=lambda s:s.x)[0]
      si= self.T.izquierda(sp.x)
      self.encontrarEvento(si,sp,p)
      spp= sorted(list(evento.I|evento.C), key=lambda s:s.x)[-1]
      sd= self.T.derecha(spp.x)
      self.encontrarEvento(spp,sd,p)
  def encontrarEvento(self, si, sd, p):
    print(f"Comprobar si hay nuevos eventos con {si} y {sd} en {p}")
    if not si or not sd: return
    interseccion = si.interseccion(sd)
    if not interseccion: return
    if p< interseccion:
      e = Evento(interseccion)
      e.C.add(si)
      e.C.add(sd)
      self.Q.add(e)
  def barrer(self):
      for e in self.Q.eventos.q:
        self.procesar(e)
