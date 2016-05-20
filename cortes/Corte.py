
import Queue as Q

class Tela( object ):

    def __init__( self , ancho , alto , cortes ):
        self.ancho = ancho 
        self.alto = alto 
        self.i_actual = 0
        self.j_actual = 0
        self.cortes = cortes

    def cortar( self ):
        cola = Q.PriorityQueue()
        for corte in self.cortes:
            cola.put( corte )
        parada = False
        i = 1 # i representa el i actual
        j = 1 # j representa el j actual
        iMax = self.alto # iMax representa la altura maxima a la que se va a insertar
        renglon_nuevo = True
        inserciones = []
        while parada != True:
            meto = False
            intentos = []
            iMax = self.alto - i + 1
            while meto != True:
                if cola.qsize() == 0:
                    break
                corte = cola.get( )
                if corte.cabe( self.ancho - j  + 1 , iMax - i + 1 ) == True:
                    iMax = corte.alto 
                    j = j + corte.ancho
                    inserciones.append( corte )
                    renglon_nuevo = False
                    corte.cantidad = corte.cantidad - 1
                    if corte.cantidad > 0:
                        cola.put( corte )
                    meto = True
                else:
                    invertido = Corte( corte.alto , corte.ancho , corte.cantidad )
                    if invertido.cabe( self.ancho - j  + 1 , iMax - i + 1 ) == True:
                        iMax = invertido.alto 
                        j = j + invertido.ancho
                        inserciones.append( invertido )
                        renglon_nuevo = False
                        invertido.cantidad = corte.cantidad - 1
                        if invertido.cantidad > 0:
                            cola.put( invertido )
                        meto = True
                    else:
                        #revisar si cabe al reves
                        intentos.append( corte )
                        if cola.empty( ):
                            meto = True
                            break
                if meto is True:
                    for intento in intentos:
                        cola.put( intento )
            if meto != True and renglon_nuevo == False:
                renglon_nuevo = True
                i = iMax
            elif meto != True and renglon_nuevo == True:
                parada = True
        return inserciones


                




class Corte(object):
    """esta clase representa un corte"""
    def __init__(self, ancho , alto , cantidad ):
        self.alto = alto
        self.ancho = ancho
        self.area = self.calcular_area( )
        self.cantidad = cantidad

    def calcular_area( self ):
        return self.ancho * self.alto

    def cabe( self , ancho , alto ):
        if self.ancho <= ancho and self.alto <= alto :
            return True
        return False

    def __cmp__( self , other ):
        return cmp( self.area , other.area ) * -1

    def __str__(self):
        return "ancho: %i alto:%i " % ( self.ancho , self.alto )
        


