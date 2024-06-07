from lista import remove,show_list

superheroes = [
    {
        "nombre": "Superman",
        "año_aparicion": 1938,
        "casa_comic": "DC",
        "biografia": "Superman, cuyo nombre real es Kal-El, es un kryptoniano que fue enviado a la Tierra antes de la destrucción de su planeta natal, Krypton. Criado como Clark Kent en Smallville, usa sus poderes para proteger a la humanidad."
    },
    {
        "nombre": "Batman",
        "año_aparicion": 1939,
        "casa_comic": "DC",
        "biografia": "Batman, el alter ego de Bruce Wayne, es un vigilante de Gotham City que combate el crimen tras presenciar el asesinato de sus padres cuando era niño. Utiliza su inteligencia, habilidades de combate y tecnología avanzada."
    },
    { 
        "nombre": "Capitana Marvel",
        "año_aparicion": 1968,
        "casa_comic": "Marvel",
        "biografia": "Capitana Marvel, cuyo nombre real es Carol Danvers, es una antigua oficial de la Fuerza Aérea de los Estados Unidos que obtiene poderes sobrehumanos tras fusionarse con el ADN de un extraterrestre Kree. Sus habilidades incluyen fuerza sobrehumana, vuelo y la capacidad de absorber y proyectar energía. Es una de las heroínas más poderosas del universo Marvel."
    },
    {
        "nombre": "Wonder Woman",
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Wonder Woman, también conocida como Diana Prince, es una princesa amazona de la isla de Themyscira. Dotada de poderes divinos y entrenada en el combate, lucha por la justicia, el amor y la igualdad. Es conocida por su lazo de la verdad, sus brazaletes indestructibles y su tiara, que puede ser usada como un arma."
    },
    {
        "nombre": "Wonder Woman",
        "año_aparicion": 1941,
        "casa_comic": "DC",
        "biografia": "Wonder Woman, también conocida como Diana Prince, es una princesa amazona de la isla de Themyscira. Dotada de poderes divinos y entrenada en el combate, lucha por la justicia, el amor y la igualdad."
    },
    {
        "nombre": "Spider-Man",
        "año_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "Spider-Man, o Peter Parker, es un joven neoyorquino que obtiene habilidades arácnidas después de ser mordido por una araña radiactiva. Combina sus deberes de superhéroe con los desafíos cotidianos de su vida personal, usa un traje rojo y azul."
    },
    {
        "nombre": "Iron Man",
        "año_aparicion": 1963,
        "casa_comic": "Marvel",
        "biografia": "Iron Man es el alter ego de Tony Stark, un multimillonario y genio inventor que, tras una grave herida, crea una armadura avanzada para salvar su vida y combatir el mal. Es uno de los miembros fundadores de los Vengadores."
    },
    {
        "nombre": "Captain America",
        "año_aparicion": 1941,
        "casa_comic": "Marvel",
        "biografia": "Captain America, cuyo nombre real es Steve Rogers, es un supersoldado creado durante la Segunda Guerra Mundial. Con su escudo indestructible y su sentido del honor, lucha por la libertad y la justicia."
    },
    {
        "nombre": "Thor",
        "año_aparicion": 1962,
        "casa_comic": "Marvel",
        "biografia": "Thor es el dios del trueno en la mitología nórdica y uno de los superhéroes más poderosos de Marvel. Con su martillo Mjolnir, lucha para proteger a la Tierra y los Nueve Reinos de diversas amenazas."
    },
    {
        "nombre": "The Flash",
        "año_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "The Flash, conocido como Barry Allen, es el hombre más rápido del mundo. Utiliza su increíble velocidad para combatir el crimen y proteger Central City, además de ser un miembro clave de la Liga de la Justicia."
    },
    {
        "nombre": "Star-Lord",
        "año_aparicion": 1976,
        "casa_comic": "Marvel",
        "biografia": "Star-Lord, cuyo nombre real es Peter Jason Quill, es un aventurero intergaláctico y líder de los Guardianes de la Galaxia. Es hijo de una humana y el rey de un imperio alienígena. Peter Quill es conocido por su ingenio, su valentía y su habilidad para liderar, así como por su uso de tecnología avanzada y armamento especializado."
    },  
    {
        "nombre": "Green Lantern",
        "año_aparicion": 1940,
        "casa_comic": "DC",
        "biografia": "Green Lantern es el alias de varios superhéroes, siendo Hal Jordan el más conocido. Miembro del Green Lantern Corps, utiliza un anillo de poder para crear construcciones de luz sólida y mantener la paz en el universo."
    },
    {
        "nombre": "Wolverine",
        "año_aparicion": 1974,
        "casa_comic": "Marvel",
        "biografia": "Wolverine, también conocido como Logan, es un mutante con habilidades regenerativas, garras retráctiles y un esqueleto recubierto de adamantium. Es un miembro clave de los X-Men y conocido por su ferocidad en el combate."
    },
    {
        "nombre": "Doctor Strange",
        "año_aparicion": 1963,
        "casa_comic": "DC",
        "biografia": "Doctor Strange, cuyo nombre real es Stephen Vincent Strange, es un ex neurocirujano que se convierte en el Hechicero Supremo para proteger la Tierra de amenazas mágicas y místicas. Tras un accidente automovilístico que le dejó las manos gravemente dañadas, buscó la cura en las artes místicas y se convirtió en un poderoso maestro de las artes arcanas."
    }
]
superheroes_con_traje=[]
superheroes_1963=[]
info_flash_star=[]
superheroes_con_bms=[]
contador1=0
contador2=0

remove(superheroes,"nombre","Green Lantern")
for index,superheroe in enumerate(superheroes):
    if superheroe["nombre"]=="Wolverine":
        añowolverine=superheroe["año_aparicion"]
    if superheroe["nombre"]== "Doctor Strange":
        superheroe["casa_comic"]="Marvel"
    if "traje" in superheroe["biografia"] or "armadura" in superheroe["biografia"]:
        superheroes_con_traje.append(superheroe["nombre"])
    if superheroe["año_aparicion"]<1963:
        superheroes_1963.append(superheroe["nombre"])
    if superheroe["nombre"]== "Capitana Marvel":
        casa_capitana=superheroe["casa_comic"]
    if superheroe["nombre"]== "Wonder Woman":
        casa_wonder=superheroe["casa_comic"]
    if superheroe["nombre"]=="The Flash" or superheroe["nombre"]=="Star-Lord":
        info_flash_star.append(superheroe)
    if superheroe["nombre"].startswith("B") or superheroe["nombre"].startswith("M") or superheroe["nombre"].startswith("S"):
        superheroes_con_bms.append(superheroe["nombre"])
    if superheroe["casa_comic"]=="Marvel":
        contador1+=1
    if superheroe["casa_comic"]=="DC":
        contador2+=1

show_list("---Superheroes",superheroes)
print(f"El año de aparicion de Wolverine es: {añowolverine}")
show_list("---Superheroes con traje o armadura",superheroes_con_traje)
show_list("---Superheroes cuya fecha de aparición es anterior a 1963",superheroes_1963)
print(f"La casa de Capitana Marvel es {casa_capitana.upper()} y la casa de Wonder Woman es {casa_wonder.upper()}")
show_list("---Informacion de Flash y Star-Lord",info_flash_star)
show_list("---Superheroes que empiezan con B,M y S",superheroes_con_bms)
print(f"La cantidad de superheroes que hay de Marvel son {contador1} y de DC {contador2}")