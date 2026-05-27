# GPIO 제어를 위한 MotionSensor 클래스 import
# PIR(인체 감지 센서) 사용
from gpiozero import MotionSensor

# 일정 시간 대기(sleep) 함수 import
from time import sleep

# HTTP 요청을 보내기 위한 라이브러리 import
# 노트북 Flask 서버에 요청 보낼 때 사용
import requests


# PIR 센서를 GPIO17 핀에 연결
# BCM 기준 GPIO17 사용
pir = MotionSensor(17)


# 사진을 저장할 노트북의 IP 주소
# 본인 노트북 IP로 변경해야 함
LAPTOP_IP = "192.168.0.10"


# 시스템 시작 메시지 출력
print("System Ready")


# 무한 반복
while True:

    # 움직임이 감지될 때까지 대기
    pir.wait_for_motion()

    # 움직임 감지 메시지 출력
    print("Motion detected!")

    # 노트북 Flask 서버의 /capture 주소 호출
    # → 노트북에서 사진 촬영 실행
    requests.get(f"http://{LAPTOP_IP}:5000/capture")

    # 사진 촬영 완료 메시지 출력
    print("Photo captured on laptop!")

    # 5초 대기
    # 계속 연속 촬영되는 것을 방지
    sleep(5)
