
# Summer School Workshop Structure

This repository contains a collection of notebooks, scripts, and data for various modules in the Summer School program. The structure is organized to support topics in agent-based modeling, local Large Language Models (LLMs), as well as single- and multi-agent augmented analytics.

## Structure Overview

### 📁 Local_LLM_via_Ollama
Hands-on exploration with local LLMs using the Ollama framework:
- `ollama_llms.ipynb`
- `EXERCISES.txt`: Supplementary tasks

### 📁 Python_Single-Agent_Augmented_Analytics
Focused on single-agent analytic workflows:
- `app.py`: Main application script
- `Slides_*.pdf`: Presentation slides
- 📁 `data`: includes `global-shark-attack.csv`
- 📁 `static`, `templates`: Supporting folders

### 📁 Python_Multi-Agent_Augmented_Analytics
Contains a multi-agent augmented analytics example:
- 📁 `data`: includes `global-shark-attack.csv`

### 📁 Agent_Based_Credit_Risk_Modeling
Includes Python notebooks and implementations for agent-based modeling in the context of credit risk:
- `agent_based_model_credit_risk.ipynb`
- `agent_based_modeling_money_agents.ipynb`
- `agent_based_modeling_agentpy` (folder)
- `agent_based_modeling_mesa` (folder)
- `Slides_*.pdf`: Presentation slides for workshops

### 📄 Additional Files
- `Syllabus-Summer-2025_DataScience_Fintech_GELL.pdf`: Program syllabus
- `requirements.txt`: Python dependencies
- `.gitignore`, `.devcontainer/`: Development environment configuration

---

This structure allows participants to navigate easily between course materials, code, and datasets. Each folder corresponds to a key topic in the program.

## Run OLLAMA in your Codespace
   
   Ollama is software designed to simplify the process of running open-source large language models (LLMs) on your local computer / in your Codespace. It acts as a local model manager and runtime, handling everything from downloading the model files to setting up a local environment where you can interact with them.

   Ollama has already been installed in your codespace (see files devcontainer.json and setup.sh).

   For an overview of available LLMs see: https://ollama.com/search.

   To run ollama on GitHub Codespaces, import LLMs etc., open a new Terminal and type:
   ```bash
   # Start ollama (keep Terminal open)
   ollama serve

   # Open a new Terminal and use the following command to list all available LLMs
   ollama list

   # Import and run LLM 'Llama 3.2' (2.0 GB)
   ollama run llama3.2:latest

   # Quit the model
   /bye

   # Find running ollama processes
   ps aux | grep ollama

   # Stop all ollama processes
   pkill -f ollama
   ```


## Sync Origin with Upstream

```bash
# Option (1): Sync your fork/clone to exactly match the upstream (your local changes may be overwritten)
git fetch upstream
git checkout master
git reset --hard upstream/master
git push origin master --force

# Option (2): Sync your fork/clone with the upstream (your local changes are preserved but merge conflicts may have to be resolved)
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
```