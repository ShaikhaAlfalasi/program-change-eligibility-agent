# Program Change Eligibility Agent

AI agent for evaluating student eligibility for undergraduate program change requests at the University of Sharjah.

## Overview

The agent retrieves the required student and program information from Supabase, gathers the requested program's study plan and requirements, performs deterministic eligibility checks, and sends the resulting evidence package to Gemini for processing and generation of the final eligibility assessment.

## Project Structure

### Core Files

* **`eligibility_agent.py`** — Main agent workflow. Validates the request ID and request type, builds the evidence package, runs the eligibility checks, constructs the Gemini prompt, sends the evidence to the LLM, and extracts the final recommendation (`APPROVE`, `REJECT`, or `REQUIRES_REVIEW`).

* **`database.py`** — Handles the Supabase database operations required by the agent, including retrieving the request, student information, current program, requested program, completed courses, and related program data.

* **`eligibility_checks.py`** — Performs the deterministic eligibility calculations, including checking the student's CGPA requirement, identifying applicable completed courses, calculating completed and applicable credit hours, and determining whether the required thresholds are satisfied.

* **`evidence.py`** — Builds the evidence package provided to Gemini. It gathers the student's information, current and requested program details, study-plan information, university course information, and other supporting evidence into a structured format for the LLM.

* **`llm_client.py`** — Handles the Gemini API connection, sends the prepared eligibility evidence and prompt to the LLM, and provides a fallback response when the Gemini request cannot be completed.

### Data

The **`data/`** folder contains reference information used by the agent:

* **`bachelors_program_catalog.txt`** — Contains the bachelor's degree program catalog used to identify available programs and program details.

* **`program_change_constraints.txt`** — Contains the rules and requirements used to evaluate whether a student satisfies the conditions for a program change.

* **`university_courses.txt`** — Contains the university mandatory course list used when determining applicable completed courses and credit hours.

### Tests

* **`test_database.py`** — Tests the Supabase database retrieval functions.

* **`test_eligibility_checks.py`** — Tests the deterministic eligibility calculations, including CGPA and applicable credit-hour checks.

* **`test_evidence.py`** — Tests the construction of the evidence package provided to Gemini.

* **`test_llm_client.py`** — Tests the Gemini LLM client and its API interaction.

* **`test_eligibility_agent.py`** — Runs an end-to-end test of the complete Program Change Eligibility Agent.

* **`test_config.py`** — Contains configuration used by the test environment.

### Supabase

* **`supabase/`** — Contains the Supabase project configuration and database-related files associated with the agent.
