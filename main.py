
# This is a simple function that check if the user is okay after dropping his/her phone.
# The phone has to check because it not normal for the user the drop his/her phone.
# I could have used PYTHON VOICE RECOGNITION, but at the time of writing this function, I didn't have microphone but I believe you get the idea.

def on_fall():
    ans = input("Are you okay?: ")
    if ans == " ":  # if the response is null for some number of seconds, then alert police and for first aid.
        print("Alerting the security and for first aid... just keep breathing, help is coming soon.")
        print("Added your current location as well.")
        # This part of my code is not running for some reasons I don't know.
        # In this case, if the phone falls down and the user also faints, then the code will wait for some seconds and then call for help.

    if ans == "yes":
        print("Just checking on you ")

    elif ans == "no":
        ans = input("Should I alert somebody?: ")
        if ans == "no":
            print("Take care of yourself....")
        elif ans == "yes":
            ans = input("Who should I alert?: ")
            if ans == "ambulance":
                print("alerting the ambulance")
                print("add victim current location")
                # security alert will be sent for FIRST AID...
            elif ans == "husband":
                print("alerting your husband ")
                print("add victim current location")
                # security alert will be sent to the husband...
            else:
                print("alerting the security.....")
                print("add victim current location...")
                # Automatically, this should alert the police...
        else:
            print("Will check back on you later...")
    else:
        print("Am glad you doing okay...")
    return False
# In all this, even if the screen get broken, the code will still run to save the user and also get help as soon as possible.


on_fall()
