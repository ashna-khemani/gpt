# Journey through terminal

import openai
openai.api_key = open('key.txt', 'r').read().strip("\n")

def chat(inp, message_history, role='user'):
    message_history.append({"role":role, "content":inp})
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message_history
    )

    reply_content = completion.choices[0].message.content
    message_history.append({"role":"assistant", "content":reply_content})
    return reply_content, message_history


message_history = [{"role":"user", "content":"You are a story game bot that proposes a hypothetical fantastical situation, and 2-4 possible actions a player can choose from. These options are provided by you. Once the player chooses an action, you must narrate what happens next, and provide more options for actions, repeating this process. When presenting the story and action options, present only the story and start immediately, with no additional commentary or acknowledgement. Label the action options as '1:   ,' '2:   ,' and so on. If you understand, say 'OK' and start the game when I say 'begin.'"},
                   {"role":"assistant", "content":"OK. Begin when you are ready."}]

reply_content, message_history = chat("begin", message_history)

for i in range(3):
    print("\n", reply_content)
    next_inp = input("\nEnter response: ")
    reply_content, message_history = chat(reply_content, message_history)
    