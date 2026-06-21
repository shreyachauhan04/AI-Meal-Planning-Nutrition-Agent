from dotenv import load_dotenv
from src.agent import create_nutrition_agent

# Load OpenAI API key from .env file
load_dotenv()

def main():
    print("Welcome to your AI Nutrition & Meal Planning Agent!")
    agent_executor = create_nutrition_agent()
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        
        response = agent_executor.invoke({"input": user_input})
        print(f"Agent: {response['output']}")

if __name__ == "__main__":
    main()