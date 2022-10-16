import pygame 
from sys import exit

pygame.init()

screenWidth , screenHeight = 800,800
FBS = 10
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenWidth,screenHeight))

class grid:
    def __init__(self):
        self.board =[['','',''],
                     ['','',''],
                     ['','','']] 
        self.cell_size = screenWidth//3
        self.player = ['X','O']
        self.current_player = self.player[0]
        self.index = 0

        self.font = pygame.font.Font('freesansbold.ttf', 128)
        self.win_font = pygame.font.Font('freesansbold.ttf',32)
        
        
    def draw(self,screen):
        for i,k in enumerate(self.board):
            for j , v in enumerate(k):
                pygame.draw.rect(screen,(200,200,200),pygame.Rect(i*self.cell_size,j*self.cell_size,self.cell_size,self.cell_size),1)
                if v != '':
                    player_font_surface = self.font.render(v,True,(255,255,255))
                    screen.blit(player_font_surface,(i*self.cell_size+ self.cell_size//2 - player_font_surface.get_width()//2 , j*self.cell_size + self.cell_size//2 - player_font_surface.get_width()//2))
            
    def player_input(self):
        if pygame.mouse.get_pressed()[0]:
            
            mouse_x , mouse_y = pygame.mouse.get_pos()
            cell_x , cell_y = mouse_x //self.cell_size , mouse_y // self.cell_size
            if self.board[cell_x][cell_y] == '':
                self.index += 1
                self.board[cell_x][cell_y] = self.current_player 
                self.current_player = self.player[self.index%2]
            
            
    def win_condition(self):
        #check the diagonal
        if self.board[0][0] != '' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return True
        if self.board[2][0] != ''and self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            return True
        #check the rows
        for i in range(3):
            if  self.board[i][0] != '' and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] :
                return True
        #checking the columns
        for i in range(3):
            if self.board[0][i] != ''and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return True
        
        return False
        


    def update(self,screen):
        self.draw(screen)
        if not self.win_condition():
            self.player_input()
        else:
            if self.current_player == 'X':
                winning_player = 'O'
            else:
                winning_player = 'X'
            win_font_surface = self.win_font.render('player {} win'.format(winning_player),True,(255,0,0))
            screen.blit(win_font_surface,((screenWidth//2) - (win_font_surface.get_width()//2),(screenHeight//2) - (win_font_surface.get_width()//2)))

Game = grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((0,0,0))
    Game.update(screen)

    clock.tick(FBS)
    pygame.display.update()