 # -*- coding: utf-8 -*-



import cv2 as cv
import numpy as np
from PIL import ImageGrab
from python_imagesearch.imagesearch import imagesearch, imagesearcharea
import time
import mouse
import keyboard
from timeit import default_timer as timer
from datetime import datetime
import sys 




time.sleep(2) 
temp = True
print("STARTED : " , datetime.now().strftime("%H:%M:%S"))


while True :
    time.sleep(0.2)
    keyboard.press('e')
    time.sleep(0.1)
    solucan = imagesearch("solucan.png", 0.9)
    if solucan[0] != -1:
        mouse.move(solucan[0]+10,solucan[1]+10)
        time.sleep(0.1)
        mouse.click("right")
    else :
        sys.exit()
    time.sleep(0.2)
    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')
    
    start2 = timer()
    
    while True :
        
        
        pencere = imagesearch("pencere.png", 0.9)
        
        if pencere[0] != -1: # pencere bulunduysa
            
            print("pencere bulundu")
            start2 = timer()
        
            #palamut = imagesearch("palamut.png",0.9)
            altin = imagesearch("altin2.png",0.9)
            yabbie = imagesearch("yabbie.png", 0.9)
            
            if altin[0] != -1 or yabbie[0] != -1: # balık bulunduysa
                
                print("BALIK BULUNDU")
                temp = True
                break
            else:
                keyboard.press('esc')
                time.sleep(0.1)
                keyboard.release('esc')
                time.sleep(0.2)
                mouse.move(1453,605)
                time.sleep(0.1)
                mouse.click("right")
                time.sleep(0.1)
                solucan = imagesearch("solucan.png", 0.9)
                if solucan[0] != -1:
                    mouse.move(solucan[0]+10,solucan[1]+10)
                    time.sleep(0.1)
                    mouse.click("right")
                else :
                    print("FINISHED : " , datetime.now().strftime("%H:%M:%S"))
                    sys.exit()
                time.sleep(0.2)
                keyboard.press('space')
                time.sleep(0.1)
                keyboard.release('space')
        else :
            if timer()-start2 >= 10 :
                start2 = timer()
                solucan = imagesearch("solucan.png", 0.9)
                if solucan[0] != -1:
                    mouse.move(solucan[0]+10,solucan[1]+10)
                    time.sleep(0.1)
                    mouse.click("right")
                    time.sleep(0.1)
                else :
                    print("FINISHED : " , datetime.now().strftime("%H:%M:%S"))
                    sys.exit()
                keyboard.press('space')
                time.sleep(0.1)
                keyboard.release('space')
                time.sleep(0.1)
                
            continue
            
                
            
   
    start = timer()
    cap = ImageGrab.grab(bbox=(343,171,622,420))
    frame1 = np.array(cap)
    cap = ImageGrab.grab(bbox=(343,171,622,420))
    frame2 = np.array(cap)
    
    
    while temp :
     
            
            diff = cv.absdiff(frame1, frame2)
            gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
            blur = cv.GaussianBlur(gray, (5,5), 0)
            _,thresh = cv.threshold(blur, 57, 200, cv.THRESH_BINARY)
            dilated = cv.dilate(thresh, None, iterations = 7)
            contours,_ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        
            for cnt in contours:
                
                area = cv.contourArea(cnt)
                if 975 > area > 260 :
                
                    
                    #cv.drawContours(frame, [cnt],-1,(0,255,0),2)
                    x1,y1,x2,y2 = cv.boundingRect(cnt)
                    cv.rectangle(frame1, (x1,y1), (x1+x2,y1+y2), (0,255,0))
                    coordinate_x = ((x1+x1+x2)/2)+343
                    coordinate_y = ((y1+y1+y2)/2)+171
                    
                    mouse.move(coordinate_x,coordinate_y)
                    
                    
                    #print(x1,y1,x1+x2,y1+y2)
                    
        
                    b, g, r = frame1[149,202]
                    
                    g = int(g)
                    
                    if g == 163 :
                        
                        pos2 = imagesearcharea("Miss.png", 343,171,622,420,0.34)
                        
                        if pos2[0] != -1:
                            
                            print("HIT OR MISS")
                        else:
                            print("CLICK")                       
                            mouse.click("left")
                        
                        
                                       
                        
                    # else :
                    #     print("dışarda")
                    
            cv.namedWindow("Feed") 
            cv.moveWindow("Feed", 1639, 452)
            cv.imshow("Feed", frame1)
            
            frame1 = frame2
            cap = ImageGrab.grab(bbox=(343,171,622,420))
            frame2 = np.array(cap)
        
            
            if cv.waitKey(1) == 27:
                temp = False
            
            if timer()-start >= 15:
                temp = False
             
            
    
    cv.destroyAllWindows()
    keyboard.release("e")
    

 
 