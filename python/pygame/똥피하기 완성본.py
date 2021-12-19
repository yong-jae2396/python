import random
import pygame

# 기본 초기화 파트 (반드시 해야 하는 것들)
#----------------------------------------------------------#
pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기") # 게임 이름

# FPS
clock = pygame.time.Clock()
#--------------------------------------------------------------#




# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 만들기
background = pygame.image.load("C:/Users/김용재/Desktop/파이썬/python/pygame/background.png")

# 캐릭터 만들기
character = pygame.image.load("C:/Users/김용재/Desktop/파이썬/python/pygame/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 똥만들기

# 1번째 똥 만들기
ddong = pygame.image.load("C:/Users/김용재/Desktop/파이썬/python/pygame/enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10

# 2번째 똥 만들기
ddong2 = pygame.image.load("C:/Users/김용재/Desktop/파이썬/python/pygame/enemy.png")
ddong_size2 = ddong2.get_rect().size
ddong_width2 = ddong_size2[0]
ddong_height2 = ddong_size2[1]
ddong_x_pos2 = random.randint(0, screen_width - ddong_width2)
ddong_y_pos2 = 0
ddong_speed2 = 20

# 3번째 똥 만들기
ddong3 = pygame.image.load("C:/Users/김용재/Desktop/파이썬/python/pygame/enemy.png")
ddong_size3 = ddong3.get_rect().size
ddong_width3 = ddong_size3[0]
ddong_height3 = ddong_size3[1]
ddong_x_pos3 = random.randint(0, screen_width - ddong_width3)
ddong_y_pos3 = 0
ddong_speed3 = 20



# 이동 위치
to_x = 0
to_y = 0
character_speed = 12

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간 
total_time = 20


# 시작 시간 
start_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(40) # 게임화면의 초당 프레임 수를 설정
    
    
    # 2. 이벤트 처리 (키보드, 마우스 등)   
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
            
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key ==  pygame.K_RIGHT:
                to_x += character_speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0        
        
    # 3. 게임캐릭터 위치 정의
    character_x_pos += to_x
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width 
    
    # 1번째 똥 위치정의    
    ddong_y_pos += ddong_speed
    
    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
        
        ddong_y_pos += ddong_speed
    
    # 2번째 똥 위치정의
    ddong_y_pos2 += ddong_speed2
    
    if ddong_y_pos2 > screen_height:
        ddong_y_pos2 = 0
        ddong_x_pos2 = random.randint(0, screen_width - ddong_width2)    
       
        ddong_y_pos2 += ddong_speed2

    # 3번째 똥 위치 정의
    ddong_y_pos3 += ddong_speed3
    
    if ddong_y_pos3 > screen_height:
        ddong_y_pos3 = 0
        ddong_x_pos3 = random.randint(0, screen_width - ddong_width3)    
       
        ddong_y_pos3 += ddong_speed3



    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    # 1번째 똥 충돌 처리
    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos
    
    # 2번째 똥 충돌 처리
    ddong2_rect = ddong2.get_rect()
    ddong2_rect.left = ddong_x_pos2
    ddong2_rect.top = ddong_y_pos2
    
    # 3번째 똥 충돌 처리
    ddong3_rect = ddong3.get_rect()
    ddong3_rect.left = ddong_x_pos3
    ddong3_rect.top = ddong_y_pos3
    
    if character_rect.colliderect(ddong_rect) or character_rect.colliderect(ddong2_rect) or character_rect.colliderect(ddong3_rect):
        print("충돌했어요 !!")
        running = False

    # 5. 타이머 만들기 
    
    # 경과 시간 계산 
    elapsed_time = ((pygame.time.get_ticks() - start_ticks) / 1000) # 경과 시간(ms)을 1000으로 나우어서 초(s) 단위로 표시
    timer = game_font.render(str(int(total_time - elapsed_time)),True, (255, 255, 255)) # 출력할 글자, True, 글자 색상
    
    
    # 6. 화면에 그리기 
    screen.blit(background, (0, 0)) # 배경화면 그리기
    screen.blit(character ,(character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))    # 1번째 똥 그리기
    screen.blit(ddong2, (ddong_x_pos2, ddong_y_pos2)) # 2번째 똥 그리기
    screen.blit(ddong3, (ddong_x_pos3, ddong_y_pos3)) # 3번째 똥 그리기
    screen.blit (timer, (10,10)) # 타이머 그리기
    
    
    # 만약 시간이 0 이하가 되면 게임 클리어
    if total_time - elapsed_time <= 0:
        print("게임 클리어 !!!!")
        running = False
    
    pygame.display.update() # 게임화면을 다시 그리기! (반복적으로 되어야 함)
    
# 종료 되기전에 잠시 대기
pygame.time.delay(1000) # 1초 정도 대기 (me)

# pygame 종료  
pygame.quit()
