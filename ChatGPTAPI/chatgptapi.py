# %%
# Now what the hell is this?
## This is literally just communicating with Chat through terminal. That's all.

# %% Set up openai
import openai
openai.api_key = open("key.txt", "r").read().strip('\n')

# %% Send a sample message, print the output
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user", "content":"What is the circumference of the moon in km?"}]
)
print(completion)

# %% Print ONLY the reply from above
reply_content = completion.choices[0].message.content
print(reply_content)






# %% Create message history, get input, echo it
message_history = []
user_input = input(">: ")
print("User's input was ", user_input)

# %% Add input to msg_hist, get the reply
message_history.append({"role": "user", "content": user_input})
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_history,
)
reply_content = completion.choices[0].message.content
print(reply_content)

# %% Add the reply to msg_hist
message_history.append({"role": "assistant", "content": reply_content})

# %% Get another input and reply
user_input = input(">: ")
print("User's input was ", user_input)
message_history.append({"role": "user", "content": user_input})
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_history,
)

reply_content = completion.choices[0].message.content
print(reply_content)
# note we're not adding it to message history! We prob should but whatever








# %% make this a function based thing

# Clear message_history
message_history = []

def chat(inp, role='user'):
    # Add user input to history
    message_history.append({"role": "user", "content": inp})
    
    # Get a response and get its reply_content, print it
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
    )  
    reply_content = completion.choices[0].message.content
    print(reply_content) 

    # Add the reply_content to history and return the content
    message_history.append({"role": "assistant", "content": reply_content})

    return reply_content

for i in range(2):
    user_input = input(">: ")
    print("User's input was ", user_input, "/n")
    chat(user_input)
    print()

# %%
