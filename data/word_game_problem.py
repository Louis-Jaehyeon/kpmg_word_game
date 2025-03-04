import random
import time
import csv
from pygame import mixer
import pygame

pygame.init()
mixer.init()


def run_word_game(): # 게임 실행 함수 정의

    # 정답 개수와 시작 시간의 변수 초기화
    correct_count = 0
    start_time = 0 # 게임 시작 시간 변수 초기화

    # word.txt에서 요소 불러오기 및 리스트화
    words = open("word.txt", 'r')
    data = words.read().split()
    print(data)
    words.close()

    # 게임 시작 선언 
    print("준비? 엔터를 입력하세요")
    start = str(input("엔터를 입력하세요: "))

    # 게임 시작
    if start == "":
        start_time = time.time()
    # 다섯번 반복하기
        for i in [1,2,3,4,5]:
            print(f"Question #{i}")
            # 리스트 요소 중 랜덤으로 한개 불러오기
            random_word = random.choice(data)
            print(random_word)
            # 사용자 입력 받기
            answer = str(input())
            # 정답/오답 판단, 사운드 출력 및 정답 개수 카운트
            if random_word == answer:
                mixer.music.load('../assets/good.wav') # 소리파일 path
                mixer.music.play()
                correct_count += 1
                print("정답입니다")

            else:
                mixer.music.load('../assets/bad.wav') # 소리파일 path
                mixer.music.play()
                print("오답입니다")

    # 게임 종료 시간 기록
    end_time = time.time() 
    game_duration = end_time - start_time 

    # 게임 종료 후, 정답 개수와 진행 시간 출력하기
    print("게임 종료")
    print(f"총 정답 개수: {correct_count} / 5")
    print(f"게임 진행 시간: {game_duration:.2f}초")

    # 게임 결과 파일에 저장하기
    with open("words_game_score.csv", "a", encoding="utf-8", newline='') as file: 
        file.write(f"{correct_count}, {game_duration:.2f}\n")

if __name__ == "__main__":
    run_word_game() # 게임 실행 함수 호출