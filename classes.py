import pygame
from pygame.locals import *
pygame.init()

import random
import os
import math

import functions



class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        '''
        M.__init__()
        Initializes Mouse
        '''
        pygame.sprite.Sprite.__init__(self)
        self.x=0
        self.y=0
        self.image=pygame.Surface((1,1)).convert()
        self.image.fill((0,0,0))
        self.image.set_alpha(0)        
        self.rect=self.image.get_rect()
        
        self.tool_tip_counter=0

        
    def update(self):
        '''
        M.update() --> None
        This method is used to move this sprite around on screen, and track the
        mouse.
        '''
        self.rect.left=self.x
        self.rect.top=self.y
        
        
        

class Buildings_In_To_Build(pygame.sprite.Sprite):
    
    hero_building_list=[]
    
    def __init__(self, image, y, level, name, helvet, building_type, effect_info, maintenance_cost, unlock_info, unique=False):
        '''
        B.__init__(surface, int, int, str, Font, str, list, int, str, Unique)
        Initializes B with a given image, on screen y-coordinate, level, name, 
        font, string referring to what type of building it is, information on 
        what the building does, how high the building's maintenance cost is, 
        information on how to unlock the building, and a reference to if it is a
        unique building.
        '''
        pygame.sprite.Sprite.__init__(self)
        menu_divider=pygame.Surface((127,2)).convert()
        menu_divider.fill((23,50,57))    
        
        self.name_formated=name[0].upper()+name[1:]
        while "_" in self.name_formated:
            self.name_formated=self.name_formated[:self.name_formated.find("_")]+" "+self.name_formated[self.name_formated.find("_")+1].upper()+self.name_formated[self.name_formated.find("_")+2:]
        
        name_font=pygame.font.Font(helvet, 12)
        if name=="jousting_league":
            font=pygame.font.Font(helvet, 10)
            name_text=font.render("{}".format(self.name_formated), True, (255,255,255))
        elif name=="arcane_academy":
            font=pygame.font.Font(helvet, 11)
            name_text=font.render("{}".format(self.name_formated), True, (255,255,255))
        elif name=="gambling_house":
            font=pygame.font.Font(helvet, 11)
            name_text=font.render("{}".format(self.name_formated), True, (255,255,255))
        elif name=="pegasus_olympics":
            font=pygame.font.Font(helvet, 9)
            name_text=font.render("{}".format(self.name_formated), True, (255,255,255))
        elif "national_epic" in name:
            font=pygame.font.Font(helvet, 10)
            name_text=font.render("{}".format(self.name_formated), True, (255,255,255))
        elif name=="national_treasury":
            font=pygame.font.Font(helvet, 9)
            name_text=font.render("{}".format(self.name_formated), True, (255,255,255))
        elif name=="continental_gardens":
            font=pygame.font.Font(helvet, 9)
            name_text=font.render("{}".format(self.name_formated), True, (255,255,255))
        else:
            name_text=name_font.render("{}".format(self.name_formated), True, (255,255,255))
            
        turns_left_font=pygame.font.Font(helvet, 10) 
        if level!=1:
            turns_left_text=turns_left_font.render("Locked", True, (255,255,255))
        if level==1:
            turns_left_text=turns_left_font.render("Turns: ", True, (255,255,255))
        if level==0 and name=="house":
            turns_left_text=turns_left_font.render("Turns: ", True, (255,255,255))
        if level==0 and name!="house":
            turns_left_text=turns_left_font.render("Turns: N/A", True, (255,255,255))
        if building_type=="hero building":
            turns_left_text=turns_left_font.render("Locked", True, (255,255,255))
            Buildings_In_To_Build.hero_building_list+=[self]
        if building_type=="unique building":
            turns_left_text=turns_left_font.render("Locked", True, (255,255,255))
            
        self.icon_small=pygame.transform.scale(image, (30, 30))
        self.icon_big=pygame.transform.scale(image, (57, 57))
        self.image=pygame.Surface((117,32)).convert()
        self.image.fill((0,0,0))
        self.image.blit(self.icon_small, (0,0))
        self.image.blit(menu_divider, (0,30))
        self.image.blit(name_text, (33,3))
        self.image.blit(turns_left_text, (38,16))     
        
        self.rect=self.image.get_rect()
        self.rect.top=y
        self.rect.left=11
        self.level=level
        self.name=name
        self.reset_top=y
        self.building_type=building_type
        
        if level==1:
            self.production_needed=100
        if level==2:
            self.production_needed=250
        if level==3:
            self.production_needed=300
        
        if self.name=="house":
            self.production_needed=16
        if self.name=="cater_to_a_hero":
            self.production_needed=1
        if building_type=="hero building":
            self.production_needed=200
        if building_type=="unique building":
            self.production_needed=320
        self.maintenance_cost=maintenance_cost
        self.unique_object=None
        if unique!=False:
            self.unique_object=unique
            
        self.discription_box=pygame.Surface((250, 71)).convert()   
        if name=="pegasus_olympics":
            name_font=pygame.font.Font(helvet, 11)
        if name=="continental_gardens":
            name_font=pygame.font.Font(helvet, 9)
        discription_text=name_font.render(self.name_formated, True, (255,255,255)) 
        effect_text_x=40
        effect_text_y=12
        if "national_epic" not in name:
            for i in effect_info:
                temp_text=turns_left_font.render(i, True, (255,255,255))
                self.discription_box.blit(temp_text, (40, effect_text_y))
                effect_text_y+=10
        if "national_epic" in name:
            for i in effect_info:
                if i!=effect_info[-1]:
                    temp_text=turns_left_font.render(i+",", True, (255,255,255))
                if i==effect_info[-1]:
                    temp_text=turns_left_font.render(i, True, (255,255,255))
                if (effect_text_x+temp_text.get_size()[0]+3)>=250:
                    effect_text_x=40
                    effect_text_y+=10
                self.discription_box.blit(temp_text, (effect_text_x, effect_text_y))
                if (effect_text_x+temp_text.get_size()[0]+3)<250:
                    effect_text_x+=temp_text.get_size()[0]+3
                    
        if maintenance_cost!=0:
            maintenance_text=turns_left_font.render("Maintenance: {}".format(maintenance_cost), True, (255,255,255))
            self.discription_box.blit(maintenance_text, (40, effect_text_y))
        self.discription_box.blit(self.icon_small, (5,5))
        self.discription_box.blit(discription_text, (40, 1))
        
        unlock_info_words=[]
        while unlock_info!="":
            if " " not in unlock_info:
                unlock_info_words+=[unlock_info]
                unlock_info=""
            if " " in unlock_info:
                unlock_info_words+=[unlock_info[:unlock_info.find(" ")]]
                unlock_info=unlock_info[unlock_info.find(" ")+1:]
        unlock_info_words[0]="Unlock Condition: "+unlock_info_words[0]
            
        unlock_text_x=3
        unlock_text_y=35
        for i in unlock_info_words:
            temp_text=turns_left_font.render(i, True, (255,255,255))
            if (unlock_text_x+temp_text.get_size()[0]+3)>=250:
                unlock_text_x=3
                unlock_text_y+=10
            self.discription_box.blit(temp_text, (unlock_text_x, unlock_text_y))
            if (unlock_text_x+temp_text.get_size()[0]+3)<250:
                unlock_text_x+=temp_text.get_size()[0]+3
                
            

            
class Town(pygame.sprite.Sprite):
    players=0
    def __init__(self, town_name, ai, town_img, town_distroyed_img):
        '''
        T.__init__(str, bool, surface, surface)
        Initializes T with a given name, Boolean to see if it is controlled by 
        an AI, an image of what the town looks like, and an image of what the 
        town looks like after it has been destroyed. 
        '''
        pygame.sprite.Sprite.__init__(self)
        self.town_name=town_name
        Town.players+=1
        self.player_number=Town.players
        self.ai=ai
        self.turn_phase=None
        self.difficulty_level=None
        if self.ai==True:
            self.turn_phase=""
            self.difficulty_level=3
        self.eliminated=False

        self.image=town_img
        self.rect=self.image.get_rect()
        self.town_distroyed=town_distroyed_img
        
        #Defining general stats
        self.production=5
        self.gold=5
        self.gold_per_turn=4
        self.defence=12
        self.food=15
        self.favor=10
        self.happiness=4
        self.base_happiness=4     
        self.population=10
        self.houses=10
        self.defence_from_buildings=0
        self.maintenance_cost=0
        
        
        self.constructing=None
        self.constructing_icon=None
        
        #Defining things related to the level 1, 2, and 3 buildings
        self.level_2_buildings_locked=True
        self.level_3_buildings_locked=True
        
        self.production_building_level=0
        self.gold_building_level=0
        self.defence_building_level=0
        self.food_building_level=0
        self.favor_building_level=0
        self.happiness_building_level=0
        
        self.production_building_progress=0
        self.gold_building_progress=0
        self.defence_building_progress=0
        self.food_building_progress=0
        self.favor_building_progress=0 
        self.happiness_building_progress=0 
        
        self.level_1_buildings=0
        self.level_2_buildings=0
        self.level_3_buildings=0
        
        #Defining things related to the other buildings
        self.house_building_progress=0
        self.catering_to=None
        
        #Defining things related to the hero buildings
        self.warrior_building=False           #Barracks
        self.mage_building=False              #Archane Achademy
        self.rogue_building=False             #Pub
        self.priest_building=False            #Church
        self.knight_building=False            #Armory 
        self.archer_building=False            #Shooting Range
        self.pegasus_knight_building=False    #Stable
        
        self.warrior_building_progress=0
        self.mage_building_progress=0
        self.rogue_building_progress=0
        self.priest_building_progress=0
        self.knight_building_progress=0
        self.archer_building_progress=0
        self.pegasus_knight_building_progress=0
        self.hero_buildings=0
        
        #Defining things related to the unique buildings
        self.colosseum=False
        self.mystical_shrine=False
        self.gambling_house=False
        self.chapel=False
        self.jousting_league=False
        self.hunting_grounds=False
        self.pegasus_olympics=False
        self.national_epic_s=False
        self.national_epic_m=False
        self.national_epic_l=False
        self.volcanic_forge=False
        self.national_treasury=False
        self.stronghold=False
        self.continental_gardens=False
        self.heroic_tribute=False
        self.academy_of_art=False
        
        self.colosseum_progress=0
        self.mystical_shrine_progress=0
        self.gambling_house_progress=0
        self.chapel_progress=0
        self.jousting_league_progress=0
        self.hunting_grounds_progress=0
        self.pegasus_olympics_progress=0
        self.national_epic_s_progress=0
        self.national_epic_m_progress=0
        self.national_epic_l_progress=0
        self.volcanic_forge_progress=0
        self.national_treasury_progress=0
        self.stronghold_progress=0
        self.continental_gardens_progress=0
        self.heroic_tribute_progress=0
        self.academy_of_art_progress=0
        
        #Defining stats related to the favor this town has with the heroes
        self.warrior_favor=10
        self.mage_favor=10
        self.rogue_favor=10
        self.priest_favor=10
        self.knight_favor=10
        self.archer_favor=10
        self.pegasus_knight_favor=10
        self.total_favor=70
        
        self.turns_since_warrior_visit=0
        self.turns_since_mage_visit=0
        self.turns_since_rogue_visit=0
        self.turns_since_priest_visit=0
        self.turns_since_knight_visit=0
        self.turns_since_archer_visit=0
        self.turns_since_pegasus_knight_visit=0
        
        self.warrior_event=False
        self.mage_event=False
        self.priest_event=False
        self.rogue_event=False
        self.knight_event=False
        self.archer_event=False
        self.pegasus_knight_event=False

        #Defining things related to the hero events
        self.turns_for_warrior_event=10
        self.turns_for_mage_event=10
        self.turns_for_rogue_event=10
        self.turns_for_priest_event=10
        self.turns_for_knight_event=10
        self.turns_for_archer_event=10
        self.turns_for_pegasus_knight_event=10
        
        self.warrior_event_cooldown=30
        self.mage_event_cooldown=30
        self.rogue_event_cooldown=30
        self.priest_event_cooldown=30
        self.knight_event_cooldown=30
        self.archer_event_cooldown=30
        self.pegasus_knight_event_cooldown=30
        
        self.warrior_passive_ability_active=False
        self.mage_passive_ability_active=False
        self.rogue_passive_ability_active=False
        self.priest_passive_ability_active=False
        self.knight_passive_ability_active=False
        self.archer_passive_ability_active=False
        self.pegasus_knight_passive_ability_active=False
        
        
        

        self.messages_to_display=[]

        self.hero_in_town=False
        self.heroes_in_town=[]
        self.total_defence=self.defence

        
    def place_town(self):
        '''
        T.place_town() --> None
        This determines the onscreen location of the a town.
        '''
        
        #This part of the code uses the unit circle to discover where on screen
        #a given town should be placed.
        self.rect.centery=220-((math.cos((math.pi*2)/Town.players*self.player_number))*120)
        self.rect.centerx=370-((math.sin((math.pi*2)/Town.players*self.player_number))*180)
        


class Hero(pygame.sprite.Sprite):
    heroes=[]
    FavorForAlly=45
    def __init__(self, name, hero_class, img_dirr, helvet):
        '''
        H.__init__(str, str, str, Font)
        Initializes H with a given name, the name of H's class, a reference to a
        directory, and a font.
        '''
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.hero_class=hero_class
        self.hero_class_formated=hero_class[0].upper()+hero_class[1:]
        if hero_class=="pegasus_knight":
            self.hero_class_formated="Pegasus Knight"
        self.town_favors=[]
        self.location="middle"
        self.destination=None
        self.c_destination=None
        self.moving=False
        self.moving_direction=None
        self.steps=0
        Hero.heroes+=[self]
        
        for i in range(0,Town.players):
            self.town_favors+=[10]
        if hero_class=="warrior":
            os.chdir(img_dirr+"/heroes/warrior")
        if hero_class=="mage":
            os.chdir(img_dirr+"/heroes/mage")
        if hero_class=="rogue":
            os.chdir(img_dirr+"/heroes/rogue")
        if hero_class=="priest":
            os.chdir(img_dirr+"/heroes/priest")
        if hero_class=="knight":
            os.chdir(img_dirr+"/heroes/knight")
        if hero_class=="archer":
            os.chdir(img_dirr+"/heroes/archer")
        if hero_class=="pegasus_knight":
            os.chdir(img_dirr+"/heroes/pegasus_knight")
            
        self.hero_dirr=os.getcwd()
        self.idle_frames=[]
        self.up_frames=[]
        self.down_frames=[]
        self.left_frames=[]
        self.right_frames=[]
        self.diag_t_l_frames=[]
        self.diag_t_r_frames=[]
        self.diag_b_l_frames=[]
        self.diag_b_r_frames=[]
        for i in range(1,5):
            temp_frame=pygame.image.load("frame_idle_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,0,255))
            self.idle_frames+=[temp_frame]
            temp_frame=pygame.image.load("frame_up_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,0,255))
            self.up_frames+=[temp_frame]
            temp_frame=pygame.image.load("frame_down_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,0,255))
            self.down_frames+=[temp_frame]
            temp_frame=pygame.image.load("frame_left_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,0,255))
            self.left_frames+=[temp_frame]
            temp_frame=pygame.image.load("frame_right_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,0,255))
            self.right_frames+=[temp_frame]
            temp_frame=pygame.image.load("frame_diag_t_l_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,0,255))
            self.diag_t_l_frames+=[temp_frame]
            temp_frame=pygame.image.load("frame_diag_t_r_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,0,255))
            self.diag_t_r_frames+=[temp_frame]
            temp_frame=pygame.image.load("frame_diag_b_l_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,0,255))
            self.diag_b_l_frames+=[temp_frame]
            temp_frame=pygame.image.load("frame_diag_b_r_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,0,255))
            self.diag_b_r_frames+=[temp_frame]
            
        #add frames so it loops
        if self.hero_class!="warrior" and self.hero_class!="pegasus_knight":
            #The Warrior's and Pegasus Knight's idle frames will loop naturally
            self.idle_frames=self.idle_frames+[self.idle_frames[2], self.idle_frames[1]]
        self.up_frames=self.up_frames+[self.up_frames[2], self.up_frames[1]]
        self.down_frames=self.down_frames+[self.down_frames[2], self.down_frames[1]]
        self.left_frames=self.left_frames+[self.left_frames[2], self.left_frames[1]]
        self.right_frames=self.right_frames+[self.right_frames[2], self.right_frames[1]]
        self.diag_t_l_frames=self.diag_t_l_frames+[self.diag_t_l_frames[2], self.diag_t_l_frames[1]]
        self.diag_t_r_frames=self.diag_t_r_frames+[self.diag_t_r_frames[2], self.diag_t_r_frames[1]]
        self.diag_b_l_frames=self.diag_b_l_frames+[self.diag_b_l_frames[2], self.diag_b_l_frames[1]]
        self.diag_b_r_frames=self.diag_b_r_frames+[self.diag_b_r_frames[2], self.diag_b_r_frames[1]]
        
        self.image=self.idle_frames[0]
        self.rect=self.image.get_rect()
        self.rect.centery=220-((math.cos((math.pi*2)/7*(8-len(Hero.heroes))))*30)
        self.rect.centerx=370-((math.sin((math.pi*2)/7*(8-len(Hero.heroes))))*30)
        self.centery_float=self.rect.centery
        self.centerx_float=self.rect.centerx
        self.bottom_start=self.rect.bottom
        self.centerx_start=self.rect.centerx
        
        self.frame_num=0
        self.frame_pause=0
        
        event_intro_icon=pygame.image.load("event_intro_icon.bmp").convert()
        event_success_icon=pygame.image.load("event_success_icon.bmp").convert()
        event_failure_icon=pygame.image.load("event_failure_icon.bmp").convert()
        gain_passive_ability_icon=pygame.image.load("gain_passive_ability_icon.bmp").convert()
        
        
        
        
        os.chdir(img_dirr+"/menu")
        message_box=pygame.image.load("message_box.bmp").convert()
        message_box.set_colorkey((255,0,255))
        message_title_font=pygame.font.Font(helvet, 15)
        message_text_font=pygame.font.Font(helvet, 12)
        
        #This part of the code creates the message boxes that are used to 
        #comunicate with the player that they a hero event has activated
        self.event_intro_box=pygame.transform.scale(message_box, (280,180))
        event_intro_icon=pygame.transform.scale(event_intro_icon, (100,75))
        event_title_text=message_title_font.render("Event:", True, (255,255,255))
        self.event_intro_box.blit(event_title_text, (115,10))
        surface_for_text=pygame.Surface((186,1)).convert()
        surface_for_text.fill((0,0,0))
        if self.hero_class=="warrior":
            info_text="Oh no, Bandits have appeared on the outskirts of your town! Get the Warrior over here within 10 turns to deal with them, or you will lose 50% of your population!"
        if self.hero_class=="mage":
            info_text="Oh no, a Curse has been placed on your town! Get the Mage over here within 10 turns to deal with it, or you will lose 50% of your population!"
        if self.hero_class=="rogue":
            info_text="Oh no, Robbers have been running rampant in your town! Get the Rogue over here within 10 turns to deal with them, or you will lose 50% of your population!"
        if self.hero_class=="priest":
            info_text="Oh no, Satan! This is bad! Get the Priest over here within 10 turns, or you will lose 50% of your population!"
        if self.hero_class=="knight":
            info_text="Reports have been raised that a craven that was transporting food to your town might be attacked! Get the Knight over here within 10 turns, so he can protect it, or you will lose 50% of your population!"
        if self.hero_class=="archer":
            info_text="You have received information that your town might soon be attacked! Get the Archer over here within 10 turns so he can train your forces, or you will lose 50% of your population!"
        if self.hero_class=="pegasus_knight":
            info_text="Barbarians have been sighted nearby, but where are they coming from? Get the Pegasus Knight over here within 10 turns so she can scout around and find them, otherwise you will lose 50% of your population!"
        
        text_box=functions.fit_text_to_box(info_text, surface_for_text, message_text_font)
        self.event_intro_box=pygame.transform.scale(self.event_intro_box, (280,text_box.get_size()[1]+85+30))
        self.event_intro_box.blit(text_box, (14, 85))
        
        
        if self.hero_class!="pegasus_knight":
            event_hero_class_text=message_title_font.render("{}".format(self.hero_class_formated), True, (255,255,255))
            self.event_intro_box.blit(event_hero_class_text, (115,25))
        if self.hero_class=="pegasus_knight":
            event_hero_class_text_1=message_title_font.render("Pegasus".format(self.hero_class_formated), True, (255,255,255))
            event_hero_class_text_2=message_title_font.render("Knight".format(self.hero_class_formated), True, (255,255,255))
            self.event_intro_box.blit(event_hero_class_text_1, (115,25))
            self.event_intro_box.blit(event_hero_class_text_2, (115,40))
        self.event_intro_box.blit(event_intro_icon, (10,5))
            
        #This part of the code creates the message boxes that are used to 
        #comunicate with the player that the have failed in a hero event    
        self.event_failure_box=pygame.transform.scale(message_box, (280,180))
        event_failure_icon=pygame.transform.scale(event_failure_icon, (100,75))            
        event_failure_text=message_title_font.render("Failure", True, (255,255,255)) 
        self.event_failure_box.blit(event_title_text, (115,10)) 
        surface_for_text=pygame.Surface((186,1)).convert()
        surface_for_text.fill((0,0,0))          
        if self.hero_class=="warrior":
            info_text="Time's up! The Warrior hasn't come by! The Bandits have attacked! 50% of your population is now dead!"
        if self.hero_class=="mage":
            info_text="Time's up! The Mage hasn't come by! The Curse has taken effect! 50% of your population is now dead!"
        if self.hero_class=="rogue":
            info_text="Time's up! The Rogue hasn't come by! The Robbers have stolen everyone's stuff! 50% of your population left!"
        if self.hero_class=="priest":
            info_text="Time's up! The Priest hasn't come by! Satan has attacked! 50% of your population is now dead!"
        if self.hero_class=="knight":
            info_text="Time's up! The Knight hasn't come by! The Caravan with food has been attacked! 50% of your population is now dead!"
        if self.hero_class=="archer":
            info_text="Time's up! The Archer hasn't come by! You have been attacked, and were unable to defend yourself! 50% of your population is now dead!"
        if self.hero_class=="pegasus_knight":
            info_text="Time's up! The Pegasus Knight hasn't come by! The Barbarians have attacked! 50% of your population is now dead!"
            
        text_box=functions.fit_text_to_box(info_text, surface_for_text, message_text_font)
        self.event_failure_box=pygame.transform.scale(self.event_failure_box, (280,text_box.get_size()[1]+85+30))
        self.event_failure_box.blit(text_box, (14, 85))
                
        if self.hero_class!="pegasus_knight":
            self.event_failure_box.blit(event_hero_class_text, (115,25))
            self.event_failure_box.blit(event_failure_text, (115, 40))
        if self.hero_class=="pegasus_knight":
            self.event_failure_box.blit(event_hero_class_text_1, (115,25))
            self.event_failure_box.blit(event_hero_class_text_2, (115,40))
            self.event_failure_box.blit(event_failure_text, (115, 55))
        self.event_failure_box.blit(event_failure_icon, (10,5))
        
        #This part of the code creates the message boxes that are used to 
        #comunicate with the player that the have sucseeded in a hero event           
        self.event_success_box=pygame.transform.scale(message_box, (280,180))
        event_success_icon=pygame.transform.scale(event_success_icon, (100,75))         
        event_success_text=message_title_font.render("Success", True, (255,255,255))  
        self.event_success_box.blit(event_title_text, (115,10))  
        surface_for_text=pygame.Surface((186,1)).convert()
        surface_for_text.fill((0,0,0))        
        if self.hero_class=="warrior":
            info_text="Yay! The Warrior has come by! You are safe from the Bandits!"
        if self.hero_class=="mage":
            info_text="Yay! The Mage has come by! You are safe from the Curse!"
        if self.hero_class=="rogue":
            info_text="Yay! The Rogue has come by! You are safe from the Robbers!"
        if self.hero_class=="priest":
            info_text="Yay! The Priest has come by! You are safe from Satan!"
        if self.hero_class=="knight":
            info_text="Yay! The Knight has come by! The Caravan is now safe!"
        if self.hero_class=="archer":
            info_text="Yay! The Archer has come by! Your Defences are now secure!"
        if self.hero_class=="pegasus_knight":
            info_text="Yay! The Pegasus Knight has come by! You are safe from the Barbarians!"
            
            
        text_box=functions.fit_text_to_box(info_text, surface_for_text, message_text_font)
        self.event_success_box=pygame.transform.scale(self.event_success_box, (280,text_box.get_size()[1]+85+30))
        self.event_success_box.blit(text_box, (14, 85))
            
        if self.hero_class!="pegasus_knight":
            self.event_success_box.blit(event_hero_class_text, (115,25))
            self.event_success_box.blit(event_success_text, (115, 40))
        if self.hero_class=="pegasus_knight":
            self.event_success_box.blit(event_hero_class_text_1, (115,25))
            self.event_success_box.blit(event_hero_class_text_2, (115,40))
            self.event_success_box.blit(event_success_text, (115, 55))
        self.event_success_box.blit(event_success_icon, (10,5))
        
        
        #This part of the code creates the message boxes that are used to 
        #comunicate with the player that the have gained a passive hero ability 
        self.gain_passive_ability_box=pygame.transform.scale(message_box, (280,180))
        gain_passive_ability_icon=pygame.transform.scale(gain_passive_ability_icon, (100,75))
        gain_passive_ability_text=message_title_font.render("A New Ally!", True, (255,255,255))
        self.gain_passive_ability_box.blit(gain_passive_ability_text, (115,10))
        surface_for_text=pygame.Surface((186,1)).convert()
        surface_for_text.fill((0,0,0))
        if self.hero_class=="warrior":
            info_text="You have earned Eirika's respect, and as such, she has buckled down on unruly workers in your town to increase production."
        if self.hero_class=="mage":
            info_text="You have earned Lute's respect, and as such, she has used some minor duplication magic to increase you treasury."
        if self.hero_class=="rogue":
            info_text="You wake up to the sounds of cheering, and see Colm handing out jewels to your citizens. He later says you have gained his respect, and he wish to share some of his luxurey resourses with your people."
        if self.hero_class=="priest":
            info_text="You have earned Moulder's respect, and as such, he has blessed your soil to increase its output of crops."
        if self.hero_class=="knight":
            info_text="You have earned Seth's respect, and as such, he has spoken quite highly of you, increasing your favor."
        if self.hero_class=="archer":
            info_text="You have earned Innes's respect, and as such, he has taken it upon himself to improve your defences."
        if self.hero_class=="pegasus_knight":
            info_text="You have earned Venessa's respect, and as such, she has shared her wisdom with you, and made your town slightly better at everything."
            
        text_box=functions.fit_text_to_box(info_text, surface_for_text, message_text_font)
        self.gain_passive_ability_box=pygame.transform.scale(self.gain_passive_ability_box, (280,text_box.get_size()[1]+85+30))
        self.gain_passive_ability_box.blit(text_box, (14, 85))
        
        self.gain_passive_ability_box.blit(gain_passive_ability_icon, (10,5))
        
        
        #This part of the code creates the message boxes that are used to 
        #comunicate with the player that the have lost a passive hero ability 
        os.chdir(img_dirr+"/heroes")
        lose_passive_ability_icon=pygame.image.load("lose_passive_ability_icon.bmp").convert()
        self.lose_passive_ability_box=pygame.transform.scale(message_box, (280,180))
        lose_passive_ability_icon=pygame.transform.scale(lose_passive_ability_icon, (100,75))
        lose_passive_ability_text_1=message_title_font.render("An Ally has", True, (255,255,255))
        lose_passive_ability_text_2=message_title_font.render("been lost", True, (255,255,255))
        self.lose_passive_ability_box.blit(lose_passive_ability_text_1, (115,10))
        self.lose_passive_ability_box.blit(lose_passive_ability_text_2, (115,35))
        surface_for_text=pygame.Surface((186,1)).convert()
        surface_for_text.fill((0,0,0))
        if self.hero_class=="warrior":
            info_text="You have lost Eirika's respect, and as such, she will no longer be helping your production speed."
        if self.hero_class=="mage":
            info_text="You have lost Lute's respect, and as such, she will no longer be helping your gold output."
        if self.hero_class=="rogue":
            info_text="You have lost Colm's respect, and as such, he will no longer be helping your happiness."
        if self.hero_class=="priest":
            info_text="You have lost Moulder's respect, and as such, he will no longer be helping your crop yeild."
        if self.hero_class=="knight":
            info_text="You have lost Seth's respect, and as such, he will no longer be helping your reputation."
        if self.hero_class=="archer":
            info_text="You have lost Innes's respect, and as such, he will no longer be helping your defences."
        if self.hero_class=="pegasus_knight":
            info_text="You have lost Venessa's respect, and as such, she will no longer be giving you advice."
            
            
        text_box=functions.fit_text_to_box(info_text, surface_for_text, message_text_font)
        self.lose_passive_ability_box=pygame.transform.scale(self.lose_passive_ability_box, (280,text_box.get_size()[1]+85+30))
        self.lose_passive_ability_box.blit(text_box, (14, 85))
        
        self.lose_passive_ability_box.blit(lose_passive_ability_icon, (10,5))
        
        
        
        os.chdir(img_dirr+"/menu")
        self.personal_info_screen=pygame.image.load("hero_info_screen.bmp").convert()
        button_font=pygame.font.Font(helvet, 14)
        
        exit_info_screen_text=button_font.render("Close", True, (255,255,251))
        self.exit_info_screen_button=pygame.image.load("button.bmp").convert()
        self.exit_info_screen_button=pygame.transform.scale(self.exit_info_screen_button, (100,25))
        self.exit_info_screen_button.set_colorkey(self.exit_info_screen_button.get_at((0,0)))
        self.exit_info_screen_button_rect=self.exit_info_screen_button.get_rect()
        self.exit_info_screen_button_rect.top=200
        self.exit_info_screen_button_rect.right=200
        self.exit_info_screen_button.blit(exit_info_screen_text, (5, 5))
        
        
        

        
    def Move(self, towns):
        '''
        H.Move(list) --> None
        This method is used to determine where the given hero will be moving
        towards, and staying at for the next set of turns.
        '''
        self.frame_pause=4
        self.steps=0
        towns_to_use=[]
        favor_to_use=[]
        total_favor=0
        for i in towns:
            
            
            if i.happiness>-10:
                if self.hero_class=="warrior":
                    if i.eliminated==False and i.warrior_favor>0:
                        towns_to_use+=[i]
                        favor_to_use+=[i.warrior_favor]
                        total_favor+=i.warrior_favor
                if self.hero_class=="mage":
                    if i.eliminated==False and i.mage_favor>0:
                        towns_to_use+=[i]
                        favor_to_use+=[i.mage_favor]
                        total_favor+=i.mage_favor
                if self.hero_class=="rogue":
                    if i.eliminated==False and i.rogue_favor>0:
                        towns_to_use+=[i]
                        favor_to_use+=[i.rogue_favor]
                        total_favor+=i.rogue_favor
                if self.hero_class=="priest":
                    if i.eliminated==False and i.priest_favor>0:
                        towns_to_use+=[i]
                        favor_to_use+=[i.priest_favor]
                        total_favor+=i.priest_favor
                if self.hero_class=="knight":
                    if i.eliminated==False and i.knight_favor>0:
                        towns_to_use+=[i]
                        favor_to_use+=[i.knight_favor]
                        total_favor+=i.knight_favor
                if self.hero_class=="archer":
                    if i.eliminated==False and i.archer_favor>0:
                        towns_to_use+=[i]
                        favor_to_use+=[i.archer_favor]
                        total_favor+=i.archer_favor
                if self.hero_class=="pegasus_knight":
                    if i.eliminated==False and i.pegasus_knight_favor>0:
                        towns_to_use+=[i]
                        favor_to_use+=[i.pegasus_knight_favor]
                        total_favor+=i.pegasus_knight_favor
                    
        if total_favor>0 or len(towns_to_use)==0:
            if len(towns_to_use)!=0:
                destination_num=random.randint(1,total_favor)
                favor_counter=0
                destination_picked=False
                for i in range(0,len(towns_to_use)):
                    favor_counter+=favor_to_use[i]
                    if destination_num<=favor_counter and destination_picked==False:
                        self.destination=towns_to_use[i]
                        destination_picked=True
            if len(towns_to_use)==0:
                self.destination="middle"
                self.c_destination="middle"
            if self.destination!=self.location:
                self.moving=True
                if self.location=="middle":
                    self.c_destination=self.destination
                    if abs(self.c_destination.rect.centerx-370)*2<abs(self.c_destination.rect.centery-220):
                        if self.c_destination.rect.centery>220:
                            self.moving_direction="down"
                        if self.c_destination.rect.centery<220:
                            self.moving_direction="up"
                    elif abs(self.c_destination.rect.centerx-370)>abs(self.c_destination.rect.centery-220)*2:
                        if self.c_destination.rect.centerx>370:
                            self.moving_direction="right"
                        if self.c_destination.rect.centerx<370:
                            self.moving_direction="left"
                    else:
                        if self.c_destination.rect.centerx>370 and self.c_destination.rect.centery<220:
                            self.moving_direction="top_right"
                        if self.c_destination.rect.centerx>370 and self.c_destination.rect.centery>220:
                            self.moving_direction="bottom_right"
                        if self.c_destination.rect.centerx<370 and self.c_destination.rect.centery<220:
                            self.moving_direction="top_left"
                        if self.c_destination.rect.centerx<370 and self.c_destination.rect.centery>220:
                            self.moving_direction="bottom_left"
                            
                if self.location!="middle":
                    self.c_destination="middle"
                    if abs(self.location.rect.centerx-370)*2<abs(self.location.rect.centery-220):
                        if self.location.rect.centery>220:
                            self.moving_direction="up"
                        if self.location.rect.centery<220:
                            self.moving_direction="down"
                    elif abs(self.location.rect.centerx-370)>abs(self.location.rect.centery-220)*2:
                        if self.location.rect.centerx>370:
                            self.moving_direction="left"
                        if self.location.rect.centerx<370:
                            self.moving_direction="right"
                    else:
                        if self.location.rect.centerx>370 and self.location.rect.centery<220:
                            self.moving_direction="bottom_left"
                        if self.location.rect.centerx>370 and self.location.rect.centery>220:
                            self.moving_direction="top_left"
                        if self.location.rect.centerx<370 and self.location.rect.centery<220:
                            self.moving_direction="bottom_right"
                        if self.location.rect.centerx<370 and self.location.rect.centery>220:
                            self.moving_direction="top_right"
                            
                            
    def info_menu_open(self, background):
        '''
        H.info_menu_open(pygame.Surface) --> None
        A method used to help construct the Hero Info panel, by placing place H 
        onto the given pygame.Surface
        '''
        background.blit(self.personal_info_screen, (20,20))
        background.blit(self.give_gift_button, self.give_gift_button_rect)
        background.blit(self.exit_info_screen_button, self.exit_info_screen_button_rect)
        
        return
                         
                         
    def update(self):
        '''
        H.update()
        This method is used to move the hero in question around onscreen, as
        well as change which sprite they are using.
        '''
        self.frame_pause+=1
        if self.moving==True:
            self.steps+=1
            if self.c_destination=="middle" and self.location=="middle" and self.destination=="middle":
                self.steps=50
            if self.steps!=50:
                if self.moving_direction=="up":
                    frames_to_use=self.up_frames
                if self.moving_direction=="down":
                    frames_to_use=self.down_frames
                if self.moving_direction=="left":
                    frames_to_use=self.left_frames
                if self.moving_direction=="right":
                    frames_to_use=self.right_frames
                    
                if self.moving_direction=="bottom_left":
                    frames_to_use=self.diag_b_l_frames
                if self.moving_direction=="bottom_right":
                    frames_to_use=self.diag_b_r_frames
                if self.moving_direction=="top_left":
                    frames_to_use=self.diag_t_l_frames
                if self.moving_direction=="top_right":
                    frames_to_use=self.diag_t_r_frames
                    
                if self.c_destination!="middle":
                    self.centerx_float+=(self.c_destination.rect.centerx-370)/50
                    self.centery_float+=(self.c_destination.rect.centery-220)/50
                    self.rect.centerx=self.centerx_float
                    self.rect.centery=self.centery_float
                    
                if self.c_destination=="middle":
                    self.centerx_float-=(self.location.rect.centerx-370)/50
                    self.centery_float-=(self.location.rect.centery-220)/50
                    self.rect.centerx=self.centerx_float
                    self.rect.centery=self.centery_float
                
            if self.steps==50:
                self.moving=False
                if self.c_destination!="middle":
                    self.location=self.destination
                if self.c_destination=="middle":
                    self.c_destination=self.location
                    self.location="middle"
                    
        if self.moving==False:
            frames_to_use=self.idle_frames
            
        if self.frame_pause==5:
            self.frame_pause=0
            self.frame_num+=1
            if self.frame_num>=len(frames_to_use):
                self.frame_num=0
            self.image=frames_to_use[self.frame_num]
            
            
    def follow_dragon(self, dragon_x, dragon_y, frames_to_use):
        '''
        H.follow_dragon(int, int, list) --> None
        This method is used to move the hero so that they are following the 
        dragon.
        '''
        self.frame_pause+=1
        self.rect.bottom=(dragon_y-220)+self.bottom_start
        self.rect.centerx=(dragon_x-370)+self.centerx_start
        if self.frame_pause==5:
            self.frame_pause=0
            self.frame_num+=1
            if self.frame_num>=len(frames_to_use):
                self.frame_num=0
            self.image=frames_to_use[self.frame_num]
        
        
        
class Dragon(pygame.sprite.Sprite):
    def __init__(self, img_dirr):
        '''
        D.__init__(str)
        Initializes D with a given reference to a directory.
        '''
        pygame.sprite.Sprite.__init__(self)
        self.on_screen=False
        self.attacking=None
        self.attacks=0
        self.to_attack_patern=[]
        self.attack_stop_point=0
        self.current_attack_point=0
        os.chdir(img_dirr+"/dragon")
        self.image=pygame.image.load("dragon_idle_frame.bmp").convert()
        self.image.set_colorkey((255,255,255))
        self.rect=self.image.get_rect()
        self.rect.centerx=-30
        self.rect.centery=564
        self.centerx_float=self.rect.centerx
        self.centery_float=self.rect.centery
        self.fall_back_reference_x=370
        self.fall_back_reference_y=164
        self.leaving_reference_x=0
        self.leaving_reference_y=0
        self.recover_frame_counter=0
        
        self.sprite_phase="intro"
        self.sprite_counter=0
        self.frame_pause=0
        self.intro_frames=[]
        for i in range(1,3):
            temp_frame=pygame.image.load("dragon_intro_frame_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,255,255))
            self.intro_frames+=[temp_frame]
        self.intro_frames+=[temp_frame]
        self.intro_frames+=[self.intro_frames[0]]
        
        self.take_off_frames=[]
        for i in range(1,5):
            temp_frame=pygame.image.load("dragon_take_off_frame_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,255,255))
            self.take_off_frames+=[temp_frame]
            
        self.flying_frames=[]
        for i in range(1,5):
            temp_frame=pygame.image.load("dragon_flying_frame_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,255,255))
            self.flying_frames+=[temp_frame]
        self.flying_frames+=[self.flying_frames[2]]
        self.flying_frames+=[self.flying_frames[1]]
        
        self.distance_fell=0
        self.falling_back_frames=[]
        for i in range(1,4):
            temp_frame=pygame.image.load("dragon_falling_back_frame_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,255,255))
            self.falling_back_frames+=[temp_frame]
        
        self.recover_frames=self.falling_back_frames[::-1]
            
        self.landing_frames=[]
        for i in range(1,5):
            temp_frame=pygame.image.load("dragon_landing_frame_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,255,255))
            self.landing_frames+=[temp_frame]
            
        self.attacking_frames=[]
        for i in range(1,10):
            temp_frame=pygame.image.load("dragon_attack_frame_{}.bmp".format(i)).convert()
            temp_frame.set_colorkey((255,255,255))
            self.attacking_frames+=[temp_frame]    
        self.intro_frames=self.landing_frames+self.intro_frames
        
        
    def eliminate_towns(self, towns):
        '''
        D.eliminate_towns(list) --> None
        This method is used before the dragon spawns in, and is used to figure
        out both the dragon's attack pattern, and who the dragon will be
        eliminating.
        '''
        
        print("--------")
        
        self.on_screen=True
        towns_to_use=[]
        favors_to_use=[]
        for i in towns:
            if i.eliminated==False:
                towns_to_use+=[i]            
                favors_to_use+=[i.total_favor]
                
                print("{}: {}".format(i.town_name, i.total_favor))
            if i.eliminated==True:
                print("{}: Eliminated".format(i.town_name, i.total_favor))
                
        
        to_attack=random.randrange(0,len(towns_to_use))
        self.to_attack_patern=[towns_to_use[to_attack]]
        while towns_to_use[to_attack].total_favor!=min(favors_to_use):
            to_attack=random.randrange(0,len(towns_to_use))
            if towns_to_use[to_attack] not in self.to_attack_patern:
                self.to_attack_patern+=[towns_to_use[to_attack]]
            
        self.attacking=self.to_attack_patern[self.attacks]  
        if self.to_attack_patern[-1].total_favor<=0:
            self.attack_stop_point=((self.to_attack_patern[-1].total_favor+abs(self.to_attack_patern[-1].total_favor)+1)/(self.attacking.total_favor+abs(self.to_attack_patern[-1].total_favor)+1))*50
        if self.to_attack_patern[-1].total_favor>0:
            self.attack_stop_point=(self.to_attack_patern[-1].total_favor/self.attacking.total_favor)*50
            
        
        
    def update(self, towns):
        '''
        D.update(list) --> None
        This method is used to move the dragon around onscreen, as well as
        change the dragon's sprite. This method is also used to change which
        phase the dragon is currently on, meaning if it is being introduced,
        flying, taking off, landing, falling backwards, or attacking.
        '''
        self.frame_pause+=1
        
        if self.rect.centery!=164 and self.rect.centerx!=370 and self.sprite_phase=="intro":
            self.centerx_float+=(370--30)/100
            self.centery_float+=(164-564)/100
            self.rect.centerx=self.centerx_float
            self.rect.centery=self.centery_float
            if self.rect.centery==164 and self.rect.centerx==370:
                self.sprite_counter=0
        
        if self.current_attack_point!=int(self.attack_stop_point) and self.sprite_phase=="moving":
            self.current_attack_point+=1
            self.centerx_float+=(self.attacking.rect.centerx-370)/50
            self.centery_float+=(self.attacking.rect.centery-220)/50
            self.rect.centerx=self.centerx_float
            self.rect.centery=self.centery_float
            
        if self.sprite_phase=="leaving":
            if self.sprite_counter==len(self.take_off_frames) or self.rect.centerx!=self.leaving_reference_x:
                self.centerx_float+=(770-self.leaving_reference_x)/200
                self.centery_float+=(564-self.leaving_reference_y)/200
                self.rect.centerx=self.centerx_float
                self.rect.centery=self.centery_float
                if self.rect.centery==self.leaving_reference_y and self.rect.centerx==self.leaving_reference_x:
                    self.sprite_counter=0
            
        if self.sprite_phase=="intro":
            if self.frame_pause==5:
                self.frame_pause=0
                if self.rect.centery==164 and self.rect.centerx==370:
                    self.image=self.intro_frames[self.sprite_counter]
                    self.sprite_counter+=1
                    if self.sprite_counter==len(self.intro_frames):
                        self.sprite_phase="taking_off"
                        self.sprite_counter=0
                if self.rect.centery!=164 and self.rect.centerx!=370:
                    self.image=self.flying_frames[self.sprite_counter]
                    self.sprite_counter+=1
                    if self.sprite_counter==len(self.flying_frames):
                        self.sprite_counter=0
                    
        if self.sprite_phase=="taking_off":
            if self.frame_pause==5:
                self.frame_pause=0
                self.image=self.take_off_frames[self.sprite_counter]
                self.sprite_counter+=1
                if self.sprite_counter==len(self.take_off_frames):
                    self.sprite_phase="moving"
                    self.sprite_counter=0
            
        if self.sprite_phase=="moving":
            Hero.heroes[0].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[0].down_frames)
            Hero.heroes[1].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[1].diag_b_l_frames)
            Hero.heroes[2].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[2].left_frames)
            Hero.heroes[3].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[3].diag_t_l_frames)
            Hero.heroes[4].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[4].diag_t_r_frames)
            Hero.heroes[5].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[5].right_frames)
            Hero.heroes[6].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[6].diag_b_r_frames)
            if self.frame_pause==5:
                self.frame_pause=0
                self.image=self.flying_frames[self.sprite_counter]
                self.sprite_counter+=1
                if self.sprite_counter==len(self.flying_frames):
                    self.sprite_counter=0
            if self.current_attack_point==int(self.attack_stop_point):
                self.sprite_counter=0
                if self.attack_stop_point==50:
                    self.frame_pause=0
                    self.attacking.eliminated=True
                    self.attacking.image=self.attacking.town_distroyed
                    self.attack_stop_point=0
                    self.current_attack_point=0
                    self.sprite_phase="landing"
                    for i in Hero.heroes:
                        i.location=self.attacking
                        i.centerx_float=i.rect.centerx
                        i.centery_float=i.rect.centery
                        i.Move(towns)
                elif self.attack_stop_point!=50:
                    self.sprite_counter=0
                    self.frame_pause=0
                    self.distance_fell=0
                    self.fall_back_reference_x=self.rect.centerx
                    self.fall_back_reference_y=self.rect.centery
                    self.sprite_phase="falling_back"
                    
        if self.sprite_phase=="falling_back":
            Hero.heroes[0].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[0].down_frames)
            Hero.heroes[1].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[1].diag_b_l_frames)
            Hero.heroes[2].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[2].left_frames)
            Hero.heroes[3].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[3].diag_t_l_frames)
            Hero.heroes[4].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[4].diag_t_r_frames)
            Hero.heroes[5].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[5].right_frames)
            Hero.heroes[6].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[6].diag_b_r_frames)
            if self.frame_pause==5:
                self.frame_pause=0
                self.image=self.falling_back_frames[self.sprite_counter]
                self.sprite_counter+=1
            self.distance_fell+=1
            if self.distance_fell!=16:
                self.centerx_float+=(370-self.fall_back_reference_x)/15
                self.centery_float+=(164-self.fall_back_reference_y)/15
                self.rect.centerx=self.centerx_float
                self.rect.centery=self.centery_float
            if self.distance_fell==15:
                self.sprite_counter=0
                self.sprite_phase="recovering"
                
        if self.sprite_phase=="recovering":
            for i in range(0,7):
                Hero.heroes[i].follow_dragon(self.rect.centerx, self.rect.bottom, Hero.heroes[i].idle_frames)
            if self.frame_pause==5:
                self.frame_pause=0
                self.image=self.recover_frames[self.sprite_counter]
                self.sprite_counter+=1
                if self.sprite_counter==len(self.recover_frames):
                    self.sprite_counter=0
                    self.rect.centery=164
                    self.rect.centerx=370
                    self.centerx_float=self.rect.centerx
                    self.centery_float=self.rect.centery
                    self.recover_frame_counter
                    self.attacks+=1
                    self.current_attack_point=0
                    self.attacking=self.to_attack_patern[self.attacks]  
                    if self.to_attack_patern[-1].total_favor<=0:
                        self.attack_stop_point=((self.to_attack_patern[-1].total_favor+abs(self.to_attack_patern[-1].total_favor)+1)/(self.attacking.total_favor+abs(self.to_attack_patern[-1].total_favor)+1))*50
                    if self.to_attack_patern[-1].total_favor>0:
                        self.attack_stop_point=(self.to_attack_patern[-1].total_favor/self.attacking.total_favor)*50
                    self.sprite_phase="taking_off"
                
        if self.sprite_phase=="landing":
            if self.frame_pause==5:
                self.frame_pause=0
                self.image=self.landing_frames[self.sprite_counter]
                self.sprite_counter+=1
                if self.sprite_counter==len(self.landing_frames):
                    self.sprite_phase="attacking"
                    self.sprite_counter=0       
                
        if self.sprite_phase=="attacking":
            if self.frame_pause==5:
                self.frame_pause=0
                self.image=self.attacking_frames[self.sprite_counter]
                self.sprite_counter+=1
                if self.sprite_counter==len(self.attacking_frames):
                    self.sprite_counter=0   
                    self.leaving_reference_x=self.rect.centerx
                    self.leaving_reference_y=self.rect.centery                
                    self.sprite_phase="leaving"
                    
        if self.sprite_phase=="leaving":
            if self.frame_pause==5:
                self.frame_pause=0
                if self.rect.centery==self.leaving_reference_y and self.rect.centerx==self.leaving_reference_x:
                    self.image=self.take_off_frames[self.sprite_counter]
                    self.sprite_counter+=1
                if self.rect.centery!=self.leaving_reference_y and self.rect.centerx!=self.leaving_reference_x:
                    self.frame_pause=0
                    self.image=self.flying_frames[self.sprite_counter]
                    self.sprite_counter+=1 
                    if self.sprite_counter==len(self.flying_frames):
                        self.sprite_counter=0   
                if (self.rect.centerx-(self.image.get_size()[0]/2))>560 or (self.rect.centery-(self.image.get_size()[1]/2))>480:
                    self.sprite_phase="intro"
                    self.on_screen=False
                    self.rect.centery=564
                    self.rect.centerx=-30
                    self.centerx_float=self.rect.centerx
                    self.centery_float=self.rect.centery
                    self.attacking=None
                    self.attacks=0
                    self.to_attack_patern=[]
        
            
            
class Unique_Building(object):
    uniques_built=0
    uniques=[]
    def __init__(self, name, img_dirr, building_icon, helvet):
        '''
        U.__init__(str, str, surface, Font)
        Initializes U with a given name, reference to a directory, surface, and 
        font.
        '''
        self.name=name
        self.built=False
        
        os.chdir(img_dirr+"/menu")  
        self.built_message=pygame.image.load("message_box.bmp").convert()
        self.built_message=pygame.transform.scale(self.built_message, (280, 180))
        self.built_message.set_colorkey((255,0,255))
        built_message_title_font=pygame.font.Font(helvet, 15)
        built_message_text_font=pygame.font.Font(helvet, 12)
        
        self.built_message.blit(building_icon, (10, 5))
        name_formated=name[0].upper()+name[1:]
        while "_" in name_formated:
            name_formated=name_formated[:name_formated.find("_")]+" "+name_formated[name_formated.find("_")+1].upper()+name_formated[name_formated.find("_")+2:]
            
        name_text=built_message_title_font.render(name_formated, True, (255,255,255))        
        built_text=built_message_title_font.render("Has Been Built!", True, (255,255,255))      
        
        self.built_message.blit(name_text, (90, 10))
        self.built_message.blit(built_text, (90, 25))
        
        info_text="The {} has been constructed by another player! You are now no longer able to build this unique building.".format(name_formated)
        
        surface_for_text=pygame.Surface((186,1)).convert()
        surface_for_text.fill((0,0,0))
        
        text_box=functions.fit_text_to_box(info_text, surface_for_text, built_message_text_font)
        self.built_message=pygame.transform.scale(self.built_message, (280,text_box.get_size()[1]+85+30))
        self.built_message.blit(text_box, (14, 90))
        
        Unique_Building.uniques+=[self]