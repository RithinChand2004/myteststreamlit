import pyautogui as pt
from time import sleep
import pyperclip
import random
sleep(3)

position1 = pt.locateOnScreen("Smiley_paperclip.png", confidence=0.6)
x = position1[0]
y = position1[1]

#Gets message
def getmessage():
    global x, y

    position = pt.locateOnScreen("Smiley_paperclip.png", confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration=0.5)
    pt.moveTo(x + 90 ,y - 60, duration=0.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("meassage received: "+ whatsapp_message)

    return whatsapp_message


#Post
def post_response(message):
    global x, y

    position = pt.locateOnScreen("Smiley_paperclip.png", confidence=0.6)
    x = position[0]
    y = position[1] 
    pt.moveTo(x + 200, y + 20, duration=0.5)
    pt.click()
    pt.typewrite(message, interval=0.01)

    #pt.typewrite("\n", interval=0.01)   

#Processes Response
def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any questions!"

    else:
        if random_no == 0:
            return "That's cool"
        elif random_no == 1:
            return "yeah"
        else:
            return "Hmmm"



#Check for new message
def check_for_new_message():
    pt.moveTo(x + 90 , y - 60, duration = 0.5)

while True:
    #Continuously check for the green point and new messages
    try:
        position = pt.locateOnScreen("green_point.png", confidence = 0.7)

        if position is not None: 
            pt.moveTo(position)
            pt.moveRel(-100,0)
            pt.click()
            sleep(0.5)


    except(Exception):
        print("No new messages found")    

    if pt.pixelMatchesColor(int(x + 90),int(y - 60),(32,44,51),tolerance=10):
        print("is grey")
        processed_message = process_response(getmessage())
        post_response(processed_message)
    else:
        print("No new messages")
    sleep(5)
    

    check_for_new_message()
