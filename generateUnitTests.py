from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import os

anthropic = Anthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"],
)

base_dir = os.getcwd()

program_paths = [
    os.path.join(base_dir, "program1", "program1.py"),
    os.path.join(base_dir, "program2", "program2.py"),
    os.path.join(base_dir, "program3", "program3.py"),
    os.path.join(base_dir, "program4", "program4.py"),
    os.path.join(base_dir, "program5", "program5.py"),
    os.path.join(base_dir, "program6", "program6.py"),
    os.path.join(base_dir, "program7", "program7.py"),
    os.path.join(base_dir, "program8", "program8.py"),
    os.path.join(base_dir, "program9", "program9.py"),
    os.path.join(base_dir, "program10", "program10.py"),
    os.path.join(base_dir, "program11", "program11.py"),
    os.path.join(base_dir, "program12", "program12.py"),
    os.path.join(base_dir, "program13", "program13.py"),
    os.path.join(base_dir, "program14", "program14.py"),
    os.path.join(base_dir, "program15", "program15.py"),
    os.path.join(base_dir, "program16", "program16.py"),
    os.path.join(base_dir, "program17", "program17.py"),
    os.path.join(base_dir, "program18", "program18.py"),
    os.path.join(base_dir, "program19", "program19.py"),
    os.path.join(base_dir, "program20", "program20.py"),
    os.path.join(base_dir, "program21", "program21.py"),
    os.path.join(base_dir, "program22", "program22.py"),
    os.path.join(base_dir, "program23", "program23.py"),
    os.path.join(base_dir, "program24", "program24.py"),
    os.path.join(base_dir, "program25", "program25.py"),
    os.path.join(base_dir, "program26", "program26.py"),
    os.path.join(base_dir, "program27", "program27.py"),
    os.path.join(base_dir, "program28", "program28.py"),
    os.path.join(base_dir, "program29", "program29.py"),
    os.path.join(base_dir, "program30", "program30.py"),
    os.path.join(base_dir, "program31", "program31.py"),
    os.path.join(base_dir, "program32", "program32.py"),
    os.path.join(base_dir, "program33", "program33.py"),
    os.path.join(base_dir, "program34", "program34.py"),
    os.path.join(base_dir, "program35", "program35.py"),
    os.path.join(base_dir, "program36", "program36.py"),
    os.path.join(base_dir, "program37", "program37.py"),
    os.path.join(base_dir, "program38", "program38.py"),
    os.path.join(base_dir, "program39", "program39.py"),
    os.path.join(base_dir, "program40", "program40.py"),
]

# Loop through each Program Path
for program_path in program_paths:
    program_name = os.path.splitext(os.path.basename(program_path))[0]
    test_file_path = os.path.join(os.path.dirname(program_path), f"{program_name}_test.py")

    with open(program_path, "r") as f:
        program_code = f.read()

    # Generate unit tests using Anthropic
    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=300,
        prompt=f"{HUMAN_PROMPT} Write unit tests for the following Python code using Pytest. 
        First provide the function followed by the test code. 
        The code is: {AI_PROMPT}\n\n{program_code}\n\n"
    )

    # Extract the code from AI's response
    ai_response = completion.completion

    # Save unit tests to a file
    with open(test_file_path, "w") as f:
        f.write(ai_response)

    print(f"Extracted test code for {program_name} and saved to {test_file_path}")
