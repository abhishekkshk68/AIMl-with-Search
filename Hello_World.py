import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("bot_5brain.brn"):
    kernel.bootstrap(brainFile = "bot_5brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_5brain.brn")

# kernel now ready for use
while True:
    print (kernel.respond(input("Enter your message >> ")))