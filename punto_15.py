from random import choice
from lista import show_list_list, by_name, search

entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]

pokemons = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Pikachu",
        "nivel": 20,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Pikachu",
        "nivel": 33,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Tyrantrum",
        "nivel": 58,
        "tipo": "Roca",
        "subtipo": "Dragón"
    },
    {
        "nombre": "Terrakion",
        "nivel": 62,
        "tipo": "Roca",
        "subtipo": "Lucha"
    },
    {
        "nombre": "Wingull",
        "nivel": 22,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 44,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Dragonite",
        "nivel": 55,
        "tipo": "Dragón",
        "subtipo": "Volador"
    },
    {
        "nombre": "Aerodactyl",
        "nivel": 52,
        "tipo": "Roca",
        "subtipo": "Volador"
    }
]

names = ["Ash Ketchum", "Goh", "Leon", "Chloe", "Raihan"]

lista_entrenadores = []

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)

for pokemon in pokemons:
    pos = search(lista_entrenadores, 'nombre', choice(names))
    if pos is not None:
        lista_entrenadores[pos]['sublist'].append(pokemon)
    else:
        print('no existe el entrenador')

lista_entrenadores.sort(key=by_name)

def cantidad_de_pokemons(entrenador):
    lista_pokemones=[]
    for entrenadores in lista_entrenadores:
        if entrenador==entrenadores["nombre"]:
            lista_pokemones.append(entrenadores["sublist"])
            return lista_pokemones
def promedio_de_nivel_de_pokemons(entrenador):
    total = 0
    cant = 0
    for entrenadores in lista_entrenadores:
        if entrenador == entrenadores["nombre"]:
            for i in entrenadores["sublist"]:
                total += float(i["nivel"])
                cant += 1
            if cant == 0:
                return 0
            promedio = total / cant
            return promedio
    return None
    
def datos_del_entrenador(entrenador):
    datos=[]
    for entrenadores in lista_entrenadores:
        if entrenador==entrenadores["nombre"]:
            datos.append(entrenadores)
            return datos
        
def porcentaje_ganadas():
    nombres=[]
    for entrenador in lista_entrenadores:
        total_batallas = entrenador["batallas_ganadas"] + entrenador["batallas_perdidas"]
        porcentaje=(entrenador["batallas_ganadas"] / total_batallas) * 100
        if porcentaje > 79:
            nombres.append(entrenador["nombre"])
    return nombres

def entrenadores_con_pokemones_de_fuego_planta_y_agua():
    lista=[]
    for entrenador in lista_entrenadores:
        for i in entrenador["sublist"]:
            if i["tipo"]=="Fuego" or i["tipo"]=="Planta" or i["tipo"]=="Agua" and i["subtipo"]=="Volador":
                datospokemon=[i["nombre"]+"-"+i["tipo"]]
                if i["tipo"]=="Agua":
                    datospokemon=[i["nombre"]+"-"+i["tipo"]+"-"+i["subtipo"]]
                lista.append(entrenador["nombre"])
                lista.append(datospokemon)
    return lista
def entrenadores_con_pokemon_determinado(pokemon):
    entrenadores_con_pokemon = []
    for entrenador in lista_entrenadores:
        for pokemones in entrenador["sublist"]:
            if pokemones["nombre"] == pokemon:
                entrenadores_con_pokemon.append(entrenador["nombre"])
                break
    return entrenadores_con_pokemon
def entrenadores_con_pokemons_repetidos():
    entrenadores_repetidos = []
    for entrenador in lista_entrenadores:
        nombres_pokemons = [pokemon["nombre"] for pokemon in entrenador["sublist"]]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            entrenadores_repetidos.append(entrenador["nombre"])
    return entrenadores_repetidos

def entrenadores_con_pokemons_especificos():
    entrenadores_especificos = []
    for entrenador in lista_entrenadores:
        for pokemon in entrenador["sublist"]:
            if pokemon["nombre"]=="Tyrantrum" or pokemon["nombre"]=="Terrakion" or pokemon["nombre"]=="Wingull":
                entrenadores_especificos.append(entrenador["nombre"])
                break
    return entrenadores_especificos

def entrenador_tiene_pokemon(entrenador_nombre, pokemon_nombre):
    for entrenador in lista_entrenadores:
        if entrenador["nombre"] == entrenador_nombre:
            for pokemon in entrenador["sublist"]:
                if pokemon["nombre"] == pokemon_nombre:
                    return entrenador, pokemon
    return None, None
entrenadores_con_mas_de_3_torneos=[]
mastorneos=0
mayornivel=0
for entrenador in lista_entrenadores:
    if entrenador["torneos_ganados"]>3:
        entrenadores_con_mas_de_3_torneos.append(entrenador["nombre"])
    if entrenador["torneos_ganados"]>mastorneos:
        mastorneos=entrenador["torneos_ganados"]
        entrenadormasganador=entrenador["nombre"]

pos=search(lista_entrenadores,"nombre",entrenadormasganador)
for i in lista_entrenadores[pos]["sublist"]:
    if i["nivel"]>mayornivel:
        mayornivel=i["nivel"]
        pokemondemasnivel=i["nombre"]
                
    
pokemones_de_un_entrenador=cantidad_de_pokemons("Goh")
datos=datos_del_entrenador("Ash Ketchum")
entrenadores_79=porcentaje_ganadas()
lista_entrenadores_con_pokemones_fpya=entrenadores_con_pokemones_de_fuego_planta_y_agua()
promedio_pokemons=promedio_de_nivel_de_pokemons("Ash Ketchum")
entrenadores_con_el_pokemon=entrenadores_con_pokemon_determinado("Pikachu")
entrenadores_repetidos = entrenadores_con_pokemons_repetidos()
entrenadores_especificos = entrenadores_con_pokemons_especificos()
entrenador, pokemon = entrenador_tiene_pokemon("Ash Ketchum", "Charizard")
show_list_list("Entrenador","Pokemones",lista_entrenadores)
print(f"Los pokemones del entredador ingresado son: {len(pokemones_de_un_entrenador)}")
print(f"Los entrenadores con mas de 3 torneos ganados son {entrenadores_con_mas_de_3_torneos}")
print(f"El entrenador con mas torneos ganados es {entrenadormasganador} y su pokemon de mayor nivel es {pokemondemasnivel}")
print("Los datos del entrenador ingresado son:")
show_list_list("Entrenador","Pokemones",datos)
print(f"Los entrenadores con mas del 79 porciento de batallas ganadas son:{entrenadores_79}")
print(f"Los entrenadores con pokemones de fuego, planta y agua/volador son: {lista_entrenadores_con_pokemones_fpya}")
print(f"El promedio de nivel de los pokemones del entrenador ingresado es: {promedio_pokemons}")
print(f"Los entrenadores con el pokemon ingresado son: {entrenadores_con_el_pokemon}")
print(f"Los entrenadores que tienen a Tyrantrum, Terrakion o Wingull son {entrenadores_especificos}")
if entrenador is not None and pokemon is not None:
    print("El entrenador tiene el pokemon, los datos son:")
    print(f"Datos del entrenador: {entrenador['nombre']}")
    print(f"Torneos ganados: {entrenador['torneos_ganados']}")
    print(f"Batallas perdidas: {entrenador['batallas_perdidas']}")
    print(f"Batallas ganadas: {entrenador['batallas_ganadas']}")
    print(f"Datos del Pokémon: {pokemon['nombre']}")
    print(f"Nivel: {pokemon['nivel']}")
    print(f"Tipo: {pokemon['tipo']}")
    print(f"Subtipo: {pokemon['subtipo']}")
else:
    print("El entrenador no tiene el pokemon ingresado")
    