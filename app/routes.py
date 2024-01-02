from flask import render_template, flash
from app import app
from app.forms import ThreadForm
from app.services.gptllm import GptLLM


@app.route('/thread', methods=['GET', 'POST'])
def thread():
    form = ThreadForm()
    
    if form.validate_on_submit():
        client = GptLLM()
        
        # ID of neuroscientist assistant
        assistant_id = "asst_jlr9oELusyk2cBKFAFg7gjo2"
        
        message = form.prompt.data
        
        # Send message to neuroscientist assistant
        form.messages = client.SendMessage(message, assistant_id)
    
    return render_template('thread.html', title='GPT Assistants', form=form)