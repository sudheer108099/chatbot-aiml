import aiml
import os.path as path
import pickle
import webbrowser
from urllib.parse import quote

BOTZ = 'botz'
SESSION_ID = 69420

KERNEL_PICKLE = 'kernel'
LEARNFILE = 'startup.xml'
INIT_COMMAND = ['LOAD AIML B', "EMERGENCY NUMBERS GALORE"]

kernel = aiml.Kernel()
kernel.setTextEncoding(None)
kernel.bootstrap(learnFiles=LEARNFILE, commands=INIT_COMMAND, chdir=BOTZ)
# if path.exists(pick := path.join(BOTZ, KERNEL_PICKLE)):
#     with open(pick, 'rb') as f:
#         session_data = pickle.load(f)
#         for key, val in session_data.items():
#             kernel.setPredicate(key, val, SESSION_ID)
#         bot_resp = kernel.respond('hello', SESSION_ID)
# else:
#     bot_resp = kernel.respond('login', SESSION_ID)
# while True:
#     if bot_resp.startswith('OPEN BROWSER: '):
#         bot_resp = bot_resp[14:]
#         query_str = bot_resp[bot_resp.find('##') + 2:]
#         url = bot_resp[:bot_resp.find('##')] + quote(query_str)
#         print('<<<', url)
#         webbrowser.open(url, 2)
#     else:
#         print('<<<', bot_resp)
#     user_inp = input('>>> ')
#     if user_inp == 'bye' or user_inp == 'quit':
#         break
#     bot_resp = kernel.respond(user_inp, SESSION_ID)
# session_data = kernel.getSessionData(SESSION_ID)
# with open(pick, 'wb+') as f:
#     pickle.dump(session_data, f)
