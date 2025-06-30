
# Summer School Workshop Structure

This repository contains a collection of notebooks, scripts, and data for various modules in the Summer School program. The structure is organized to support topics in agent-based modeling, local Large Language Models (LLMs), as well as single- and multi-agent augmented analytics.

## Structure Overview

### 📁 Local_LLM_via_Ollama
Hands-on exploration with local LLMs using the Ollama framework:
- `ollama_llms.ipynb`
- `EXERCISES.txt`: Supplementary tasks

### 📁 Python_Single-Agent_Augmented_Analytics
Focused on single-agent analytic workflows:
- `app_step_01.py`: Main application script
- `Slides_*.pdf`: Presentation slides
- 📁 `data`, `static`, `templates`: Supporting folders
- `tiny_llm_next_word_prediction.ipynb`: Notebook for LLM-based prediction

### 📁 Python_Multi-Agent_Augmented_Analytics
Contains multi-agent augmented analytics:
- 📁 `data`: includes `autoscout24_data.csv`

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