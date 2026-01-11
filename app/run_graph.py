from graph import app

def run():
    print("---- Healthy Craving Agent Starting ----")

    # Input Data
    user_input="I really want samosa and fries"
    initial_state= {"user_craving": user_input}

    # Run the graph
    # Analyst -> Chef -> End
    result= app.invoke(initial_state)

    # Print Result
    print("/n" + "="*50)
    print("FINAL OUTPUT:")
    print("="*50)
    print(result['final_recipe'])

if __name__ == "__main__":
    run()