DOCUMENTACIÓN DEL PROYECTO: juegoRol
=======================================
Repositorio: https://github.com/javilass/juegoRol
Autor: javilass
Lenguaje: Python

--------------------------------------------------------------------------------
1. DESCRIPCIÓN GENERAL
--------------------------------------------------------------------------------
juegoRol es un proyecto educativo en Python que simula un pequeño juego de rol
(RPG) por consola. El objetivo principal del proyecto es practicar conceptos
de Programación Orientada a Objetos (POO), específicamente:

    - Herencia (clases Guerrero y Mago heredan de Personaje)
    - Polimorfismo (cada subclase sobrescribe atacar() y usar_habilidad())
    - Composición (cada Personaje tiene un Inventario propio)
    - Encapsulamiento básico de atributos y comportamiento

El programa crea un jugador, le asigna distintos personajes (un mago y un
guerrero), simula ataques, gestiona un inventario de objetos y aplica daño
a los personajes, todo mostrado por consola (print).


--------------------------------------------------------------------------------
2. ESTRUCTURA DE ARCHIVOS
--------------------------------------------------------------------------------
README.md          Título del proyecto (sin contenido adicional).
personaje.py        Clase base Personaje.
guerrero.py         Clase Guerrero (hereda de Personaje).
mago.py             Clase Mago (hereda de Personaje).
jugador.py          Clase Jugador, controla qué personaje se usa.
inventario.py       Clase Inventario, contenedor de objetos.
objeto.py           Clase Objeto, representa ítems del juego.
main.py             Punto de entrada; ejecuta la simulación del juego.


--------------------------------------------------------------------------------
3. DIAGRAMA DE RELACIONES (TEXTUAL)
--------------------------------------------------------------------------------
                     Personaje
                    /          \
              Guerrero         Mago

    Jugador  ---(1 a muchos)--->  Personaje (personaje.py)
    Personaje ---(1 a 1)--->  Inventario
    Inventario ---(1 a muchos)--->  Objeto

--------------------------------------------------------------------------------
4. DESCRIPCIÓN DE CADA MÓDULO
--------------------------------------------------------------------------------

4.1 personaje.py — Clase Personaje
--------------------------------------------------------------------------------
Clase base de la que heredan todos los personajes jugables.

Atributos (definidos en __init__):
    nombre       (str)  Nombre del personaje.
    edad         (int)  Recibe el parámetro "nivel", pero se guarda en el
                         atributo "edad" (ver nota en sección 6, Observaciones).
    vida         (int)  Puntos de vida actuales.
    inventario   (Inventario) Un inventario propio, instanciado automáticamente.

Métodos:
    __init__(nombre, nivel, vida)
        Inicializa nombre, nivel/edad, vida y crea un Inventario nuevo.

    atacar()
        Imprime un mensaje genérico de ataque. Pensado para ser sobrescrito
        (polimorfismo) por las subclases Guerrero y Mago.

    recibir_danio(danio)
        Resta "danio" a la vida del personaje. Si la vida queda bajo 0, se
        fija en 0 (evita vida negativa). Imprime el daño recibido y la vida
        actual resultante.

    usar_habilidad()
        Imprime un mensaje genérico de habilidad. También pensado para ser
        sobrescrito por las subclases.

    mostrar_informacion()
        Imprime nombre, nivel y vida del personaje.
        (Contiene un bug: usa self.nivel, atributo que no existe — ver
        sección 6, Observaciones).


4.2 guerrero.py — Clase Guerrero (hereda de Personaje)
--------------------------------------------------------------------------------
Atributos adicionales:
    fuerza (int)  Puntos de fuerza física del guerrero.

Métodos:
    __init__(nombre, nivel, vida, fuerza)
        Llama a super().__init__() para heredar nombre, nivel, vida e
        inventario, y añade el atributo fuerza.

    atacar()  [sobrescribe a Personaje.atacar]
        Imprime un ataque cuerpo a cuerpo usando los puntos de fuerza.

    usar_habilidad()  [sobrescribe a Personaje.usar_habilidad]
        Imprime el uso de la habilidad "Golpe de espada".


4.3 mago.py — Clase Mago (hereda de Personaje)
--------------------------------------------------------------------------------
Atributos adicionales:
    poder_magico (int)  Puntos de poder mágico del mago.

Métodos:
    __init__(nombre, nivel, vida, poder_magico)
        Llama a super().__init__() para heredar nombre, nivel, vida e
        inventario, y añade el atributo poder_magico.

    atacar()  [sobrescribe a Personaje.atacar]
        Imprime un ataque mágico usando los puntos de poder mágico.

    usar_habilidad()  [sobrescribe a Personaje.usar_habilidad]
        Imprime el uso de la habilidad "Bola de Fuego".


4.4 jugador.py — Clase Jugador
--------------------------------------------------------------------------------
Representa a la persona que juega y controla un personaje.

Atributos:
    nombre       (str)        Nombre del jugador.
    personaje    (Personaje)  Personaje seleccionado (None hasta que se elija).

Métodos:
    __init__(nombre)
        Inicializa el nombre del jugador; personaje queda en None.

    seleccionar_personaje(personaje)
        Asigna un objeto Personaje (o subclase) al jugador e imprime
        confirmación.

    mostrar_personaje()
        Si el jugador tiene un personaje asignado, imprime cuál es;
        si no, informa que no hay personaje seleccionado.


4.5 inventario.py — Clase Inventario
--------------------------------------------------------------------------------
Gestiona una colección de objetos (ítems) asociada a un personaje.

Atributos:
    objetos (list)  Lista de instancias de Objeto.

Métodos:
    __init__()
        Inicializa la lista de objetos vacía.

    agregar_objeto(objeto)
        Añade un Objeto a la lista e imprime confirmación.

    mostrar_inventario()
        Imprime el contenido del inventario. Si está vacío, indica
        "El inventario está vacío"; en caso contrario, lista cada objeto
        con su nombre y tipo.


4.6 objeto.py — Clase Objeto
--------------------------------------------------------------------------------
Representa un ítem del juego (arma, consumible, etc.).

Atributos:
    nombre (str)  Nombre del objeto.
    tipo   (str)  Categoría del objeto (ej: "Arma", "Consumible").

Métodos:
    __init__(nombre, tipo)
        Inicializa nombre y tipo del objeto.

    mostrar_informacion()
        Imprime el nombre y el tipo del objeto.
        (Los mensajes concatenan la palabra "Objeto" directamente sin
        espacio ni separador — ver sección 6, Observaciones).


4.7 main.py — Punto de entrada del programa
--------------------------------------------------------------------------------
Contiene la función main(), que orquesta toda la simulación del juego.
Se ejecuta solo si el archivo se corre directamente (if __name__ == "__main__").

Flujo de ejecución de main():

    1. Crear un Jugador llamado "Javi".

    2. Crear un Mago llamado "Gandalf" (nivel 12, vida 50, poder mágico 150).
    3. Asociar el mago al jugador y mostrarlo.
    4. El mago ataca y usa su habilidad ("Bola de Fuego").
    5. Crear dos Objetos: "Poción de vida" (Consumible) y
       "Staff del Arcangel" (Arma).
    6. Agregar ambos objetos al inventario del mago y mostrarlo.
    7. Aplicar 15 puntos de daño al mago.

    8. Crear un Guerrero llamado "Aragorn" (nivel 20, vida 100, fuerza 150).
    9. Asociar el guerrero al mismo jugador y mostrarlo.
    10. El guerrero ataca y usa su habilidad ("Golpe de espada").
    11. Crear dos Objetos: "Poción de fuerza" (Consumible) y
        "Excalibur" (Arma).
    12. Agregar ambos objetos al inventario del guerrero y mostrarlo.
    13. Aplicar 12 puntos de daño al guerrero.

Nota técnica: la función main() comienza con la instrucción "pass" seguida
del resto del código, todo indentado dentro de la función. En Python,
"pass" no interrumpe la ejecución (es una operación nula), así que el
resto del bloque se ejecuta con normalidad; es simplemente una línea
sobrante sin efecto sobre el comportamiento del programa.


--------------------------------------------------------------------------------
5. CÓMO EJECUTAR EL JUEGO
--------------------------------------------------------------------------------
Requisitos: Python 3 instalado, sin dependencias externas.

Pasos:
    1. Clonar el repositorio:
       git clone https://github.com/javilass/juegoRol.git

    2. Entrar a la carpeta del proyecto:
       cd juegoRol

    3. Ejecutar:
       python main.py
       (o "python3 main.py" según el sistema)

Salida esperada: una secuencia de mensajes por consola describiendo la
creación del jugador, la selección de personajes, los ataques, el manejo
de inventario y el daño recibido por cada personaje (mago y guerrero).


--------------------------------------------------------------------------------
6. OBSERVACIONES Y POSIBLES MEJORAS
--------------------------------------------------------------------------------
Estos son detalles detectados al revisar el código, útiles como guía de
mejora (no son obligatorios, pero corrigen inconsistencias):

  a) mostrar_informacion() de la clase Personaje nunca se llama desde
     main.py, por lo que el bug anterior no se manifiesta al ejecutar el
     programa tal como está.

  b) En objeto.py, mostrar_informacion() imprime "Objeto{self.nombre}" y
     "Objeto{self.tipo}" sin espacio ni separador entre la palabra "Objeto"
     y el valor real, lo que genera una salida poco clara (ej: "ObjetoStaff
     del Arcangel"). Tampoco se usa en main.py actualmente.

  c) El proyecto no maneja entrada del usuario (input()); todos los valores
     están fijados directamente en el código (hardcodeados) dentro de
     main.py. Una mejora natural sería permitir elegir nombre, clase de
     personaje y ver un combate interactivo entre dos personajes.

  d) No hay manejo de errores (por ejemplo, daño negativo, nombres vacíos,
     etc.), lo cual es razonable dado el propósito educativo del proyecto.


--------------------------------------------------------------------------------
7. RESUMEN DE CONCEPTOS DE POO APLICADOS
--------------------------------------------------------------------------------
Herencia:        Guerrero y Mago heredan atributos y métodos de Personaje
                  mediante super().__init__().

Polimorfismo:     Tanto Guerrero como Mago sobrescriben atacar() y
                  usar_habilidad() con comportamientos distintos, aunque
                  se invoquen con la misma interfaz.

Composición:      Cada Personaje "tiene un" Inventario (no "es un"
                  Inventario), y cada Inventario "tiene" una lista de
                  Objetos.

Encapsulamiento:  Cada clase agrupa sus propios atributos y comportamientos
                  relacionados (por ejemplo, Inventario controla el acceso
                  a su lista de objetos mediante agregar_objeto()).


