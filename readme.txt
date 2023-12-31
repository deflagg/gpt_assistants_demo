Install Python

Create and activate environment
PS> python3 -m venv .venv
PS> & d:/source/vscode/gpt_assistants_demo/.venv/Scripts/Activate.ps1

Create Readme.txt
Import all required imports/dependencies
Take a snapshot of the imports and save in requirments.txt file (pip freeze > requirements.txt)

Export and run Application
export FLASK_APP=gpt_assistants_demo.py
flask run --port 5000

Create a .secrets file
openai_api_key=YOUR_OPENAI_API