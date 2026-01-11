from fastapi import FastAPI, HTTPException
from app.models import RecipeRequest
from app.graph import app as agent_app # Importing langgraph brain

# Initialize API
app= FastAPI(
    title="Healthy Crave Agent",
    description="An AI agent that turns bad cravings into healthy recipes. ",
    version="1.0"
)

# Define Endpoint
@app.post("/generate-recipe")
async def generate_recipe(request: RecipeRequest):
    try:
        # Prepare the input for the graph
        initial_state= {"user_craving": request.craving}

        # Run agent using invoke()
        result=agent_app.invoke(initial_state)

        # extract data
        final_recipe=result.get("final_recipe", "Error generating recipe. ")
        analysis=result.get("analysis", "No analysis available. ")

        # Return JSON response
        return {
            "analysis": analysis,
            "recipe": final_recipe
        }

    except Exception as e:
            # If anything explodes, tell user
            raise HTTPException(status_code=500, detail=str(e))

# Health Check
@app.get("/health")
def health_check():
    return {"status": "health", "service": "ready"}