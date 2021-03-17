import aiml
import os.path as path
import pickle

BOTZ = 'botz'

KERNEL_PICKLE = 'kernel'
LEARNFILE = 'startup.xml'
INIT_COMMAND = ['LOAD AIML B', "EMERGENCY NUMBERS GALORE"]

if __name__ == '__main__':
    if path.exists(pick := path.join(BOTZ, KERNEL_PICKLE)):
        with open(pick, 'rb') as f:
            kernel = pickle.load(f)
    else:
        kernel = aiml.Kernel()
        kernel.setTextEncoding(None)
        kernel.bootstrap(learnFiles=LEARNFILE,
                         commands=INIT_COMMAND,
                         chdir=BOTZ)
    bot_resp = kernel.respond('login')
    while True:
        print('<<<', bot_resp)
        user_inp = input('>>> ')
        if user_inp == 'bye' or user_inp == 'quit':
            break
        bot_resp = kernel.respond(user_inp)
    print(kernel.getSessionData(kernel._globalSessionID))
    # with open(pick, 'wb+') as f:
    #     pickle.dump(kernel, f)
