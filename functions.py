import pygame
from pygame.locals import *
pygame.init()

import random

import classes

#This code contains all of the functions that are used by the game


def check_building_progress(current_player, towns):
    '''
    check_building_progress(Town, list) --> None
    The purpose of this function is to check how much progress the given Town 
    has made towards whatever it is they are currently building. This function 
    is to be activated at the beginning of each turn for each player. This 
    function begins by checking the production stat of the current player, what 
    the current play is constructing, and finally, how much progress the current
    player has made towards the thing they are building. Once it has this 
    information, it adds up the current players' current production to the total
    amount of production they have contributed towards the building. If the user
    has completed the building, this function will give the player the 
    appropriate reward, or rewards for its completion.
    '''
    
    if current_player.constructing!=None:
        
        
        #This part of the code is for if the player is building a production 
        #building
        if current_player.constructing.building_type=="production building":
            if current_player.production_building_level==0:
                current_player.production_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.production_building_progress>=1:
                    current_player.level_1_buildings+=1
                    current_player.production_building_progress=0
                    current_player.production_building_level+=1
                    current_player.production+=5
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None
            elif current_player.production_building_level==1:
                current_player.production_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.production_building_progress>=1:
                    current_player.level_2_buildings+=1
                    current_player.production_building_progress=0
                    current_player.production_building_level+=1
                    current_player.production+=5
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None
            elif current_player.production_building_level==2:
                current_player.production_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.production_building_progress>=1:
                    current_player.level_3_buildings+=1
                    current_player.production_building_progress=0
                    current_player.production_building_level+=1
                    current_player.production+=10
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None
                    
        #This part of the code is for if the player is building a gold building.
        elif current_player.constructing.building_type=="gold building":
            if current_player.gold_building_level==0:
                current_player.gold_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.gold_building_progress>=1:
                    current_player.level_1_buildings+=1
                    current_player.gold_building_progress=0
                    current_player.gold_building_level+=1
                    current_player.gold_per_turn+=5
                    current_player.constructing=None
            elif current_player.gold_building_level==1:
                current_player.gold_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.gold_building_progress>=1:
                    current_player.level_2_buildings+=1
                    current_player.gold_building_progress=0
                    current_player.gold_building_level+=1
                    current_player.gold_per_turn+=15
                    current_player.constructing=None
            elif current_player.gold_building_level==2:
                current_player.gold_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.gold_building_progress>=1:
                    current_player.level_3_buildings+=1
                    current_player.gold_building_progress=0
                    current_player.gold_building_level+=1
                    current_player.gold_per_turn+=25
                    current_player.constructing=None   
                    
        #This part of the code is for if the player is building a defence 
        #building.
        elif current_player.constructing.building_type=="defence building":
            if current_player.defence_building_level==0:
                current_player.defence_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.defence_building_progress>=1:
                    current_player.level_1_buildings+=1
                    current_player.defence_building_progress=0
                    current_player.defence_building_level+=1
                    current_player.defence+=10
                    current_player.constructing=None
            elif current_player.defence_building_level==1:
                current_player.defence_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.defence_building_progress>=1:
                    current_player.level_2_buildings+=1
                    current_player.defence_building_progress=0
                    current_player.defence_building_level+=1
                    current_player.defence+=20
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None
            elif current_player.defence_building_level==2:
                current_player.defence_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.defence_building_progress>=1:
                    current_player.level_3_buildings+=1
                    current_player.defence_building_progress=0
                    current_player.defence_building_level+=1
                    current_player.defence+=30
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None  
                    
        #This part of the code is for if the player is building a food building.    
        elif current_player.constructing.building_type=="food building":
            if current_player.food_building_level==0:
                current_player.food_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.food_building_progress>=1:
                    current_player.level_1_buildings+=1
                    current_player.food_building_progress=0
                    current_player.food_building_level+=1
                    current_player.food+=10
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None
            elif current_player.food_building_level==1:
                current_player.food_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.food_building_progress>=1:
                    current_player.level_2_buildings+=1
                    current_player.food_building_progress=0
                    current_player.food_building_level+=1
                    current_player.food+=15
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None
            elif current_player.food_building_level==2:
                current_player.food_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.food_building_progress>=1:
                    current_player.level_3_buildings+=1
                    current_player.food_building_progress=0
                    current_player.food_building_level+=1
                    current_player.food+=20
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None     
                    
        #This part of the code is for if the player is building a favor building
        elif current_player.constructing.building_type=="favor building":
            if current_player.favor_building_level==0:
                current_player.favor_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.favor_building_progress>=1:
                    current_player.level_1_buildings+=1
                    current_player.favor_building_progress=0
                    current_player.favor_building_level+=1
                    current_player.favor+=5
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None
            elif current_player.favor_building_level==1:
                current_player.favor_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.favor_building_progress>=1:
                    current_player.level_2_buildings+=1
                    current_player.favor_building_progress=0
                    current_player.favor_building_level+=1
                    current_player.favor+=5
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None
            elif current_player.favor_building_level==2:
                current_player.favor_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.favor_building_progress>=1:
                    current_player.level_3_buildings+=1
                    current_player.favor_building_progress=0
                    current_player.favor_building_level+=1
                    current_player.favor+=5
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None 
                    
        #This part of the code is for if the player is building a happiness
        #building.
        elif current_player.constructing.building_type=="happiness building":
            if current_player.happiness_building_level==0:
                current_player.happiness_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.happiness_building_progress>=1:
                    current_player.level_1_buildings+=1
                    current_player.happiness_building_progress=0
                    current_player.happiness_building_level+=1
                    current_player.base_happiness+=4
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None
            elif current_player.happiness_building_level==1:
                current_player.happiness_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.happiness_building_progress>=1:
                    current_player.level_2_buildings+=1
                    current_player.happiness_building_progress=0
                    current_player.happiness_building_level+=1
                    current_player.base_happiness+=4
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None
            elif current_player.happiness_building_level==2:
                current_player.happiness_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.happiness_building_progress>=1:
                    current_player.level_3_buildings+=1
                    current_player.base_happiness+=4
                    current_player.happiness_building_progress=0
                    current_player.happiness_building_level+=1
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None 
                    
        #This part of the code is for if the player is building a hero building.
        elif current_player.constructing.building_type=="hero building":
            if current_player.constructing.name=="barracks":
                current_player.warrior_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.warrior_building_progress>=1:
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None 
                    current_player.warrior_building=True
                    current_player.hero_buildings+=1
            elif current_player.constructing.name=="arcane_academy":
                current_player.mage_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.mage_building_progress>=1:
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None 
                    current_player.mage_building=True   
                    current_player.hero_buildings+=1 
            elif current_player.constructing.name=="pub":
                current_player.rogue_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.rogue_building_progress>=1:
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None 
                    current_player.rogue_building=True   
                    current_player.hero_buildings+=1    
            elif current_player.constructing.name=="church":
                current_player.priest_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.priest_building_progress>=1:
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None 
                    current_player.priest_building=True  
                    current_player.hero_buildings+=1     
            elif current_player.constructing.name=="armory":
                current_player.knight_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.knight_building_progress>=1:
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None 
                    current_player.knight_building=True 
                    current_player.hero_buildings+=1      
            elif current_player.constructing.name=="shooting_range":
                current_player.archer_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.archer_building_progress>=1:
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None 
                    current_player.archer_building=True 
                    current_player.hero_buildings+=1      
            elif current_player.constructing.name=="stable":
                current_player.pegasus_knight_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.pegasus_knight_building_progress>=1:
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None 
                    current_player.pegasus_knight_building=True
                    current_player.hero_buildings+=1   
                    
        #This part of the code is for if the player is building a unique 
        #building.                    
        elif current_player.constructing.building_type=="unique building":     
            if current_player.constructing.name=="colosseum":
                current_player.colosseum_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.colosseum_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.colosseum=True
            elif current_player.constructing.name=="mystical_shrine":
                current_player.mystical_shrine_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.mystical_shrine_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.mystical_shrine=True
            elif current_player.constructing.name=="gambling_house":
                current_player.gambling_house_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.gambling_house_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.gambling_house=True
            elif current_player.constructing.name=="chapel":
                current_player.chapel_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.chapel_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.chapel=True
            elif current_player.constructing.name=="jousting_league":
                current_player.jousting_league_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.jousting_league_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.jousting_league=True
            elif current_player.constructing.name=="hunting_grounds":
                current_player.hunting_grounds_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.hunting_grounds_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.hunting_grounds=True
            elif current_player.constructing.name=="pegasus_olympics":
                current_player.pegasus_olympics_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.pegasus_olympics_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.pegasus_olympics=True
            elif current_player.constructing.name=="national_epic_(s)":
                current_player.national_epic_s_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.national_epic_s_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.production+=3
                    current_player.gold_per_turn+=5
                    current_player.defence+=5
                    current_player.food+=5
                    current_player.favor+=2
                    current_player.base_happiness+=2
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.national_epic_s=True
            elif current_player.constructing.name=="national_epic_(m)":
                current_player.national_epic_m_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.national_epic_m_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.production+=3
                    current_player.gold_per_turn+=5
                    current_player.defence+=5
                    current_player.food+=5
                    current_player.favor+=2
                    current_player.base_happiness+=2
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.national_epic_m=True
            elif current_player.constructing.name=="national_epic_(l)":
                current_player.national_epic_l_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.national_epic_l_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.production+=3
                    current_player.gold_per_turn+=5
                    current_player.defence+=5
                    current_player.food+=5
                    current_player.favor+=2
                    current_player.base_happiness+=2
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.national_epic_l=True
            elif current_player.constructing.name=="volcanic_forge":
                current_player.volcanic_forge_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.volcanic_forge_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.production+=10
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.volcanic_forge=True
            elif current_player.constructing.name=="national_treasury":
                current_player.national_treasury_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.national_treasury_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.gold_per_turn+=35
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.national_treasury=True
            elif current_player.constructing.name=="stronghold":
                current_player.stronghold_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.stronghold_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.defence+=50
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.stronghold=True
            elif current_player.constructing.name=="continental_gardens":
                current_player.continental_gardens_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.continental_gardens_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.food+=30
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.continental_gardens=True
            elif current_player.constructing.name=="heroic_tribute":
                current_player.heroic_tribute_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.heroic_tribute_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.favor+=5
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.heroic_tribute=True
            elif current_player.constructing.name=="academy_of_art":
                current_player.academy_of_art_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.academy_of_art_progress>=1:
                    classes.Unique_Building.uniques_built+=1
                    current_player.base_happiness+=16
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing.unique_object.built=True   
                    for i in towns:
                        if i!=current_player:
                            i.messages_to_display+=[current_player.constructing.unique_object.built_message]
                        if i.constructing==current_player.constructing and i!=current_player:
                            i.constructing=None
                    current_player.constructing=None 
                    current_player.academy_of_art=True
            
        #This part of the code is for if the player is building something found 
        #under the Other tab.                  
        elif current_player.constructing.building_type=="other building":
            if current_player.constructing.name=="house":
                current_player.house_building_progress+=current_player.production_progress/current_player.constructing.production_needed
                if current_player.house_building_progress>=1:
                    current_player.maintenance_cost+=current_player.constructing.maintenance_cost
                    current_player.gold_per_turn-=current_player.constructing.maintenance_cost
                    current_player.constructing=None 
                    current_player.house_building_progress=0
                    current_player.houses+=1
            elif current_player.constructing.name=="cater_to_a_hero":
                if current_player.catering_to.hero_class=="warrior":
                    current_player.warrior_favor+=10
                if current_player.catering_to.hero_class=="mage":
                    current_player.mage_favor+=10
                if current_player.catering_to.hero_class=="rogue":
                    current_player.rogue_favor+=10
                if current_player.catering_to.hero_class=="priest":
                    current_player.priest_favor+=10
                if current_player.catering_to.hero_class=="knight":
                    current_player.knight_favor+=10
                if current_player.catering_to.hero_class=="archer":
                    current_player.archer_favor+=10
                if current_player.catering_to.hero_class=="pegasus_knight":
                    current_player.pegasus_knight_favor+=10
                current_player.constructing=None 
                current_player.catering_to=None
            
        #This part of the code checks to see if the player has unlocked the 
        #level 1 or 2 buildings.
        if current_player.level_1_buildings==3:
            current_player.level_2_buildings_locked=False
        if current_player.level_2_buildings==3:
            current_player.level_3_buildings_locked=False
            
            
            
            
            

            
def update_to_build_menu(current_player, l_1, l_2, l_3, hero_building_tab, unique_building_tab, other_tab, to_build_rects, clearer, turns_left_font):
    '''
    update_to_build_menu(Town, Rect, Rect, Rect, Rect, Rect, Rect, list, Surface, Font) --> None
    This function has the purpose of manipulating the menu that displays what 
    the current player can and can't build, so that is menu is easier to 
    navigate. Whenever a player is done building something, they can no longer 
    build it (excluding the options found under the "Other" tab), so this 
    function makes it so those buildings are no longer accessible to the current
    player. This function does the same for any unique buildings that have been 
    constructed by any player, and thus, cannot be built. This function is 
    activated at the start of each players turn.
    '''
    
    #This part of the code resets the position of all the tabs.
    l_1.top=107
    l_2.top=127
    l_3.top=147
    hero_building_tab.top=167
    unique_building_tab.top=187
    other_tab.top=207
    
    change_by=0
    for i in to_build_rects:
        #This part of the code is used to see if a building is locked to the 
        #current player.
        locked_building=False
        if i.level==2 and current_player.level_2_buildings_locked==True:
            locked_building=True
        if i.level==3 and current_player.level_3_buildings_locked==True:
            locked_building=True
        if i.building_type=="production building" and i.level>current_player.production_building_level+1:
            locked_building=True
        if i.building_type=="gold building" and i.level>current_player.gold_building_level+1:
            locked_building=True
        if i.building_type=="defence building" and i.level>current_player.defence_building_level+1:
            locked_building=True
        if i.building_type=="food building" and i.level>current_player.food_building_level+1:
            locked_building=True
        if i.building_type=="favor building" and i.level>current_player.favor_building_level+1:
            locked_building=True
        if i.building_type=="happiness building" and i.level>current_player.happiness_building_level+1:
            locked_building=True
        if i.building_type=="hero building" and current_player.favor_building_level==0:
            locked_building=True
        if i.building_type=="unique building" and i.name=="colosseum":
            if i.unique_object.built==True or current_player.favor_building_level<2 or current_player.warrior_favor<classes.Hero.FavorForAlly or current_player.warrior_building==False:
                locked_building=True
        if i.building_type=="unique building" and i.name=="mystical_shrine":
            if i.unique_object.built==True or current_player.favor_building_level<2 or current_player.mage_favor<classes.Hero.FavorForAlly or current_player.mage_building==False:
                locked_building=True
        if i.building_type=="unique building" and i.name=="gambling_house":
            if i.unique_object.built==True or current_player.favor_building_level<2 or current_player.rogue_favor<classes.Hero.FavorForAlly or current_player.rogue_building==False:
                locked_building=True
        if i.building_type=="unique building" and i.name=="chapel":
            if i.unique_object.built==True or current_player.favor_building_level<2 or current_player.priest_favor<classes.Hero.FavorForAlly or current_player.priest_building==False:
                locked_building=True
        if i.building_type=="unique building" and i.name=="jousting_league":
            if i.unique_object.built==True or current_player.favor_building_level<2 or current_player.knight_favor<classes.Hero.FavorForAlly or current_player.knight_building==False:
                locked_building=True
        if i.building_type=="unique building" and i.name=="hunting_grounds":
            if i.unique_object.built==True or current_player.favor_building_level<2 or current_player.archer_favor<classes.Hero.FavorForAlly or current_player.archer_building==False:
                locked_building=True
        if i.building_type=="unique building" and i.name=="pegasus_olympics":
            if i.unique_object.built==True or current_player.favor_building_level<2 or current_player.pegasus_knight_favor<classes.Hero.FavorForAlly or current_player.pegasus_knight_building==False:
                locked_building=True
        if i.building_type=="unique building" and i.name=="national_epic_(s)":
            if i.unique_object.built==True or current_player.level_1_buildings!=6:
                locked_building=True
        if i.building_type=="unique building" and i.name=="national_epic_(m)":
            if i.unique_object.built==True or current_player.level_2_buildings!=6:
                locked_building=True
        if i.building_type=="unique building" and i.name=="national_epic_(l)":
            if i.unique_object.built==True or current_player.level_3_buildings!=6:
                locked_building=True
        if i.building_type=="unique building" and i.name=="volcanic_forge":
            if i.unique_object.built==True or current_player.production_building_level!=3:
                locked_building=True
        if i.building_type=="unique building" and i.name=="national_treasury":
            if i.unique_object.built==True or current_player.gold_building_level!=3:
                locked_building=True
        if i.building_type=="unique building" and i.name=="stronghold":
            if i.unique_object.built==True or current_player.defence_building_level!=3:
                locked_building=True
        if i.building_type=="unique building" and i.name=="continental_gardens":
            if i.unique_object.built==True or current_player.food_building_level!=3:
                locked_building=True
        if i.building_type=="unique building" and i.name=="heroic_tribute":
            if i.unique_object.built==True or current_player.favor_building_level!=3:
                locked_building=True
        if i.building_type=="unique building" and i.name=="academy_of_art":
            if i.unique_object.built==True or current_player.happiness_building_level!=3:
                locked_building=True
        updated_text=turns_left_font.render("Locked", True, (255,255,255))
        i.image.blit(clearer, (38,16))
        i.image.blit(updated_text, (38,16))
        
        #This part of the code is used to see how long it will take for the 
        #current player to build a given building.
        if locked_building==False:
            turns_to_build_num=0
            #Level 1, 2, and 3 buildings
            if i.building_type=="production building" and i.level>current_player.production_building_level:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.production_building_progress)/current_player.production_progress
            if i.building_type=="gold building" and i.level>current_player.gold_building_level:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.gold_building_progress)/current_player.production_progress
            if i.building_type=="defence building" and i.level>current_player.defence_building_level:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.defence_building_progress)/current_player.production_progress
            if i.building_type=="food building" and i.level>current_player.food_building_level:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.food_building_progress)/current_player.production_progress
            if i.building_type=="favor building" and i.level>current_player.favor_building_level:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.favor_building_progress)/current_player.production_progress
            if i.building_type=="happiness building" and i.level>current_player.happiness_building_level:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.happiness_building_progress)/current_player.production_progress
            #Hero buildings
            if i.name=="barracks" and current_player.warrior_building==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.warrior_building_progress)/current_player.production_progress
            if i.name=="arcane_academy" and current_player.mage_building==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.mage_building_progress)/current_player.production_progress
            if i.name=="pub" and current_player.rogue_building==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.rogue_building_progress)/current_player.production_progress
            if i.name=="church" and current_player.priest_building==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.priest_building_progress)/current_player.production_progress
            if i.name=="armory" and current_player.knight_building==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.knight_building_progress)/current_player.production_progress
            if i.name=="shooting_range" and current_player.archer_building==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.archer_building_progress)/current_player.production_progress
            if i.name=="stable" and current_player.pegasus_knight_building==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.pegasus_knight_building_progress)/current_player.production_progress
            #Unique buildings
            if i.name=="colosseum" and current_player.colosseum==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.colosseum_progress)/current_player.production_progress
            if i.name=="mystical_shrine" and current_player.mystical_shrine==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.mystical_shrine_progress)/current_player.production_progress
            if i.name=="gambling_house" and current_player.gambling_house==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.gambling_house_progress)/current_player.production_progress
            if i.name=="chapel" and current_player.chapel==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.chapel_progress)/current_player.production_progress
            if i.name=="jousting_league" and current_player.jousting_league==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.jousting_league_progress)/current_player.production_progress
            if i.name=="hunting_grounds" and current_player.hunting_grounds==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.hunting_grounds_progress)/current_player.production_progress
            if i.name=="pegasus_olympics" and current_player.pegasus_olympics==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.pegasus_olympics_progress)/current_player.production_progress
            if i.name=="national_epic_(s)" and current_player.national_epic_s==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.national_epic_s_progress)/current_player.production_progress
            if i.name=="national_epic_(m)" and current_player.national_epic_m==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.national_epic_m_progress)/current_player.production_progress
            if i.name=="national_epic_(l)" and current_player.national_epic_l==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.national_epic_l_progress)/current_player.production_progress
            if i.name=="volcanic_forge" and current_player.volcanic_forge==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.volcanic_forge_progress)/current_player.production_progress
            if i.name=="national_treasury" and current_player.national_treasury==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.national_treasury_progress)/current_player.production_progress
            if i.name=="stronghold" and current_player.stronghold==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.stronghold_progress)/current_player.production_progress
            if i.name=="continental_gardens" and current_player.continental_gardens==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.continental_gardens_progress)/current_player.production_progress
            if i.name=="heroic_tribute" and current_player.heroic_tribute==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.heroic_tribute_progress)/current_player.production_progress
            if i.name=="academy_of_art" and current_player.academy_of_art==False:
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.academy_of_art_progress)/current_player.production_progress
            #Houses
            if i.building_type=="other building" and i.name=="house":
                turns_to_build_num=(i.production_needed-i.production_needed*current_player.house_building_progress)/current_player.production_progress
            if int(turns_to_build_num)<turns_to_build_num:
                turns_to_build_num+=1
            #Catering to a hero
            if i.building_type=="other building" and i.name=="cater_to_a_hero":
                turns_to_build_num="N/A"
                
            if type(turns_to_build_num)==str:
                updated_text=turns_left_font.render("Turns: {}".format(turns_to_build_num), True, (255,255,255))
            if type(turns_to_build_num)!=str:
                updated_text=turns_left_font.render("Turns: {}".format(int(turns_to_build_num)), True, (255,255,255))
            i.image.blit(clearer, (38,16))
            i.image.blit(updated_text, (38,16))
            
        #If a building has been built, it will no longer appear in the building 
        #menu. This part of the code make it so if something is built, 
        #everything below it is shifted up. 
        i.rect.top=i.reset_top-change_by
        if i.building_type=="production building" and i.level<=current_player.production_building_level:
            change_by+=32
        if i.building_type=="gold building" and i.level<=current_player.gold_building_level:
            change_by+=32
        if i.building_type=="defence building" and i.level<=current_player.defence_building_level:
            change_by+=32
        if i.building_type=="food building" and i.level<=current_player.food_building_level:
            change_by+=32
        if i.building_type=="favor building" and i.level<=current_player.favor_building_level:
            change_by+=32
        if i.building_type=="happiness building":
            change_by=0
            
        if i.name=="barracks" and current_player.warrior_building==True:
            change_by+=32
        if i.name=="arcane_academy" and current_player.mage_building==True:
            change_by+=32
        if i.name=="pub" and current_player.rogue_building==True:
            change_by+=32
        if i.name=="church" and current_player.priest_building==True:
            change_by+=32
        if i.name=="armory" and current_player.knight_building==True:
            change_by+=32
        if i.name=="shooting_range" and current_player.archer_building==True:
            change_by+=32
        if i.name=="stable":
            change_by=0
            
        if i.name=="colosseum" and i.unique_object.built==True:
            change_by+=32
        if i.name=="mystical_shrine" and i.unique_object.built==True:
            change_by+=32
        if i.name=="gambling_house" and i.unique_object.built==True:
            change_by+=32
        if i.name=="chapel" and i.unique_object.built==True:
            change_by+=32
        if i.name=="jousting_league" and i.unique_object.built==True:
            change_by+=32
        if i.name=="hunting_grounds" and i.unique_object.built==True:
            change_by+=32
        if i.name=="pegasus_olympics" and i.unique_object.built==True:
            change_by+=32
        if i.name=="national_epic_(s)" and i.unique_object.built==True:
            change_by+=32
        if i.name=="national_epic_(m)" and i.unique_object.built==True:
            change_by+=32
        if i.name=="national_epic_(l)" and i.unique_object.built==True:
            change_by+=32
        if i.name=="volcanic_forge" and i.unique_object.built==True:
            change_by+=32
        if i.name=="national_treasury" and i.unique_object.built==True:
            change_by+=32
        if i.name=="stronghold" and i.unique_object.built==True:
            change_by+=32
        if i.name=="continental_gardens" and i.unique_object.built==True:
            change_by+=32
        if i.name=="heroic_tribute" and i.unique_object.built==True:
            change_by+=32
        if i.name=="academy_of_art":
            change_by=0
            
    
def manage_population(town, turn_number):
    '''
    manage_population(Town, int) --> None
    This function is used at the start of each players turn, and has the purpose
    of updating the current players' population. There are three stats that 
    affect population: food, defence, and houses. If a player has more food than
    population, then their population will slowly grow until it is equal to the 
    food stat. However, if the current player has less food the population, then
    its population stat will slowly decrease. The rate at which the population 
    grows or shrinks is dependent on how much more or less food the current 
    player has than population. If a player has more population then defence, 
    every few turns that player has a chance at losing one member of its 
    population. This chance increases the more their population stat exceeds 
    there defence. Finally, with houses, if a player has a higher population 
    then houses, its population stat will instantly go down to match the houses 
    stat. A player can only get a higher population if they have enough houses.
    '''
    
    if town.food>town.population:
        town.population+=1
    
    if turn_number/5==int(turn_number/5) and town.defence+(len(town.heroes_in_town)*10)<town.population:
        if random.randint(1,10)<=(town.population-(town.defence+(len(town.heroes_in_town)*10))):
            town.population-=1
            
    if town.population>town.houses:
        town.population=town.houses
        
            
def update_happiness(current_player, turn_number):
    '''
    update_happiness(town, int) --> None
    This function is run at the beginning of each players turn in order to 
    update the given player's happiness stat. Several factors are used to check
    what a player's happiness stat should be, including: how many turns have 
    passed, if the given player doesn't have enough food to feed its population,
    if the player doesn't have enough defence to protect its population, and 
    which buildings the player has built.
    '''
    
    happiness=current_player.base_happiness-int(turn_number/10)
    
    if current_player.food<current_player.population:
        happiness-=5
    if current_player.defence+(len(current_player.heroes_in_town)*10)<current_player.population:
        happiness-=5
    if current_player.gold_per_turn==0:
        happiness-=1
    if current_player.gold_per_turn<0:
        happiness-=3
    if current_player.gold<0:
        happiness-=15
        current_player.gold=0
    current_player.happiness=happiness
    
    return

    
def update_favor(towns):
    '''
    update_favor(list) --> None
    This function is used after all players have taken a turn, and it serves to
    increase, decrease or do nothing to the amount of favor each town has with
    each hero. Several things can modify the amount of favor a hero has with a
    town, including the town's current happiness stat, whether or not a hero is
    in the given town, and which buildings a town has built.
    '''
    for i in towns:
        
        modifiers=find_favor_modifier(i)
        
        c=0
        for ii in modifiers:
            
            if c==0:
                i.warrior_favor=max(0, i.warrior_favor+ii[0])
            if c==1:
                i.mage_favor=max(0, i.mage_favor+ii[0])
            if c==2:
                i.rogue_favor=max(0, i.rogue_favor+ii[0])
            if c==3:
                i.priest_favor=max(0, i.priest_favor+ii[0])
            if c==4:
                i.knight_favor=max(0, i.knight_favor+ii[0])
            if c==5:
                i.archer_favor=max(0, i.archer_favor+ii[0])
            if c==6:
                i.pegasus_knight_favor=max(0, i.pegasus_knight_favor+ii[0])
            
            c+=1
            
            
        #This part of the code updates the favor stats found within the Hero sprites
        for i in classes.Hero.heroes:
            i.town_favors=[]
        for i in towns:
            i.total_favor=i.warrior_favor+i.mage_favor+i.rogue_favor+i.priest_favor+i.knight_favor+i.archer_favor+i.pegasus_knight_favor
            classes.Hero.heroes[0].town_favors+=[i.warrior_favor]
            classes.Hero.heroes[1].town_favors+=[i.mage_favor]
            classes.Hero.heroes[2].town_favors+=[i.rogue_favor]
            classes.Hero.heroes[3].town_favors+=[i.priest_favor]
            classes.Hero.heroes[4].town_favors+=[i.knight_favor]
            classes.Hero.heroes[5].town_favors+=[i.archer_favor]
            classes.Hero.heroes[6].town_favors+=[i.pegasus_knight_favor]
            
            
def update_production(current_player):
    '''
    update_production(Town) --> None
    Updates the number used to determine how much progress the player makes
    towards building things.
    '''
    current_player.production_progress=current_player.production+current_player.population
    return
            
    

def update_hero_screen(current_player, hero_info_screen, hero_screen_clear, hero_info_font, towns):
    '''
    update_hero_screen(Town, Surface, Surface, Font, list) --> Surface
    In order for a player to make the correct decisions, the need to have
    certain information supplied to them. This information is given through the 
    Hero Info menu. This function is run at the beginning of each player's turn,
    and its purpose is to build and return an image that supply's the player 
    with important information regarding the heroes.

    '''
    hero_info_screen.blit(hero_screen_clear, (23,63))
    
    
    
    #Creates modifier and favor info
    modifiers=find_favor_modifier(current_player)    
    
    c=0
    for i in classes.Hero.heroes:
        hero_info_screen.blit(i.idle_frames[0], (40-i.idle_frames[0].get_size()[0]/2, 65+(c*38)))
        name_text=hero_info_font.render("{}".format(i.name), True, (255,255,255))
        hero_info_screen.blit(name_text, (90-name_text.get_size()[0]/2, 75+(c*38)))
        class_text=hero_info_font.render("{}".format(i.hero_class_formated), True, (255,255,255))
        hero_info_screen.blit(class_text, (180-class_text.get_size()[0]/2, 75+(c*38)))
        favor_num_text=hero_info_font.render("{}".format(i.town_favors[current_player.player_number-1]), True, (255,255,255))
        hero_info_screen.blit(favor_num_text, (250-favor_num_text.get_size()[0]/2, 75+(c*38)))
        
        
        if modifiers[c][0]>=0:
            if modifiers[c][1]==True:
                modifier_text=hero_info_font.render("Max", True, (255,255,255))
            if modifiers[c][1]==False:
                modifier_text=hero_info_font.render("(+{})".format(modifiers[c][0]), True, (255,255,255))
              
        if modifiers[c][0]<0:
            modifier_text=hero_info_font.render("({})".format(modifiers[c][0]), True, (255,255,255))
        hero_info_screen.blit(modifier_text, (304-modifier_text.get_size()[0]/2, 75+(c*38)))
        
        #Displays the turns since a hero last visited a town
        if i.hero_class=="warrior":
            last_visit_text=hero_info_font.render("{}".format(current_player.turns_since_warrior_visit), True, (255,255,255))
        if i.hero_class=="mage":
            last_visit_text=hero_info_font.render("{}".format(current_player.turns_since_mage_visit), True, (255,255,255))
        if i.hero_class=="rogue":
            last_visit_text=hero_info_font.render("{}".format(current_player.turns_since_rogue_visit), True, (255,255,255))
        if i.hero_class=="priest":
            last_visit_text=hero_info_font.render("{}".format(current_player.turns_since_priest_visit), True, (255,255,255))
        if i.hero_class=="knight":
            last_visit_text=hero_info_font.render("{}".format(current_player.turns_since_knight_visit), True, (255,255,255))
        if i.hero_class=="archer":
            last_visit_text=hero_info_font.render("{}".format(current_player.turns_since_archer_visit), True, (255,255,255))
        if i.hero_class=="pegasus_knight":
            last_visit_text=hero_info_font.render("{}".format(current_player.turns_since_pegasus_knight_visit), True, (255,255,255))
        hero_info_screen.blit(last_visit_text, (385-last_visit_text.get_size()[0]/2, 75+(c*38)))
        
        #This part of the code determines which town a hero likes the most
        skip_for_favorite=[]
        c2=0
        for ii in towns:
            if ii.eliminated==True:
                skip_for_favorite+=[c2]
            c2+=1
        highest_favor=min(i.town_favors)
        highest_favors=0
        c2=0
        for ii in i.town_favors:
            if c2 not in skip_for_favorite:
                if ii==highest_favor:
                    highest_favors+=1
                if ii>highest_favor:
                    highest_favor=ii
                    highest_favors=1
            c2+=1
            
        if highest_favors==1:
            favorite_town_text=hero_info_font.render("{}".format(towns[i.town_favors.index(highest_favor)].town_name), True, (255,255,255))
        if highest_favors!=1:
            favorite_town_text=hero_info_font.render("Undecided", True, (255,255,255))
        hero_info_screen.blit(favorite_town_text, (488-favorite_town_text.get_size()[0]/2, 75+(c*38)))
        c+=1
        
    return hero_info_screen



def find_favor_modifier(current_player):
    '''
    find_favor_modifier(Town) --> [[int, bool], [int, bool], ... ,[int, bool]]
    Used by update_favor() and update_hero_screen()
    Returns a list of lists. Each element refers to a different hero. The first
    element of the sub-list is that heroes's favor modifier, the second element
    is True if the Town will reach its maximum favor with this modifier.
    If the max favor is exceded, the returnd ints will be reduced.
    '''
    
    output=[]
    
    c=0
        
    favor_and_buildings=[[current_player.warrior_favor, current_player.warrior_building, current_player.colosseum], [current_player.mage_favor, current_player.mage_building, current_player.mystical_shrine], [current_player.rogue_favor, current_player.rogue_building, current_player.gambling_house], [current_player.priest_favor, current_player.priest_building, current_player.chapel], [current_player.knight_favor, current_player.knight_building, current_player.jousting_league], [current_player.archer_favor, current_player.archer_building, current_player.hunting_grounds], [current_player.pegasus_knight_favor, current_player.pegasus_knight_building, current_player.pegasus_olympics]]
        
    for i in classes.Hero.heroes:
        
        modifier=0
        max_favor=current_player.favor+5
        
        
        if current_player.happiness<=-10:
            modifier-=15
        if current_player.happiness<=-5 and current_player.happiness>-10:
            if i in current_player.heroes_in_town:
                modifier-=5
            if i not in current_player.heroes_in_town:
                modifier-=6
        if current_player.happiness<0 and current_player.happiness>-5:
            if i in current_player.heroes_in_town:
                modifier-=3
            if i not in current_player.heroes_in_town:
                modifier-=4
        if current_player.happiness<=5 and current_player.happiness>=0:
            if i in current_player.heroes_in_town:
                modifier+=1
            if i not in current_player.heroes_in_town:
                modifier+=0
        if current_player.happiness<=10 and current_player.happiness>5:
            if i in current_player.heroes_in_town:
                modifier+=10
            if i not in current_player.heroes_in_town:
                modifier+=8
        if current_player.happiness>10:
            if i in current_player.heroes_in_town:
                modifier+=14
            if i not in current_player.heroes_in_town:
                modifier+=10
            
        #This part of the code gives the player favor bonuses with a hero
        #if they have that heroes building, or unique building, as well as
        #updating the stat.
        modifier+=current_player.favor_building_level
    
        if current_player.national_epic_s==True:
            modifier+=1
        if current_player.national_epic_m==True:
            modifier+=1
        if current_player.national_epic_l==True:
            modifier+=1
        if current_player.heroic_tribute==True:
            modifier+=5
            
        
        if favor_and_buildings[c][1]==True:
            modifier+=3
            max_favor+=25
        if favor_and_buildings[c][2]==True:
            modifier+=20
            max_favor+=20
            
        if modifier>0:
            modifier=int((modifier/2)+0.5)
            
        if favor_and_buildings[c][0]>=max_favor and modifier>=0:
            output+=[[0, True]]
        elif (favor_and_buildings[c][0]+modifier)>max_favor:
            output+=[[max_favor-favor_and_buildings[c][0], False]]
        elif (favor_and_buildings[c][0]+modifier)<=max_favor:
            output+=[[modifier, False]]
            
        
        c+=1
        
    return output





    
    
def update_hero_events(current_player):
    '''
    update_hero_events(Town) --> None
    If a hero doesn't visit a town is a long time, then that town has a chance
    to obtain what is known as a Hero Event. If this happens, the town needs to
    try and have the hero visit them within 10 turns, or the will half of
    their population. This function is used at the start of each player's turn
    to check if the player qualifies for one of these events, as well as
    penalize the player if they fail an event, and check to see if the player
    has succeeded in an event.
    '''
    current_player.warrior_event_cooldown=max(current_player.warrior_event_cooldown-1, 0)
    current_player.mage_event_cooldown=max(current_player.mage_event_cooldown-1, 0)
    current_player.rogue_event_cooldown=max(current_player.rogue_event_cooldown-1, 0)
    current_player.priest_event_cooldown=max(current_player.priest_event_cooldown-1, 0)
    current_player.knight_event_cooldown=max(current_player.knight_event_cooldown-1, 0)
    current_player.archer_event_cooldown=max(current_player.archer_event_cooldown-1, 0)
    current_player.pegasus_knight_event_cooldown=max(current_player.pegasus_knight_event_cooldown-1, 0)    
    
    for i in current_player.heroes_in_town:
        if i.hero_class=="warrior":
            current_player.turns_since_warrior_visit=0
            if current_player.warrior_event==True:
                current_player.warrior_event=False
                current_player.messages_to_display+=[classes.Hero.heroes[0].event_success_box]
        if i.hero_class=="mage":
            current_player.turns_since_mage_visit=0
            if current_player.mage_event==True:
                current_player.mage_event=False
                current_player.messages_to_display+=[classes.Hero.heroes[1].event_success_box]
        if i.hero_class=="rogue":
            current_player.turns_since_rogue_visit=0
            if current_player.rogue_event==True:
                current_player.rogue_event=False
                current_player.messages_to_display+=[classes.Hero.heroes[2].event_success_box]
        if i.hero_class=="priest":
            current_player.turns_since_priest_visit=0
            if current_player.priest_event==True:
                current_player.priest_event=False
                current_player.messages_to_display+=[classes.Hero.heroes[3].event_success_box]
        if i.hero_class=="knight":
            current_player.turns_since_knight_visit=0
            if current_player.knight_event==True:
                current_player.knight_event=False
                current_player.messages_to_display+=[classes.Hero.heroes[4].event_success_box]
        if i.hero_class=="archer":
            current_player.turns_since_archer_visit=0
            if current_player.archer_event==True:
                current_player.archer_event=False
                current_player.messages_to_display+=[classes.Hero.heroes[5].event_success_box]
        if i.hero_class=="pegasus_knight":
            current_player.turns_since_pegasus_knight_visit=0
            if current_player.pegasus_knight_event==True:
                current_player.pegasus_knight_event=False
                current_player.messages_to_display+=[classes.Hero.heroes[6].event_success_box]

    if current_player.warrior_event==True:
        current_player.turns_for_warrior_event-=1
        if current_player.turns_for_warrior_event==0:
            current_player.warrior_event=False
            current_player.messages_to_display+=[classes.Hero.heroes[0].event_failure_box]
            current_player.warrior_event_cooldown=15
            current_player.population=max(current_player.population-5, 3)
    if current_player.mage_event==True:
        current_player.turns_for_mage_event-=1
        if current_player.turns_for_mage_event==0:
            current_player.mage_event=False
            current_player.messages_to_display+=[classes.Hero.heroes[1].event_failure_box]
            current_player.mage_event_cooldown=15
            current_player.population=max(current_player.population-5, 3)
    if current_player.rogue_event==True:
        current_player.turns_for_rogue_event-=1
        if current_player.turns_for_rogue_event==0:
            current_player.rogue_event=False
            current_player.messages_to_display+=[classes.Hero.heroes[2].event_failure_box]
            current_player.rogue_event_cooldown=15
            current_player.population=max(current_player.population-5, 3)
    if current_player.priest_event==True:
        current_player.turns_for_priest_event-=1
        if current_player.turns_for_priest_event==0:
            current_player.priest_event=False
            current_player.messages_to_display+=[classes.Hero.heroes[3].event_failure_box]
            current_player.priest_event_cooldown=15
            current_player.population=max(current_player.population-5, 3)
    if current_player.knight_event==True:
        current_player.turns_for_knight_event-=1
        if current_player.turns_for_knight_event==0:
            current_player.knight_event=False
            current_player.messages_to_display+=[classes.Hero.heroes[4].event_failure_box]
            current_player.knight_event_cooldown=15
            current_player.population=max(current_player.population-5, 3)
    if current_player.archer_event==True:
        current_player.turns_for_archer_event-=1
        if current_player.turns_for_archer_event==0:
            current_player.archer_event=False
            current_player.messages_to_display+=[classes.Hero.heroes[5].event_failure_box]
            current_player.archer_event_cooldown=15
            current_player.population=max(current_player.population-5, 3)
    if current_player.pegasus_knight_event==True:
        current_player.turns_for_pegasus_knight_event-=1
        if current_player.turns_for_pegasus_knight_event==0:
            current_player.pegasus_knight_event=False
            current_player.messages_to_display+=[classes.Hero.heroes[6].event_failure_box]
            current_player.pegasus_knight_event_cooldown=15
            current_player.population=max(current_player.population-5, 3)

    if random.randint(15,30)<current_player.turns_since_warrior_visit and current_player.warrior_event==False and current_player.warrior_event_cooldown==0:
        current_player.warrior_event=True
        current_player.turns_for_warrior_event=10
        current_player.messages_to_display+=[classes.Hero.heroes[0].event_intro_box]
    if random.randint(15,30)<current_player.turns_since_mage_visit and current_player.mage_event==False and current_player.mage_event_cooldown==0:
        current_player.mage_event=True
        current_player.turns_for_mage_event=10
        current_player.messages_to_display+=[classes.Hero.heroes[1].event_intro_box]
    if random.randint(15,30)<current_player.turns_since_rogue_visit and current_player.rogue_event==False and current_player.rogue_event_cooldown==0:
        current_player.rogue_event=True
        current_player.turns_for_rogue_event=10
        current_player.messages_to_display+=[classes.Hero.heroes[2].event_intro_box]
    if random.randint(15,30)<current_player.turns_since_priest_visit and current_player.priest_event==False and current_player.priest_event_cooldown==0:
        current_player.priest_event=True
        current_player.turns_for_priest_event=10
        current_player.messages_to_display+=[classes.Hero.heroes[3].event_intro_box]
    if random.randint(15,30)<current_player.turns_since_knight_visit and current_player.knight_event==False and current_player.knight_event_cooldown==0:
        current_player.knight_event=True
        current_player.turns_for_knight_event=10
        current_player.messages_to_display+=[classes.Hero.heroes[4].event_intro_box]
    if random.randint(15,30)<current_player.turns_since_archer_visit and current_player.archer_event==False and current_player.archer_event_cooldown==0:
        current_player.archer_event=True
        current_player.turns_for_archer_event=10
        current_player.messages_to_display+=[classes.Hero.heroes[5].event_intro_box]
    if random.randint(15,30)<current_player.turns_since_pegasus_knight_visit and current_player.pegasus_knight_event==False and current_player.pegasus_knight_event_cooldown==0:
        current_player.pegasus_knight_event=True
        current_player.turns_for_pegasus_knight_event=10
        current_player.messages_to_display+=[classes.Hero.heroes[6].event_intro_box]
        
        


def apply_passive_hero_abilities(current_player):
    '''
    apply_passive_hero_abilities(Town) --> None
    Checks to see if the given Town has lost or gained a hero as an ally.
    If they have, this function gives that player a reward, or takes it away.
    '''
    if current_player.warrior_passive_ability_active==False and current_player.warrior_favor>=classes.Hero.FavorForAlly:
        current_player.warrior_passive_ability_active=True
        current_player.production+=5
        current_player.messages_to_display+=[classes.Hero.heroes[0].gain_passive_ability_box]
    if current_player.warrior_passive_ability_active==True and current_player.warrior_favor<classes.Hero.FavorForAlly:
        current_player.warrior_passive_ability_active=False
        current_player.production-=5
        current_player.messages_to_display+=[classes.Hero.heroes[0].lose_passive_ability_box]
        
    if current_player.mage_passive_ability_active==False and current_player.mage_favor>=classes.Hero.FavorForAlly:
        current_player.mage_passive_ability_active=True
        current_player.gold_per_turn+=4
        current_player.messages_to_display+=[classes.Hero.heroes[1].gain_passive_ability_box]
    if current_player.mage_passive_ability_active==True and current_player.mage_favor<classes.Hero.FavorForAlly:
        current_player.mage_passive_ability_active=False
        current_player.gold_per_turn-=4
        current_player.messages_to_display+=[classes.Hero.heroes[1].lose_passive_ability_box]
        
    if current_player.rogue_passive_ability_active==False and current_player.rogue_favor>=classes.Hero.FavorForAlly:
        current_player.rogue_passive_ability_active=True
        current_player.base_happiness+=2
        current_player.messages_to_display+=[classes.Hero.heroes[2].gain_passive_ability_box]
    if current_player.rogue_passive_ability_active==True and current_player.rogue_favor<classes.Hero.FavorForAlly:
        current_player.rogue_passive_ability_active=False
        current_player.base_happiness-=2
        current_player.messages_to_display+=[classes.Hero.heroes[2].lose_passive_ability_box]
        
    if current_player.priest_passive_ability_active==False and current_player.priest_favor>=classes.Hero.FavorForAlly:
        current_player.priest_passive_ability_active=True
        current_player.food+=4
        current_player.messages_to_display+=[classes.Hero.heroes[3].gain_passive_ability_box]
    if current_player.priest_passive_ability_active==True and current_player.priest_favor<classes.Hero.FavorForAlly:
        current_player.priest_passive_ability_active=False
        current_player.food-=4
        current_player.messages_to_display+=[classes.Hero.heroes[3].lose_passive_ability_box]
        
    if current_player.knight_passive_ability_active==False and current_player.knight_favor>=classes.Hero.FavorForAlly:
        current_player.knight_passive_ability_active=True
        current_player.favor+=2
        current_player.messages_to_display+=[classes.Hero.heroes[4].gain_passive_ability_box]
    if current_player.knight_passive_ability_active==True and current_player.knight_favor<classes.Hero.FavorForAlly:
        current_player.knight_passive_ability_active=False
        current_player.favor-=2
        current_player.messages_to_display+=[classes.Hero.heroes[4].lose_passive_ability_box]
        
    if current_player.archer_passive_ability_active==False and current_player.archer_favor>=classes.Hero.FavorForAlly:
        current_player.archer_passive_ability_active=True
        current_player.defence+=7
        current_player.messages_to_display+=[classes.Hero.heroes[5].gain_passive_ability_box]
    if current_player.archer_passive_ability_active==True and current_player.archer_favor<classes.Hero.FavorForAlly:
        current_player.archer_passive_ability_active=False
        current_player.defence-=7
        current_player.messages_to_display+=[classes.Hero.heroes[5].lose_passive_ability_box]
        
    if current_player.pegasus_knight_passive_ability_active==False and current_player.pegasus_knight_favor>=classes.Hero.FavorForAlly:
        current_player.pegasus_knight_passive_ability_active=True
        current_player.production+=3
        current_player.gold_per_turn+=2
        current_player.base_happiness+=1
        current_player.food+=1
        current_player.favor+=1
        current_player.defence+=2
        current_player.messages_to_display+=[classes.Hero.heroes[6].gain_passive_ability_box]
    if current_player.pegasus_knight_passive_ability_active==True and current_player.pegasus_knight_favor<classes.Hero.FavorForAlly:
        current_player.pegasus_knight_passive_ability_active=False
        current_player.production-=3
        current_player.gold_per_turn-=2
        current_player.base_happiness-=1
        current_player.food-=1
        current_player.favor-=1
        current_player.defence-=2
        current_player.messages_to_display+=[classes.Hero.heroes[6].lose_passive_ability_box]
        
        
        
        
        
def fit_text_to_box(text, surface_for_text, message_text_font):
    '''
    fit_text_to_box(String, pygame.Surface, pygame.Font) --> pygame.Surface
    Takes a String, pygame.Surface, and pyame.Font as arguments, and returns a 
    copy of the given pygame.Surface with the given String writen on it, using 
    the given font. The returned surface will maintain its original length,
    but may have its height changed to accomidate the newly added words.
    If the given String has a " | " in it, they will be treated as a line break.
    '''
    letter_size=message_text_font.render("W", True, (255,255,255)).get_size()[1]+1
    surface_size_x=surface_for_text.get_size()[0]
    text_list=[]
    while text!="":
        if " " not in text:
            text_list+=[text]
            text=""
        if " " in text:
            text_list+=[text[:text.find(" ")]]
            text=text[text.find(" ")+1:]
        
    text_x=0
    text_y=0
    lines=[]
    for i in text_list:
        if i!="|":
            temp_text=message_text_font.render(i, True, (255,255,255))
            if (text_x+temp_text.get_size()[0]+3)>=surface_size_x:
                text_x=0
                text_y+=letter_size
            lines+=[[temp_text, (text_x, text_y)]]
            if (text_x+temp_text.get_size()[0]+3)<surface_size_x:
                text_x+=temp_text.get_size()[0]+3
        if i=="|":
            text_x=0
            text_y+=letter_size
    surface_for_text=pygame.transform.scale(surface_for_text, (surface_for_text.get_size()[0],text_y+letter_size))
    
    for i in lines:
        surface_for_text.blit(i[0], i[1])
        
    return surface_for_text




def ai_build_hero_building(current_player, max_to_build):
    '''
    ai_build_hero_building(Town, int) --> None
    Used to decide if an AI player should work on a hero building. Takes a Town
    as the first argument, the Town is assumed to be AI controlled. The second 
    argument is an int. If the given Town has a number of hero buildings equal 
    to or greater then the value of the given int, then it will not construct
    a hero building.
    '''
    
    if current_player.constructing==None and current_player.favor_building_level>0 and False in [current_player.warrior_building,  current_player.mage_building,  current_player.rogue_building,  current_player.priest_building,  current_player.knight_building,  current_player.archer_building,  current_player.pegasus_knight_building]:
        hero_buildings=0
        most_progress=[[-1]]
        c=0
        for i in [current_player.warrior_building_progress, current_player.mage_building_progress, current_player.rogue_building_progress, current_player.priest_building_progress, current_player.knight_building_progress, current_player.archer_building_progress, current_player.pegasus_knight_building_progress]:
            if i>=1:
                hero_buildings+=1
            if i<1 and i>most_progress[0][0]:
                most_progress=[[i, c]]
            elif i<1 and i==most_progress[0][0]:
                most_progress+=[[i, c]]
            c+=1
        if hero_buildings<max_to_build:
            current_player.constructing=classes.Buildings_In_To_Build.hero_building_list[most_progress[random.randrange(0,len(most_progress))][1]]    
    
    return
