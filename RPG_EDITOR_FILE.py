import pygame
import os
import random

'''
To Do List:

5. Make a list that has all of the enemies and continues to the next enemy once the last was defeated

7. Add some kind of a level up system or way to gain new abilities

8. Find some way to make a screen appear in between defeating enemies

Commit Testing??
'''

#setup window
pygame.init()
WN = pygame.display.set_mode((900,500))
pygame.display.set_caption("RPG2")

WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
BROWN = (137,111,88)
BLACK = (0,0,0)
YELLOW = (255,255,0)

FPS = 60
player = ""
font = pygame.font.SysFont('Times New Roman', 16)
font2 = pygame.font.SysFont('Times New Roman', 50)
font3 = pygame.font.SysFont('Times New Roman', 25)

#create images
image = ""
GOBLIN_IMAGE = pygame.image.load(os.path.join('Assets', 'Goblin.gif'))
GOBLIN_IMAGE = pygame.transform.scale(GOBLIN_IMAGE, (200,200))
PURE_DEATH_IMAGE = pygame.image.load(os.path.join('Assets', 'PURE_DEATH_IMAGE.png'))
PURE_DEATH_IMAGE = pygame.transform.scale(PURE_DEATH_IMAGE, (200,200))
WARRIOR_IMAGE = pygame.image.load(os.path.join('Assets', 'WARRIOR_IMAGE.gif'))
WARRIOR_IMAGE = pygame.transform.scale(WARRIOR_IMAGE, (100,100))
MAGE_IMAGE = pygame.image.load(os.path.join('Assets', 'MAGE_IMAGE.gif'))
MAGE_IMAGE = pygame.transform.scale(MAGE_IMAGE, (100,100))
PRIEST_IMAGE = pygame.image.load(os.path.join('Assets', 'PRIEST_IMAGE.gif'))
PRIEST_IMAGE = pygame.transform.scale(PRIEST_IMAGE, (100,100))
CAVE_IMAGE = pygame.image.load(os.path.join('Assets', 'Cave.gif'))
PLACE_HOLDER_BACKGROUND = pygame.image.load(os.path.join('Assets', 'PLACE_HOLDER_BACKGROUND.png'))
ATTACK_BUTTON = pygame.image.load(os.path.join('Assets', 'ATTACK_BUTTON.png'))
ATTACK_BUTTON = pygame.transform.scale(ATTACK_BUTTON, (100,50))
ITEMS_BUTTON = pygame.image.load(os.path.join('Assets', 'ITEMS_BUTTON.png'))
ITEMS_BUTTON = pygame.transform.scale(ITEMS_BUTTON, (100,50))
YIELD_BUTTON = pygame.image.load(os.path.join('Assets', 'YIELD.png'))
YIELD_BUTTON = pygame.transform.scale(YIELD_BUTTON, (100,50))
EMPTY_BUTTON = pygame.image.load(os.path.join('Assets', 'menu_buttons_template.png'))
EMPTY_BUTTON = pygame.transform.scale(EMPTY_BUTTON, (100,50))
EMPTY_BUTTON_RED = pygame.image.load(os.path.join('Assets', 'EMPTY_BUTTON_RED.png'))
EMPTY_BUTTON_RED = pygame.transform.scale(EMPTY_BUTTON_RED, (100,50))
EMPTY_BUTTON_RED_2 = pygame.image.load(os.path.join('Assets', 'EMPTY_BUTTON_RED_2.png'))
EMPTY_BUTTON_RED_2 = pygame.transform.scale(EMPTY_BUTTON_RED_2, (100,50))
FIREBALL_BUTTON = pygame.image.load(os.path.join('Assets', 'FIREBALL_BUTTON.png'))
FIREBALL_BUTTON = pygame.transform.scale(FIREBALL_BUTTON, (100,50))
MAGIC_BLOCK_BUTTON = pygame.image.load(os.path.join('Assets', 'MAGIC_BLOCK_BUTTON.png'))
MAGIC_BLOCK_BUTTON = pygame.transform.scale(MAGIC_BLOCK_BUTTON, (100,50))
BACK_BUTTON = pygame.image.load(os.path.join('Assets', 'BACK_BUTTON.png'))
BACK_BUTTON = pygame.transform.scale(BACK_BUTTON, (100,50))
YES_BUTTON = pygame.image.load(os.path.join('Assets', 'YES_BUTTON.png'))
YES_BUTTON = pygame.transform.scale(YES_BUTTON, (100,50))
NO_BUTTON = pygame.image.load(os.path.join('Assets', 'NO_BUTTON.png'))
NO_BUTTON = pygame.transform.scale(NO_BUTTON, (100,50))
SLASH_BUTTON = pygame.image.load(os.path.join('Assets', 'SLASH_BUTTON.png'))
SLASH_BUTTON = pygame.transform.scale(SLASH_BUTTON, (100,50))
SHIELD_BLOCK_BUTTON = pygame.image.load(os.path.join('Assets', 'SHIELD_BLOCK_BUTTON.png'))
SHIELD_BLOCK_BUTTON = pygame.transform.scale(SHIELD_BLOCK_BUTTON, (100,50))
FURY_BUTTON = pygame.image.load(os.path.join('Assets', 'FURY_BUTTON.png'))
FURY_BUTTON = pygame.transform.scale(FURY_BUTTON, (100,50))
SMITE_BUTTON = pygame.image.load(os.path.join('Assets', 'SMITE_BUTTON.png'))
SMITE_BUTTON = pygame.transform.scale(SMITE_BUTTON, (100,50))
HEAL_BUTTON = pygame.image.load(os.path.join('Assets', 'HEAL_BUTTON.png'))
HEAL_BUTTON = pygame.transform.scale(HEAL_BUTTON, (100,50))
PRAY_BUTTON = pygame.image.load(os.path.join('Assets', 'PRAY_BUTTON.png'))
PRAY_BUTTON = pygame.transform.scale(PRAY_BUTTON, (100,50))
MANA_POTION_BUTTON = pygame.image.load(os.path.join('Assets', 'MANA_POTION_BUTTON.png'))
MANA_POTION_BUTTON = pygame.transform.scale(MANA_POTION_BUTTON, (100,50))
HEALTH_POTION_BUTTON = pygame.image.load(os.path.join('Assets', 'HEALTH_POTION_BUTTON.png'))
HEALTH_POTION_BUTTON = pygame.transform.scale(HEALTH_POTION_BUTTON, (100,50))
IDOL_OF_LIGHT_BUTTON = pygame.image.load(os.path.join('Assets', 'IDOL_OF_LIGHT_BUTTON.png'))
IDOL_OF_LIGHT_BUTTON = pygame.transform.scale(IDOL_OF_LIGHT_BUTTON, (100,50))
STAFF_WHACK_BUTTON = pygame.image.load(os.path.join('Assets', 'STAFF_WHACK_BUTTON.png'))
STAFF_WHACK_BUTTON = pygame.transform.scale(STAFF_WHACK_BUTTON, (100,50))
CHOOSE_MAGE_IMAGE = pygame.image.load(os.path.join('Assets', 'CHOOSE_MAGE_IMAGE.png'))
CHOOSE_MAGE_IMAGE = pygame.transform.scale(CHOOSE_MAGE_IMAGE, (100,100))
CHOOSE_WARRIOR_IMAGE = pygame.image.load(os.path.join('Assets', 'CHOOSE_WARRIOR_IMAGE.png'))
CHOOSE_WARRIOR_IMAGE = pygame.transform.scale(CHOOSE_WARRIOR_IMAGE, (100,100))
CHOOSE_PRIEST_IMAGE = pygame.image.load(os.path.join('Assets', 'CHOOSE_PRIEST_IMAGE.png'))
CHOOSE_PRIEST_IMAGE = pygame.transform.scale(CHOOSE_PRIEST_IMAGE, (100,100))
FIREBALL_MODEL = pygame.image.load(os.path.join('Assets', 'FIREBALL_MODEL.png'))
FIREBALL_MODEL = pygame.transform.scale(FIREBALL_MODEL, (100,100))
MAGIC_SHIELD_IMAGE = pygame.image.load(os.path.join('Assets', 'MAGIC_SHIELD_IMAGE.png'))
MAGIC_SHIELD_IMAGE = pygame.transform.scale(MAGIC_SHIELD_IMAGE, (100,100))
RESET_BUTTON = pygame.image.load(os.path.join('Assets', 'RESET_BUTTON.png'))
RESET_BUTTON = pygame.transform.scale(RESET_BUTTON, (100,50))
EXIT_BUTTON = pygame.image.load(os.path.join('Assets', 'EXIT_BUTTON.png'))
EXIT_BUTTON = pygame.transform.scale(EXIT_BUTTON, (100,50))
MAIN_MENU_IMAGE = pygame.image.load(os.path.join('Assets', 'MAIN_MENU_IMAGE.png'))
CLEAR_IMAGE = pygame.image.load(os.path.join('Assets', 'CLEAR_IMAGE.png'))
CLEAR_IMAGE = pygame.transform.scale(CLEAR_IMAGE, (100,100))
DARKNESS_IMAGE = pygame.image.load(os.path.join('Assets', 'DARKNESS.png'))
SELECT_IMAGE = pygame.image.load(os.path.join('Assets', 'SELECT_IMAGE.png'))
SLEEPING_IMAGE = pygame.image.load(os.path.join('Assets', 'SLEEPING_IMAGE.png'))
PATHS_IMAGE = pygame.image.load(os.path.join('Assets', 'PATHS_IMAGE.png'))
ENEMY_CLEAR_IMAGE = pygame.transform.scale(CLEAR_IMAGE, (200,200))
ENEMY_SELECT_IMAGE = pygame.transform.scale(SELECT_IMAGE, (200,200))
PLAY_BUTTON = pygame.image.load(os.path.join('Assets', 'PLAY_BUTTON.png'))
PLAY_BUTTON = pygame.transform.scale(PLAY_BUTTON, (100,50))
PLAY_BUTTON_HOVER = pygame.image.load(os.path.join('Assets', 'PLAY_BUTTON_HOVER.png'))
PLAY_BUTTON_HOVER = pygame.transform.scale(PLAY_BUTTON_HOVER, (100,50))
QUIT_BUTTON = pygame.image.load(os.path.join('Assets', 'QUIT_BUTTON.png'))
QUIT_BUTTON = pygame.transform.scale(QUIT_BUTTON, (100,50))
QUIT_BUTTON_HOVER = pygame.image.load(os.path.join('Assets', 'QUIT_BUTTON_HOVER.png'))
QUIT_BUTTON_HOVER = pygame.transform.scale(QUIT_BUTTON_HOVER, (100,50))
OPTIONS_BUTTON = pygame.image.load(os.path.join('Assets', 'OPTIONS_BUTTON.png'))
OPTIONS_BUTTON = pygame.transform.scale(OPTIONS_BUTTON, (100,50))
OPTIONS_BUTTON_HOVER = pygame.image.load(os.path.join('Assets', 'OPTIONS_BUTTON_HOVER.png'))
OPTIONS_BUTTON_HOVER = pygame.transform.scale(OPTIONS_BUTTON_HOVER, (100,50))
BACK_BUTTON_MENU = pygame.image.load(os.path.join('Assets', 'BACK_BUTTON_MENU.png'))
BACK_BUTTON_MENU = pygame.transform.scale(BACK_BUTTON_MENU, (100,50))
BACK_BUTTON_MENU_HOVER = pygame.image.load(os.path.join('Assets', 'BACK_BUTTON_MENU_HOVER.png'))
BACK_BUTTON_MENU_HOVER = pygame.transform.scale(BACK_BUTTON_MENU_HOVER, (100,50))

#button class
class Button:
    def __init__(self, x, y, image_normal, image_hover, image_state):
        self.image_normal = image_normal
        self.image_hover = image_hover
        self.image_state = image_state
        self.image = self.image_normal[self.image_state]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    #draws buttons
    def draw(self):
        self.image = self.image_normal[self.image_state]
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.image = self.image_hover

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.image = self.image_normal[self.image_state]
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        if action:
            return True

        WN.blit(self.image, (self.rect.x, self.rect.y))

#initializes buttons
button_1_images = {"menu" : ATTACK_BUTTON, "attack" : "", "items" : HEALTH_POTION_BUTTON, "yield" : YES_BUTTON}
button_2_images = {"menu" : ITEMS_BUTTON, "attack" : "", "items" : MANA_POTION_BUTTON, "yield" : NO_BUTTON}
button_3_images = {"menu" : YIELD_BUTTON, "attack" : BACK_BUTTON, "items" : BACK_BUTTON, "yield" : EMPTY_BUTTON}
button_4_images = {"menu" : EMPTY_BUTTON, "attack" : "", "items" : IDOL_OF_LIGHT_BUTTON, "yield" : EMPTY_BUTTON}
button_1 = Button(25,390, button_1_images, EMPTY_BUTTON, "menu")
button_2 = Button(125,390, button_2_images, EMPTY_BUTTON, "menu")
button_3 = Button(25,440, button_3_images, EMPTY_BUTTON, "menu")
button_4 = Button(125,440, button_4_images, EMPTY_BUTTON, "menu")

choose_mage_image = {"start_screen" : CHOOSE_MAGE_IMAGE,}
choose_warrior_image = {"start_screen" : CHOOSE_WARRIOR_IMAGE}
choose_priest_image = {"start_screen" : CHOOSE_PRIEST_IMAGE}
mage_button = Button(250,250, choose_mage_image, EMPTY_BUTTON, "start_screen")
warrior_button = Button(400,250, choose_warrior_image, EMPTY_BUTTON, "start_screen")
priest_button = Button(550,250, choose_priest_image, EMPTY_BUTTON, "start_screen")

character_button_images = {"null":CLEAR_IMAGE}
enemy_button_images = {"null":ENEMY_CLEAR_IMAGE}
player1_character_button = Button(150,200, character_button_images, CLEAR_IMAGE, "null")
player2_character_button = Button(25, 125, character_button_images, CLEAR_IMAGE, "null")
player3_character_button = Button(150,50, character_button_images, CLEAR_IMAGE, "null")
player4_character_button = Button(25, 275, character_button_images, CLEAR_IMAGE, "null")
character_buttons = [player1_character_button, player2_character_button, player3_character_button, player4_character_button]
enemy_character_button = Button(700,200, enemy_button_images, CLEAR_IMAGE, "null")

play_button_images = {"null":PLAY_BUTTON}
quit_button_images = {"null":QUIT_BUTTON}
options_button_images = {"null":OPTIONS_BUTTON}
back_button_menu_images = {"null":BACK_BUTTON_MENU}

play_button = Button(400,250, play_button_images, PLAY_BUTTON_HOVER, "null")
quit_button = Button(400,400, quit_button_images, QUIT_BUTTON_HOVER, "null")
options_button = Button(400,325, options_button_images, OPTIONS_BUTTON_HOVER, "null")
back_button_menu = Button(25,425, back_button_menu_images, BACK_BUTTON_MENU_HOVER, "null")

def button_1_pressed():
    global current_player
    global players
    global targeting_spell
    if button_1.image_state == "menu":
        button_1.image_state = "attack"
        button_2.image_state = "attack"
        button_3.image_state = "attack"
        button_4.image_state = "attack"
    elif button_1.image_state == "attack":
        if players[current_player].name == "Mage":
            if players[current_player].mana < 5:
                print("Not Enough Mana")
            else:
                targeting_spell = "Fireball"
        if players[current_player].name == "Warrior":
            targeting_spell = "Slash"
        if players[current_player].name == "Priest":
            if players[current_player].mana < 2:
                print("Not Enough Mana")
            else:
                targeting_spell = "Smite"
    elif button_1.image_state == "items":
        players[current_player].cast_health_potion()
    elif button_1.image_state == "yield":
        for player in players:
            player.health = 0
def buttons_menu_state():
    button_1.image_state = "menu"
    button_2.image_state = "menu"
    button_3.image_state = "menu"
    button_4.image_state = "menu"
def button_2_pressed():
    global current_player
    global players
    global targeting_spell
    if button_2.image_state == "menu":
        button_1.image_state = "items"
        button_2.image_state = "items"
        button_3.image_state = "items"
        button_4.image_state = "items"
    elif button_2.image_state == "attack":
        if players[current_player].name == "Mage":
            if players[current_player].mana < 3:
                print("Not Enough Mana")
            else:
                targeting_spell = "Magic Block"
        if players[current_player].name == "Warrior":
            players[current_player].cast_shield_block()
        if players[current_player].name == "Priest":
            if players[current_player].mana < 5:
                print("Not Enough Mana")
            else:
                targeting_spell = "Heal"
    elif button_2.image_state == "items":
        players[current_player].cast_mana_potion()
    elif button_2.image_state == "yield":
        buttons_menu_state()
def button_3_pressed():
    global current_player
    global players
    global targeting_spell
    if button_3.image_state == "menu":
        button_1.image_state = "yield"
        button_2.image_state = "yield"
        button_3.image_state = "yield"
        button_4.image_state = "yield"
    elif button_3.image_state == "attack":
        buttons_menu_state()
    elif button_3.image_state == "items" :
        buttons_menu_state()
def button_4_pressed():
    global current_player
    global players
    global targeting_spell
    if button_4.image_state == "attack":
        if players[current_player].name == "Mage":
            targeting_spell = "Staff Whack"
        if players[current_player].name == "Warrior":
            players[current_player].cast_fury()
        if players[current_player].name == "Priest":
            players[current_player].cast_pray(enemy1)
    elif button_4.image_state == "items":
        players[current_player].cast_idol_of_light()
class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
    def draw(self, hp, max_hp, type, length, width):
        if hp >= self.max_hp:
            self.hp = self.max_hp
        if type == "health":
            #update with new health
            self.hp = hp
            self.max_hp = max_hp
            #calculate health ratio
            ratio = self.hp / self.max_hp
            pygame.draw.rect(WN, BLACK, (self.x, self.y, length, width))
            pygame.draw.rect(WN, GREEN, (self.x, self.y, length * ratio, width))
        elif type == "mana":
            if self.max_hp != player.max_mana:
                self.max_hp = player.max_mana
            #update with new health
            self.hp = hp
            self.max_hp = max_hp
            #calculate health ratio
            ratio = self.hp / self.max_hp
            pygame.draw.rect(WN, BLACK, (self.x, self.y, length, width))
            pygame.draw.rect(WN, BLUE, (self.x, self.y, length * ratio, width))
        elif type == "rage":
            #update with new health
            self.hp = hp
            self.max_hp = max_hp
            #calculate health ratio
            ratio = self.hp / self.max_hp
            pygame.draw.rect(WN, BLACK, (self.x, self.y, length, width))
            pygame.draw.rect(WN, RED, (self.x, self.y, length * ratio, width))
class Enemy:
    def __init__(self, strength, faith, intellect, model, name, image):
        self.strength = strength
        self.faith = faith
        self.intellect = intellect
        self.model = model
        self.name = name
        self.img = image
        self.max_health = 0 + self.strength*10
        self.health = self.max_health
        self.max_mana = intellect * 2
        self.mana = self.max_mana
        self.prev_spell = None
        self.pot_uses = 2
        self.current_health = self.max_health
        self.current_frame = 0
        self.action = 0
        self.animations = []
        self.update_time = pygame.time.get_ticks()
        self.turn = False
        self.animating = False
        self.display_health = self.health
        self.projectile = []
        self.atmosphere = CLEAR_IMAGE
        self.particle_animation = 0
        self.particle_animations_list = []
        self.particles_current_frame = 0
        self.particle_update_time = pygame.time.get_ticks()
        self.enemy_healthbar = HealthBar(700, 125, self.current_health , self.max_health)
        self.enemy_manabar = HealthBar(700, 150, self.mana , self.max_mana)
        self.shield_health = 0
        self.blocked_damage = 0
        self.damage_taken_numbers = []
        self.heal_taken_numbers = []

    def drawing(self):
        self.img = self.animations[self.action][self.current_frame]
        if pygame.time.get_ticks() - self.update_time > 100:
            self.update_time = pygame.time.get_ticks()
            self.current_frame += 1
        if self.current_frame >= len(self.animations[self.action]):
            self.action = 0
            self.current_frame = 0
            self.update_time = pygame.time.get_ticks()
        if self.action != 0 and pygame.time.get_ticks() - self.update_time > 50 and self.current_frame+1 >= len(self.animations[self.action]):
            self.animating = False
        WN.blit(self.img, (self.model.x, self.model.y))
        draw_text("", font, RED, 450, 250)
        self.enemy_healthbar.draw(self.current_health, self.max_health, "health",  150, 20)
        self.enemy_manabar.draw(self.mana, self.max_mana, "mana", 150, 20)
        if self.animating == False:
            self.display_health = self.health
        draw_text(f"{self.mana} / {self.max_mana}", font3, WHITE, 715, 145)
        draw_text(f"{self.display_health} / {self.max_health}", font3, WHITE, 715, 120)
        target_enemy_color = WHITE
        if self.model.collidepoint(pygame.mouse.get_pos()):
            target_enemy_color = RED
        else:
            target_enemy_color = WHITE
        if self.shield_health > 0:
            WN.blit(MAGIC_SHIELD_IMAGE, (self.model.x+50, self.model.y+50))
            draw_text(f"{self.shield_health}", font, BLUE, self.model.x+100, self.model.y+100)
        draw_text(f"{self.name}", font3, target_enemy_color, 715, 100)
        for projectile_model in self.projectile:
            if projectile_model.x > self.fireball_target.model.x:
                projectile_model.x -= 10
            if projectile_model.y > self.fireball_target.model.y:
                projectile_model.y -= 5
            if projectile_model.x <= self.fireball_target.model.x and projectile_model.y <= self.fireball_target.model.y:
                self.projectile.remove(projectile_model)
                self.particle_animation = 1
        for projectile_model in self.projectile:
            WN.blit(FIREBALL_MODEL, (projectile_model.x, projectile_model.y))
        if self.mana >= self.max_mana:
            self.mana = self.max_mana
        if self.health >= self.max_health:
            self.health = self.max_health
        
        if not self.animating:
            for number, damage in enumerate(self.damage_taken_numbers):
                draw_text(f"-{damage[0]}", pygame.font.SysFont('Times New Roman', int(damage[0]//2 + 15)), RED, self.model.x + 50, self.damage_taken_numbers[number][1] + 50)
                self.damage_taken_numbers[number][1] -= 1
                if self.damage_taken_numbers[number][1] <= self.model.y - 100:
                    self.damage_taken_numbers.remove(damage)
        
        if not self.animating:
            for number, heal in enumerate(self.heal_taken_numbers):
                draw_text(f"-{heal[0]}", pygame.font.SysFont('Times New Roman', int(heal[0]//2 + 15)), GREEN, self.model.x + 50, self.heal_taken_numbers[number][1] + 50)
                self.heal_taken_numbers[number][1] -= 1
                if self.heal_taken_numbers[number][1] <= self.model.y - 100:
                    self.heal_taken_numbers.remove(heal)
    
    def particle_animations(self):
        if self.particle_animation != 0:
            img = self.particle_animations_list[self.particle_animation][self.particles_current_frame]
            img = pygame.transform.scale(img, (self.fireball_target.model.width, self.fireball_target.model.height))
            if pygame.time.get_ticks() - self.particle_update_time > 100:
                self.particle_update_time = pygame.time.get_ticks()
                self.particles_current_frame += 1
            if self.particles_current_frame >= len(self.particle_animations_list[self.particle_animation]):
                self.animating = False
                self.particles_current_frame = 0
                self.particle_animation = 0
                self.particle_update_time = pygame.time.get_ticks()
            WN.blit(img, (self.fireball_target.model))
    def hurt(self, damage, type, crit_chance):
        crit = random.random()
        if crit <= crit_chance:
            damage *=  2
            print("Critical hit!")
        if self.name == "Pure Death" and type == "Holy":
            damage *= 2
        if self.shield_health > 0:
            if self.shield_health >= damage:
                print(f"{self.name} prevented {damage} damage")
                self.shield_health -= damage
                damage = 0
            else:
                damage -= self.shield_health
                print(f"{self.name} prevented {self.shield_health} damage")
                self.shield_health = 0

        if self.blocked_damage > 0 and damage > 0:
            print(f"{self.name} blocked {damage * self.blocked_damage}")
            damage *= (1-self.blocked_damage)
            damage //= 1
            self.blocked_damage = 0
        print(f"{self.name} take {damage} damage")
        self.damage_taken_numbers.append([damage, self.model.y])
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, heal, type, crit_chance):
        crit = random.random()
        if crit <= crit_chance:
            heal *=  2
            print("Critical Heal!")
        self.heal_taken_numbers.append([heal, self.model.y])
        if self.name == "Pure Death" and type == "Holy":
            self.health -= heal*2
        else:
            self.health += heal


class Goblin(Enemy):
    def __init__(self, strength, faith, intellect, model, name, image):
        super().__init__(strength, faith, intellect, model, name, image)
        temp_list = []
        self.animations.append([image, image]) #0 = idle, 1 = on fire, 2 = using sword
        for i in range(8):
            img = pygame.image.load(os.path.join('Assets/GOBLIN_HURT', f'Goblin_Fire_{i}.png'))
            img = pygame.transform.scale(img, (200,200))
            temp_list.append(img)
        self.animations.append(temp_list)
        temp_list = []
        for i in range(8):
            img = pygame.image.load(os.path.join('Assets/GOBLIN_HIT', f'GOBLIN_HIT_{i}.png'))
            img = pygame.transform.scale(img, (200,200))
            temp_list.append(img)
        self.animations.append(temp_list)
        self.spell_animation = ""


        self.particle_animations_list.append([CLEAR_IMAGE, CLEAR_IMAGE]) #0 = nothing, 1 = on fire
        temp_list = []
        for i in range(8):
            img = pygame.image.load(os.path.join('Assets/GOBLIN_HURT', f'FIRE_PARTICLES_{i}.png'))
            img = pygame.transform.scale(img, (200,200))
            temp_list.append(img)
        self.particle_animations_list.append(temp_list)
    def enemy_turn(self, player):
        spell = random.choice(["Slash", "Fireball"])
        if self.mana < 2:
            spell = "Slash"
        if self.health <= 50 and self.pot_uses > 0:
            spell = "Health Potion"
        if spell == "Slash":
            self.cast_slash(player)
        elif spell == "Fireball":
            self.cast_fireball(player)
        elif spell == "Health Potion":
            self.cast_health_potion()
    
    def cast_slash(self, target):
        self.animating = True
        self.current_frame = 0
        self.action = 2
        damage = (random.randint(0, 5) + self.strength)
        print(f"goblin attacks for {damage} damage")
        target.hurt(damage, "Physical", 0.2)
    def cast_fireball(self, target):
        self.animating = True
        projectile_model = pygame.Rect(700, 250, 100, 50)
        self.fireball_target = target
        self.projectile.append(projectile_model)
        damage = (random.randint(5, 10) + self.intellect)
        print(f"goblin attacks for {damage} damage")
        target.hurt(damage, "Fire", 0.3)
        self.mana -= 2
    def cast_health_potion(self):
        self.health += 25
        print("The goblin uses a potion and recovers 25 health.")
        self.pot_uses -= 1
        if self.pot_uses == 0:
            print("The goblin has no more potions!")
        self.current_health = self.health
    def update(self):
        pass
class Pure_Death(Enemy):
    def __init__(self, strength, faith, intellect, model, name, image):
        super().__init__(strength, faith, intellect, model, name, image)
        self.animations.append([image, image])
        self.darkness = False
        self.darkness_tick_time = pygame.time.get_ticks()

    def enemy_turn(self, target):
        spell = random.choice(["Darkness", "Soul Drain"])
        if self.darkness == True:
            spell = "Soul Drain"
        if spell == "Darkness":
            self.cast_darkness(target)
        elif spell == "Soul Drain":
            self.cast_soul_drain(target)
    def cast_darkness(self, target):
        self.darkness = True
    def cast_soul_drain(self, target):
        target.mana -= 10
        target.rage_damage -= 10
        damage = 10
        target.hurt(damage, "Death", 0)
        self.health += 100
    def update(self):
        if self.darkness == True and pygame.time.get_ticks() - self.darkness_tick_time > 500:
            self.atmosphere = DARKNESS_IMAGE
            for player in players:
                if player.health > 0:
                    player.hurt(1, "Dark", 0)
            self.darkness_tick_time = pygame.time.get_ticks()
class Player_Character:
    def __init__(self, strength, faith, intellect, model, name, image):
        self.name = name
        self.strength = strength
        self.faith = faith
        self.intellect = intellect
        self.max_health = 100 + self.strength * 10
        self.health = self.max_health
        self.max_mana = self.intellect * 2
        self.mana = self.max_mana
        self.shield_health = 0
        self.max_rage = 5 * self.strength
        self.rage_damage = 0
        self.model = model
        self.update_time = pygame.time.get_ticks()
        self.img = image
        self.spell_animation = ""
        self.prayers = 0
        self.extra_lives = 0
        self.player_projectile = [] 
        self.damage_taken_multiplier = 0
        self.particle_animation = 0
        self.particle_animations_list = []
        self.particles_current_frame = 0
        self.particle_update_time = pygame.time.get_ticks()
        self.player_healthbar = HealthBar(self.model.y*-1.2+600, 400, self.health , self.max_health)
        self.player_manabar = HealthBar(self.model.y*-1.2+600, 450, self.mana , self.max_mana)
        self.player_ragebar = HealthBar(self.model.y*-1.2+600, 450, self.rage_damage , self.max_rage)
        self.taken_turn = False
        self.blocked_damage = 0
        self.damage_taken_numbers = []
        self.heal_taken_numbers = []
    def cast_mana_potion(self):
        self.mana += 10
        print("You use mana potion and gain 10 mana")
        self.extra_lives = 0
        enemy1.turn = True
        buttons_menu_state()
    def cast_health_potion(self):
        self.health += 25
        print("You use health potion and gain 25 health")
        self.extra_lives = 0
        enemy1.turn = True
        buttons_menu_state()
    def cast_idol_of_light(self):
        self.extra_lives += 1
        print("You used an Idol of Light and will be protected from death next turn")
        enemy1.turn = True
        buttons_menu_state()
    def drawing(self):
        global current_player
        global players
        WN.blit(self.img, (self.model.x, self.model.y))
        draw_text("", font, RED, 450, 250)
        self.player_healthbar.draw(self.health, self.max_health, "health", 75, 10)
        draw_text(f"{self.health} / {self.max_health}", font, WHITE, self.model.y*-1.2+600, 375,)
        if self.name != "Warrior":
            self.player_manabar.draw(self.mana, self.max_mana, "mana", 75, 10)
            draw_text(f"{self.mana} / {self.max_mana}", font, WHITE,self.model.y*-1.2+600, 425)
        if self.shield_health > 0:
            WN.blit(MAGIC_SHIELD_IMAGE, (self.model.x, self.model.y))
            draw_text(f"{self.shield_health}", font, BLUE, self.model.x+50, self.model.y+50)
        for projectile_model in self.player_projectile:
            WN.blit(FIREBALL_MODEL, (projectile_model.x, projectile_model.y))
        if self.name == "Warrior":
            self.player_ragebar.draw(self.rage_damage, self.max_rage, "rage", 75, 10)
            draw_text(f"{self.rage_damage} / {self.max_rage}", font, WHITE, self.model.y*-1.2+600, 425)
        target_player_color = WHITE
        if self == players[current_player]:
            target_player_color = BLUE
        else:
            target_player_color = WHITE
        if self.model.collidepoint(pygame.mouse.get_pos()):
            target_player_color = GREEN
        draw_text(f"{self.name}", font, target_player_color, self.model.y*-1.2+615, 460)
        if self.health <= 0 and self.extra_lives != 0:
            self.health = 50
            print("You Died, but by the grace of light were brought back to life!")
        
        if players[current_player].name == "Mage":
            button_1_images["attack"] = FIREBALL_BUTTON
            button_2_images["attack"] = MAGIC_BLOCK_BUTTON
            button_4_images["attack"] = STAFF_WHACK_BUTTON
        elif players[current_player].name == "Warrior":
            button_1_images["attack"] = SLASH_BUTTON
            button_2_images["attack"] = SHIELD_BLOCK_BUTTON
            button_4_images["attack"] = FURY_BUTTON
        elif players[current_player].name == "Priest":
            button_1_images["attack"] = SMITE_BUTTON
            button_2_images["attack"] = HEAL_BUTTON
            button_4_images["attack"] = PRAY_BUTTON
        if self.rage_damage >= self.max_rage:
            self.rage_damage = self.max_rage
        if self.mana >= self.max_mana:
            self.mana = self.max_mana
        if self.health >= self.max_health:
            self.health = self.max_health
        if self.taken_turn:
            WN.blit(SLEEPING_IMAGE, (self.model))
        for number, damage in enumerate(self.damage_taken_numbers):
            draw_text(f"-{damage[0]}", pygame.font.SysFont('Times New Roman', int(damage[0]//2 + 15)), RED, self.model.x + 50, self.damage_taken_numbers[number][1] + 50)
            self.damage_taken_numbers[number][1] -= 1
            if self.damage_taken_numbers[number][1] <= self.model.y - 100:
                self.damage_taken_numbers.remove(damage)
        
        for number, heal in enumerate(self.heal_taken_numbers):
            draw_text(f"-{heal[0]}", pygame.font.SysFont('Times New Roman', int(heal[0]//2 + 15)), GREEN, self.model.x + 50, self.heal_taken_numbers[number][1] + 50)
            self.heal_taken_numbers[number][1] -= 1
            if self.heal_taken_numbers[number][1] <= self.model.y - 100:
                self.heal_taken_numbers.remove(heal)

    def hurt(self, damage, type, crit_chance):
        crit = random.random()
        if crit <= crit_chance:
            damage *=  2
            print("Critical hit!")
        
        if self.shield_health > 0:
            if type == "Fire":
                self.mana += 6
                if crit <= crit_chance:
                    print(f"{self.name}'s magic shield prevents the critical strike")
                    damage /= 2
            if self.shield_health >= damage:
                print(f"{self.name} prevented {damage} damage")
                self.shield_health -= damage
                damage = 0
            else:
                damage -= self.shield_health
                print(f"{self.name} prevented {self.shield_health} damage")
                self.shield_health = 0

        if self.damage_taken_multiplier > 0:
            print(f"{self.name} take {self.damage_taken_multiplier}% more damage due to rage")
            damage += damage*(self.damage_taken_multiplier/100)//1
        if self.blocked_damage > 0 and damage > 0:
            print(f"you blocked {damage * self.blocked_damage} damage and gained rage")
            self.rage_damage += damage * self.blocked_damage
            self.rage_damage //= 1
            damage *= (1-self.blocked_damage)
            damage //= 1
            self.blocked_damage = 0
        print(f"You take {damage} damage")
        self.damage_taken_numbers.append([damage, self.model.y])
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, heal, type, crit_chance):
        crit = random.random()
        if crit <= crit_chance:
            heal *=  2
            print("Critical Heal!")
        self.heal_taken_numbers.append([heal, self.model.y])
        self.health += heal


    def attack_animation(self):
        if self.mana > self.max_mana:
                self.mana = self.max_mana
        if self.health > self.max_health:
            self.health = self.max_health
        if self.spell_animation == "Fireball":
            for projectile_model in self.player_projectile:
                if projectile_model.y > enemy1.model.y:
                    projectile_model.y -= 10
                if projectile_model.y < enemy1.model.y:
                    projectile_model.y += 10
                if projectile_model.x < 700:
                    projectile_model.x += 10
                else:
                    self.player_projectile.remove(projectile_model)
                    enemy1.action = 0
            if len(self.player_projectile) == 0:
                self.particle_animation = 1
                self.spell_animation = ""
    def particle_animations(self, target):
        if self.particle_animation != 0:
            img = self.particle_animations_list[self.particle_animation][self.particles_current_frame]
            img = pygame.transform.scale(img, (target.model.width, target.model.height))
            if pygame.time.get_ticks() - self.particle_update_time > 100:
                self.particle_update_time = pygame.time.get_ticks()
                self.particles_current_frame += 1
            if self.particles_current_frame >= len(self.particle_animations_list[self.particle_animation]):
                enemy1.animating = False
                self.particles_current_frame = 0
                self.particle_animation = 0
                self.particle_update_time = pygame.time.get_ticks()
            WN.blit(img, (target.model.x, target.model.y))
class Mage(Player_Character):
    def __init__(self, strength, faith, intellect, model, name, image):
        super().__init__(strength, faith, intellect, model, name, image)
        self.particle_animations_list.append([CLEAR_IMAGE, CLEAR_IMAGE]) #0 = nothing, 1 = on fire
        temp_list = []
        for i in range(8):
            img = pygame.image.load(os.path.join('Assets/GOBLIN_HURT', f'FIRE_PARTICLES_{i}.png'))
            img = pygame.transform.scale(img, (200,200))
            temp_list.append(img)
        self.particle_animations_list.append(temp_list)

    def cast_staff_whack(self, target):
        damage = 5 + self.strength
        self.mana += 5
        print(f"You Whack the {target.name} for {damage} damage")
        target.hurt(damage, "Physical", 0)
        self.extra_lives = 0
        enemy1.turn = True
        buttons_menu_state()

    def cast_fireball(self, target):
        projectile_model = pygame.Rect(self.model.x, self.model.y, 100, 50)
        self.player_projectile.append(projectile_model)
        self.spell_animation = "Fireball"
        enemy1.animating = True 
        damage = random.randint(5,15) + self.intellect*2
        crit = random.random()
        target.hurt(damage, "Fire", crit)
        self.damage_just_done = damage
        self.mana -= 5
        self.extra_lives = 0
        enemy1.turn = True
        buttons_menu_state()
    def cast_magic_block(self, target):
        block = random.randint(5,15) + self.intellect
        target.shield_health += block
        print("You use Magic Block and create a barrier with", block, "health.")
        self.mana -= 3
        self.extra_lives = 0
        enemy1.turn = True
        buttons_menu_state()
class Warrior(Player_Character):
    def __init__(self, strength, faith, intellect, model, name, image):
        super().__init__(strength, faith, intellect, model, name, image)
    def cast_slash(self, target):
        damage = 5 + self.strength + self.rage_damage
        crit = random.random()
        target.hurt(damage, "Physical", crit)
        if self.rage_damage > 0:
            print(f"You dealt {self.rage_damage} extra damage due to Shield Block!")
            self.rage_damage = 0
        self.extra_lives = 0
        enemy1.turn = True
        buttons_menu_state()
    def cast_shield_block(self):
        block = 0.3 + self.strength*0.01
        self.blocked_damage = block
        print(f"You use Shield Block and block {block*100}% damage. you are now the goblin's target")
        self.extra_lives = 0
        enemy1.turn = True
        buttons_menu_state()
    def cast_fury(self):
        self.hurt(15, "Physical", 0)
        self.rage_damage += 15
        if self.health <= self.max_health/2:
            self.rage_damage += 30
        if self.rage_damage >= self.max_rage:
            self.rage_damage = self.max_rage
        self.damage_taken_multiplier = self.rage_damage*100//self.max_rage
        self.extra_lives = 0
        enemy1.turn = True
        buttons_menu_state()
class Priest(Player_Character):
    def __init__(self, strength, faith, intellect, model, name, image):
        super().__init__(strength, faith, intellect, model, name, image)
    def cast_smite(self, target):
        damage = 10 + self.faith
        crit = random.random()
        target.hurt(damage, "Holy", crit)
        self.mana -= 2
        self.extra_lives = 0
        enemy1.turn = True
        buttons_menu_state()
    def cast_heal(self, target):
        heal = random.randint(15,30) + self.faith
        print("You heal yourself for", heal, "health.")
        target.heal(heal, "Holy", self.faith*0.01)
        self.mana -= 5
        self.extra_lives = 0
        enemy1.turn = True
        buttons_menu_state()

    def cast_pray(self, target):
        if target == pure_death:
            if target.darkness == True:
                target.darkness = False 
                target.atmosphere = CLEAR_IMAGE
                print("Your prayer clears the darkness")
        if self.prayers == 6:
            damage = self.faith * 10
            print(f"Divine Wrath punishes the {target.name}, dealing {damage} damage")
            self.health += self.faith*5
            target.hurt(damage, "Holy", 0)
            self.prayers = 0
        else:
            crit = random.random()
            if crit <= 0.05 + self.faith*0.001:
                self.health += 10*self.faith
                self.mana += 2*self.faith
                print(f"Your prayers have been answered, you heal {10*self.faith} health and gain {2*self.faith} mana")
            self.prayers += 1
            self.mana += 3
            print(f"{7-self.prayers} prayers remaining until Divine Wrath")
        self.extra_lives = 0
        enemy1.turn = True
        buttons_menu_state()
enemy1 = Goblin(10, 0, 5, pygame.Rect(700, 200, 200, 200), "Goblin", GOBLIN_IMAGE)
pure_death = Pure_Death(100, 100, 100, pygame.Rect(700, 200, 200, 200), "Pure Death", PURE_DEATH_IMAGE)
player = Player_Character(10, 10, 10, pygame.Rect(100, 200, 100, 100), "Null", MAGE_IMAGE)
def choose_class(name):
    global player
    global image
    if name == "Mage":
        player = Mage(3, 1, 10, pygame.Rect(100, 250, 100, 100), "Mage", MAGE_IMAGE)
    elif name == "Warrior":
        player = Warrior(10, 3, 1, pygame.Rect(100, 250, 100, 100), "Warrior", WARRIOR_IMAGE)
    elif name == "Priest":
        player = Priest(1, 10, 7, pygame.Rect(100, 250, 100, 100), "Priest", PRIEST_IMAGE)

priest = Priest(1, 10, 7, pygame.Rect(150, 50, 100, 100), "Priest", PRIEST_IMAGE)
warrior = Warrior(10, 3, 1, pygame.Rect(25, 125, 100, 100), "Warrior", WARRIOR_IMAGE)
mage = Mage(3, 1, 10, pygame.Rect(150, 200, 100, 100), "Mage", MAGE_IMAGE)
mage2 = Mage(3, 1, 10, pygame.Rect(25, 275, 100, 100), "Mage", MAGE_IMAGE)
warrior2 = Warrior(10, 3, 1, pygame.Rect(25, 275, 100, 100), "Warrior", WARRIOR_IMAGE)
players = [mage, warrior, priest, warrior2]
current_player = 0

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	WN.blit(img, (x, y))

def reset_game():
    global enemy1
    global pure_death
    global enemy_healthbar
    global background
    for player in players:
        player.health = player.max_health
        player.mana = player.max_mana
        player.rage_damage = 0
        player.prayers = 0
        player.extra_lives = 0
        player.shield_health = 0
        player.taken_turn = False
    enemy1.health = enemy1.max_health
    enemy1.mana = enemy1.max_mana
    enemy1.turn = False
    button_1.image_state = "menu"
    button_2.image_state = "menu"
    button_3.image_state = "menu"
    button_4.image_state = "menu"
    background = PLACE_HOLDER_BACKGROUND

reset_button_image = {"start_screen" : RESET_BUTTON}
restart_button = Button(300,250, reset_button_image, EMPTY_BUTTON, "start_screen")

exit_button_image = {"start_screen" : EXIT_BUTTON}
exit_button = Button(400,250, exit_button_image, EMPTY_BUTTON, "start_screen")
#main gameplay loop
def main():
    global current_player
    global pure_death 
    global enemy1
    global enemy_healthbar
    global targeting_spell
    global game_over
    global background
    level1 = ""
    level2 = ""
    level3 = ""
    levels = [level1, level2, level3]
    game_over = False
    target = random.choice(players)
    screen_y_position = -1750
    screen_x_position = -270
    current_player = 0
    #creates hitboxes for goblin and player
    text_pos = 75
    text =""
    enemy1.turn = False
    background = PLACE_HOLDER_BACKGROUND
    main_menu = True
    spell_text_color = WHITE
    targeting_spell = "Null"
    #sets FPS
    clock = pygame.time.Clock()
    running = True
    while running:
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if main_menu == True:
            WN.blit(MAIN_MENU_IMAGE, (0,0))
            if play_button.draw():
                main_menu = False
            if options_button.draw():
                print("Kappa123")
            if quit_button.draw():
                pygame.quit()
            pygame.display.update()
        elif background == PLACE_HOLDER_BACKGROUND and main_menu == False:
            WN.blit(PATHS_IMAGE, (screen_x_position,screen_y_position))
            if keys[pygame.K_UP] and screen_y_position <= 0:
                screen_y_position += 10
            if keys[pygame.K_DOWN] and screen_y_position >= -2000:
                screen_y_position -= 10
            if keys[pygame.K_LEFT] and screen_x_position <= 0:
                screen_x_position += 10
            if keys[pygame.K_RIGHT] and screen_x_position >= -500:
                screen_x_position -= 10
            mage_button.rect.x, mage_button.rect.y  = screen_x_position+675, screen_y_position+2100
            priest_button.rect.x, priest_button.rect.y  = screen_x_position+850, screen_y_position+1350
            warrior_button.rect.x, warrior_button.rect.y  = screen_x_position+675, screen_y_position+1800
            if mage_button.draw():
                level_number = 1
                background = CAVE_IMAGE
            elif warrior_button.draw():
                if level1 == "completed":
                    enemy1 = pure_death 
                    enemy_healthbar = HealthBar(700, 150, enemy1.current_health , enemy1.max_health)
                    background = CAVE_IMAGE
                else:
                    print("moron")
            elif priest_button.draw():
                background = CAVE_IMAGE
            elif back_button_menu.draw():
                main_menu = True
        else:
            WN.blit(background, (0,0))
            WN.blit(enemy1.atmosphere, (0,0))
            enemy1.drawing()
            enemy1.update()
            for player in players:
                player.drawing()
            if players[current_player].health <= 0 and not game_over:
                current_player += 1
                if current_player == len(players):
                        current_player = 0
            players[current_player].drawing()
            players[current_player].attack_animation()
            enemy1.particle_animations()
            players[current_player].particle_animations(enemy1)
            WN.blit(SELECT_IMAGE, (players[current_player].model.x, players[current_player].model.y))
            if enemy1.animating == False and len(enemy1.projectile) == 0 and enemy1.animating == False and enemy1.model.x == 700:
                text = "PLAYER TURN"
            if enemy1.turn == False and text_pos != 75 and enemy1.animating == False and len(enemy1.projectile) == 0:
                text_pos -= 10
            if enemy1.turn == True and text_pos != 705 and enemy1.animating == False:
                text_pos += 10
            draw_text(text, font, RED, text_pos, 25)
            if len(players[current_player].player_projectile) == 0 and not enemy1.turn and len(enemy1.projectile) == 0 and enemy1.animating == False and players[current_player].health > 0:
                can_press_buttons = True
            else:
                can_press_buttons = False           
            if button_3.draw():
                if can_press_buttons == True:
                    button_3_pressed()     
            if button_4.draw():
                if can_press_buttons == True:              
                    button_4_pressed()
            if button_1.draw():
                if can_press_buttons == True: 
                    button_1_pressed()
            if button_2.draw():
                if can_press_buttons == True:
                    button_2_pressed()
            if targeting_spell == "Null" and can_press_buttons:
                for i in range(len(players)):
                    if character_buttons[i].draw():
                        if players[i].taken_turn == False:
                            current_player = i
            if targeting_spell == "Null":
                if enemy_character_button.draw():
                    print("Hi")
            if targeting_spell != "Null":
                draw_text(f"Cast {targeting_spell}", font, spell_text_color, pygame.mouse.get_pos()[0]+10, pygame.mouse.get_pos()[1]+10)

                if targeting_spell == "Fireball":
                    spell_text_color = RED
                    if enemy_character_button.draw():
                        if enemy1.health > 0:
                            players[current_player].cast_fireball(enemy1)
                            targeting_spell = "Null"
                if targeting_spell == "Magic Block":
                    spell_text_color = BLUE
                    for i in range(len(players)):
                        if character_buttons[i].draw():
                            if players[i].health > 0:
                                players[current_player].cast_magic_block(players[i])
                                targeting_spell = "Null"
                if targeting_spell == "Staff Whack":
                    spell_text_color = BROWN
                    if enemy_character_button.draw():
                        if enemy1.health > 0:
                            players[current_player].cast_staff_whack(enemy1)
                            targeting_spell = "Null"

                if targeting_spell == "Slash":
                    spell_text_color = BLACK
                    if enemy_character_button.draw():
                        if enemy1.health > 0:
                            players[current_player].cast_slash(enemy1)
                            targeting_spell = "Null"
                
                if targeting_spell == "Smite":
                    spell_text_color = WHITE
                    if enemy_character_button.draw():
                        if enemy1.health > 0:
                            players[current_player].cast_smite(enemy1)
                            targeting_spell = "Null"
                if targeting_spell == "Heal":
                    spell_text_color = YELLOW
                    if enemy_character_button.draw():
                        if enemy1.health > 0:
                            players[current_player].cast_heal(enemy1)
                            targeting_spell = "Null"
                    for i in range(len(players)):
                        if character_buttons[i].draw():
                            if players[i].health > 0:
                                players[current_player].cast_heal(players[i])
                                targeting_spell = "Null"
                if pygame.mouse.get_pressed()[2] == 1:
                    targeting_spell = "Null"
            if all(players[i].health < 1 for i in range(len(players))):
                draw_text("YOU LOSE :(", font2, RED, 325, 150)
                game_over = True
                if restart_button.draw():
                    game_over = False
                    reset_game()
                if exit_button.draw():
                    background = PLACE_HOLDER_BACKGROUND
                    main_menu = True 
                enemy1.turn = False
                enemy1.health = enemy1.max_health
                enemy1.current_health = enemy1.max_health
            elif enemy1.health < 1:
                draw_text("YOU WIN B)", font2, GREEN, 325, 150)
                levels[level_number-1] = "completed"
                if restart_button.draw():
                    game_over = False
                    reset_game()
                if exit_button.draw():
                    pygame.quit()
                enemy1.turn = False
            if enemy1.turn and len(players[current_player].player_projectile) == 0 and len(enemy1.projectile) == 0 and enemy1.animating == False and enemy1.action == 0 and not game_over:
                players[current_player].spell_animation = ""
                text = "GOBLIN TURN"
                enemy1.current_health = enemy1.health
                for ply in players:
                    if players[current_player] == ply:
                        ply.taken_turn = True
                        enemy1.turn = False 
                if not game_over:
                    if all(players[i].taken_turn or players[i].health <= 0 for i in range(len(players))):
                            enemy1.turn = True
                    else:
                        current_player += 1
                        for i in range(len(players)):
                            if current_player == len(players):
                                current_player = 0
                            if players[current_player].taken_turn:
                                current_player += 1
                if text_pos == 705 and any(players[i].taken_turn for i in range(len(players))):
                    current_player = 0
                    while target.health <= 0:
                        target = random.choice(players)
                    for player in players:
                        if player.blocked_damage > 0:
                            target = player
                    enemy1.enemy_turn(target)
                    enemy1.turn = False
                    for player in players:
                        player.taken_turn = False
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()