from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
from random import choice

app = FastAPI()

# Ejercicio 1: Agregar Pokémon favorito
# Lista inicial Pokémon favoritos
favorite_pokemons = []

# Modelo Pydantic para Pokémon
class Pokemon(BaseModel):
    id: int
    name: str
    type: str
    level: int

# Endpoint para agregar Pokémon
@app.post("/pokemons/", response_model=Pokemon)
async def add_pokemon(pokemon: Pokemon):
    # Verificar si el Pokémon ya existe
    for existing_pokemon in favorite_pokemons:
        if existing_pokemon.id == pokemon.id:
            raise HTTPException(
                status_code=400,
                detail=f"Pokémon con ID {pokemon.id} ya existe"
            )
    
    # Agregar el nuevo Pokémon
    favorite_pokemons.append(pokemon)
    return pokemon

# Ejercicio 2: (Mostrar Pokemons) Modificado por el Ejercicio 4:
@app.get("/pokemons/filter/", response_model=List[Pokemon])
async def filter_pokemons(type: Optional[str] = None, level: Optional[int] = None):
    filtered_pokemons = favorite_pokemons.copy()
    if type:
        filtered_pokemons = [p for p in filtered_pokemons if p.type.lower() == type.lower()]
    
    if level is not None:
        filtered_pokemons = [p for p in filtered_pokemons if p.level == level]
    
    if not filtered_pokemons:
        raise HTTPException(
            status_code=404,
            detail="No se encontraron Pokémon que coincidan con los filtros"
        )
    
    return filtered_pokemons
# Ejercicio 3: Mostrar un Pokémon específico por ID
@app.get("/pokemons/{pokemon_id}", response_model=Pokemon)
async def get_pokemon(pokemon_id: int):
    for pokemon in favorite_pokemons:
        if pokemon.id == pokemon_id:
            return pokemon
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Pokémon con ID {pokemon_id} no encontrado"
    )

# Ejercicio 5: Asigna un Pokémon inicial a tu equipo
# Variable para almacenar el equipo Pokémon (inicialmente vacío)
pokemon_team = []

@app.post("/team/assign-starter/", response_model=Pokemon)
async def assign_random_starter(force_replace: bool = False):
    global pokemon_team
    
    # Verificar si ya hay un Pokémon inicial en el equipo
    existing_starter = next((p for p in pokemon_team if p.id in [pokemon.id for pokemon in favorite_pokemons]), None)
    
    if existing_starter:
        if not force_replace:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya tienes un Pokémon inicial en tu equipo. Usa force_replace=True para reemplazarlo"
            )
        # Remover solo si es un Pokémon inicial
        pokemon_team = [p for p in pokemon_team if p.id not in [pokemon.id for pokemon in favorite_pokemons]]
    
    # Seleccionar un Pokémon inicial aleatorio
    if not favorite_pokemons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay Pokémon iniciales disponibles"
        )
    
    random_starter = choice(favorite_pokemons)
    pokemon_team.append(random_starter)
    
    return random_starter

# Endpoint adicional para ver el equipo actual
@app.get("/team/", response_model=List[Pokemon])
async def get_team():
    return pokemon_team

# Ejercicio 6: Actualizar la información del Pokémon
@app.put("/pokemons/{pokemon_id}", response_model=Pokemon)
async def update_pokemon(pokemon_id: int, updated_pokemon: Pokemon):
    # Buscar el Pokémon en la lista de favoritos
    for index, pokemon in enumerate(favorite_pokemons):
        if pokemon.id == pokemon_id:
            # Actualizar nombre, tipo y nivel (excepto el ID)
            favorite_pokemons[index] = Pokemon(
                id=pokemon_id,  # Mantener el ID original
                name=updated_pokemon.name,
                type=updated_pokemon.type,
                level=updated_pokemon.level
            )
            return favorite_pokemons[index]
    
    # Si no se encuentra el Pokémon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Pokémon con ID {pokemon_id} no encontrado"
    )
    
# Ejercicio 7: Eliminar un Pokémon de la Lista Inicial
@app.delete("/pokemons/{pokemon_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pokemon(pokemon_id: int):
    # Buscar y eliminar el Pokémon
    for i, pokemon in enumerate(favorite_pokemons):
        if pokemon.id == pokemon_id:
            favorite_pokemons.pop(i)
            return f'Pokemon {i.name} ha sido borrado'
    
    # Si no se encuentra el Pokémon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Pokémon con ID {pokemon_id} no encontrado"
    )

