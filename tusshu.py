import winsound


print("NICE TO MEET YOU MAN ITS BABY")

while True:
    try:
        AI = int(input("Work (Enter 0 to exit): "))
        if AI == 0:
                   
            break
        
        match AI:
            case 1:
                winsound.PlaySound("1.wav", 0)#hey tushar  
            case 2:
                winsound.PlaySound("2.wav", 0)#kahi kahi
            case 3:
                winsound.PlaySound("3.wav", 0)#
            case 4:
                winsound.PlaySound("4.wav", 0)
            case 5:
                winsound.PlaySound("5.wav", 0)
            case 6:
                winsound.PlaySound("6.wav", 0)
    except ValueError:
                       winsound.PlaySound("listen ask simple question 1.wav", 0)
    
    
     