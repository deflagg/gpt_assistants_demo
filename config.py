from dotenv import dotenv_values

class Config:
    # Access environment variables
    SECRET_KEY = "192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf" # dotenv_values(".secrets").get("FORM_WTF_SECRET") or 'you-will-never-guess'