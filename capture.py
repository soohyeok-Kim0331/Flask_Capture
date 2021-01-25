from flask import Flask, g, make_response, Response, request
import cv2

app = Flask(__name__)
video = cv2.VideoCapture(0)
print(type(video))
@app.route('/')
def index():
    return "Hello SITL This is video example"
def gen(video):
    pic = True
    while (pic == True):
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)
        pic = False

    cv2.destroyAllWindows()
    cv2.imwrite('frame.jpg', frame)


@app.route('/video_start')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='5000')