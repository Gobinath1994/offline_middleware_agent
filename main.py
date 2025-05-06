# ------------------------------------------------------------------------------
# Import necessary modules
# ------------------------------------------------------------------------------

from fastapi import FastAPI                  # FastAPI is the web framework for building REST APIs
from pydantic import BaseModel               # Pydantic is used for validating incoming request data
from langchain_agent import agent            # Your initialized LangChain agent (imported from local module)

# ------------------------------------------------------------------------------
# Create FastAPI app instance
# ------------------------------------------------------------------------------

app = FastAPI()

# ------------------------------------------------------------------------------
# Define the request schema using Pydantic
# ------------------------------------------------------------------------------

class QueryRequest(BaseModel):
    query: str    # Expecting a JSON body with a "query" string (natural language input)

# ------------------------------------------------------------------------------
# Define the /query POST endpoint
# ------------------------------------------------------------------------------

@app.post("/query")
async def process_query(req: QueryRequest):
    """
    Accepts a natural language query from the frontend and returns the LLM agent's response.
    
    Args:
        req (QueryRequest): JSON request body containing the user's natural language query.
    
    Returns:
        dict: Contains both the original input and the agent's generated output.
    """

    # Log the incoming query for debugging
    print(f"🚀 Received query: {req.query}")

    try:
        # Invoke the agent with the user query
        response = agent.invoke(req.query)

        # Log the agent's result
        print(f"✅ LLM response: {response}")

        # Return input and response in a JSON structure
        return {"input": req.query, "output": response}

    except Exception as e:
        # Catch and log any unexpected error
        print(f"❌ Error in agent: {e}")

        # Return a safe fallback response
        return {"input": req.query, "output": f"Error: {e}"}