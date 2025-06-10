# Project Setup & Workflow Augmented Analytics Application

In this workshop, we will develop an Augmented Analytics Application using 
Python (programming language), Flask (backend web framework) and Koyeb (cloud 
platform designed for deploying and running web applications).

Below is a structured approach to guide this workshop.

Please use the sample data provided (car data), as this has been properly prepared.

**Minimal project folder structure:**

```bash
project/
│
├── .devcontainer/
│    └── devcontainer.json       → Configuration file for setting up the Dev Container
│
├── app_step_01.py               → The main app file (step 1)
├── Procfile                     → Configuration file for deployment (e.g. on Koyeb)
├── data/
│   ├── autoscout24_data.csv     → .csv file with car data
│   └── credentials.json         → JSON file storing the OpenAI API key
│
├── static/
│   ├── css/
|   |    └── styles.css          → File to define styles (CSS) in HTML pages
|   ├── logo.svg                 → .svg graphic (use your own if required)
|   └── graphic.png              → graphic.png (placeholder, will dynamically be overwritten)
│   
├── templates/
│   └── index_step_01.html       → Main HTML page for user input and output (step 1)
│
└── requirements.txt             → File to specify the Python libraries
```

The following files are **ready to use** and don't need to be modified:
- devcontainer.json 
- Procfile
- autoscout24_data.csv
- logo.svg
- graphic.png
- requirements.txt

The file **app_step_01.py** contains a minimalistic web application to have a starting point.

```bash
# To execute the code in **app_step_01.py** open a Terminal and type:
python app_step_01.py
```

## 1. Audit Existing Files

- Configuration: Check .devcontainer/devcontainer.json and Procfile setup.
- Backend: Discuss the required functionality of app.py in your team.
- Data: Examine the file autoscout24_data.csv.
- OpenAI API-key: Ensure credentials.json is available and contains a valid API-key.
  - An API-key is available on the course days (Week 11 & Week 12) on Moodle.
    (use the API-key only on GitHub Codespaces, do not make it public on GitHub)

```bash
{
	"openai": {
		"api_key": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    }
}
```

- Frontend: Verify templates/ and static/ files for completeness.
- You may add additional .html - files showing a) the data and b) example questions.
- Dependencies: Ensure requirements.txt includes all necessary libraries.

**Outcome:** Clear understanding of what’s available and what needs to be added.

---

## 2. Define Backend Requirements

- Framework: In this course we will use Flask as the web framework.
- Data Handling: Read the file './data/autoscout24_data.csv' to a pandas data frame.
- Routes: Ensure endpoints for the index.html page and each additional .html page.
- API Integration: Securely access credentials.json and handle OpenAI queries.
- Error Handling: Implement error responses for data loading and API failures.
- Deployment: Validate Procfile for production readiness.

**Outcome:** Defined backend structure and integration roadmap.

---

## 3. Define Frontend Requirements

- Ensure index.html contains: 
  - a field for user inputs (prompts)  
  - a field to display the AI-generated Python code  
  - a field to display AI-generated explanations about the Python code.
  - a field to display the output of the executed Python code (text or grapic).
- Styling: Confirm styles.css covers layout and UI elements.

**Outcome:** Frontend structure aligned with backend needs.

---

## 4. Implement Backend Logic

- Load Data: Read autoscout24_data.csv into a pandas DataFrame.
- Define the main route for the web application / → index_step_01.html
- Define routes for each additional .html page (e.g. data.html and questions.html)
- API Integration: Handle OpenAI queries (POST/GET requests).
- Generate, extract and execute the Python code provided by the LLM.
- Testing: Validate functionality using a browser or Postman.

**Outcome:** Fully functional backend with necessary logic.

---

## 5. Connect Frontend to Backend

- Template Variables: Pass data from Flask to HTML.
- Visuals: Generate and store graphics in static/.
- API responses: Display API responses in index.html.

**Outcome:** Seamless frontend-backend integration.

---

## 6. Prepare for Deployment

- Procfile: Ensure it correctly references 'web: gunicorn app:app'.
- Dependencies: Verify requirements.txt includes all required packages.
- Environment Variables: Secure the OpenAI API-key (use only in your GitHub Codespaces environment).

**Outcome:** Deployment-ready project.

---

## 7. Final Testing & Iteration

- Dev Container: Run in GitHub Codespaces to confirm environment consistency.
- Deployment Testing: Push to hosting and verify routes, data, and API calls.
- Feedback & Iteration: Optimize based on user testing.

**Outcome:** A deployed, fully tested application.

---

## 8. Sync Origin with Upstream

```bash
# Option (1): Sync your fork/clone to exactly match the upstream (your local changes will be overwritten)
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