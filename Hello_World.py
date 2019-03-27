import aiml
import os
import wikipedia
kernel = aiml.Kernel()

if os.path.isfile("bot_newbrain.brn"):
    kernel.bootstrap(brainFile = "bot_newbrain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_newbrain.brn")

# kernel now ready for use
while True:
    Message =kernel.respond(input("Enter your message >> "))
    if (Message.find('Search')==True):
        print(wikipedia.summary('Message'))
    print(Message)

