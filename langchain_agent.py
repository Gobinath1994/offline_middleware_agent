# Import OpenAI wrapper from LangChain (supports local LLMs via OpenAI-compatible APIs)
from langchain_community.llms import OpenAI

# Import LangChain agent utilities
from langchain.agents import initialize_agent, Tool, AgentType

# Import your custom tool function to fetch overdue invoices
from tools.crm_tools import get_overdue_invoices

# ------------------------------------------------------------------------------
# Step 1: Configure connection to your local LLM (e.g., LM Studio)
# ------------------------------------------------------------------------------

llm = OpenAI(
    base_url="http://192.168.0.14:1234/v1",  # Local LLM server (compatible with OpenAI API)
    api_key="lm-studio",                    # Dummy key, required even for local models
    model_name="mistral"                    # Name of the model being served (e.g., Mistral 7B)
)

# ------------------------------------------------------------------------------
# Step 2: Register tools (functions the agent is allowed to call)
# ------------------------------------------------------------------------------

tools = [
    Tool(
        name="get_overdue_invoices",                # Name the agent will reference
        func=get_overdue_invoices,                  # Actual Python function to run
        description="Fetch overdue invoices for a customer. Provide the customer name as input."  # Help text for the LLM
    )
]

# ------------------------------------------------------------------------------
# Step 3: Initialize LangChain Agent (ReAct-style zero-shot agent)
# ------------------------------------------------------------------------------

agent = initialize_agent(
    tools=tools,                                   # List of tools the agent can use
    llm=llm,                                       # Language model (LLM) to interpret user queries
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,   # Agent strategy: ReAct-style zero-shot tool use
    verbose=True,                                  # Print internal agent reasoning to the console
    handle_parsing_errors=True,                    # Gracefully handle formatting issues from the LLM

    # Agent behavior configuration (instructional prompt)
    agent_kwargs={
        "prefix": (
            "You are an internal AI assistant that responds to CRM/ERP queries using tools.\n"
            "You must follow this structure strictly:\n\n"
            "Thought: <your reasoning>\n"
            "Action: <tool name from the list>\n"
            "Action Input: <tool input as a string>\n\n"
            "Then wait for the Observation.\n"
            "Repeat Thought → Action → Action Input if needed.\n"
            "When ready, give the user the result like:\n"
            "Final Answer: <your complete answer>\n\n"
            "⚠️ Do NOT skip 'Action Input'.\n"
            "⚠️ Do NOT mix 'Final Answer' with any 'Action'.\n"
            "Only use tools exactly as named."
        ),
        "max_iterations": 10,                       # Max steps the agent can take before stopping
        "early_stopping_method": "generate"         # If limit hit, try to generate final answer anyway
    }
)