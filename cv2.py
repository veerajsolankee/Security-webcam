import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):


      #read the frame while the camera is on
      ret,frame = videoCaptureObject .read()

      #cv2.imwrite() method is used to save a image to any stranger device
      img_name="img"+str(number)+".png"
      cv2.imwrite(img_name,frame)
      start_time=time.time

      result = False

    return img_name
def uploadfile(img_name):
    access_token="zXMRSWjhVMYAAAAAAAAAAQYgzlnEW9ik-c8XxvKuEZjUpocEsRUc9QwnqXHOjiK-"
    file=img_name
    file_from=file
    file_to="Viraj singh"+(img_name)
    dba=dropbox.Dropbox(access_token)
    with open(file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("fileUploaded")
def main():
    while(True):
     if((time.time()-start_time)>=5):
      name=take_snapshot()
      uploadfile(name)
main()  
