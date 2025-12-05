from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)

    tools = []  # Add tools here later if needed
    agent = create_agent(model=model, tools=tools)

    print("Welcome! Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        print("\nAssistant: ", end="")
        for chunk in agent.stream([HumanMessage(content=user_input)]):
            if hasattr(chunk, "content") and chunk.content:
                print(chunk.content, end="")

        print()

if __name__ == "__main__":
    main()
