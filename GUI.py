# from main import CIRCLE_RADIUS, CIRCLE_WIDTH, SPACE, SQUARE_SIZE
import pygame

pygame.init()
pygame.font.init()
fnt=pygame.font.SysFont("comiscans",40)

Bo=[" " for _ in range(9)]
class Grid:
    Board=[Bo[i*3:(i+1)*3] for i in range(3)]
    print(Board)
    def __init__(self,rows,cols,width,height):
        self.rows=rows
        self.cols=cols
        self.cubes=[[Cube(self.Board[i][j],i,j,width,height) for j in range(cols)] for i in range(rows)]
        self.width=width
        self.height=height
        self.selected=None
        self.board=None

    def update_board(self):
        self.board=[[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def draw(self,screen):
        # Drawing the lines 
        gap=self.width/3
        for i in range(self.rows+1):
            pygame.draw.line(screen,(0,0,0),(0,i*gap),(self.width,i*gap),4)
            pygame.draw.line(screen,(0,0,0),(i*gap,0),(i*gap,self.height),4)

        # # Drawing the cubes
        # for i in range(self.rows):
        #     for j in range(self.cols):
        #         self.cubes[i][j].draw(screen)

    def click(self,pos):
        if pos[0]< self.width and pos[1]< self.height:
            gap=self.width/3
            x=pos[0]//gap
            y=pos[1]//gap
            return (int(y),int(x))

    def select(self,row,col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected=False
        self.cubes[row][col].selected=True
        self.selected=(row,col)

    def draw_figure(self,screen,player):
        SQUARE_SIZE=150
        SPACE=30
        CIRCLE_RADIUS=60
        CIRCLE_WIDTH=10
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col]==1:
                    pygame.draw.circle( screen, (0,0,0), (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
                elif self.board[row][col]==2:
                    pygame.draw.line( screen, (0,0,0), (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 10 )	
                    pygame.draw.line( screen, (0,0,0), (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 10 )






class Cube:
    def __init__(self,value,row,col,width,height):
        self.value=value
        self.row=row
        self.col=col
        self.width=width
        self.height=height
        self.selected=False

    def draw(self,screen):
    #     gap=self.width/3
    #     x=self.col*gap
    #     y=self.row*gap
    #     if self.value!=" ":
    #         Text=fnt.render(self.value,1,(255,0,0))
    #         screen.blit(Text,(x+(gap/2 -Text.get_width()/2),y+(gap/2 -Text.get_height()/2)))
    #     if self.selected:
    #         pygame.draw.rect(screen,(255,0,0),(x,y,gap,gap),3)
        for i in range(self.row):
            for j in range(self.col):
                pygame.draw.circle(screen,(0,0,0),(int(j*200+200//2),int(i*200+200//2)),60,15)

    def set_val(self,val):
        self.value=val

        

def redraw_window(screen,board):
    screen.fill((255,255,255))
    text=fnt.render(None,1,(0,0,0))
    screen.blit(text,(250,250))
    board.draw(screen)


def main():
    screen=pygame.display.set_mode((460,500))
    pygame.display.set_caption("TicTacToe")
    board=Grid(3,3,460,460)
    run =True
    player="X"
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                clicked=board.click(pos)
                if clicked:
                    board.select=(clicked[0],clicked[1])
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    print("enter")
                    board.draw_figure(screen,player)
                    pygame.display.update()
                    player="O" if player=="X" else "X"
        redraw_window(screen,board)
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
