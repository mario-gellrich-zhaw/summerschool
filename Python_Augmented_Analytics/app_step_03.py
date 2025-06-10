"""
This module - when fully developed - sets up a Flask web application that 
interacts with the OpenAI GPT-3.5-turbo model. It loads an OpenAI API key from 
a credentials file, reads data from a CSV file, and allows users to submit 
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

# Set dark background for all plots
plt.style.use('dark_background')

app = Flask(__name__)

# Load OpenAI API key from credentials.json
try:
    with open('./data/credentials.json', encoding='utf-8') as file:
        credentials = json.load(file)
        API_KEY = credentials['openai']['api_key']
except FileNotFoundError as exc:
    raise ValueError(
        "Please provide OpenAI API key in the credentials.json file."
    ) from exc

# Initialize OpenAI client
client = OpenAI(api_key=API_KEY)

@app.route("/", methods=["GET", "POST"])
def index():
    gpt_response = ""
    execution_result = ""
    code_to_execute = ""
    show_graphic = False  # Initialize with False

    # Remove any existing graphics
    if os.path.exists("./static/graphic.png"):
        os.remove("./static/graphic.png")

    # Load CSV data
    data = pd.read_csv("./data/autoscout24_data.csv")

    # Create a string that describes the structure of the DataFrame
    data_struct_desc = f"Columns: {list(data.columns)}\n\n"
    data_struct_desc += f"Data types:\n{data.dtypes}\n\n"
    data_struct_desc += f"Example rows:\n{data.head(5).to_string(index=False)}"

    if request.method == "POST":
        user_prompt = request.form.get("prompt", "")

        # Context prompt for GPT, describing the DataFrame
        prompt_for_gpt = (
            "You have a pandas DataFrame called 'data' "
            "loaded from './data/autoscout24_data.csv'. "
            "Here is the structure of the DataFrame:\n\n"
            f"{data_struct_desc}\n\n"
            "Please write Python code that works with this DataFrame.\n\n"
            f"User Prompt: {user_prompt}"
        )

        # Call GPT-3.5-turbo via OpenAI's ChatCompletion endpoint
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt_for_gpt}],
                max_tokens=300
            )
            # Extract the model's response
            gpt_response = response.choices[0].message.content

            # Extract code between triple backticks
            code_blocks = re.findall(r"```(?:python)?(.*?)```", 
                                     gpt_response, re.DOTALL)
            if code_blocks:
                code_to_execute = code_blocks[0].strip()
            else:
                # If no code blocks found, treat the entire response as code
                code_to_execute = gpt_response.strip()

            # Prepare to capture stdout
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

                # Check if a plot was created by inspecting the current figure
                if plt.get_fignums():  # Check if any figures exist
                    plt.savefig("./static/graphic.png")
                    plt.close()
                    show_graphic = True
                else:
                    show_graphic = False
            except Exception as ex:
                execution_result = f"Error executing code:\n{ex}"
            else:
                # Capture print statements
                execution_result = redirected_output.getvalue()
            finally:
                # Restore stdout
                sys.stdout = old_stdout

        except Exception as e:
            gpt_response = f"Error calling OpenAI API: {str(e)}"

    return render_template(
        "index_step_03.html",
        prompt=request.form.get("prompt", ""),
        gpt_response=gpt_response,
        code_to_execute=code_to_execute,
        execution_result=execution_result,
        show_graphic=show_graphic
    )

if __name__ == "__main__":
    app.run(debug=True)