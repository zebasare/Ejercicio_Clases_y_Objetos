import math

class Punto: 
  def __init__(self,x=0,y=0): 
    self.x=x 
    self.y=y 
  def __str__(self): 
    return f"Punto ubicado en {self.x,self.y}"

  def cuadrante(self): 
    if self.x>0 and self.y>0: 
      print("El punto esta en el primer cuadrante") 
    elif self.x<0 and self.y>0:
      print("El punto esta en el segundo cuadrante")
    elif self.x<0 and self.y<0: 
      print("El punto se encuentra en el tercer cuadrante")
    elif self.x>0 and self.y<0: 
      print("El punto se encuatra en el cuarto cuadrante")
    else: 
      print("El punto se encuentra en el origen") 
  def vector(self,p): 
      vectX=(p.x-self.x) 
      vectY=(p.y-self.y)
      print(f"Vector resultante : {vectX,vectY}")
  def distancia(self,p): 
    dist=math.sqrt( (p.x-self.x)**2 + (p.y-self.y)**2)
    print(f"Distancia del vector generado : ",dist)

class Rectangulo: 
    def __init__(self,inicial=Punto(0,0),final=Punto(0,0)): 
      self.inicial=inicial
      self.final=final
    def base_altura_area(self): 
      base=self.final.x-self.inicial.x 
      altura=self.final.y-self.inicial.y 
      print("Base :",base)
      print("Altura: ",altura)
      print("Area: ", base * altura)









unpunto=Punto()
otropunto=Punto(2,3)
unpunto.cuadrante()
unpunto.vector(otropunto)
unpunto.distancia(otropunto)
rect=Rectangulo(unpunto,otropunto)
rect.base_altura_area()
print("End")

