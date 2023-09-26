import cv2 as cv 
import numpy as np
import time
import math
import playsound
# Distance constants 
KNOWN_DISTANCE = 20 #INCHES
PERSON_WIDTH = 19 #INCHES
MOBILE_WIDTH = 3.0 #INCHES

# Object detector constant 
CONFIDENCE_THRESHOLD = 0.4
NMS_THRESHOLD = 0.3
def calculate(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist
# colors for object detected
COLORS = [(255,0,0),(255,0,255),(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
GREEN =(0,255,0)
BLACK =(0,0,0)
# defining fonts 
FONTS = cv.FONT_HERSHEY_COMPLEX

# getting class names from classes.txt file 
class_names = []
with open("classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
#  setttng up opencv net
yoloNet = cv.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

yoloNet.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
yoloNet.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)
model = cv.dnn_DetectionModel(yoloNet)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

# object detector funciton /method
def object_detector(image,imgg):
    classes, scores, boxes = model.detect(image, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    # creating empty list to add objects data
    global lisst
    data_list =[]
    lisst=[]
    for (classid, score, box) in zip(classes, scores, boxes):
        # define color of each, object based on its class id 
        color= COLORS[int(classid) % len(COLORS)]
        
        label = "%s" % (class_names[classid[0]])
        
        # draw rectangle on and label on object
        cv.rectangle(imgg,box, (255,0,0), 1)
        cv.putText(imgg, label, (box[0], box[1]-14), FONTS, 0.5, color, 2)
    
        # getting the data 
        # 1: class name  2: object width in pixels, 3: position where have to draw text(distance)
        if classid ==0: # person class id 
            data_list.append([class_names[classid[0]], box[2], (box[0], box[1])])
            lisst.append([box[0], box[1],box[2],box[3]])
        # if you want inclulde more classes then you have to simply add more [elif] statements here
        # returning list containing the object data.
    return data_list

def focal_length_finder (measured_distance, real_width, width_in_rf):
    focal_length = (width_in_rf * measured_distance) / real_width

    return focal_length

# distance finder function 
def distance_finder(focal_length, real_object_width, width_in_frmae):
    distance = (real_object_width * focal_length) / width_in_frmae
    return distance

# reading the reference image from dir 
ref_person = cv.imread('ReferenceImages/image1.png')
ref_mobile = cv.imread('ReferenceImages/image2.png')

#mobile_data = object_detector(ref_mobile)
#mobile_width_in_rf = mobile_data[1][1]

person_data = object_detector(ref_person,ref_person)
person_width_in_rf = person_data[0][1]

print(f"Person width in pixels : {person_width_in_rf}")

# finding focal length 
focal_person = focal_length_finder(KNOWN_DISTANCE, PERSON_WIDTH, person_width_in_rf)

#focal_mobile = focal_length_finder(KNOWN_DISTANCE, MOBILE_WIDTH, mobile_width_in_rf)
cap = cv.VideoCapture('Videos/walking.mp4')
#cap = cv.VideoCapture(0)
while True:
    img = cv.imread('white.jpeg')
    img = cv.resize(img,(600,400))
    ret, frame = cap.read()
    frame=cv.resize(frame, (600,400))
    data = object_detector(frame,img)
    
    cv.rectangle(img, (450, 370), (600,400),(0,0,0),-1 )
    cv.rectangle(img, (440, 300), (600,370),(99,99,99),-1 )
    cv.putText(img, f'No. of persons:{len(lisst)}', (451,385), FONTS, 0.48, (255,0,255), 1)
    cv.putText(img,'', (451,385), FONTS, 0.48, (255,255,255), 1)
    for d in data:
        if d[0] =='person':
            distance=0
            distance = distance_finder(focal_person, PERSON_WIDTH, d[1])
            x, y = d[2]
        cv.rectangle(img, (x, y+18), (x+50,y),(0,0,0),-1 )
        #cv.putText(frame, f'D:{round(distance,1)}', (x,y+10), FONTS, 0.48, GREEN, 1)
    pt1=(len(lisst)+2)*[0]
    pt2=(len(lisst)+2)*[0]
    dist0=(len(lisst))*[0]
    qw=0
    qwes=0
    for (x,y,w,h) in lisst:
            qw=1+qw
            cv.rectangle(img,(x,y),(x+w,y+h),(0,0,0),-1)
            cv.putText(img, f'D:{round(distance)}', (x,y+10), FONTS, 0.48, GREEN, 1)
            cv.putText(img,f'No Social Distance:', (441,315), FONTS, 0.48, (255,255,255), 1)

            #cv.putText(img, f'persons-{qw}', (x,y+29),1,cv.FONT_HERSHEY_PLAIN,(0,0,255),1,cv.LINE_AA)
            
    if len(lisst)>1:
        for i in range(len(lisst)):
            faces=lisst
            #print(faces)
            x1=faces[i][0]
            y1=faces[i][2]
            z1=faces[i][1]
            q1=faces[i][3]
            mid1=int(x1+y1/2)
            mid2=int(z1+q1/2)
            pt1[i]=mid1
            pt2[i]=mid2
        for i in range(0,(len(faces)-1),1):
            for j in range(i+1,len(faces),1):
                #cv.putText(frame, f'person{i+1}', (x+30,y+35), FONTS, 0.48, GREEN, 1)
                #print(pt1[i],pt2[i])
                mid11=int((pt1[i]+pt1[j])/2)
                mid12=int((pt2[i]+pt2[j])/2)
                dis=calculate(pt1[i],pt2[i],pt1[j],pt2[j])
                per_to_person=round(dis)
                #print(f"distance from person{i+1} to person{j+1} is {round(dis,2)}")
                for a in range(len(lisst)):
                    y11=faces[a][2]
                    pers=distance_finder(focal_person, PERSON_WIDTH, y11)
                    dist0[a]=pers
                    dist0.sort()
                    cam_to_person=dist0[0]
                    
                if per_to_person<100: #and cam_to_person<50:
                        print(qwes)
                        qwes=qwes+1
                        cv.line(img,((pt1[i],pt2[i])),((pt1[j],pt2[j])),GREEN,2)
                        #print("hemanth asdasd asd ad wef wdws few fw f ewf we  sdc s d ")
                        #print(f"distance from person{i} to person{j} is {per_to_person}")             
                        cv.putText(img,f'{round(distance)}',(mid11,mid12),1,cv.FONT_HERSHEY_PLAIN,(255,255,255),1,cv.LINE_AA)
                        cv.putText(img,f'{qwes}', (471,340), 1,cv.FONT_HERSHEY_PLAIN,(255,255,255),1,cv.LINE_AA)

                        '''with open('social.mp3','r'):
                            playsound.playsound('social.mp3')'''
                else:
                    xas=1
                    #cv.line(img,((pt1[i],pt2[i])),((pt1[j],pt2[j])),(0,0,255),2)
    cv.imshow('frame',frame)
    cv.imshow('persons',img)
    #time.sleep(0.2)
    key = cv.waitKey(1)
    if key ==ord('q'):
        break
cv.destroyAllWindows()
cap.release()
