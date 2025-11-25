minerals = {
    "quartz" :
    {
        "hardness": 7,
        "luster": "vitreous",
        "colour": "white"
    },
    "calcite" :
    {
        "hardness": 3,
        "luster": "vitreous",
        "colour": "white"
    },
    "talc" :
    {
        "hardness": 1,
        "luster": "pearly",
        "colour": "white"
    },
    "gypsum" :
    {
        "hardness": 2,
        "luster": "vitreous",
        "colour": "white"
    },
    "feldspar" :
    {
        "hardness": 6,
        "luster": "vitreous",
        "colour": "white"
    },
    "pyrite" :
    {
        "hardness": 6,
        "luster": "metallic",
        "colour": "greenish"
    },
    "heamitite" :
    {
        "hardness": 5.5,
        "luster": "metallic",
        "colour": "Reddish brown"
    },
    "galena" :
    {
        "hardness": 2.5,
        "luster": "metallic",
        "colour": "grey"
    },
    "graphite" :
    {
        "hardness": 1.5,
        "luster": "metallic",
        "colour": "black"
    }
}
        
def mineral_identification(hardness,luster,colour):
    possible = []
    for mineral, props in minerals.items():
        if (abs(props["hardness"] - hardness) <= 0.5 and props["luster"] == luster.lower() and props["colour"] == colour.lower()):
            possible.append(mineral)
            return possible

hardness = float(input("what is the hardness of this mineral? - "))
luster = (input("what is the luster of this mineral? - ")).lower()
colour = (input("what is the colour of this mineral? - ")).lower()

results = mineral_identification(hardness, luster, colour)
if results: 
    for mineral in results:
        print(mineral)

else:
    print("No Exact match  found!")

