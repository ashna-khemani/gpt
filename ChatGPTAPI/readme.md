*Video: https://www.youtube.com/watch?v=c-g6epk3fFE*
## Secret key
Get a secret key from OpenAI
Paste it into a file `key.txt`

## How to get `openai` to work (using virtualenv)
Check pip3 is latest version
`virtualenv .env`
`source .env/bin/activate`
`pip3 install openai`
Set Python interpreter to .env/recommended vers.

## How to install `gradio` (or what worked for me)
Activate the `.env` -- see above
`sudo pip3 install gradio`
You can maybe do without the sudo?? Had some wheel/permission issues for me
