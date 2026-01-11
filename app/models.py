from pydantic import BaseModel

# Input: What user must send
class RecipeRequest(BaseModel):
    craving: str

# Output
class RecipeResponse(BaseModel):
    recipe_name: str
    ingredients: str
    instructions: str
    heath_analysis: str
    
