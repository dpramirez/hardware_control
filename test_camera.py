
from camera.camera import *
from threading import Thread
import time
import threading

rtsp_stream_link = 2
video_stream_widget = RTSPVideoWriterObject(rtsp_stream_link)

endRec = False
t1 = threading.Thread(target = video_stream_widget.startRecord) 
t1.start() 
time.sleep(10)
video_stream_widget.update_record(True)   
time.sleep(5)
print('..............')


         