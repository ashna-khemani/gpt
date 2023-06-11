*Video: https://www.youtube.com/watch?v=c-g6epk3fFE*
## Secret key
* Get a secret key from OpenAI
* Paste it into a file `key.txt`

## Get a virtualenv running
1. `virtualenv .env`
2. `source .env/bin/activate`

## How to get `openai` to work (using virtualenv)
1. Check pip3 is latest version
2. `pip3 install openai`
3. Set Python interpreter to .env (recommended version)

## How to install `gradio` (or what worked for me)
1. Activate the `.env` -- see above
2. `sudo pip3 install gradio`
    1. You can maybe do without the sudo?? Had some wheel/permission issues 
