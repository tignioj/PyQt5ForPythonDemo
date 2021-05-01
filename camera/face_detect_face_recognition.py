import cv2
import dlib, os
import imutils
import numpy as np
import matplotlib.pyplot as plt
import face_recognition


# 方法 显示图片
def show_image(image, title):
    plt.title(title)
    plt.imshow(image)
    plt.axis("off")


# 方法：绘制人脸矩形框
def plot_rectangle(image, faces):
    for face in faces:
        cv2.rectangle(image,
                      (face.left(), face.top()),
                      (face.right(), face.bottom()),
                      (255, 0, 0),
                      4)
        return image


# 导入cnn模型
def faceDetect(image):
    # image = imutils.resize(image, width=800, height=900)
    # face_location = face_recognition.face_locations(image, model="cnn")
    face_location = face_recognition.face_locations(image)
    face_landmarks_list = face_recognition.face_landmarks(image)

    # 给检测出的人脸绘制矩形框
    # img_result = plot_rectangle(image.copy(), face_location)
    for (top, right, bottom, left) in face_location:
        # 8 创建画布

        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

        # 9 显示最终的检测效果
        cv2.putText(image, "HOG", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), cv2.LINE_4)
        # show_image(image, "face detection")

        # cv2.imwrite("result_cnn.jpg", cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB))

    # img_result = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image


def _testVideo():
    video_capture = cv2.VideoCapture(1)
    while True:
        ret, frame = video_capture.read()
        detected_img = faceDetect(frame)
        cv2.imshow("face", detected_img)
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            video_capture.release()
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    # face_recognition.load_image_file("../faces/7.jpeg")
    _testVideo()

