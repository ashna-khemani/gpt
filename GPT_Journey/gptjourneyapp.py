# %%
import openai
from flask import Flask, render_template, request, session
import re

openai.api_key = open('key.txt', 'r').read().strip("\n")

app = Flask(__name__)
app.secret_key = 'secret'

# %% Method to get an image
def get_img(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512",
        )
        img_url = response.data[0].url
    except Exception as e:
        img_url = "https://pythonprogramming.net/static/images/imgfailure.png"
    
    return img_url

# %% Method to ChatGPT a response
def chat(inp, message_history, role='user'):
    message_history.append({"role":role, "content":f"{inp}"})
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message_history
    )

    reply_content = completion.choices[0].message.content
    message_history.append({"role":"assistant", "content":reply_content})
    return reply_content, message_history


# %% Flask time! Homepage
@app.route("/", methods=["GET", "POST"])
def index():
    title = "GPT Journey"
    button_messages = {}
    button_states = {}
    if request.method == "GET":     # when user first visits page:
        # give the pre-prompt
        session['message_history'] = [{"role":"user", "content":"You are a story game bot that proposes a hypothetical fantastical situation, and 2-4 possible actions a player can choose from. These options are provided by you. Once the player chooses an action, you must narrate what happens next, and provide more options for actions, repeating this process. When presenting the story and action options, present only the story and start immediately, with no additional commentary or acknowledgement. Label the action options as 'Option 1,' 'Option 2,' and so on. If you understand, say 'OK' and start the game when I say 'begin.'"},
                   {"role":"assistant", "content":"OK. Begin when you are ready."}]
        
        message_history = session['message_history']
        reply_content, message_history = chat("Begin", message_history)

        # get options from text
        text = reply_content.split("Option 1")[0]
        options = re.findall("Option \d:.*", reply_content)

        # Put options as buttons
        for i, option in enumerate(options):
            button_messages[f"button{i+1}"] = option
        
        for button_name in button_messages:
            button_states[button_name] = False

    message = None
    button_name = None

    if request.method == "POST":
        message_history = session["message_history"]
        button_messages = session['button_messages']

        # The button that got pressed
        button_name = request.form.get('button_name')
        button_states[button_name] = True
        message = button_messages.get(button_name)

        reply_content, message_history = chat(message, message_history)

        # Get the story text and new options
        text = reply_content.split("Option 1")[0]
        options = re.findall("Option \d:.*", reply_content)

        button_messages = {}    # clear out button_messages so we don't have conflicting no. of options round to round
        for i, option in enumerate(options):
            button_messages[f"button{i+1}"] = option
        
        for button_name in button_messages.keys():
            button_states[button_name] = False

    session['message_history'] = message_history
    session['button_messages'] = button_messages

    image_url =  get_img(text)

    return render_template ("index.html", title=title, text=text, image_url=image_url, button_messages=button_messages, button_states=button_states, message=message)


if __name__ == '__main__':
    app.run(debug=True)