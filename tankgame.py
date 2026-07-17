#importing necassary libararies
import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()

clock = pygame.time.Clock()

#Setting the widht and height for the window
WIDTH, HEIGHT = 1280, 720

#Setting the surface
surface = pygame.display.set_mode((WIDTH, HEIGHT))

# Loading Images and scaling them to size
background_image = pygame.image.load("main_menu.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

controls_image = pygame.image.load("freal_controls.png")
controls_image = pygame.transform.scale(controls_image, (WIDTH, HEIGHT))

paused_image = pygame.image.load("paused.png")
paused_image = pygame.transform.scale(paused_image, (WIDTH, HEIGHT))

game_over_image = pygame.image.load("game_over.png")
game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

maze_image = pygame.image.load("tankmaze.png").convert()

maze_image = pygame.transform.scale(maze_image, (WIDTH, HEIGHT))
maze_image.set_colorkey((255, 255, 255))

#Getting the rect and mask for collisoin purposes
maze_rect = maze_image.get_rect()
maze_mask = pygame.mask.from_surface(maze_image)

#Making the display
DISPLAYSURF = pygame.display.set_mode((1280, 720))

BLACK = (0, 0, 0)

#Game name caption
pygame.display.set_caption('Steel Titans')

#Making my own theme for the Main Menu
my_theme = themes.THEME_SOLARIZED.copy()
my_theme.background_color = (0, 0, 0, 0)
my_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE

my_theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
my_theme.widget_font = pygame_menu.font.FONT_MUNRO
my_theme.widget_font_size = 100
my_theme.widget_font_color = (0, 0, 0)
my_theme.widget_offset = (0, 500)
my_theme.selection_color = (0, 0, 0)

my_theme.widget_selection_effect = pygame_menu.widgets.HighlightSelection(border_width=3, margin_x=20, margin_y=10)
my_theme.widget_font_color_selected = (255, 255, 255)
my_theme.widget_background_color_selected = (0, 0, 0)
my_theme.widget_border_color = (50, 50, 50)
my_theme.widget_border_width = 3
my_theme.widget_border_inflate = (20, 10)

current_screen = "main"  

# Functions for the Main Menu
def start():
    global current_screen, red_tank, blue_tank, all_sprites, all_bullets
    current_screen = "game"

    #Making the sprites empty in the start
    all_sprites.empty()
    all_bullets.empty()
    explosion_group.empty()

    red_tank = Redtank()
    blue_tank = Bluetank()
    all_sprites.add(red_tank)
    all_sprites.add(blue_tank)

#Back to main menu
def back_to_main():
    global current_screen
    current_screen = "main"

#Shows controls screen
def controls_menu():
    global current_screen
    current_screen = "controls"

#Draws the background for different occasions
def draw_background():
    if current_screen == "main":
        surface.blit(background_image, (0, 0))

    elif current_screen == "controls":
        surface.blit(controls_image, (0, 0))

    elif current_screen == "game":
        surface.fill((255, 255, 255))
        surface.blit(maze_image, (0, 0))

    elif current_screen == "paused":
        surface.blit(paused_image, (0, 0))

    elif current_screen == "game_over":
        surface.blit(game_over_image, (0, 0))

#Implementing the Main Menu
mainmenu = pygame_menu.Menu('', WIDTH, HEIGHT, theme=my_theme,
                            onclose=pygame_menu.events.NONE,
                            columns=3, rows=1)

# Adding Buttons
mainmenu.add.button('Play', start)
mainmenu.add.button('Controls', controls_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

# Making the Control screen
controls_screen = pygame_menu.Menu('', WIDTH, HEIGHT, theme=my_theme,
                            onclose=pygame_menu.events.NONE)

#Adding button
controls_screen.add.button('Back', back_to_main)

# Making the paused screen
paused_screen = pygame_menu.Menu('', WIDTH, HEIGHT, theme=my_theme,
                                   onclose=pygame_menu.events.NONE,
                                    position=(20, 80, False))

paused_screen.add.button('Back to Main', back_to_main)

# Main game screen
game_screen = pygame_menu.Menu('', WIDTH, HEIGHT, theme=my_theme,
                               onclose=pygame_menu.events.NONE)

# Game Over screen
game_over_screen = pygame_menu.Menu('', WIDTH, HEIGHT, theme=my_theme,
                                    onclose=pygame_menu.events.NONE,
                                    position=(10, 60, False),
                                    columns=2, rows=1)

game_over_screen.add.button('Restart', start)
game_over_screen.add.button('Back to Main', back_to_main)

# The bullet class
class Bullets(pygame.sprite.Sprite):
        
        # Setting the appearance of the bullet
        def __init__(self, pos, angle, color, owner):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
            pygame.draw.circle(self.image, color, (5,5), 5)
            self.mask = pygame.mask.from_surface(self.image)

            #Setting the basic attributes for the bullet
            self.pos = pygame.math.Vector2(pos)
            self.rect = self.image.get_rect(center=self.pos)

            self.speed = 5
            self.direction = pygame.math.Vector2(0, -1).rotate(-angle)

            self.owner = owner
            self.lifetime = 12 * 60          

        #Updating the bullet
        def update(self):

            # Defining the speed and collision with walls
            self.pos += self.direction * self.speed
            self.rect.center = self.pos

            if self.pos.x <= 5 or self.pos.x >= WIDTH - 5:
                self.direction.x *= -1

            if self.pos.y <= 5 or self.pos.y >= HEIGHT - 5:
                self.direction.y *= -1
            
            #Checking collision with tank
            if not pygame.Rect(0, 0, WIDTH, HEIGHT).colliderect(self.rect):
                self.owner.bullets_count -= 1
                self.kill()

            #Bullet lifetime
            self.lifetime -= 1
            if self.lifetime <= 0:
                self.owner.bullets_count -= 1
                self.kill()

# Tank class
class Redtank(pygame.sprite.Sprite):
    
    # Making the tank appearance
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("redtank.png")
        self.image = pygame.transform.scale(self.image, (35, 50)) 
        self.original_image = self.image
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)   
        self.pos = pygame.math.Vector2(self.rect.center)

        # Bullet angle initilsed
        self.angle = 0
        self.speed = 0  
        
        # Setting bullets 
        self.max_bullets = 5
        self.bullets_count = 0
        self.shoot_cooldown = 0

    #Updating the tank
    def update(self):
        #Applying the keys for the tank to move around
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a]:
            self.angle += 4
        if pressed_keys[pygame.K_d]:
            self.angle -= 4
        self.speed = 0
        if pressed_keys[pygame.K_w]:
            self.speed = 2.5
        if pressed_keys[pygame.K_s]:
            self.speed = -2.5

        #Setting the direction and the movements
        self.direction = pygame.math.Vector2(0, -1).rotate(-self.angle)
        self.pos += self.direction * self.speed

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=self.pos)

        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))
        self.pos = pygame.math.Vector2(self.rect.center)

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    # Shooting method
    # Spawning the bullet
    def shoot(self):
        if self.bullets_count < self.max_bullets and self.shoot_cooldown == 0:
            offset = 30
            bullet_pos = self.pos + self.direction * offset
            
            bullet = Bullets(bullet_pos, self.angle, (255, 0, 0), self)
            all_bullets.add(bullet)
            self.bullets_count += 1
            self.shoot_cooldown = 9

# Blue tank class
class Bluetank(pygame.sprite.Sprite):
    def __init__(self):
        # Making the tank appearance
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bluetank.png")
        self.image = pygame.transform.scale(self.image, (35, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.original_image = self.image

        self.rect = self.image.get_rect()
        self.rect.center = (1000, 500)
        self.pos = pygame.math.Vector2(self.rect.center)

        self.angle = 0
        self.speed = 0
        self.shoot_cooldown = 0

        self.max_bullets = 5
        self.bullets_count = 0

    #Updating the Blue tank
    def update(self):

        #Applying the keys to move the tank around
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.angle += 4
        if pressed_keys[pygame.K_RIGHT]:
            self.angle -= 4
        self.speed = 0
        if pressed_keys[pygame.K_UP]:
            self.speed = 2.5
        if pressed_keys[pygame.K_DOWN]:
            self.speed = -2.5

        # Direction and movement
        self.direction = pygame.math.Vector2(0, -1).rotate(-self.angle)
        self.pos += self.direction * self.speed

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)

        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))
        self.pos = pygame.math.Vector2(self.rect.center)

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    # Shoot method
    def shoot(self):
        # Spawning bullets
        if self.bullets_count < self.max_bullets and self.shoot_cooldown == 0:
            offset = 30
            bullet_pos = self.pos + self.direction * offset

            bullet = Bullets(bullet_pos, self.angle, (0, 0, 255), self)
            all_bullets.add(bullet)
            self.bullets_count += 1
            self.shoot_cooldown = 9

# Creating instaces
red_tank = Redtank()
blue_tank = Bluetank()
all_sprites = pygame.sprite.Group()
all_sprites.add(red_tank)
all_sprites.add(blue_tank)
all_bullets = pygame.sprite.Group()

BLACK = (0, 0, 0)

# Making Explosion class
class Explosion(pygame.sprite.Sprite):

    # Making the animation
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(f"exp{num}.png").convert()
            img = pygame.transform.scale(img, (150, 150))
            img.set_colorkey(BLACK)
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    #Updating the Explosion and setting the explosion speed
    def update(self):
        explosion_speed = 4
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

explosion_group = pygame.sprite.Group()

# Tank collision with the maze wall
def wall_collision(tank, old_pos):
        offset = (int(tank.rect.x - maze_rect.x), int(tank.rect.y - maze_rect.y))

        if maze_mask.overlap(tank.mask, offset):
            tank.pos = pygame.math.Vector2(old_pos)
            tank.rect.center = old_pos

timer = 0

winner = ""

running = True

while running:

    draw_background()

    events = pygame.event.get()
    for event in events:
        
        # The quit function
        if event.type == pygame.QUIT:
            running = False
        
        # Changing b/w 'paused' and 'game' screens
        if event.type == pygame.KEYDOWN:
            if current_screen == 'paused':

                if event.key == pygame.K_p:
                    current_screen = 'game'

            elif current_screen == 'game':
                
                if event.key == pygame.K_p:
                    current_screen = 'paused'
    
    # Updating stuff
    if current_screen == "main":
        mainmenu.update(events)
        mainmenu.draw(surface)

    elif current_screen == "controls":
        controls_screen.update(events)  
        controls_screen.draw(surface)

    elif current_screen == "paused":
        paused_screen.update(events)  
        paused_screen.draw(surface)
        
    elif current_screen == "game":
        # all_sprites.update()
        # all_bullets.update()

        explosion_group.update()
        explosion_group.draw(surface)
        
        # Storing old positions of tanks before collision.
        red_old_pos = pygame.math.Vector2(red_tank.pos)
        blue_old_pos = pygame.math.Vector2(blue_tank.pos)

        all_sprites.update()
        all_bullets.update()

        wall_collision(red_tank, red_old_pos)
        wall_collision(blue_tank, blue_old_pos)
    
        # Bullet and Maze collision for bouncing off the walls at an angle 
        for bullet in list(all_bullets):
            offset = (int(bullet.rect.x - maze_rect.x), int(bullet.rect.y - maze_rect.y))
            if maze_mask.overlap(bullet.mask, offset):
                bullet.direction.x *= -1
                bullet.pos += bullet.direction * bullet.speed
                bullet.rect.center = bullet.pos

            offset = (int(bullet.rect.x - maze_rect.x), int(bullet.rect.y - maze_rect.y))
            if maze_mask.overlap(bullet.mask, offset):
                bullet.direction.x *= -1
                bullet.direction.y *= -1
                bullet.pos += bullet.direction * bullet.speed
                bullet.rect.center = bullet.pos
        
        # Bullet and tank collision for the red tank
        for bullet in list(all_bullets):
            if bullet.owner != red_tank:
                offset = (bullet.rect.x - red_tank.rect.x, bullet.rect.y - red_tank.rect.y)
                if red_tank.mask.overlap(bullet.mask, offset):
                    bullet.owner.bullets_count -= 1
                    bullet.kill()
                    explosion = Explosion(bullet.rect.centerx, bullet.rect.centery)  
                    explosion_group.add(explosion)
                    red_tank.kill()
                    winner = "Blue"
                    print('RED TANK HIT')
                    timer = 60

            # Bullet and tank collision for the blue tank        
            if bullet.owner != blue_tank:
                offset = (bullet.rect.x - blue_tank.rect.x, bullet.rect.y - blue_tank.rect.y)
                if blue_tank.mask.overlap(bullet.mask, offset):
                    bullet.owner.bullets_count -= 1
                    bullet.kill()
                    explosion = Explosion(bullet.rect.centerx, bullet.rect.centery) 
                    explosion_group.add(explosion)
                    blue_tank.kill()
                    winner = "Red"
                    print('BLUE TANK HIT')
                    timer = 60

        all_sprites.draw(surface)
        all_bullets.draw(surface)
  
        pressed_keys = pygame.key.get_pressed()

        # Shooting keystrokes
        if pressed_keys[pygame.K_q]:
            red_tank.shoot()

        if pressed_keys[pygame.K_RSHIFT]:
            blue_tank.shoot()

        # Tank collison with each other
        if pygame.Rect.colliderect(red_tank.rect, blue_tank.rect):
            collision_vector = red_tank.pos - blue_tank.pos
            if collision_vector.length() > 0:
                collision_vector = collision_vector.normalize()
                
            push_distance = 3
            red_tank.pos += collision_vector * push_distance
            blue_tank.pos -= collision_vector * push_distance

            red_tank.speed = 0
            blue_tank.speed = 0

            red_tank.rect.center = red_tank.pos
            blue_tank.rect.center = blue_tank.pos
        
        # Timer for the 'game over' screen to show
        if timer > 0:
            timer -= 1
            if timer == 0:
                current_screen = 'game_over'
    
    # Game over screen
    elif current_screen == "game_over":
        game_over_screen.update(events)

        text = pygame.font.Font(pygame_menu.font.FONT_MUNRO, 150).render(f"{winner} Tank Wins!", True, (0, 0, 0))
        rect = text.get_rect()
        rect.center = (WIDTH // 2, 450)
        surface.blit(text, rect)
        game_over_screen.draw(surface)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()