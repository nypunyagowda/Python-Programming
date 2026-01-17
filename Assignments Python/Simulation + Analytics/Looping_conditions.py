PIN = 1234
trials = 0
success = False
while trials<3:
    INPUT_PIN = int(input(f"trial {trials} | PIN>> "))
    trials+=1
    if INPUT_PIN == PIN:
        print("SUCCESS")
        break
    else:
        print("FAILURE, TRY AGAIN!")
if not success:
    print("Failed")



   
