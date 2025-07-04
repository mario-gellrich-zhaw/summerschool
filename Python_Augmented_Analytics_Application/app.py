"""
This module - when fully developed - sets up a Flask web application that 
interacts with the OpenAI GPT-3.5-turbo model. It loads an OpenAI API key from 
an environmental variable, reads data from a CSV file, and allows users to submit 
prompts to generate Python code that works with the DataFrame loaded from the 
CSV file. The generated code is then executed, and the results are displayed on 
a web page.
"""

import os
import json
from openai import OpenAI
import pandas as pd
from flask import Flask, render_template, request

import io
import sys
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Set your OpenAI API key here or set it as an environment variable
# Linux/macOS (bash/zsh): export OPENAI_API_KEY="your-api-key-here"
# On Windows (Command Prompt): set OPENAI_API_KEY=your-api-key-here
# On Koyeb: set the environment variable in the Koyeb dashboard

# Load OpenAI API key from credentials.json
try:
    with open('../credentials.json', encoding='utf-8') as file:
        credentials = json.load(file)
        API_KEY = credentials['openai']['api_key']
except FileNotFoundError as exc:
    raise ValueError(
        "Please provide OpenAI API key in the credentials.json file."
    ) from exc

# Initialize OpenAI client
client = OpenAI(api_key=API_KEY)

# Load OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Set dark background for all plots
# plt.style.use('dark_background')

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    gpt_response = ""
    execution_result = ""
    code_to_execute = ""
    show_graphic = False

    if os.path.exists("./static/graphic.png"):
        os.remove("./static/graphic.png")

    columns = ['Date','Year','Type','Country','Area','Location','Activity',
               'Name','Sex','Age','Injury','Fatal', 'Time','Species']
    data = pd.read_csv("./data/global-shark-attack.csv", sep=";")[columns]

    data_struct_desc = f"Columns: {list(data.columns)}\n\n"
    data_struct_desc += f"Data types:\n{data.dtypes}\n\n"
    data_struct_desc += f"Example rows:\n{data.head(5).to_string(index=False)}"

    if request.method == "POST":
        user_prompt = request.form.get("prompt", "")

        prompt_for_gpt = (
            "You have a pandas DataFrame called 'data' "
            "loaded from './data/global-shark-attack.csv' with sep=';'. "
            "Here is the structure of the DataFrame:\n\n"
            f"{data_struct_desc}\n\n"
            f"Use only the columns provided in {data_struct_desc}.\n\n"
            "Please write Python code that works with this DataFrame.\n\n"
            f"User Prompt: {user_prompt}"
        )

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt_for_gpt}],
                max_tokens=300
            )
            gpt_response = response.choices[0].message.content
            code_blocks = re.findall(r"```(?:python)?(.*?)```", 
                                     gpt_response, re.DOTALL)
            if code_blocks:
                code_to_execute = code_blocks[0].strip()
            else:
                code_to_execute = gpt_response.strip()

            old_stdout = sys.stdout
            redirected_output = io.StringIO()
            sys.stdout = redirected_output

            try:
                exec_globals = {
                    "data": data,
                    "pd": pd,
                    "plt": plt
                }
                exec(code_to_execute, exec_globals)

                if plt.get_fignums():
                    plt.savefig("./static/graphic.png")
                    plt.close()
                    show_graphic = True
            except Exception as ex:
                execution_result = f"Error executing code:\n{ex}"
            else:
                execution_result = redirected_output.getvalue()
            finally:
                sys.stdout = old_stdout

        except Exception as e:
            gpt_response = f"Error calling OpenAI API: {str(e)}"

    return render_template(
        "index.html",
        prompt=request.form.get("prompt", ""),
        gpt_response=gpt_response,
        code_to_execute=code_to_execute,
        execution_result=execution_result,
        show_graphic=show_graphic
    )


@app.route("/data")
def data_page():
    try:
        columns = ['Date','Year','Type','Country','Area','Location','Activity',
            'Name','Sex','Age','Injury','Fatal', 'Time','Species']
        data = pd.read_csv("./data/global-shark-attack.csv", sep=";")[columns]
        sample = data.head(10).to_html(classes="data", index=False)
    except Exception as e:
        sample = f"<p>Error loading data: {e}</p>"
    return render_template("data.html", table_html=sample)


@app.route("/questions")
def example_question():
    example_prompt = "Which species of shark is the most common?"
    return render_template("questions.html", prompt_example=example_prompt)


if __name__ == "__main__":
    app.run(debug=True)
