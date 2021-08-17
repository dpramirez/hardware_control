from threading import Thread
import cv2
import time
import multiprocessing
import threading

class RTSPVideoWriterObject(object):
    def __init__(self, src=0):
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(src)

        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def endRecord(self):
        self.capture.release()
        self.output_video.release()
        exit(1)

    def startRecord(self):
        global endRec
        self.frame_width = 640#int(self.capture.get(3))
        self.frame_height = 480#int(self.capture.get(4))
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.output_video = cv2.VideoWriter('fileOutput.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 320.0, (self.frame_width, self.frame_height))
        while True:          
            try:
                self.output_video.write(self.frame)
                #print(endRec)
                if endRec:
                    self.endRecord()
            except AttributeError:
                pass

    



if __name__ == '__main__':

    rtsp_stream_link = 2
    video_stream_widget = RTSPVideoWriterObject(rtsp_stream_link)

    endRec = False
    t1 = threading.Thread(target = video_stream_widget.startRecord) 
    t1.start() 
    time.sleep(5)
    endRec = True
    print('..............')
    print(endRec)

         