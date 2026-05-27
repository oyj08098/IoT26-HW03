# Flask 웹 서버를 사용하기 위한 라이브러리 import
from flask import Flask

# OpenCV 라이브러리 import (카메라 제어용)
import cv2

# 현재 날짜와 시간을 가져오기 위한 라이브러리 import
from datetime import datetime


# Flask 앱 생성
# __name__ 은 현재 실행 중인 파일 이름을 의미
app = Flask(__name__)


# "/capture" 주소로 접속하면 실행되는 함수
# 예: http://라즈베리파이IP:5000/capture
@app.route('/capture')
def capture():

    # 카메라 연결
    # 0 = 기본 카메라 장치
    # cv2.CAP_DSHOW = Windows DirectShow 방식 사용
    # (라즈베리파이에서는 보통 이 옵션 없이 사용함)
    camera = cv2.VideoCapture(0)

    # 카메라로부터 한 프레임(사진) 읽기
    # ret = 성공 여부(True/False)
    # frame = 실제 이미지 데이터
    ret, frame = camera.read()

    # 카메라 읽기 성공 여부 출력
    print("RET =", ret)

    # 사진 촬영 성공 시
    if ret:

        # 현재 시간을 기반으로 파일 이름 생성
        # 예: 20260511_193000.jpg
        filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")

        # 이미지를 JPG 파일로 저장
        cv2.imwrite(filename, frame)

        # 저장 완료 메시지 출력
        print("Saved:", filename)

    # 촬영 실패 시
    else:
        print("Camera failed!")

    # 카메라 장치 해제
    camera.release()

    # 웹 브라우저에 표시될 응답
    return "Photo captured!"


# Flask 서버 실행
# host='0.0.0.0'
# → 같은 네트워크의 다른 기기에서도 접속 가능
#
# port=5000
# → 5000번 포트 사용
app.run(host='0.0.0.0', port=5000)
