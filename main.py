from jugador import Jugador
from inventario import Inventario
from personaje import Personaje
from mago import Mago
from objeto import Objeto
from guerrero import Guerrero

#no es un método porque no está en una clase, entonces es una función

def main():
    pass

# =========
# CREAR JUGADOR
# ==========

    nuevo_jugador = Jugador("Javi")

# =========
# CREAR PERSONAJE
# ==========

    mago = Mago("Gandalf",12,50,150)
    
# =========
# ASOCIAR JUGADOR CON PERSONAJE
# ==========

    nuevo_jugador.seleccionar_personaje(mago)
    nuevo_jugador.mostrar_personaje()
    
# =========
# ATAQUE DEL MAGO
# ==========

    mago.atacar()
    mago.usar_habilidad()

# =========
# CREAR OBJETO
# =========

    pocion = Objeto("Poción de vida", "Consumible")
    staff = Objeto("Staff del Arcangel", "Arma")
    
# =========
# AGREGAR OBJETO AL INVENTARIO
# =========

    mago.inventario.agregar_objeto(pocion)
    mago.inventario.agregar_objeto(staff)

    mago.inventario.mostrar_inventario()

# =========
# RECIBIR DAÑO
# =========

    mago.recibir_danio(15)
    
# =================================================================

# =========
# CREAR PERSONAJE
# ==========

    guerrero = Guerrero("Aragorn",20,100,150)
    
# =========
# ASOCIAR JUGADOR CON PERSONAJE
# ==========

    nuevo_jugador.seleccionar_personaje(guerrero)
    nuevo_jugador.mostrar_personaje()
    
# =========
# ATAQUE DEL MAGO
# ==========

    guerrero.atacar()
    guerrero.usar_habilidad()

# =========
# CREAR OBJETO
# =========

    pocion = Objeto("Poción de fuerza", "Consumible")
    espada = Objeto("Excalibur", "Arma")
    
# =========
# AGREGAR OBJETO AL INVENTARIO
# =========

    guerrero.inventario.agregar_objeto(pocion)
    guerrero.inventario.agregar_objeto(espada)

    guerrero.inventario.mostrar_inventario()

# =========
# RECIBIR DAÑO
# =========

    guerrero.recibir_danio(12)




if __name__ == "__main__":
    main() #aquí digo que si estoy usando un archivo llamado main, entonces ejecuto la función main
    
    