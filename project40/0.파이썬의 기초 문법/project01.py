# 숫자 맞추기 게임
import random
random_number = random.randint(1, 100)

#print("random_number:", random_number)
game_count = 1
while True:
    try:
        my_number = int(input("1부터 100까지의 숫자를 입력하세요: "))
        if my_number < random_number:
            print("UP")
        elif my_number > random_number:
            print("DOWN")
        elif my_number == random_number:
            print(f"정답입니다! {game_count}번 만에 맞추셨습니다.")
            break
        game_count += 1
    except:
        print("숫자를 입력해주세요.")