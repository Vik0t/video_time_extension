import cv2 as cv

frameSize = (256, 256)
y2, x2 = frameSize
out = cv.VideoWriter('output_video.mp4', cv.VideoWriter_fourcc(*'H264'), 10.0, frameSize)

for i in range(9):
    videoCapture = cv.VideoCapture('AI_video.mp4')

    while videoCapture.isOpened():
        ret, frame = videoCapture.read()
        if ret:
            frameArray = [frame[0:y2, 0:x2],            # 0
                          frame[0:y2, x2:x2*2],         # 1
                          frame[0:y2, x2*2:x2*3],       # 2
                          frame[y2:y2*2, 0:x2],         # 3
                          frame[y2:y2*2, x2:x2*2],      # 4
                          frame[y2:y2*2, x2*2:x2*3],    # 5
                          frame[y2*2:y2*3, 0:x2],       # 6
                          frame[y2*2:y2*3, x2:x2*2],    # 7
                          frame[y2*2:y2*3, x2*2:x2*3]]  # 8

            out.write(frameArray[i])
        else:
            break

out.release()
cv.destroyAllWindows()
