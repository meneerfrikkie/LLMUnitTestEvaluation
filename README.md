# Exploring Claude AI's Capability in Unit Test Generation: An Investigative Study
## ELEN4010: Individual Project

## Author
Muaawiyah Dadabhay (https://github.com/meneerfrikkie)
Student Number: 2426234  

---

## Description

This repository contains scripts and data files related to the ELEN4010 Individual Ibvestigation Report. In this investigation, a dataset of Python programs known as HumanEval was used to prompt a Large Language Model (Claude AI) with the task of generating unit tests for these programs. Three key metrics were employed to evaluate the effectiveness of the generated unit tests: testing outcomes, branch coverage, and execution time. A Python plugin tool called \texttt{pytest-cov} was used as the evaluation tool, and the testing framework promoted to the AI was Pytest. The testing outcomes resulted in a 45.00\% pass rate. The branch coverage achieved by the generated unit tests averaged an impressive 96.11\%. Additionally, the average execution time of a single unit test was found to be 0.08 seconds, meeting the commonly accepted criterion of being under 1.00 seconds.

---

## Files

1. `loadHumanEval.py`:
2. `generateUnitTests.py`
3. `runTests.sh`
4. `testResults.txt`
5. `database.pdf`: PDF version of the project database.
6. `database.csv`: CSV version of the project database.

---

## Acknowledgments

The script `loadHumanEval.py` has been provided by T. Kolia (Student Number: 2423748). My sincere gratitude for their contribution to assisting me in extracting data from the HumanEval dataset.

---

## Usage

1. **Prerequisites:**
   - Ensure Python is installed on your system.
   - Install pytest and pytest-cov by running:
     ```bash
     pip install pytest pytest-cov
     ```
   - Obtain an API key from Anthropics. You can activate the API in the environment via:
     ```bash
     export ANTHROPIC_API_KEY="your_api_key"
     ```

2. **Running the scripts:**
   - Execute `loadHumanEval.py` by running: `python loadHumanEval.py`
   - Execute `generateUnitTests.py` by running: `python generateUnitTests.py`
   - Execute `runTests.sh` by running: `./runTests.sh`
   - View generated outputs in `testResults.txt`.
   - Utilize `database.pdf` and `database.csv` for reference or analysis.
