import time

while True:
        uni = input("Enter your time in Second: ")
        try:
            to_stop= abs(int(uni))
        except KeyboardInterrupt:
            break
        except:
            print("Not a number!")
        while to_stop > 0:
            m, s = divmod(to_stop, 60)
            h, m = divmod(m, 60)
            d, h = divmod(h, 24)
            time_left= str(d).zfill(2) +" D: "+ str(h).zfill(2) +" H: "+ str(m).zfill(2) +" M: "+ str(s).zfill(2)+" S"
            print(time_left + "\r", end="")
            time.sleep(1)
            to_stop -= 1
        



