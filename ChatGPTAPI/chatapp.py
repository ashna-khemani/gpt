# %% Setup
import gradio as gr
import openai
openai.api_key = open("key.txt", "r").read().strip('\n')

# %% Give it a message history where you explain the task
message_history = [{'role':'user', 'content':f"You are a Shakespeare bot. I will provide you with a scenario or subjects. You must only reply with a Shakespearean sonnet about that scene or subjects. Reply with OK if you understand"}, {'role':'assistant', 'content':f'OK'}]

# %% Create the function to return responses
def predict(input):
    global message_history
    message_history.append({'role':'user', 'content':input})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({'role':'assistant','content':reply_content})

    # response is a set of tuples with input and replies,
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]

    return response

# %% Build the gradio app
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Type message here").style(container=False)
        txt.submit(predict, txt, chatbot) # submitting makes bot uses predict to gen a response
        # txt.submit(lambda: "", None, txt) # does same thing as below line but slower
        txt.submit(None, None, txt, _js="() => {''}")   # empty the the box when submitted

demo.launch()
# %%
