#!/bin/bash

# Get the directory of this script
SCRIPT_DIR="$(dirname "$0")"

# Set the program directory relative to the script directory
PROGRAM_DIR="$SCRIPT_DIR"

# Name of the text file to store results
OUTPUT_FILE="testResults.txt"

# Clear the output file if it exists
> "$OUTPUT_FILE"

# Loop through each program directory
for ((i=1; i<=40; i++))
do
    PROGRAM_PATH="$PROGRAM_DIR/program$i"
    if [ -d "$PROGRAM_PATH" ]; then
        # Run pytest-cov command for the program
        echo "Running tests for program$i..."
        pytest --cov=program$i --cov-report=term --cov-branch "$PROGRAM_PATH/program${i}_test.py" >> "$OUTPUT_FILE" 2>&1
        echo "Tests for program$i finished."
    else
        echo "Program $i not found."
    fi
done

echo "All tests finished. Results stored in $OUTPUT_FILE"
