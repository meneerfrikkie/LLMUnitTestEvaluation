import os
import datasets

# Load the HumanEval dataset
dataset = datasets.load_dataset("openai_humaneval")

# Initialize the loop variable
i = 0  

for row in dataset["test"]:  # Or iterate over the desired split
    problem_text = row["prompt"]
    problem_solution = row["canonical_solution"]
    problem_id = row["task_id"]  # Assuming "id" is the unique identifier

    # Create a directory for the program
    folder_name = f"program_{i+1}"  # Add underscore for readability
    os.makedirs(folder_name, exist_ok=True)

    # Create the Python file and write the solution content
    filename = os.path.join(folder_name, f"program_{i+1}.py")
    with open(filename, "w", encoding='utf-8') as file:
        file.write(problem_solution)

    print(f"Solution for program {i+1} saved to {filename}")

    i += 1  # Increment the loop variable
