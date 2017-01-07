import pygame
from pygame.locals import *
pygame.init()

import os
import random

import classes
import functions




size=(640, 480)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Hero Town")

#screen=pygame.display.set_mode((640, 480), pygame.FULLSCREEN)

helvet=pygame.font.match_font("Helvetica", True, False)

base_dirr=os.getcwd()
img_dirr=base_dirr+"/images"
text_dirr=base_dirr+"/text"
how_to_play_text_dirr=text_dirr+"/how_to_play"







#create players
os.chdir(img_dirr+"/village")
town=pygame.image.load("village_on_map.bmp").convert()
town=pygame.transform.scale(town, (40, 40))
town_distroyed=pygame.image.load("town_distroyed.bmp").convert()
town_distroyed=pygame.transform.scale(town_distroyed, (40, 40))
towns=[]
for i in range(0,2):
    temp_town=classes.Town("Player "+str(i+1), False, town, town_distroyed)
    towns+=[temp_town]
town_group=pygame.sprite.Group(towns)
winner=towns[0]

#define heroes
warrior=classes.Hero("Eirika", "warrior", img_dirr, helvet)
mage=classes.Hero("Lute", "mage", img_dirr, helvet)
rogue=classes.Hero("Colm", "rogue", img_dirr, helvet)
priest=classes.Hero("Moulder", "priest", img_dirr, helvet)
knight=classes.Hero("Seth", "knight", img_dirr, helvet)
archer=classes.Hero("Innes", "archer", img_dirr, helvet)
pegasus_knight=classes.Hero("Venessa", "pegasus_knight", img_dirr, helvet)
hero_group=pygame.sprite.OrderedUpdates([warrior, pegasus_knight, mage, archer, rogue, knight, priest])

#define dragon
dragon=classes.Dragon(img_dirr)
dragon_group=pygame.sprite.Group(dragon)
dragon_turn=False

#define mouse
mouse=classes.Mouse()
m_group=pygame.sprite.Group(mouse)

turn_number=1

#Creates background
os.chdir(img_dirr+"/village")
full_map=pygame.image.load("full_map.bmp").convert()
full_map=pygame.transform.scale(full_map, (640, 380))

#Creates the icons for the level 1, 2, and 3 buildings
os.chdir(img_dirr+"/village/buildings/production")
workshop_icon=pygame.image.load("workshop.bmp").convert()
workshop_icon=pygame.transform.scale(workshop_icon, (75, 75))
workshop_icon.set_colorkey((255,0,255))
stone_works_icon=pygame.image.load("stone_works.bmp").convert()
stone_works_icon=pygame.transform.scale(stone_works_icon, (75, 75))
stone_works_icon.set_colorkey((255,0,255))
forge_icon=pygame.image.load("forge.bmp").convert()
forge_icon=pygame.transform.scale(forge_icon, (75, 75))
forge_icon.set_colorkey((255,0,255))
os.chdir(img_dirr+"/village/buildings/gold")
market_place_icon=pygame.image.load("market_place.bmp").convert()
market_place_icon=pygame.transform.scale(market_place_icon, (75, 75))
market_place_icon.set_colorkey((255,0,255))
trading_post_icon=pygame.image.load("trading_post.bmp").convert()
trading_post_icon=pygame.transform.scale(trading_post_icon, (75, 75))
trading_post_icon.set_colorkey((255,0,255))
trade_network_icon=pygame.image.load("trade_network.bmp").convert()
trade_network_icon=pygame.transform.scale(trade_network_icon, (75, 75))
trade_network_icon.set_colorkey((255,0,255))
os.chdir(img_dirr+"/village/buildings/defence")
walls_icon=pygame.image.load("walls.bmp").convert()
walls_icon=pygame.transform.scale(walls_icon, (75, 75))
walls_icon.set_colorkey((255,0,255))
watchtower_icon=pygame.image.load("watchtower.bmp").convert()
watchtower_icon=pygame.transform.scale(watchtower_icon, (75, 75))
watchtower_icon.set_colorkey((255,0,255))
castle_icon=pygame.image.load("castle.bmp").convert()
castle_icon=pygame.transform.scale(castle_icon, (75, 75))
castle_icon.set_colorkey((255,0,255))
os.chdir(img_dirr+"/village/buildings/food")
wheat_feild_icon=pygame.image.load("wheat_feild.bmp").convert()
wheat_feild_icon=pygame.transform.scale(wheat_feild_icon, (75, 75))
wheat_feild_icon.set_colorkey((255,0,255))
farm_icon=pygame.image.load("farm.bmp").convert()
farm_icon=pygame.transform.scale(farm_icon, (75, 75))
farm_icon.set_colorkey((255,0,255))
granary_icon=pygame.image.load("granary.bmp").convert()
granary_icon=pygame.transform.scale(granary_icon, (75, 75))
granary_icon.set_colorkey((255,0,255))
os.chdir(img_dirr+"/village/buildings/favor")
garden_icon=pygame.image.load("garden.bmp").convert()
garden_icon=pygame.transform.scale(garden_icon, (75, 75))
garden_icon.set_colorkey((255,0,255))
inn_icon=pygame.image.load("inn.bmp").convert()
inn_icon=pygame.transform.scale(inn_icon, (75, 75))
inn_icon.set_colorkey((255,0,255))
theater_icon=pygame.image.load("theater.bmp").convert()
theater_icon=pygame.transform.scale(theater_icon, (75, 75))
theater_icon.set_colorkey((255,0,255))
os.chdir(img_dirr+"/village/buildings/happiness")
monument_icon=pygame.image.load("monument.bmp").convert()
monument_icon=pygame.transform.scale(monument_icon, (75, 75))
monument_icon.set_colorkey((255,0,255))
library_icon=pygame.image.load("library.bmp").convert()
library_icon=pygame.transform.scale(library_icon, (75, 75))
library_icon.set_colorkey((255,0,255))
circus_icon=pygame.image.load("circus.bmp").convert()
circus_icon=pygame.transform.scale(circus_icon, (75, 75))
circus_icon.set_colorkey((255,0,255))

#Creates the icons for the hero buildings
os.chdir(img_dirr+"/village/buildings/hero_buildings")
barracks_icon=pygame.image.load("barracks.bmp").convert()
barracks_icon=pygame.transform.scale(barracks_icon, (75, 75))
barracks_icon.set_colorkey((255,0,255))
arcane_academy_icon=pygame.image.load("arcane_academy.bmp").convert()
arcane_academy_icon=pygame.transform.scale(arcane_academy_icon, (75, 75))
arcane_academy_icon.set_colorkey((255,0,255))
pub_icon=pygame.image.load("pub.bmp").convert()
pub_icon=pygame.transform.scale(pub_icon, (75, 75))
pub_icon.set_colorkey((255,0,255))
church_icon=pygame.image.load("church.bmp").convert()
church_icon=pygame.transform.scale(church_icon, (75, 75))
church_icon.set_colorkey((255,0,255))
armory_icon=pygame.image.load("armory.bmp").convert()
armory_icon=pygame.transform.scale(armory_icon, (75, 75))
armory_icon.set_colorkey((255,0,255))
shooting_range_icon=pygame.image.load("shooting_range.bmp").convert()
shooting_range_icon=pygame.transform.scale(shooting_range_icon, (75, 75))
shooting_range_icon.set_colorkey((255,0,255))
stable_icon=pygame.image.load("stable.bmp").convert()
stable_icon=pygame.transform.scale(stable_icon, (75, 75))
stable_icon.set_colorkey((255,0,255))

#Creates the icons for the unique buildings
os.chdir(img_dirr+"/village/buildings/uniques")
colosseum_icon=pygame.image.load("colosseum.bmp").convert()
colosseum_icon=pygame.transform.scale(colosseum_icon, (75, 75))
colosseum_icon.set_colorkey((255,0,255))
mystical_shrine_icon=pygame.image.load("mystical_shrine.bmp").convert()
mystical_shrine_icon=pygame.transform.scale(mystical_shrine_icon, (75, 75))
mystical_shrine_icon.set_colorkey((255,0,255))
gambling_house_icon=pygame.image.load("gambling_house.bmp").convert()
gambling_house_icon=pygame.transform.scale(gambling_house_icon, (75, 75))
gambling_house_icon.set_colorkey((255,0,255))
chapel_icon=pygame.image.load("chapel.bmp").convert()
chapel_icon=pygame.transform.scale(chapel_icon, (75, 75))
chapel_icon.set_colorkey((255,0,255))
jousting_league_icon=pygame.image.load("jousting_league.bmp").convert()
jousting_league_icon=pygame.transform.scale(jousting_league_icon, (75, 75))
jousting_league_icon.set_colorkey((255,0,255))
hunting_grounds_icon=pygame.image.load("hunting_grounds.bmp").convert()
hunting_grounds_icon=pygame.transform.scale(hunting_grounds_icon, (75, 75))
hunting_grounds_icon.set_colorkey((255,0,255))
pegasus_olympics_icon=pygame.image.load("pegasus_olympics.bmp").convert()
pegasus_olympics_icon=pygame.transform.scale(pegasus_olympics_icon, (75, 75))
pegasus_olympics_icon.set_colorkey((255,0,255))

national_epic_s_icon=pygame.image.load("national_epic_s.bmp").convert()
national_epic_s_icon=pygame.transform.scale(national_epic_s_icon, (75, 75))
national_epic_s_icon.set_colorkey((255,0,255))
national_epic_m_icon=pygame.image.load("national_epic_m.bmp").convert()
national_epic_m_icon=pygame.transform.scale(national_epic_m_icon, (75, 75))
national_epic_m_icon.set_colorkey((255,0,255))
national_epic_l_icon=pygame.image.load("national_epic_l.bmp").convert()
national_epic_l_icon=pygame.transform.scale(national_epic_l_icon, (75, 75))
national_epic_l_icon.set_colorkey((255,0,255))
volcanic_forge_icon=pygame.image.load("volcanic_forge.bmp").convert()
volcanic_forge_icon=pygame.transform.scale(volcanic_forge_icon, (75, 75))
volcanic_forge_icon.set_colorkey((255,0,255))
national_treasury_icon=pygame.image.load("national_treasury.bmp").convert()
national_treasury_icon=pygame.transform.scale(national_treasury_icon, (75, 75))
national_treasury_icon.set_colorkey((255,0,255))
stronghold_icon=pygame.image.load("stronghold.bmp").convert()
stronghold_icon=pygame.transform.scale(stronghold_icon, (75, 75))
stronghold_icon.set_colorkey((255,0,255))
continental_gardens_icon=pygame.image.load("continental_gardens.bmp").convert()
continental_gardens_icon=pygame.transform.scale(continental_gardens_icon, (75, 75))
continental_gardens_icon.set_colorkey((255,0,255))
heroic_tribute_icon=pygame.image.load("heroic_tribute.bmp").convert()
heroic_tribute_icon=pygame.transform.scale(heroic_tribute_icon, (75, 75))
heroic_tribute_icon.set_colorkey((255,0,255))
academy_of_art_icon=pygame.image.load("academy_of_art.bmp").convert()
academy_of_art_icon=pygame.transform.scale(academy_of_art_icon, (75, 75))
academy_of_art_icon.set_colorkey((255,0,255))

#Creates the icons for the other buildings
os.chdir(img_dirr+"/village/buildings/other")
house_icon=pygame.image.load("house.bmp").convert()
house_icon=pygame.transform.scale(house_icon, (75, 75))
house_icon.set_colorkey((255,0,255))
cater_icon=pygame.image.load("cater.bmp").convert()
cater_icon=pygame.transform.scale(cater_icon, (75, 75))
cater_icon.set_colorkey((255,0,255))

#Defines the Unique_Building objects
colosseum=classes.Unique_Building("colosseum", img_dirr, colosseum_icon, helvet)
mystical_shrine=classes.Unique_Building("mystical_shrine", img_dirr, mystical_shrine_icon, helvet)
gambling_house=classes.Unique_Building("gambling_house", img_dirr, gambling_house_icon, helvet)
chapel=classes.Unique_Building("chapel", img_dirr, chapel_icon, helvet)
jousting_league=classes.Unique_Building("jousting_league", img_dirr, jousting_league_icon, helvet)
hunting_grounds=classes.Unique_Building("hunting_grounds", img_dirr, hunting_grounds_icon, helvet)
pegasus_olympics=classes.Unique_Building("pegasus_olympics", img_dirr, pegasus_olympics_icon, helvet)
national_epic_s=classes.Unique_Building("national_epic_(s)", img_dirr, national_epic_s_icon, helvet)
national_epic_m=classes.Unique_Building("national_epic_(m)", img_dirr, national_epic_m_icon, helvet)
national_epic_l=classes.Unique_Building("national_epic_(l)", img_dirr, national_epic_l_icon, helvet)
volcanic_forge=classes.Unique_Building("volcanic_forge", img_dirr, volcanic_forge_icon, helvet)
national_treasury=classes.Unique_Building("national_treasury", img_dirr, national_treasury_icon, helvet)
stronghold=classes.Unique_Building("stronghold", img_dirr, stronghold_icon, helvet)
continental_gardens=classes.Unique_Building("continental_gardens", img_dirr, continental_gardens_icon, helvet)
heroic_tribute=classes.Unique_Building("heroic_tribute", img_dirr, heroic_tribute_icon, helvet)
academy_of_art=classes.Unique_Building("academy_of_art", img_dirr, academy_of_art_icon, helvet)

building_name_font=pygame.font.Font(helvet, 12)
turns_to_build_font=pygame.font.Font(helvet, 10)
#Defines the level 1, 2, and 3 buildings as Buildings_In_To_Build objects
workshop_to_build=classes.Buildings_In_To_Build(workshop_icon, 127, 1, "workshop", helvet, "production building", ["Production +5"], 1, "None")
stone_works_to_build=classes.Buildings_In_To_Build(stone_works_icon, 147, 2, "stone_works", helvet, "production building", ["Production +5"], 1, "Build the Workshop and 2 other Level 1 Buildings")
forge_to_build=classes.Buildings_In_To_Build(forge_icon, 167, 3, "forge", helvet, "production building", ["Production +10"], 1, "Build the Stone Works and 2 other Level 2 Buildings")
market_place_to_build=classes.Buildings_In_To_Build(market_place_icon, 159, 1, "market_place", helvet, "gold building", ["Gold per Turn +5"], 0, "None")
trading_post_to_build=classes.Buildings_In_To_Build(trading_post_icon, 179, 2, "trading_post", helvet, "gold building", ["Gold per Turn +15"], 0, "Build a Market Place and 2 other Level 1 Buildings")
trade_network_to_build=classes.Buildings_In_To_Build(trade_network_icon, 199, 3, "trade_network", helvet, "gold building", ["Gold per Turn +25"], 0, "Build a Trading Post and 2 other Level 2 Buildings")
walls_to_build=classes.Buildings_In_To_Build(walls_icon, 191, 1, "walls", helvet, "defence building", ["Defence +10"], 1, "None")
watchtower_to_build=classes.Buildings_In_To_Build(watchtower_icon, 211, 2, "watchtower", helvet, "defence building", ["Defence +20"], 1, "Build Walls and 2 other Level 1 Buildings")
castle_to_build=classes.Buildings_In_To_Build(castle_icon, 231, 3, "castle", helvet, "defence building", ["Defence +30"], 1, "Build a Watchtower and 2 other Level 2 Buildings")
wheat_feild_to_build=classes.Buildings_In_To_Build(wheat_feild_icon, 223, 1, "wheat_feild", helvet, "food building", ["Food +10"], 1, "None")
farm_to_build=classes.Buildings_In_To_Build(farm_icon, 243, 2, "farm", helvet, "food building", ["Food +15"], 1, "Build a Wheat Feild and 2 other Level 1 Buildings")
granary_to_build=classes.Buildings_In_To_Build(granary_icon, 263, 3, "granary", helvet, "food building", ["Food +20"], 1, "Build a Farm and 2 other Level 2 Buildings")
garden_to_build=classes.Buildings_In_To_Build(garden_icon, 255, 1, "garden", helvet, "favor building", ["Favor +5"], 1, "None")
inn_to_build=classes.Buildings_In_To_Build(inn_icon, 275, 2, "inn", helvet, "favor building", ["Favor +5"], 1, "Build a Garden and 2 other Level 1 Buildings")
theater_to_build=classes.Buildings_In_To_Build(theater_icon, 295, 3, "theater", helvet, "favor building", ["Favor +5"], 1, "Build an Inn and 2 other Level 2 Buildings")
monument_to_build=classes.Buildings_In_To_Build(monument_icon, 287, 1, "monument", helvet, "happiness building", ["Happiness +4"], 1, "None")
library_to_build=classes.Buildings_In_To_Build(library_icon, 307, 2, "library", helvet, "happiness building", ["Happiness +4"], 1, "Build the Monument and 2 other Level 1 Buildings")
circus_to_build=classes.Buildings_In_To_Build(circus_icon, 327, 3, "circus", helvet, "happiness building", ["Happiness +4"], 1, "Build a Library and 2 other Level 2 Buildings")

#Defines the hero buildings as Buildings_In_To_Build objects
barracks_to_build=classes.Buildings_In_To_Build(barracks_icon, 187, 0, "barracks", helvet, "hero building", ["Favor with Warrior +25"], 1, "Build a Garden")
arcane_academy_to_build=classes.Buildings_In_To_Build(arcane_academy_icon, 219, 0, "arcane_academy", helvet, "hero building", ["Favor with Mage +25"], 1, "Build a Garden")
pub_to_build=classes.Buildings_In_To_Build(pub_icon, 251, 0, "pub", helvet, "hero building", ["Favor with Rogue +25"], 1, "Build a Garden")
church_to_build=classes.Buildings_In_To_Build(church_icon, 283, 0, "church", helvet, "hero building", ["Favor with Priest +25"], 1, "Build a Garden")
armory_to_build=classes.Buildings_In_To_Build(armory_icon, 315, 0, "armory", helvet, "hero building", ["Favor with Knight +25"], 1, "Build a Garden")
shooting_range_to_build=classes.Buildings_In_To_Build(shooting_range_icon, 347, 0, "shooting_range", helvet, "hero building", ["Favor with Archer +25"], 1, "Build a Garden")
stable_to_build=classes.Buildings_In_To_Build(stable_icon, 379, 0, "stable", helvet, "hero building", ["Favor with Pegasus Knight +25"], 1, "Build a Garden")


#Defines the unique buildings as Buildings_In_To_Build objects
colosseum_to_build=classes.Buildings_In_To_Build(colosseum_icon, 207, 0, "colosseum", helvet, "unique building", ["Favor with Warrior +20"], 0, "Build an Inn and obtain more then {} Favor with the Warrior".format(classes.Hero.FavorForAlly), colosseum)
mystical_shrine_to_build=classes.Buildings_In_To_Build(mystical_shrine_icon, 239, 0, "mystical_shrine", helvet, "unique building", ["Favor with Mage +20"], 0, "Build an Inn and obtain more then {} Favor with the Mage".format(classes.Hero.FavorForAlly), mystical_shrine)
gambling_house_to_build=classes.Buildings_In_To_Build(gambling_house_icon, 271, 0, "gambling_house", helvet, "unique building", ["Favor with Rogue +20"], 0, "Build an Inn and obtain more then {} Favor with the Rogue".format(classes.Hero.FavorForAlly), gambling_house)
chapel_to_build=classes.Buildings_In_To_Build(chapel_icon, 303, 0, "chapel", helvet, "unique building", ["Favor with Priest +20"], 0, "Build an Inn and obtain more then {} Favor with the Priest".format(classes.Hero.FavorForAlly), chapel)
jousting_league_to_build=classes.Buildings_In_To_Build(jousting_league_icon, 335, 0, "jousting_league", helvet, "unique building", ["Favor with Knight +20"], 0, "Build an Inn and obtain more then {} Favor with the Knight".format(classes.Hero.FavorForAlly), jousting_league)
hunting_grounds_to_build=classes.Buildings_In_To_Build(hunting_grounds_icon, 367, 0, "hunting_grounds", helvet, "unique building", ["Favor with Archer +20"], 0, "Build an Inn and obtain more then {} Favor with the Archer".format(classes.Hero.FavorForAlly), hunting_grounds)
pegasus_olympics_to_build=classes.Buildings_In_To_Build(pegasus_olympics_icon, 399, 0, "pegasus_olympics", helvet, "unique building", ["Favor with Pegasus Knight +20"], 0, "Build an Inn and obtain more then {} Favor with the Pegasus Knight".format(classes.Hero.FavorForAlly), pegasus_olympics)
national_epic_s_to_build=classes.Buildings_In_To_Build(national_epic_s_icon, 431, 0, "national_epic_(s)", helvet, "unique building", ["Production +3", "Gold per Turn +5", "Defence +5", "Food +5", "Favor +2", "Happiness +2"], 0, "Build all Level 1 Buildings", national_epic_s)
national_epic_m_to_build=classes.Buildings_In_To_Build(national_epic_m_icon, 463, 0, "national_epic_(m)", helvet, "unique building", ["Production +3", "Gold per Turn +5", "Defence +5", "Food +5", "Favor +2", "Happiness +2"], 0, "Build all Level 2 Buildings", national_epic_m)
national_epic_l_to_build=classes.Buildings_In_To_Build(national_epic_l_icon, 495, 0, "national_epic_(l)", helvet, "unique building", ["Production +3", "Gold per Turn +5", "Defence +5", "Food +5", "Favor +2", "Happiness +2"], 0, "Build all Level 3 Buildings", national_epic_l)
volcanic_forge_to_build=classes.Buildings_In_To_Build(volcanic_forge_icon, 527, 0, "volcanic_forge", helvet, "unique building", ["Production +10"], 0, "Build the Workshop, the Stone Works, and a Forge", volcanic_forge)
national_treasury_to_build=classes.Buildings_In_To_Build(national_treasury_icon, 559, 0, "national_treasury", helvet, "unique building", ["Gold Per Turn +35"], 0, "Build a Market Place, a Trading Post, and a Trade Network", national_treasury)
stronghold_to_build=classes.Buildings_In_To_Build(stronghold_icon, 591, 0, "stronghold", helvet, "unique building", ["Defence +50"], 0, "Build Walls, a Watchtower, and a Castle", stronghold)
continental_gardens_to_build=classes.Buildings_In_To_Build(continental_gardens_icon, 623, 0, "continental_gardens", helvet, "unique building", ["Food +30"], 0, "Build a Wheat Feild, a Farm, and a Grannary", continental_gardens)
heroic_tribute_to_build=classes.Buildings_In_To_Build(heroic_tribute_icon, 655, 0, "heroic_tribute", helvet, "unique building", ["Favor +5"], 0, "Build a Garden, an Inn, and a theater", heroic_tribute)
academy_of_art_to_build=classes.Buildings_In_To_Build(academy_of_art_icon, 687, 0, "academy_of_art", helvet, "unique building", ["Happiness +16"], 0, "Build a Monument, a Library, and a Circus", academy_of_art)

#Defines the other buildings as Buildings_In_To_Build objects
house_to_build=classes.Buildings_In_To_Build(house_icon, 227, 0, "house", helvet, "other building", ["Houses +1"], 0, "None")
cater_to_build=classes.Buildings_In_To_Build(cater_icon, 259, 0, "cater_to_a_hero", helvet, "other building", ["Favor with 1 Hero +10"], 0, "None")

to_build_list=[workshop_to_build, market_place_to_build, walls_to_build, wheat_feild_to_build, garden_to_build, monument_to_build, stone_works_to_build, trading_post_to_build, watchtower_to_build, farm_to_build, inn_to_build, library_to_build, forge_to_build, trade_network_to_build, castle_to_build, granary_to_build, theater_to_build, circus_to_build, barracks_to_build, arcane_academy_to_build, pub_to_build, church_to_build, armory_to_build, shooting_range_to_build, stable_to_build, colosseum_to_build, mystical_shrine_to_build, gambling_house_to_build, chapel_to_build, jousting_league_to_build, hunting_grounds_to_build, pegasus_olympics_to_build, national_epic_s_to_build, national_epic_m_to_build, national_epic_l_to_build, volcanic_forge_to_build, national_treasury_to_build, stronghold_to_build, continental_gardens_to_build, heroic_tribute_to_build, academy_of_art_to_build, house_to_build, cater_to_build]
to_build_group=pygame.sprite.Group(to_build_list)

clear_to_build_tab=pygame.Surface((79, 14)).convert() 
clear_to_build_tab.fill((0,0,0))

#Creates various Rects and images to be displayed on screen
os.chdir(img_dirr+"/menu")

#Creates images for the menus
menu_font=pygame.font.Font(helvet, 16)
title_background=pygame.image.load("title_background.bmp").convert()
title_background=pygame.transform.scale(title_background, size)

title_main_menu=pygame.image.load("title_main_menu.bmp").convert()
title_main_menu=pygame.transform.scale(title_main_menu, (300, 370))
title_main_menu.set_colorkey((255,0,255))
title_main_menu_rect=title_main_menu.get_rect()
title_main_menu_rect.centerx=size[0]/2
title_main_menu_rect.centery=(size[1]/2)+10

menu_divider=pygame.Surface((150,3)).convert()
menu_divider.fill((23,50,57))    

set_up_game_button=pygame.Surface((200,30)).convert()
set_up_game_button.fill((0,0,0)) 
set_up_game_button.set_alpha(0)
set_up_game_button_rect=set_up_game_button.get_rect()
set_up_game_button_rect.centerx=size[0]/2
set_up_game_button_rect.centery=164
set_up_game_text=menu_font.render("Set Up Game", True, (255,255,255))
set_up_game_text_rect=set_up_game_text.get_rect()
set_up_game_text_rect.centerx=set_up_game_button_rect.centerx
set_up_game_text_rect.centery=set_up_game_button_rect.centery

how_to_play_button=pygame.Surface((200,30)).convert()
how_to_play_button.fill((0,0,0)) 
how_to_play_button.set_alpha(0)
how_to_play_button_rect=how_to_play_button.get_rect()
how_to_play_button_rect.centerx=size[0]/2
how_to_play_button_rect.centery=194
how_to_play_text=menu_font.render("How To Play", True, (255,255,255))
how_to_play_text_rect=how_to_play_text.get_rect()
how_to_play_text_rect.centerx=how_to_play_button_rect.centerx
how_to_play_text_rect.centery=how_to_play_button_rect.centery

quit_button=pygame.Surface((200,30)).convert()
quit_button.fill((0,0,0)) 
quit_button.set_alpha(0)
quit_button_rect=quit_button.get_rect()
quit_button_rect.centerx=size[0]/2
quit_button_rect.centery=224
quit_text=menu_font.render("Quit", True, (255,255,255))
quit_text_rect=quit_text.get_rect()
quit_text_rect.centerx=quit_button_rect.centerx
quit_text_rect.centery=quit_button_rect.centery

        
set_up_menu=pygame.image.load("title_set_up_menu.bmp").convert()
set_up_menu=pygame.transform.scale(set_up_menu, (500, 420))
set_up_menu.set_colorkey((255,0,255))
set_up_menu_rect=set_up_menu.get_rect()
set_up_menu_rect.centerx=size[0]/2
set_up_menu_rect.centery=size[1]/2

players_text_set_up=menu_font.render("Players:", True, (255,255,255))
add_player_icon=pygame.image.load("add_player_icon.bmp").convert()
add_player_icon.set_colorkey((255,0,255))
add_player_icon_rect=add_player_icon.get_rect()
add_player_icon_rect.centerx=245
add_player_icon_rect.centery=115

remove_player_icon=pygame.image.load("remove_player_icon.bmp").convert()
remove_player_icon.set_colorkey((255,0,255))
remove_player_icon_rect=remove_player_icon.get_rect()
remove_player_icon_rect.centerx=245
remove_player_icon_rect.centery=125
    
start_game_text=menu_font.render("Start Game", True, (255,255,255))
start_game_button=pygame.image.load("button.bmp").convert()
start_game_button.set_colorkey((255,0,255))
start_game_button=pygame.transform.scale(start_game_button, (90, 25))
start_game_button_rect=start_game_button.get_rect()
start_game_button_rect.centerx=375
start_game_button_rect.centery=117
start_game_button.blit(start_game_text, (5, 5))

back_text=menu_font.render("Back", True, (255,255,255))
set_up_back_button=pygame.image.load("button.bmp").convert()
set_up_back_button.set_colorkey((255,0,255))
set_up_back_button=pygame.transform.scale(set_up_back_button, (90, 25))
set_up_back_button_rect=set_up_back_button.get_rect()
set_up_back_button_rect.centerx=500
set_up_back_button_rect.centery=117
set_up_back_button.blit(back_text, (5, 5))

set_up_menu_divider=pygame.Surface((480,2)).convert()
set_up_menu_divider.fill((252,238,197))

edit_name_outline=pygame.image.load("edit_name_outline.bmp").convert()
edit_name_outline.set_colorkey((255,0,255))

ai_check_box_font=pygame.font.Font(helvet, 13)
edit_name_buttons=[]
make_ai_buttons=[]
ai_check_box_empty=pygame.image.load("check_box_empty.bmp").convert()
ai_check_box_empty=pygame.transform.scale(ai_check_box_empty, (10,10))
ai_check_box_empty.set_colorkey((255,0,255))
ai_check_box_checked=pygame.image.load("check_box_checked.bmp").convert()
ai_check_box_checked=pygame.transform.scale(ai_check_box_checked, (10,10))
ai_check_box_checked.set_colorkey((255,0,255))
change_ai_level_buttons=[]
for i in range(0,10):
    #Makes the button that makes a player AI or human
    temp_surface=pygame.image.load("edit_name_icon.bmp").convert()
    temp_surface=pygame.transform.scale(temp_surface, (10,10))
    temp_surface.set_colorkey((255,0,255))
    temp_rect=temp_surface.get_rect()
    edit_name_buttons+=[[temp_surface, temp_rect]]
    temp_surface=ai_check_box_empty
    temp_rect=temp_surface.get_rect()
    make_ai_buttons+=[[temp_surface, temp_rect]]
    
    #Makes the arrows for choosing a town's AI difficulty level
    temp_surface_1=pygame.image.load("change_ai_level_left.bmp").convert()
    temp_surface_1=pygame.transform.scale(temp_surface_1, (10,10))
    temp_surface_1.set_colorkey((255,0,255))
    temp_rect_1=temp_surface_1.get_rect()
    temp_surface_2=pygame.image.load("change_ai_level_right.bmp").convert()
    temp_surface_2=pygame.transform.scale(temp_surface_2, (10,10))
    temp_surface_2.set_colorkey((255,0,255))
    temp_rect_2=temp_surface_2.get_rect()
    change_ai_level_buttons+=[[[temp_surface_1, temp_rect_1],[temp_surface_2, temp_rect_2]]]
    
    

#Creates the tabs and content for the How To Play menu

tab_bottom_line=pygame.Surface((471,1)).convert()
tab_bottom_line.fill((218,185,128))

tab_font=pygame.font.Font(helvet, 12)

tab_back=pygame.image.load("folder_tab_back.bmp").convert()
tab_back.set_colorkey((255,0,255))
tab_front=pygame.image.load("folder_tab_front.bmp").convert()
tab_front.set_colorkey((255,0,255))
surface_for_info_text=pygame.Surface((461, 1)).convert()
info_text_font=pygame.font.Font(helvet, 12)

os.chdir(how_to_play_text_dirr)

#Creates the content in the General tab
os.chdir(how_to_play_text_dirr+"/general")
general_text=tab_font.render("General", True, (255,255,255))
general_tab_back=pygame.transform.scale(tab_back, (general_text.get_size()[0]+8,22))
general_tab_front=pygame.transform.scale(tab_front, (general_tab_back.get_size()[0]-2,general_tab_back.get_size()[1]-1))
general_tab_back.blit(general_tab_front, (1,1))
general_tab_rect=general_tab_back.get_rect()
general_tab_rect.left=85
general_tab_rect.top=102
general_tab_back.blit(general_text, (general_tab_back.get_size()[0]/2-(general_text.get_size()[0]/2), general_tab_back.get_size()[1]/2-(general_text.get_size()[1]/2)))

general_context_text=tab_font.render("Context", True, (255,255,255))
general_context_tab_back=pygame.transform.scale(tab_back, (general_context_text.get_size()[0]+8,22))
general_context_tab_front=pygame.transform.scale(tab_front, (general_context_tab_back.get_size()[0]-2,general_context_tab_back.get_size()[1]-1))
general_context_tab_back.blit(general_context_tab_front, (1,1))
general_context_tab_rect=general_context_tab_back.get_rect()
general_context_tab_rect.left=85
general_context_tab_rect.top=125
general_context_tab_back.blit(general_context_text, (general_context_tab_back.get_size()[0]/2-(general_context_text.get_size()[0]/2), general_context_tab_back.get_size()[1]/2-(general_context_text.get_size()[1]/2)))
general_context_info_text=functions.fit_text_to_box(open(r"context.txt").read(), surface_for_info_text, info_text_font)

general_playing_text=tab_font.render("Playing", True, (255,255,255))
general_playing_tab_back=pygame.transform.scale(tab_back, (general_playing_text.get_size()[0]+8,22))
general_playing_tab_front=pygame.transform.scale(tab_front, (general_playing_tab_back.get_size()[0]-2,general_playing_tab_back.get_size()[1]-1))
general_playing_tab_back.blit(general_playing_tab_front, (1,1))
general_playing_tab_rect=general_playing_tab_back.get_rect()
general_playing_tab_rect.left=general_context_tab_rect.right+1
general_playing_tab_rect.top=125
general_playing_tab_back.blit(general_playing_text, (general_playing_tab_back.get_size()[0]/2-(general_playing_text.get_size()[0]/2), general_playing_tab_back.get_size()[1]/2-(general_playing_text.get_size()[1]/2)))
general_playing_info_text=functions.fit_text_to_box(open(r"playing.txt").read(), surface_for_info_text, info_text_font)

general_heroes_text=tab_font.render("Heroes", True, (255,255,255))
general_heroes_tab_back=pygame.transform.scale(tab_back, (general_heroes_text.get_size()[0]+8,22))
general_heroes_tab_front=pygame.transform.scale(tab_front, (general_heroes_tab_back.get_size()[0]-2,general_heroes_tab_back.get_size()[1]-1))
general_heroes_tab_back.blit(general_heroes_tab_front, (1,1))
general_heroes_tab_rect=general_heroes_tab_back.get_rect()
general_heroes_tab_rect.left=general_playing_tab_rect.right+1
general_heroes_tab_rect.top=125
general_heroes_tab_back.blit(general_heroes_text, (general_heroes_tab_back.get_size()[0]/2-(general_heroes_text.get_size()[0]/2), general_heroes_tab_back.get_size()[1]/2-(general_heroes_text.get_size()[1]/2)))
general_heroes_info_text=functions.fit_text_to_box(open(r"heroes.txt").read(), surface_for_info_text, info_text_font)

general_winning_text=tab_font.render("Winning", True, (255,255,255))
general_winning_tab_back=pygame.transform.scale(tab_back, (general_winning_text.get_size()[0]+8,22))
general_winning_tab_front=pygame.transform.scale(tab_front, (general_winning_tab_back.get_size()[0]-2,general_winning_tab_back.get_size()[1]-1))
general_winning_tab_back.blit(general_winning_tab_front, (1,1))
general_winning_tab_rect=general_winning_tab_back.get_rect()
general_winning_tab_rect.left=general_heroes_tab_rect.right+1
general_winning_tab_rect.top=125
general_winning_tab_back.blit(general_winning_text, (general_winning_tab_back.get_size()[0]/2-(general_winning_text.get_size()[0]/2), general_winning_tab_back.get_size()[1]/2-(general_heroes_text.get_size()[1]/2)))
general_winning_info_text=functions.fit_text_to_box(open(r"winning.txt").read(), surface_for_info_text, info_text_font)

general_the_dragon_text=tab_font.render("The Dragon", True, (255,255,255))
general_the_dragon_tab_back=pygame.transform.scale(tab_back, (general_the_dragon_text.get_size()[0]+8,22))
general_the_dragon_tab_front=pygame.transform.scale(tab_front, (general_the_dragon_tab_back.get_size()[0]-2,general_the_dragon_tab_back.get_size()[1]-1))
general_the_dragon_tab_back.blit(general_the_dragon_tab_front, (1,1))
general_the_dragon_tab_rect=general_the_dragon_tab_back.get_rect()
general_the_dragon_tab_rect.left=general_winning_tab_rect.right+1
general_the_dragon_tab_rect.top=125
general_the_dragon_tab_back.blit(general_the_dragon_text, (general_the_dragon_tab_back.get_size()[0]/2-(general_the_dragon_text.get_size()[0]/2), general_the_dragon_tab_back.get_size()[1]/2-(general_the_dragon_text.get_size()[1]/2)))
general_the_dragon_info_text=functions.fit_text_to_box(open(r"the_dragon.txt").read(), surface_for_info_text, info_text_font)


#Creates the content in the Stats tab
os.chdir(how_to_play_text_dirr+"/stats")
stats_text=tab_font.render("Stats", True, (255,255,255))
stats_tab_back=pygame.transform.scale(tab_back, (stats_text.get_size()[0]+8,22))
stats_tab_front=pygame.transform.scale(tab_front, (stats_tab_back.get_size()[0]-2,stats_tab_back.get_size()[1]-1))
stats_tab_back.blit(stats_tab_front, (1,1))
stats_tab_rect=stats_tab_back.get_rect()
stats_tab_rect.left=general_tab_rect.right+1
stats_tab_rect.top=102
stats_tab_back.blit(stats_text, (stats_tab_back.get_size()[0]/2-(stats_text.get_size()[0]/2), stats_tab_back.get_size()[1]/2-(stats_text.get_size()[1]/2)))

stats_production_text=tab_font.render("Production", True, (255,255,255))
stats_production_tab_back=pygame.transform.scale(tab_back, (stats_production_text.get_size()[0]+8,22))
stats_production_tab_front=pygame.transform.scale(tab_front, (stats_production_tab_back.get_size()[0]-2,stats_production_tab_back.get_size()[1]-1))
stats_production_tab_back.blit(stats_production_tab_front, (1,1))
stats_production_tab_rect=stats_production_tab_back.get_rect()
stats_production_tab_rect.left=85
stats_production_tab_rect.top=125
stats_production_tab_back.blit(stats_production_text, (stats_production_tab_back.get_size()[0]/2-(stats_production_text.get_size()[0]/2), stats_production_tab_back.get_size()[1]/2-(stats_production_text.get_size()[1]/2)))
stats_production_info_text=functions.fit_text_to_box(open(r"production.txt").read(), surface_for_info_text, info_text_font)

stats_gold_text=tab_font.render("Gold", True, (255,255,255))
stats_gold_tab_back=pygame.transform.scale(tab_back, (stats_gold_text.get_size()[0]+8,22))
stats_gold_tab_front=pygame.transform.scale(tab_front, (stats_gold_tab_back.get_size()[0]-2,stats_gold_tab_back.get_size()[1]-1))
stats_gold_tab_back.blit(stats_gold_tab_front, (1,1))
stats_gold_tab_rect=stats_gold_tab_back.get_rect()
stats_gold_tab_rect.left=stats_production_tab_rect.right+1
stats_gold_tab_rect.top=125
stats_gold_tab_back.blit(stats_gold_text, (stats_gold_tab_back.get_size()[0]/2-(stats_gold_text.get_size()[0]/2), stats_gold_tab_back.get_size()[1]/2-(stats_gold_text.get_size()[1]/2)))
stats_gold_info_text=functions.fit_text_to_box(open(r"gold.txt").read(), surface_for_info_text, info_text_font)

stats_defence_text=tab_font.render("Defence", True, (255,255,255))
stats_defence_tab_back=pygame.transform.scale(tab_back, (stats_defence_text.get_size()[0]+8,22))
stats_defence_tab_front=pygame.transform.scale(tab_front, (stats_defence_tab_back.get_size()[0]-2,stats_defence_tab_back.get_size()[1]-1))
stats_defence_tab_back.blit(stats_defence_tab_front, (1,1))
stats_defence_tab_rect=stats_defence_tab_back.get_rect()
stats_defence_tab_rect.left=stats_gold_tab_rect.right+1
stats_defence_tab_rect.top=125
stats_defence_tab_back.blit(stats_defence_text, (stats_defence_tab_back.get_size()[0]/2-(stats_defence_text.get_size()[0]/2), stats_defence_tab_back.get_size()[1]/2-(stats_defence_text.get_size()[1]/2)))
stats_defence_info_text=functions.fit_text_to_box(open(r"defence.txt").read(), surface_for_info_text, info_text_font)

stats_food_text=tab_font.render("Food", True, (255,255,255))
stats_food_tab_back=pygame.transform.scale(tab_back, (stats_food_text.get_size()[0]+8,22))
stats_food_tab_front=pygame.transform.scale(tab_front, (stats_food_tab_back.get_size()[0]-2,stats_food_tab_back.get_size()[1]-1))
stats_food_tab_back.blit(stats_food_tab_front, (1,1))
stats_food_tab_rect=stats_food_tab_back.get_rect()
stats_food_tab_rect.left=stats_defence_tab_rect.right+1
stats_food_tab_rect.top=125
stats_food_tab_back.blit(stats_food_text, (stats_food_tab_back.get_size()[0]/2-(stats_food_text.get_size()[0]/2), stats_food_tab_back.get_size()[1]/2-(stats_food_text.get_size()[1]/2)))
stats_food_info_text=functions.fit_text_to_box(open(r"food.txt").read(), surface_for_info_text, info_text_font)

stats_favor_text=tab_font.render("Favor", True, (255,255,255))
stats_favor_tab_back=pygame.transform.scale(tab_back, (stats_favor_text.get_size()[0]+8,22))
stats_favor_tab_front=pygame.transform.scale(tab_front, (stats_favor_tab_back.get_size()[0]-2,stats_favor_tab_back.get_size()[1]-1))
stats_favor_tab_back.blit(stats_favor_tab_front, (1,1))
stats_favor_tab_rect=stats_favor_tab_back.get_rect()
stats_favor_tab_rect.left=stats_food_tab_rect.right+1
stats_favor_tab_rect.top=125
stats_favor_tab_back.blit(stats_favor_text, (stats_favor_tab_back.get_size()[0]/2-(stats_favor_text.get_size()[0]/2), stats_favor_tab_back.get_size()[1]/2-(stats_favor_text.get_size()[1]/2)))
stats_favor_info_text=functions.fit_text_to_box(open(r"favor.txt").read(), surface_for_info_text, info_text_font)

stats_happiness_text=tab_font.render("Happiness", True, (255,255,255))
stats_happiness_tab_back=pygame.transform.scale(tab_back, (stats_happiness_text.get_size()[0]+8,22))
stats_happiness_tab_front=pygame.transform.scale(tab_front, (stats_happiness_tab_back.get_size()[0]-2,stats_happiness_tab_back.get_size()[1]-1))
stats_happiness_tab_back.blit(stats_happiness_tab_front, (1,1))
stats_happiness_tab_rect=stats_happiness_tab_back.get_rect()
stats_happiness_tab_rect.left=stats_favor_tab_rect.right+1
stats_happiness_tab_rect.top=125
stats_happiness_tab_back.blit(stats_happiness_text, (stats_happiness_tab_back.get_size()[0]/2-(stats_happiness_text.get_size()[0]/2), stats_happiness_tab_back.get_size()[1]/2-(stats_happiness_text.get_size()[1]/2)))
stats_happiness_info_text=functions.fit_text_to_box(open(r"happiness.txt").read(), surface_for_info_text, info_text_font)

stats_population_text=tab_font.render("Population", True, (255,255,255))
stats_population_tab_back=pygame.transform.scale(tab_back, (stats_population_text.get_size()[0]+8,22))
stats_population_tab_front=pygame.transform.scale(tab_front, (stats_population_tab_back.get_size()[0]-2,stats_population_tab_back.get_size()[1]-1))
stats_population_tab_back.blit(stats_population_tab_front, (1,1))
stats_population_tab_rect=stats_population_tab_back.get_rect()
stats_population_tab_rect.left=stats_happiness_tab_rect.right+1
stats_population_tab_rect.top=125
stats_population_tab_back.blit(stats_population_text, (stats_population_tab_back.get_size()[0]/2-(stats_population_text.get_size()[0]/2), stats_population_tab_back.get_size()[1]/2-(stats_population_text.get_size()[1]/2)))
stats_population_info_text=functions.fit_text_to_box(open(r"population.txt").read(), surface_for_info_text, info_text_font)


#Creates the content in the Heroes tab
os.chdir(how_to_play_text_dirr+"/heroes")
heroes_text=tab_font.render("Heroes", True, (255,255,255))
heroes_tab_back=pygame.transform.scale(tab_back, (heroes_text.get_size()[0]+8,22))
heroes_tab_front=pygame.transform.scale(tab_front, (heroes_tab_back.get_size()[0]-2,heroes_tab_back.get_size()[1]-1))
heroes_tab_back.blit(heroes_tab_front, (1,1))
heroes_tab_rect=heroes_tab_back.get_rect()
heroes_tab_rect.left=stats_tab_rect.right+1
heroes_tab_rect.top=102
heroes_tab_back.blit(heroes_text, (heroes_tab_back.get_size()[0]/2-(heroes_text.get_size()[0]/2), heroes_tab_back.get_size()[1]/2-(heroes_text.get_size()[1]/2)))

heroes_warrior_text=tab_font.render("Warrior", True, (255,255,255))
heroes_warrior_tab_back=pygame.transform.scale(tab_back, (heroes_warrior_text.get_size()[0]+8,22))
heroes_warrior_tab_front=pygame.transform.scale(tab_front, (heroes_warrior_tab_back.get_size()[0]-2,heroes_warrior_tab_back.get_size()[1]-1))
heroes_warrior_tab_back.blit(heroes_warrior_tab_front, (1,1))
heroes_warrior_tab_rect=heroes_warrior_tab_back.get_rect()
heroes_warrior_tab_rect.left=85
heroes_warrior_tab_rect.top=125
heroes_warrior_tab_back.blit(heroes_warrior_text, (heroes_warrior_tab_back.get_size()[0]/2-(heroes_warrior_text.get_size()[0]/2), heroes_warrior_tab_back.get_size()[1]/2-(heroes_warrior_text.get_size()[1]/2)))
heroes_warrior_info_text=functions.fit_text_to_box(open(r"warrior.txt").read(), surface_for_info_text, info_text_font)

heroes_mage_text=tab_font.render("Mage", True, (255,255,255))
heroes_mage_tab_back=pygame.transform.scale(tab_back, (heroes_mage_text.get_size()[0]+8,22))
heroes_mage_tab_front=pygame.transform.scale(tab_front, (heroes_mage_tab_back.get_size()[0]-2,heroes_mage_tab_back.get_size()[1]-1))
heroes_mage_tab_back.blit(heroes_mage_tab_front, (1,1))
heroes_mage_tab_rect=heroes_mage_tab_back.get_rect()
heroes_mage_tab_rect.left=heroes_warrior_tab_rect.right+1
heroes_mage_tab_rect.top=125
heroes_mage_tab_back.blit(heroes_mage_text, (heroes_mage_tab_back.get_size()[0]/2-(heroes_mage_text.get_size()[0]/2), heroes_mage_tab_back.get_size()[1]/2-(heroes_mage_text.get_size()[1]/2)))
heroes_mage_info_text=functions.fit_text_to_box(open(r"mage.txt").read(), surface_for_info_text, info_text_font)

heroes_priest_text=tab_font.render("Priest", True, (255,255,255))
heroes_priest_tab_back=pygame.transform.scale(tab_back, (heroes_priest_text.get_size()[0]+8,22))
heroes_priest_tab_front=pygame.transform.scale(tab_front, (heroes_priest_tab_back.get_size()[0]-2,heroes_priest_tab_back.get_size()[1]-1))
heroes_priest_tab_back.blit(heroes_priest_tab_front, (1,1))
heroes_priest_tab_rect=heroes_priest_tab_back.get_rect()
heroes_priest_tab_rect.left=heroes_mage_tab_rect.right+1
heroes_priest_tab_rect.top=125
heroes_priest_tab_back.blit(heroes_priest_text, (heroes_priest_tab_back.get_size()[0]/2-(heroes_priest_text.get_size()[0]/2), heroes_priest_tab_back.get_size()[1]/2-(heroes_priest_text.get_size()[1]/2)))
heroes_priest_info_text=functions.fit_text_to_box(open(r"priest.txt").read(), surface_for_info_text, info_text_font)

heroes_rogue_text=tab_font.render("Rogue", True, (255,255,255))
heroes_rogue_tab_back=pygame.transform.scale(tab_back, (heroes_rogue_text.get_size()[0]+8,22))
heroes_rogue_tab_front=pygame.transform.scale(tab_front, (heroes_rogue_tab_back.get_size()[0]-2,heroes_rogue_tab_back.get_size()[1]-1))
heroes_rogue_tab_back.blit(heroes_rogue_tab_front, (1,1))
heroes_rogue_tab_rect=heroes_rogue_tab_back.get_rect()
heroes_rogue_tab_rect.left=heroes_priest_tab_rect.right+1
heroes_rogue_tab_rect.top=125
heroes_rogue_tab_back.blit(heroes_rogue_text, (heroes_rogue_tab_back.get_size()[0]/2-(heroes_rogue_text.get_size()[0]/2), heroes_rogue_tab_back.get_size()[1]/2-(heroes_rogue_text.get_size()[1]/2)))
heroes_rogue_info_text=functions.fit_text_to_box(open(r"rogue.txt").read(), surface_for_info_text, info_text_font)

heroes_knight_text=tab_font.render("Knight", True, (255,255,255))
heroes_knight_tab_back=pygame.transform.scale(tab_back, (heroes_knight_text.get_size()[0]+8,22))
heroes_knight_tab_front=pygame.transform.scale(tab_front, (heroes_knight_tab_back.get_size()[0]-2,heroes_knight_tab_back.get_size()[1]-1))
heroes_knight_tab_back.blit(heroes_knight_tab_front, (1,1))
heroes_knight_tab_rect=heroes_knight_tab_back.get_rect()
heroes_knight_tab_rect.left=heroes_rogue_tab_rect.right+1
heroes_knight_tab_rect.top=125
heroes_knight_tab_back.blit(heroes_knight_text, (heroes_knight_tab_back.get_size()[0]/2-(heroes_knight_text.get_size()[0]/2), heroes_knight_tab_back.get_size()[1]/2-(heroes_knight_text.get_size()[1]/2)))
heroes_knight_info_text=functions.fit_text_to_box(open(r"knight.txt").read(), surface_for_info_text, info_text_font)

heroes_archer_text=tab_font.render("Archer", True, (255,255,255))
heroes_archer_tab_back=pygame.transform.scale(tab_back, (heroes_archer_text.get_size()[0]+8,22))
heroes_archer_tab_front=pygame.transform.scale(tab_front, (heroes_archer_tab_back.get_size()[0]-2,heroes_archer_tab_back.get_size()[1]-1))
heroes_archer_tab_back.blit(heroes_archer_tab_front, (1,1))
heroes_archer_tab_rect=heroes_archer_tab_back.get_rect()
heroes_archer_tab_rect.left=heroes_knight_tab_rect.right+1
heroes_archer_tab_rect.top=125
heroes_archer_tab_back.blit(heroes_archer_text, (heroes_archer_tab_back.get_size()[0]/2-(heroes_archer_text.get_size()[0]/2), heroes_archer_tab_back.get_size()[1]/2-(heroes_archer_text.get_size()[1]/2)))
heroes_archer_info_text=functions.fit_text_to_box(open(r"archer.txt").read(), surface_for_info_text, info_text_font)

heroes_pegasus_knight_text=tab_font.render("Pegasus Knight", True, (255,255,255))
heroes_pegasus_knight_tab_back=pygame.transform.scale(tab_back, (heroes_pegasus_knight_text.get_size()[0]+8,22))
heroes_pegasus_knight_tab_front=pygame.transform.scale(tab_front, (heroes_pegasus_knight_tab_back.get_size()[0]-2,heroes_pegasus_knight_tab_back.get_size()[1]-1))
heroes_pegasus_knight_tab_back.blit(heroes_pegasus_knight_tab_front, (1,1))
heroes_pegasus_knight_tab_rect=heroes_pegasus_knight_tab_back.get_rect()
heroes_pegasus_knight_tab_rect.left=heroes_archer_tab_rect.right+1
heroes_pegasus_knight_tab_rect.top=125
heroes_pegasus_knight_tab_back.blit(heroes_pegasus_knight_text, (heroes_pegasus_knight_tab_back.get_size()[0]/2-(heroes_pegasus_knight_text.get_size()[0]/2), heroes_pegasus_knight_tab_back.get_size()[1]/2-(heroes_pegasus_knight_text.get_size()[1]/2)))
heroes_pegasus_knight_info_text=functions.fit_text_to_box(open(r"pegasus_knight.txt").read(), surface_for_info_text, info_text_font)

heroes_hero_quests_text=tab_font.render("Hero Quests", True, (255,255,255))
heroes_hero_quests_tab_back=pygame.transform.scale(tab_back, (heroes_hero_quests_text.get_size()[0]+8,22))
heroes_hero_quests_tab_front=pygame.transform.scale(tab_front, (heroes_hero_quests_tab_back.get_size()[0]-2,heroes_hero_quests_tab_back.get_size()[1]-1))
heroes_hero_quests_tab_back.blit(heroes_hero_quests_tab_front, (1,1))
heroes_hero_quests_tab_rect=heroes_hero_quests_tab_back.get_rect()
heroes_hero_quests_tab_rect.left=heroes_pegasus_knight_tab_rect.right+1
heroes_hero_quests_tab_rect.top=125
heroes_hero_quests_tab_back.blit(heroes_hero_quests_text, (heroes_hero_quests_tab_back.get_size()[0]/2-(heroes_hero_quests_text.get_size()[0]/2), heroes_hero_quests_tab_back.get_size()[1]/2-(heroes_hero_quests_text.get_size()[1]/2)))
heroes_hero_quests_info_text=functions.fit_text_to_box(open(r"hero_quests.txt").read(), surface_for_info_text, info_text_font)


#Creates the content in the Buildings tab
os.chdir(how_to_play_text_dirr+"/buildings")
buildings_text=tab_font.render("Buildings", True, (255,255,255))
buildings_tab_back=pygame.transform.scale(tab_back, (buildings_text.get_size()[0]+8,22))
buildings_tab_front=pygame.transform.scale(tab_front, (buildings_tab_back.get_size()[0]-2,buildings_tab_back.get_size()[1]-1))
buildings_tab_back.blit(buildings_tab_front, (1,1))
buildings_tab_rect=buildings_tab_back.get_rect()
buildings_tab_rect.left=heroes_tab_rect.right+1
buildings_tab_rect.top=102
buildings_tab_back.blit(buildings_text, (buildings_tab_back.get_size()[0]/2-(buildings_text.get_size()[0]/2), buildings_tab_back.get_size()[1]/2-(buildings_text.get_size()[1]/2)))

buildings_general_text=tab_font.render("General", True, (255,255,255))
buildings_general_tab_back=pygame.transform.scale(tab_back, (buildings_general_text.get_size()[0]+8,22))
buildings_general_tab_front=pygame.transform.scale(tab_front, (buildings_general_tab_back.get_size()[0]-2,buildings_general_tab_back.get_size()[1]-1))
buildings_general_tab_back.blit(buildings_general_tab_front, (1,1))
buildings_general_tab_rect=buildings_general_tab_back.get_rect()
buildings_general_tab_rect.left=85
buildings_general_tab_rect.top=125
buildings_general_tab_back.blit(buildings_general_text, (buildings_general_tab_back.get_size()[0]/2-(buildings_general_text.get_size()[0]/2), buildings_general_tab_back.get_size()[1]/2-(buildings_general_text.get_size()[1]/2)))
buildings_general_info_text=functions.fit_text_to_box(open(r"general.txt").read(), surface_for_info_text, info_text_font)

buildings_maintenance_text=tab_font.render("Maintenance", True, (255,255,255))
buildings_maintenance_tab_back=pygame.transform.scale(tab_back, (buildings_maintenance_text.get_size()[0]+8,22))
buildings_maintenance_tab_front=pygame.transform.scale(tab_front, (buildings_maintenance_tab_back.get_size()[0]-2,buildings_maintenance_tab_back.get_size()[1]-1))
buildings_maintenance_tab_back.blit(buildings_maintenance_tab_front, (1,1))
buildings_maintenance_tab_rect=buildings_maintenance_tab_back.get_rect()
buildings_maintenance_tab_rect.left=buildings_general_tab_rect.right+1
buildings_maintenance_tab_rect.top=125
buildings_maintenance_tab_back.blit(buildings_maintenance_text, (buildings_maintenance_tab_back.get_size()[0]/2-(buildings_maintenance_text.get_size()[0]/2), buildings_maintenance_tab_back.get_size()[1]/2-(buildings_maintenance_text.get_size()[1]/2)))
buildings_maintenance_info_text=functions.fit_text_to_box(open(r"maintenance.txt").read(), surface_for_info_text, info_text_font)

buildings_levels_1_2_3_text=tab_font.render("Levels 1,2,3", True, (255,255,255))
buildings_levels_1_2_3_tab_back=pygame.transform.scale(tab_back, (buildings_levels_1_2_3_text.get_size()[0]+8,22))
buildings_levels_1_2_3_tab_front=pygame.transform.scale(tab_front, (buildings_levels_1_2_3_tab_back.get_size()[0]-2,buildings_levels_1_2_3_tab_back.get_size()[1]-1))
buildings_levels_1_2_3_tab_back.blit(buildings_levels_1_2_3_tab_front, (1,1))
buildings_levels_1_2_3_tab_rect=buildings_levels_1_2_3_tab_back.get_rect()
buildings_levels_1_2_3_tab_rect.left=buildings_maintenance_tab_rect.right+1
buildings_levels_1_2_3_tab_rect.top=125
buildings_levels_1_2_3_tab_back.blit(buildings_levels_1_2_3_text, (buildings_levels_1_2_3_tab_back.get_size()[0]/2-(buildings_levels_1_2_3_text.get_size()[0]/2), buildings_levels_1_2_3_tab_back.get_size()[1]/2-(buildings_levels_1_2_3_text.get_size()[1]/2)))
buildings_levels_1_2_3_info_text=functions.fit_text_to_box(open(r"levels_1_2_3.txt").read(), surface_for_info_text, info_text_font)

buildings_hero_buildings_text=tab_font.render("Hero Buildings", True, (255,255,255))
buildings_hero_buildings_tab_back=pygame.transform.scale(tab_back, (buildings_hero_buildings_text.get_size()[0]+8,22))
buildings_hero_buildings_tab_front=pygame.transform.scale(tab_front, (buildings_hero_buildings_tab_back.get_size()[0]-2,buildings_hero_buildings_tab_back.get_size()[1]-1))
buildings_hero_buildings_tab_back.blit(buildings_hero_buildings_tab_front, (1,1))
buildings_hero_buildings_tab_rect=buildings_hero_buildings_tab_back.get_rect()
buildings_hero_buildings_tab_rect.left=buildings_levels_1_2_3_tab_rect.right+1
buildings_hero_buildings_tab_rect.top=125
buildings_hero_buildings_tab_back.blit(buildings_hero_buildings_text, (buildings_hero_buildings_tab_back.get_size()[0]/2-(buildings_hero_buildings_text.get_size()[0]/2), buildings_hero_buildings_tab_back.get_size()[1]/2-(buildings_hero_buildings_text.get_size()[1]/2)))
buildings_hero_buildings_info_text=functions.fit_text_to_box(open(r"hero_buildings.txt").read(), surface_for_info_text, info_text_font)

buildings_unique_text=tab_font.render("Unique", True, (255,255,255))
buildings_buildings_text=tab_font.render("Buildings", True, (255,255,255))
buildings_unique_buildings_tab_back=pygame.transform.scale(tab_back, (buildings_buildings_text.get_size()[0]+12,22))
buildings_unique_buildings_tab_front=pygame.transform.scale(tab_front, (buildings_unique_buildings_tab_back.get_size()[0]-2,buildings_unique_buildings_tab_back.get_size()[1]-1))
buildings_unique_buildings_tab_back.blit(buildings_unique_buildings_tab_front, (1,1))
buildings_unique_buildings_tab_rect=buildings_unique_buildings_tab_back.get_rect()
buildings_unique_buildings_tab_rect.left=buildings_hero_buildings_tab_rect.right+1
buildings_unique_buildings_tab_rect.top=125
buildings_unique_buildings_tab_back.blit(buildings_unique_text, (buildings_unique_buildings_tab_back.get_size()[0]/2-(buildings_unique_text.get_size()[0]/2), buildings_unique_buildings_tab_back.get_size()[1]/2-(buildings_unique_text.get_size()[1]/2)-5))
buildings_unique_buildings_tab_back.blit(buildings_buildings_text, (buildings_unique_buildings_tab_back.get_size()[0]/2-(buildings_buildings_text.get_size()[0]/2), buildings_unique_buildings_tab_back.get_size()[1]/2-(buildings_buildings_text.get_size()[1]/2)+5))
buildings_unique_buildings_info_text=functions.fit_text_to_box(open(r"unique_buildings.txt").read(), surface_for_info_text, info_text_font)

buildings_other_text=tab_font.render("Other", True, (255,255,255))
buildings_buildings_text=tab_font.render("Buildings", True, (255,255,255))
buildings_other_buildings_tab_back=pygame.transform.scale(tab_back, (buildings_buildings_text.get_size()[0]+12,22))
buildings_other_buildings_tab_front=pygame.transform.scale(tab_front, (buildings_other_buildings_tab_back.get_size()[0]-2,buildings_other_buildings_tab_back.get_size()[1]-1))
buildings_other_buildings_tab_back.blit(buildings_other_buildings_tab_front, (1,1))
buildings_other_buildings_tab_rect=buildings_other_buildings_tab_back.get_rect()
buildings_other_buildings_tab_rect.left=buildings_unique_buildings_tab_rect.right+1
buildings_other_buildings_tab_rect.top=125
buildings_other_buildings_tab_back.blit(buildings_other_text, (buildings_other_buildings_tab_back.get_size()[0]/2-(buildings_other_text.get_size()[0]/2), buildings_other_buildings_tab_back.get_size()[1]/2-(buildings_other_text.get_size()[1]/2)-5))
buildings_other_buildings_tab_back.blit(buildings_buildings_text, (buildings_other_buildings_tab_back.get_size()[0]/2-(buildings_buildings_text.get_size()[0]/2), buildings_other_buildings_tab_back.get_size()[1]/2-(buildings_buildings_text.get_size()[1]/2)+5))
buildings_other_buildings_info_text=functions.fit_text_to_box(open(r"other_buildings.txt").read(), surface_for_info_text, info_text_font)


selected_tab=0
selected_sub_tab=0
selected_tab_for_blit=general_tab_back
selected_tab_for_blit_rect=general_tab_rect
selected_sub_tab_for_blit=general_context_tab_back
selected_sub_tab_for_blit_rect=general_context_tab_rect
selected_info_text_for_blit=general_context_info_text


os.chdir(img_dirr+"/menu")
how_to_play_back_button=pygame.image.load("button.bmp").convert()
how_to_play_back_button.set_colorkey((255,0,255))
how_to_play_back_button=pygame.transform.scale(how_to_play_back_button, (90, 25))
how_to_play_back_button_rect=how_to_play_back_button.get_rect()
how_to_play_back_button_rect.centerx=500
how_to_play_back_button_rect.centery=402
how_to_play_back_button.blit(back_text, (5, 5))


#Creates UI for the screen that displays who won
winner_screen=title_main_menu
winner_screen_rect=winner_screen.get_rect()
winner_screen_rect.centerx=size[0]/2
winner_screen_rect.centery=size[1]/2

title_return_button=pygame.Surface((200,30)).convert()
title_return_button.fill((0,0,0)) 
title_return_button.set_alpha(0)
title_return_button_rect=title_return_button.get_rect()
title_return_button_rect.centerx=size[0]/2
title_return_button_rect.centery=370
title_return_text=menu_font.render("Ruturn to Tile", True, (255,255,255))
title_return_text_rect=title_return_text.get_rect()
title_return_text_rect.centerx=title_return_button_rect.centerx
title_return_text_rect.centery=title_return_button_rect.centery

players_left=0

#Creates various images for the user interface
next_turn=pygame.image.load("next_turn.bmp").convert()
next_turn=pygame.transform.scale(next_turn, (170, 26))
next_turn.set_colorkey((255,255,255))
next_turn_rect=next_turn.get_rect()
next_turn_rect.bottom=size[1]-80
next_turn_rect.right=size[0]-2

chouse_production_bar=pygame.image.load("chouse_production_next_turn.bmp").convert()
chouse_production_bar=pygame.transform.scale(chouse_production_bar, (170, 26))
chouse_production_bar.set_colorkey((255,255,255))
chouse_production_bar_rect=chouse_production_bar.get_rect()
chouse_production_bar_rect.bottom=size[1]-80
chouse_production_bar_rect.right=size[0]-2

bottom_section=pygame.image.load("bottom_section.bmp").convert()
bottom_section=pygame.transform.scale(bottom_section, (size[0], 80))
bottom_section.set_colorkey((255,255,255))
bottom_section_rect=bottom_section.get_rect()
bottom_section_rect.bottom=size[1]
bottom_section_rect.left=0

empty_production_wheel=pygame.image.load("empty_production_wheel.bmp").convert()
empty_production_wheel=pygame.transform.scale(empty_production_wheel, (77, 77))
empty_production_wheel.set_colorkey((255,0,255))
empty_wheel_rect=empty_production_wheel.get_rect()
empty_wheel_rect.bottom=size[1]
empty_wheel_rect.left=4

hammer=pygame.image.load("hammer.bmp").convert()
hammer.set_colorkey((255,0,255))
hammer=pygame.transform.scale(hammer, (57, 57))
hammer_small=pygame.transform.scale(hammer, (14, 14))

gold_coin=pygame.image.load("gold_coin.bmp").convert()
gold_coin=pygame.transform.scale(gold_coin, (14, 14))

defence_icon=pygame.image.load("defence_icon.bmp").convert()
defence_icon=pygame.transform.scale(defence_icon, (14, 14))

food_icon=pygame.image.load("food_icon.bmp").convert()
food_icon=pygame.transform.scale(food_icon, (14, 14))

favor_icon=pygame.image.load("favor_icon.bmp").convert()
favor_icon=pygame.transform.scale(favor_icon, (14, 14))

happiness_icon=pygame.image.load("happiness_icon.bmp").convert()
happiness_icon=pygame.transform.scale(happiness_icon, (14, 14))

population_icon=pygame.image.load("population_icon.bmp").convert()
population_icon=pygame.transform.scale(population_icon, (14, 14))

houses_icon=pygame.image.load("houses_icon.bmp").convert()
houses_icon=pygame.transform.scale(houses_icon, (14, 14))


hero_abilities_screen_up=False



bottom_button_font=pygame.font.Font(helvet, 15)

#Creates the images and objects used in the Hero Info screen
hero_info_button_text=bottom_button_font.render("Hero Info", True, (255,255,251))
hero_info_button=pygame.image.load("button.bmp").convert()
hero_info_button=pygame.transform.scale(hero_info_button, (100,25))
hero_info_button.set_colorkey(hero_info_button.get_at((0,0)))
hero_info_button_rect=hero_info_button.get_rect()
hero_info_button_rect.bottom=size[1]-40
hero_info_button_rect.left=175
hero_info_button.blit(hero_info_button_text, (20, 5))

exit_hero_info_button_text=bottom_button_font.render("Return To Map", True, (255,255,251))
exit_hero_info_button=pygame.image.load("button.bmp").convert()
exit_hero_info_button=pygame.transform.scale(exit_hero_info_button, (100,25))
exit_hero_info_button.set_colorkey(exit_hero_info_button.get_at((0,0)))
exit_hero_info_button_rect=exit_hero_info_button.get_rect()
exit_hero_info_button_rect.bottom=size[1]-83
exit_hero_info_button_rect.centerx=size[0]/2
exit_hero_info_button.blit(exit_hero_info_button_text, (5, 5))

hero_info_screen=pygame.image.load("hero_info_screen.bmp").convert()
hero_info_screen.set_colorkey((255,0,255))
hero_info_screen_rect=hero_info_screen.get_rect()
hero_info_screen_rect.top=30
hero_info_screen_rect.centerx=size[0]/2
hero_info_screen_up=False

hero_screen_clear=pygame.Surface((537,268)).convert()
hero_screen_clear.fill((0,0,0))   
hero_info_font=pygame.font.Font(helvet, 14)

hero_screen_divider_1=pygame.image.load("hero_screen_divider_1.bmp").convert()
hero_screen_divider_1=pygame.transform.scale(hero_screen_divider_1, (538,2))

hero_text=hero_info_font.render("Hero", True, (255,255,251))
name_text=hero_info_font.render("Name", True, (255,255,251))
class_text=hero_info_font.render("Class", True, (255,255,251))
favor_text=hero_info_font.render("Favor", True, (255,255,251))
modifier_text=hero_info_font.render("Modifier", True, (255,255,251))
turns_since_text=hero_info_font.render("Turns Since", True, (255,255,251))
last_visit_text=hero_info_font.render("Last Visit", True, (255,255,251))
favorite_text=hero_info_font.render("Favorite", True, (255,255,251))
town_text=hero_info_font.render("Town", True, (255,255,251))

hero_info_screen.blit(hero_text, (25,30))
hero_info_screen.blit(name_text, (73,30))
hero_info_screen.blit(class_text, (162,30))
hero_info_screen.blit(favor_text, (233,30))
hero_info_screen.blit(favor_text, (289,20))
hero_info_screen.blit(modifier_text, (282,40))
hero_info_screen.blit(turns_since_text, (350,20))
hero_info_screen.blit(last_visit_text, (357,40))
hero_info_screen.blit(favorite_text, (464,20))
hero_info_screen.blit(town_text, (471,40))
hero_info_screen.blit(hero_screen_divider_1, (22,60))
hero_info_screen=functions.update_hero_screen(towns[0], hero_info_screen, hero_screen_clear, hero_info_font, towns)



bottom_clear=pygame.Surface((size[0], 80)).convert()
bottom_clear.fill((0,0,0))

top_border=pygame.image.load("top_border.bmp").convert()
top_border=pygame.transform.scale(top_border, (size[0], 3))
top_border_rect=top_border.get_rect()
top_border_rect.left=0
top_border_rect.top=20

arrow=pygame.image.load("arrow.bmp").convert()
arrow=pygame.transform.scale(arrow, (20, 35))
arrow.set_colorkey((255,255,255))




#Creates the button to dismiss a notification message
dismiss_event_text=bottom_button_font.render("Close", True, (255,255,251))
dismiss_event_button=pygame.image.load("button.bmp").convert()
dismiss_event_button=pygame.transform.scale(dismiss_event_button, (100,25))
dismiss_event_button.set_colorkey(dismiss_event_button.get_at((0,0)))
dismiss_event_button_rect=dismiss_event_button.get_rect()
dismiss_event_button_rect.top=200
dismiss_event_button_rect.right=size[0]
dismiss_event_button.blit(dismiss_event_text, (5, 5))

#Creates the Rects and images needed for the menu of what the user can build
to_build_menu=pygame.image.load("to_build_menu.bmp").convert()
to_build_menu=pygame.transform.scale(to_build_menu, (130, 300))
to_build_menu.set_colorkey((255,255,255))
to_build_menu_rect=to_build_menu.get_rect()
to_build_menu_rect.left=0
to_build_menu_rect.bottom=size[1]-80
to_build_menu_up=False

to_build_menu_back=pygame.Surface((128, 300)).convert()
to_build_menu_back.fill((0,0,0))

to_build_discription_box=pygame.image.load("to_build_discription_box.bmp").convert()
to_build_discription_box=pygame.transform.scale(to_build_discription_box, (259, 77))
to_build_discription_box.set_colorkey((255,0,255))
to_build_discription_box_rect=to_build_discription_box.get_rect()
to_build_discription_box_rect.left=0
to_build_discription_box_rect.top=23

cater_to_menu=pygame.image.load("cater_to_menu.bmp").convert()
cater_to_menu=pygame.transform.scale(cater_to_menu, (290, 40))
cater_to_menu.set_colorkey((255,255,255))
cater_to_menu_rect=cater_to_menu.get_rect()
cater_to_menu_rect.left=128
cater_to_menu_rect.bottom=400

#Gets the frames that will be used in the Cater To menu
cater_to_warrior=warrior.idle_frames[0]
cater_to_warrior_rect=cater_to_warrior.get_rect()
cater_to_warrior_rect.bottom=392
cater_to_warrior_rect.left=133
cater_to_mage=mage.idle_frames[0]
cater_to_mage_rect=cater_to_mage.get_rect()
cater_to_mage_rect.bottom=392
cater_to_mage_rect.left=167
cater_to_rogue=rogue.idle_frames[0]
cater_to_rogue_rect=cater_to_rogue.get_rect()
cater_to_rogue_rect.bottom=392
cater_to_rogue_rect.left=207
cater_to_priest=priest.idle_frames[0]
cater_to_priest_rect=cater_to_priest.get_rect()
cater_to_priest_rect.bottom=392
cater_to_priest_rect.left=250
cater_to_knight=knight.idle_frames[0]
cater_to_knight_rect=cater_to_knight.get_rect()
cater_to_knight_rect.bottom=392
cater_to_knight_rect.left=290
cater_to_archer=archer.idle_frames[0]
cater_to_archer_rect=cater_to_archer.get_rect()
cater_to_archer_rect.bottom=392
cater_to_archer_rect.left=340
cater_to_pegasus_knight=pegasus_knight.idle_frames[0]
cater_to_pegasus_knight_rect=cater_to_pegasus_knight.get_rect()
cater_to_pegasus_knight_rect.bottom=392
cater_to_pegasus_knight_rect.left=375
cater_to_hero_rect_list=[[warrior, cater_to_warrior, cater_to_warrior_rect],[mage, cater_to_mage ,cater_to_mage_rect],[rogue, cater_to_rogue ,cater_to_rogue_rect],[priest, cater_to_priest,cater_to_priest_rect],[knight, cater_to_knight, cater_to_knight_rect],[archer ,cater_to_archer, cater_to_archer_rect],[pegasus_knight ,cater_to_pegasus_knight, cater_to_pegasus_knight_rect]]

blur_out_cater_to=pygame.Surface((33, 35)).convert()
blur_out_cater_to.fill((0,0,0))
blur_out_cater_to.set_alpha(100)

to_build_discription_box_clear=pygame.Surface((250, 71)).convert()
to_build_discription_box_clear.fill((0,0,0))

top_clear=pygame.Surface((size[0], 20)).convert()
top_clear.fill((0,0,0))

cater_to_clear=pygame.Surface((280, 38)).convert()
cater_to_clear.fill((0,0,0))

#Creates the various tabs that contain buildings
build_level_font=pygame.font.Font(helvet, 14)
build_level_1_text=build_level_font.render("level 1", True, (255,255,255))
to_build_level_1_plus=pygame.image.load("to_build_plus.bmp").convert()
to_build_level_1_plus=pygame.transform.scale(to_build_level_1_plus, (117, 20))
to_build_level_1_plus.blit(build_level_1_text, (15, 2))
to_build_level_1_minus=pygame.image.load("to_build_minus.bmp").convert()
to_build_level_1_minus=pygame.transform.scale(to_build_level_1_minus, (117, 20))
to_build_level_1_minus.blit(build_level_1_text, (15, 2))
to_build_level_1_rect=to_build_level_1_plus.get_rect()
to_build_level_1_rect.left=12
to_build_level_1_rect.bottom=127
to_build_level_1_down=False

build_level_2_text=build_level_font.render("level 2", True, (255,255,255))
to_build_level_2_plus=pygame.image.load("to_build_plus.bmp").convert()
to_build_level_2_plus=pygame.transform.scale(to_build_level_2_plus, (117, 20))
to_build_level_2_plus.blit(build_level_2_text, (15, 2))
to_build_level_2_minus=pygame.image.load("to_build_minus.bmp").convert()
to_build_level_2_minus=pygame.transform.scale(to_build_level_2_minus, (117, 20))
to_build_level_2_minus.blit(build_level_2_text, (15, 2))
to_build_level_2_rect=to_build_level_2_plus.get_rect()
to_build_level_2_rect.left=12
to_build_level_2_rect.bottom=147
to_build_level_2_down=False

build_level_3_text=build_level_font.render("level 3", True, (255,255,255))
to_build_level_3_plus=pygame.image.load("to_build_plus.bmp").convert()
to_build_level_3_plus=pygame.transform.scale(to_build_level_3_plus, (117, 20))
to_build_level_3_plus.blit(build_level_3_text, (15, 2))
to_build_level_3_minus=pygame.image.load("to_build_minus.bmp").convert()
to_build_level_3_minus=pygame.transform.scale(to_build_level_3_minus, (117, 20))
to_build_level_3_minus.blit(build_level_3_text, (15, 2))
to_build_level_3_rect=to_build_level_3_plus.get_rect()
to_build_level_3_rect.left=12
to_build_level_3_rect.bottom=167
to_build_level_3_down=False

build_hero_building_text=build_level_font.render("Hero Buildings", True, (255,255,255))
to_build_hero_building_plus=pygame.image.load("to_build_plus.bmp").convert()
to_build_hero_building_plus=pygame.transform.scale(to_build_hero_building_plus, (117, 20))
to_build_hero_building_plus.blit(build_hero_building_text, (15, 2))
to_build_hero_building_minus=pygame.image.load("to_build_minus.bmp").convert()
to_build_hero_building_minus=pygame.transform.scale(to_build_hero_building_minus, (117, 20))
to_build_hero_building_minus.blit(build_hero_building_text, (15, 2))
to_build_hero_building_rect=to_build_hero_building_plus.get_rect()
to_build_hero_building_rect.left=12
to_build_hero_building_rect.bottom=187
to_build_hero_building_down=False

build_unique_text=build_level_font.render("Unique Buildings", True, (255,255,255))
to_build_unique_plus=pygame.image.load("to_build_plus.bmp").convert()
to_build_unique_plus=pygame.transform.scale(to_build_unique_plus, (117, 20))
to_build_unique_plus.blit(build_unique_text, (15, 2))
to_build_unique_minus=pygame.image.load("to_build_minus.bmp").convert()
to_build_unique_minus=pygame.transform.scale(to_build_unique_minus, (117, 20))
to_build_unique_minus.blit(build_unique_text, (15, 2))
to_build_unique_rect=to_build_unique_plus.get_rect()
to_build_unique_rect.left=12
to_build_unique_rect.bottom=207
to_build_unique_down=False

build_other_text=build_level_font.render("Other", True, (255,255,255))
to_build_other_plus=pygame.image.load("to_build_plus.bmp").convert()
to_build_other_plus=pygame.transform.scale(to_build_other_plus, (117, 20))
to_build_other_plus.blit(build_other_text, (15, 2))
to_build_other_minus=pygame.image.load("to_build_minus.bmp").convert()
to_build_other_minus=pygame.transform.scale(to_build_other_minus, (117, 20))
to_build_other_minus.blit(build_other_text, (15, 2))
to_build_other_rect=to_build_other_plus.get_rect()
to_build_other_rect.left=12
to_build_other_rect.bottom=227
to_build_other_down=False

all_rects_in_to_build=[to_build_level_1_rect, workshop_to_build.rect, market_place_to_build.rect, walls_to_build.rect, wheat_feild_to_build.rect, garden_to_build.rect, monument_to_build.rect, to_build_level_2_rect, stone_works_to_build.rect, trading_post_to_build.rect, watchtower_to_build.rect, farm_to_build.rect, inn_to_build.rect, library_to_build.rect, to_build_level_3_rect, forge_to_build.rect, trade_network_to_build.rect, castle_to_build.rect, granary_to_build.rect, theater_to_build.rect, circus_to_build.rect, to_build_hero_building_rect, barracks_to_build.rect, arcane_academy_to_build.rect, pub_to_build.rect, church_to_build.rect, armory_to_build.rect, shooting_range_to_build.rect, stable_to_build.rect, to_build_unique_rect, colosseum_to_build.rect, mystical_shrine_to_build.rect, gambling_house_to_build.rect, chapel_to_build.rect, jousting_league_to_build.rect, hunting_grounds_to_build.rect, pegasus_olympics_to_build.rect, national_epic_s_to_build.rect, national_epic_m_to_build.rect, national_epic_l_to_build.rect, volcanic_forge_to_build.rect, national_treasury_to_build.rect, stronghold_to_build.rect, continental_gardens_to_build.rect, heroic_tribute_to_build.rect, academy_of_art_to_build.rect, to_build_other_rect, house_to_build.rect, cater_to_build.rect]

to_build_selecter_s=pygame.image.load("to_build_selecter_s.bmp").convert()
to_build_selecter_s.set_colorkey((255,255,255))

to_build_selecter_l=pygame.image.load("to_build_selecter_l.bmp").convert()
to_build_selecter_l.set_colorkey((255,255,255))

#misilanious fonts
top_bar_amount_font=pygame.font.Font(helvet, 12)
hero_event_info_bottom_font=pygame.font.Font(helvet, 13)
town_names_font=pygame.font.Font(helvet, 14)

background=pygame.Surface(size)
background=background.convert()
background.fill((0, 0, 0))

player_turn=0

#This part of code ensures that the menu for catering to a hero blurs out a hero
#if they are not in that town.
current_player=towns[player_turn]
functions.update_production(current_player)
functions.update_to_build_menu(current_player, to_build_level_1_rect, to_build_level_2_rect, to_build_level_3_rect, to_build_hero_building_rect, to_build_unique_rect, to_build_other_rect, to_build_list, clear_to_build_tab, turns_to_build_font)
cater_to_menu.blit(cater_to_clear, (0,5))
for i in cater_to_hero_rect_list:
    cater_to_menu.blit(i[1], (i[2].left-128, i[2].top-355))
    if i[0] not in current_player.heroes_in_town:
        cater_to_menu.blit(blur_out_cater_to, (i[2].left-128, i[2].top-355))
    
#variables for various input methods
clicked=False
scrolling_down=False
scrolling_up=False
pressed_enter=False
pressed_1=False
pressed_2=False
pressed_3=False
pressed_4=False
pressed_5=False
pressed_6=False
pressed_i=False
pressed_o=False

entering_name=False
name_being_entered=""
town_for_edit=None

arrows_selected=None
arrows_selected_num=0
select_for_construction=False

letter_down=None

hero_turn=False
in_game=False
on_main_menu=True
on_set_up_menu=False
on_how_to_play_menu=False

to_build_scroll_height=0
hero_sprite_counter=0

functions.manage_population(current_player, turn_number)
functions.update_happiness(current_player, turn_number)
current_player.gold+=current_player.gold_per_turn

clock=pygame.time.Clock()
keep_going=True
while keep_going:
    
    clock.tick(30)
    hero_sprite_counter+=1
    clicked=False
    scrolling_down=False
    scrolling_up=False
    letter_down=None
    
    
    for ev in pygame.event.get():
        
        if ev.type==QUIT:
            keep_going=False
            
        if ev.type==MOUSEMOTION:
            mouse.x=ev.pos[0]
            mouse.y=ev.pos[1]
                
        if ev.type==MOUSEBUTTONUP:
            if ev.button==1:
                clicked=True
                if entering_name==True:
                    double=False
                    for i in towns:
                        if i.town_name==name_being_entered and i.player_number!=town_for_edit.player_number:
                            double=True
                            
                    if name_being_entered!="" and double==False:
                        entering_name=False
                        town_for_edit.town_name=name_being_entered
                        name_being_entered=""
                        town_for_edit=None
            
        if ev.type==MOUSEBUTTONDOWN:
            if ev.button==4:
                scrolling_up=True
            if ev.button==5:
                scrolling_down=True
                
        if ev.type==KEYDOWN:
            if ev.key==K_ESCAPE:
                keep_going=False
                
            if in_game==True and current_player.ai==False:
                if ev.key==K_i:
                    pressed_i=True  
                    
                if hero_info_screen_up==False:
                    if ev.key==K_RETURN:
                        pressed_enter=True   
                    if ev.key==K_1:
                        pressed_1=True  
                        to_build_menu_up=True
                    if ev.key==K_2:
                        pressed_2=True  
                        to_build_menu_up=True
                    if ev.key==K_3:
                        pressed_3=True     
                        to_build_menu_up=True
                    if ev.key==K_4:
                        pressed_4=True  
                        to_build_menu_up=True
                    if ev.key==K_5:
                        pressed_5=True  
                        to_build_menu_up=True
                    if ev.key==K_6:
                        pressed_6=True           
                        to_build_menu_up=True
                    if ev.key==K_SPACE:
                        if to_build_menu_up==True:
                            to_build_menu_up=False
                        elif to_build_menu_up==False:
                            to_build_menu_up=True
                    if ev.key==K_o:
                        pressed_o=True
                        
                    if to_build_menu_up==True:
                        if arrows_selected!=None:     
                            #The user has the option to select things on the 
                            #building menu using the arrow keys, and this part 
                            #of the code makes it so if a user navigates via 
                            #this method, they do not select something that they
                            #cannot select, such as a building they have already
                            #built.
                            if ev.key==K_DOWN:
                                if arrows_selected!=cater_to_build.rect:
                                    arrows_selected_num+=1
                                    if all_rects_in_to_build[arrows_selected_num-1]==to_build_level_1_rect:
                                        if to_build_level_1_down==False:
                                            arrows_selected_num+=6
                                    if to_build_level_1_down==True:
                                        if all_rects_in_to_build[arrows_selected_num]==workshop_to_build.rect and current_player.production_building_level>0:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==market_place_to_build.rect and current_player.gold_building_level>0:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==walls_to_build.rect and current_player.defence_building_level>0:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==wheat_feild_to_build.rect and current_player.food_building_level>0:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==garden_to_build.rect and current_player.favor_building_level>0:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==monument_to_build.rect and current_player.happiness_building_level>0:
                                            arrows_selected_num+=1
                                            
                                    if all_rects_in_to_build[arrows_selected_num-1]==to_build_level_2_rect:
                                        if to_build_level_2_down==False:
                                            arrows_selected_num+=6
                                    if to_build_level_2_down==True:
                                        if all_rects_in_to_build[arrows_selected_num]==stone_works_to_build.rect and current_player.production_building_level>1:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==trading_post_to_build.rect and current_player.gold_building_level>1:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==watchtower_to_build.rect and current_player.defence_building_level>1:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==farm_to_build.rect and current_player.food_building_level>1:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==inn_to_build.rect and current_player.favor_building_level>1:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==library_to_build.rect and current_player.happiness_building_level>1:
                                            arrows_selected_num+=1
                                                
                                    if all_rects_in_to_build[arrows_selected_num-1]==to_build_level_3_rect:
                                        if to_build_level_3_down==False:
                                            arrows_selected_num+=6
                                    if to_build_level_3_down==True:
                                        if all_rects_in_to_build[arrows_selected_num]==forge_to_build.rect and current_player.production_building_level>2:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==trade_network_to_build.rect and current_player.gold_building_level>2:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==castle_to_build.rect and current_player.defence_building_level>2:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==granary_to_build.rect and current_player.food_building_level>2:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==theater_to_build.rect and current_player.favor_building_level>2:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==circus_to_build.rect and current_player.happiness_building_level>2:
                                            arrows_selected_num-=1
                                                
                                    if all_rects_in_to_build[arrows_selected_num-1]==to_build_hero_building_rect:
                                        if to_build_hero_building_down==False:
                                            arrows_selected_num+=7
                                    if to_build_hero_building_down==True:
                                        if all_rects_in_to_build[arrows_selected_num]==barracks_to_build.rect and current_player.warrior_building==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==arcane_academy_to_build.rect and current_player.mage_building==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==pub_to_build.rect and current_player.rogue_building==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==church_to_build.rect and current_player.priest_building==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==armory_to_build.rect and current_player.knight_building==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==shooting_range_to_build.rect and current_player.archer_building==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==stable_to_build.rect and current_player.pegasus_knight_building==True:
                                            arrows_selected_num+=1
                                            
                                    if all_rects_in_to_build[arrows_selected_num-1]==to_build_unique_rect:
                                        if to_build_unique_down==False:
                                            arrows_selected_num+=16
                                    if to_build_unique_down==True:
                                        if all_rects_in_to_build[arrows_selected_num]==colosseum_to_build.rect and colosseum.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==mystical_shrine_to_build.rect and mystical_shrine.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==gambling_house_to_build.rect and gambling_house.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==chapel_to_build.rect and chapel.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==jousting_league_to_build.rect and jousting_league.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==hunting_grounds_to_build.rect and hunting_grounds.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==pegasus_olympics_to_build.rect and pegasus_olympics.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==national_epic_s_to_build.rect and national_epic_s.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==national_epic_m_to_build.rect and national_epic_m.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==national_epic_l_to_build.rect and national_epic_l.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==volcanic_forge_to_build.rect and volcanic_forge.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==national_treasury_to_build.rect and national_treasury.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==stronghold_to_build.rect and stronghold.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==continental_gardens_to_build.rect and continental_gardens.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==heroic_tribute_to_build.rect and heroic_tribute.built==True:
                                            arrows_selected_num+=1
                                        if all_rects_in_to_build[arrows_selected_num]==academy_of_art_to_build.rect and academy_of_art.built==True:
                                            arrows_selected_num+=1
                                    if all_rects_in_to_build[arrows_selected_num-1]==to_build_other_rect:
                                        if to_build_other_down==False:
                                            arrows_selected_num-=1
                                arrows_selected=all_rects_in_to_build[arrows_selected_num]
                                
                            if ev.key==K_UP:
                                if arrows_selected!=to_build_level_1_rect:
                                    arrows_selected_num-=1
                                    if all_rects_in_to_build[arrows_selected_num+1]==to_build_other_rect:
                                        if to_build_unique_down==False:
                                            arrows_selected_num-=16
                                    if to_build_unique_down==True:
                                        if all_rects_in_to_build[arrows_selected_num]==academy_of_art_to_build.rect and academy_of_art.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==heroic_tribute_to_build.rect and heroic_tribute.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==continental_gardens_to_build.rect and continental_gardens.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==stronghold_to_build.rect and stronghold.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==national_treasury_to_build.rect and national_treasury.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==volcanic_forge_to_build.rect and volcanic_forge.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==national_epic_l_to_build.rect and national_epic_l.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==national_epic_m_to_build.rect and national_epic_m.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==national_epic_s_to_build.rect and national_epic_s.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==pegasus_olympics_to_build.rect and pegasus_olympics.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==hunting_grounds_to_build.rect and hunting_grounds.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==jousting_league_to_build.rect and jousting_league.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==chapel_to_build.rect and chapel.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==gambling_house_to_build.rect and gambling_house.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==mystical_shrine_to_build.rect and mystical_shrine.built==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==colosseum_to_build.rect and colosseum.built==True:
                                            arrows_selected_num-=1
                                                
                                    if all_rects_in_to_build[arrows_selected_num+1]==to_build_unique_rect:
                                        if to_build_hero_building_down==False:
                                            arrows_selected_num-=7
                                    if to_build_hero_building_down==True:
                                        if all_rects_in_to_build[arrows_selected_num]==stable_to_build.rect and current_player.pegasus_knight_building==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==shooting_range_to_build.rect and current_player.archer_building==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==armory_to_build.rect and current_player.knight_building==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==church_to_build.rect and current_player.priest_building==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==pub_to_build.rect and current_player.rogue_building==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==arcane_academy_to_build.rect and current_player.mage_building==True:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==barracks_to_build.rect and current_player.warrior_building==True:
                                            arrows_selected_num-=1
                                                
                                    if all_rects_in_to_build[arrows_selected_num+1]==to_build_hero_building_rect:
                                        if to_build_level_3_down==False:
                                            arrows_selected_num-=6
                                    if to_build_level_3_down==True:
                                        if all_rects_in_to_build[arrows_selected_num]==circus_to_build.rect and current_player.happiness_building_level>2:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==theater_to_build.rect and current_player.favor_building_level>2:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==granary_to_build.rect and current_player.food_building_level>2:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==castle_to_build.rect and current_player.defence_building_level>2:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==trade_network_to_build.rect and current_player.gold_building_level>2:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==forge_to_build.rect and current_player.production_building_level>2:
                                            arrows_selected_num-=1
                                                
                                    if all_rects_in_to_build[arrows_selected_num+1]==to_build_level_3_rect:
                                        if to_build_level_2_down==False:
                                            arrows_selected_num-=6
                                    if to_build_level_2_down==True:
                                        if all_rects_in_to_build[arrows_selected_num]==library_to_build.rect and current_player.happiness_building_level>1:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==inn_to_build.rect and current_player.favor_building_level>1:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==farm_to_build.rect and current_player.food_building_level>1:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==watchtower_to_build.rect and current_player.defence_building_level>1:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==trading_post_to_build.rect and current_player.gold_building_level>1:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==stone_works_to_build.rect and current_player.production_building_level>1:
                                            arrows_selected_num-=1
                                                
                                    if all_rects_in_to_build[arrows_selected_num+1]==to_build_level_2_rect:
                                        if to_build_level_1_down==False:
                                            arrows_selected_num-=6
                                    if to_build_level_1_down==True:
                                        if all_rects_in_to_build[arrows_selected_num]==monument_to_build.rect and current_player.happiness_building_level>0:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==garden_to_build.rect and current_player.favor_building_level>0:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==wheat_feild_to_build.rect and current_player.food_building_level>0:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==walls_to_build.rect and current_player.defence_building_level>0:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==market_place_to_build.rect and current_player.gold_building_level>0:
                                            arrows_selected_num-=1
                                        if all_rects_in_to_build[arrows_selected_num]==workshop_to_build.rect and current_player.production_building_level>0:
                                            arrows_selected_num-=1
                                arrows_selected=all_rects_in_to_build[arrows_selected_num]  
                                
                            if ev.key==K_RIGHT:
                                if arrows_selected==to_build_level_1_rect:
                                    pressed_1=True
                                elif arrows_selected==to_build_level_2_rect:
                                    pressed_2=True
                                elif arrows_selected==to_build_level_3_rect:
                                    pressed_3=True
                                elif arrows_selected==to_build_hero_building_rect:
                                    pressed_4=True
                                elif arrows_selected==to_build_unique_rect:
                                    pressed_5=True
                                elif arrows_selected==to_build_other_rect:
                                    pressed_6=True
                                else:
                                    select_for_construction=True
                                    
                            if ev.key==K_LEFT:
                                arrows_selected=None
                                arrows_selected_num=0
                                
                        if arrows_selected==None:
                            if ev.key==K_DOWN or ev.key==K_UP:
                                arrows_selected=all_rects_in_to_build[0]
                                arrows_selected_num=0
                            
                        #This part of the code allows the user to select things
                        #in the Cater To A Hero menu using keys
                        if current_player.constructing==cater_to_build:
                            if ev.key==K_q:
                                if warrior in current_player.heroes_in_town:
                                    current_player.catering_to=warrior
                            if ev.key==K_w:
                                if mage in current_player.heroes_in_town:
                                    current_player.catering_to=mage
                            if ev.key==K_e:
                                if rogue in current_player.heroes_in_town:
                                    current_player.catering_to=rogue
                            if ev.key==K_r:
                                if priest in current_player.heroes_in_town:
                                    current_player.catering_to=priest
                            if ev.key==K_t:
                                if knight in current_player.heroes_in_town:
                                    current_player.catering_to=knight
                            if ev.key==K_y:
                                if archer in current_player.heroes_in_town:
                                    current_player.catering_to=archer
                            if ev.key==K_u:
                                if pegasus_knight in current_player.heroes_in_town:
                                    current_player.catering_to=pegasus_knight
                   
                   
            if in_game==False: 
                if entering_name==True:  
                    #This makes it so the user can type in a name on the Set Up
                    #menu
                    letter_down=""
                    if ev.key==K_SPACE:
                        letter_down=" "
                        
                    if ev.key==K_BACKSPACE:
                        if len(name_being_entered)!=0:
                            name_being_entered=name_being_entered[:-1]
                            
                    keys=pygame.key.get_pressed()
                    letter_keys=[K_q, K_w, K_e, K_r, K_t, K_y, K_u, K_i, K_o, K_p, K_a, K_s, K_d, K_f, K_g, K_h, K_j, K_k, K_l, K_z, K_x, K_c, K_v, K_b, K_n, K_m, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_0, K_COMMA, K_PERIOD, K_SLASH, K_MINUS]
                    if ev.key in letter_keys:
                        letter_down=["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "/", "-"][letter_keys.index(ev.key)]
                        if keys[K_LSHIFT]==True:
                            if letter_keys.index(ev.key)<=25:
                                letter_down=letter_down.upper()   
                            if letter_keys.index(ev.key)>25:
                                letter_down=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", "_"][letter_keys.index(ev.key)-26]
                            
                    temp_text=menu_font.render(str(name_being_entered)+str(letter_down), True, (255,255,255))
                    if temp_text.get_size()[0]<87:
                        name_being_entered+=letter_down
                    
                    if ev.key==K_RETURN:
                        double=False
                        for i in towns:
                            if i.town_name==name_being_entered and i.player_number!=town_for_edit.player_number:
                                double=True
                        if name_being_entered!="" and double==False:
                            entering_name=False
                            town_for_edit.town_name=name_being_entered
                            name_being_entered=""
                            town_for_edit=None
                            
                if entering_name==False:
                    if on_main_menu==True:
                        if ev.key==K_SPACE:
                            on_main_menu=False
                            on_set_up_menu=True
                            
                        if ev.key==K_BACKSPACE:
                            keep_going=False
                            
                    elif on_set_up_menu==True:
                        if ev.key==K_SPACE:
                            if entering_name==False:
                                for i in towns:
                                    i.place_town()
                                    if i.difficulty_level==5:
                                        i.production+=5
                                last_human_player=towns[0]
                                if len(towns)==2:
                                    next_elimination=150
                                if len(towns)!=2:
                                    next_elimination=120
                                in_game=True
                                on_set_up_menu=False
                            
                        if ev.key==K_BACKSPACE:
                            on_set_up_menu=False
                            on_main_menu=True
                            
                        if ev.key==K_MINUS:
                            if classes.Town.players!=2:
                                classes.Town.players-=1
                                towns=towns[:-1]
                                town_group=pygame.sprite.Group(towns)
                                
                        keys=pygame.key.get_pressed()                                
                        if ev.key==K_EQUALS and keys[K_LSHIFT]==True:
                            if classes.Town.players!=10:
                                num_to_use=classes.Town.players
                                doubles=True
                                while doubles==True:
                                    num_to_use+=1
                                    doubles=False
                                    for i in towns:
                                        if i.town_name==("Player "+str(num_to_use)):
                                            doubles=True
                                            
                                new_town=classes.Town("Player "+str(num_to_use), False, town, town_distroyed)
                                towns+=[new_town]
                                town_group=pygame.sprite.Group(towns)                            
            
            
    if in_game==False and True in [on_main_menu, on_set_up_menu, on_how_to_play_menu]:
        background.blit(title_background, (0,0))
        
        if on_main_menu==True:
            background.blit(title_main_menu, title_main_menu_rect)
            background.blit(set_up_game_button, set_up_game_button_rect)
            background.blit(set_up_game_text, set_up_game_text_rect)
            background.blit(how_to_play_button, how_to_play_button_rect)
            background.blit(how_to_play_text, how_to_play_text_rect)
            background.blit(quit_button, quit_button_rect)
            background.blit(quit_text, quit_text_rect)
            background.blit(menu_divider, (set_up_game_button_rect.left+25, set_up_game_button_rect.bottom))
            background.blit(menu_divider, (how_to_play_button_rect.left+25, how_to_play_button_rect.bottom))
                
            collisions=mouse.rect.colliderect(set_up_game_button_rect)
            if collisions==1 and clicked==True:
                on_main_menu=False
                on_set_up_menu=True
            
            collisions=mouse.rect.colliderect(quit_text_rect)
            if collisions==1 and clicked==True:
                keep_going=False
            
            collisions=mouse.rect.colliderect(how_to_play_text_rect)
            if collisions==1 and clicked==True:
                on_main_menu=False
                on_how_to_play_menu=True
        
        if on_set_up_menu==True:
            background.blit(set_up_menu, set_up_menu_rect)
            
            #This part of the code creates and displays all of the information
            #that is shown on the Set Up menu.
            c=0
            for i in towns:
                if town_for_edit!=i:
                    temp_text=menu_font.render(i.town_name, True, (255,255,255))
                if town_for_edit==i:
                    temp_text=menu_font.render(name_being_entered, True, (255,255,255))
                background.blit(temp_text, (150+int(c/5)*260, 155+52*c-260*int(c/5)))
                
                edit_name_buttons[c][1].left=245+int(c/5)*260
                edit_name_buttons[c][1].top=155+52*c-260*int(c/5)
                
                if i.ai==True:
                    make_ai_buttons[c][0]=ai_check_box_checked
                if i.ai==False:
                    make_ai_buttons[c][0]=ai_check_box_empty
                make_ai_buttons[c][1].left=155+int(c/5)*260
                make_ai_buttons[c][1].top=180+52*c-260*int(c/5)
                
                change_ai_level_buttons[c][0][1].left=195+int(c/5)*260
                change_ai_level_buttons[c][0][1].top=181+52*c-260*int(c/5)
                change_ai_level_buttons[c][1][1].left=255+int(c/5)*260
                change_ai_level_buttons[c][1][1].top=181+52*c-260*int(c/5)
                
                if classes.Town.players>=c+1:
                    #Lets you edit a town's name
                    collisions=mouse.rect.colliderect(edit_name_buttons[c][1])
                    if collisions==1 and clicked==True:
                        entering_name=True
                        name_being_entered=towns[c].town_name
                        town_for_edit=towns[c]  
                        
                    #Switchs a town from AI to Human
                    collisions=mouse.rect.colliderect(make_ai_buttons[c][1])
                    if collisions==1 and clicked==True:
                        if towns[c].ai==True:
                            towns[c].ai=False
                            towns[c].difficulty_level=None                            
                        elif towns[c].ai==False:
                            towns[c].ai=True   
                            towns[c].difficulty_level=3
                            
                    #Change a town's difficulty level
                    collisions=mouse.rect.colliderect(change_ai_level_buttons[c][0][1])
                    if collisions==1 and clicked==True and towns[c].ai==True and towns[c].difficulty_level!=1:
                        towns[c].difficulty_level-=1
                        
                    collisions=mouse.rect.colliderect(change_ai_level_buttons[c][1][1])
                    if collisions==1 and clicked==True and towns[c].ai==True and towns[c].difficulty_level!=5:
                        towns[c].difficulty_level+=1
                        
                        
                        
                temp_text=ai_check_box_font.render("CPU", True, (255,255,255))                        
                background.blit(temp_text, (168+int(c/5)*260, 178+52*c-260*int(c/5)))
                
                if towns[c].ai==True:
                    temp_text=ai_check_box_font.render("Level: {}".format(towns[c].difficulty_level), True, (255,255,255))                        
                    background.blit(temp_text, (208+int(c/5)*260, 178+52*c-260*int(c/5)))
                
                background.blit(i.image, (100+int(c/5)*260, 155+52*c-260*int(c/5)))
                background.blit(edit_name_buttons[c][0], edit_name_buttons[c][1])
                background.blit(make_ai_buttons[c][0], make_ai_buttons[c][1])
                if towns[c].ai==True:
                    background.blit(change_ai_level_buttons[c][0][0], change_ai_level_buttons[c][0][1])
                    background.blit(change_ai_level_buttons[c][1][0], change_ai_level_buttons[c][1][1])
                
                c+=1
                
            players_amount_text=menu_font.render(str(c), True, (255,255,255))
            background.blit(players_text_set_up, (160, 110))
            background.blit(players_amount_text, (215, 110))
            background.blit(add_player_icon, add_player_icon_rect)
            background.blit(remove_player_icon, remove_player_icon_rect)
            background.blit(start_game_button, start_game_button_rect)
            background.blit(set_up_back_button, set_up_back_button_rect)
            background.blit(set_up_menu_divider, (85, 135))
            
                
                    
            if entering_name==True:
                background.blit(edit_name_outline, ((150+int((town_for_edit.player_number-1)/5)*260)-5, (155+52*(town_for_edit.player_number-1)-260*int((town_for_edit.player_number-1)/5))-2))
                
            collisions=mouse.rect.colliderect(add_player_icon_rect)
            if collisions==1 and clicked==True and classes.Town.players!=10:
                num_to_use=classes.Town.players
                doubles=True
                while doubles==True:
                    num_to_use+=1
                    doubles=False
                    for i in towns:
                        if i.town_name==("Player "+str(num_to_use)):
                            doubles=True
                new_town=classes.Town("Player "+str(num_to_use), False, town, town_distroyed)
                
                if towns[-1].ai==True:
                    new_town.ai=True
                    new_town.difficulty_level=towns[-1].difficulty_level
                
                towns+=[new_town]
                town_group=pygame.sprite.Group(towns)
            
            collisions=mouse.rect.colliderect(remove_player_icon_rect)
            if collisions==1 and clicked==True and classes.Town.players!=2:
                classes.Town.players-=1
                towns=towns[:-1]
                town_group=pygame.sprite.Group(towns)
                     
            collisions=mouse.rect.colliderect(start_game_button_rect)
            if collisions==1 and clicked==True and entering_name==False:
                for i in towns:
                    i.place_town()
                    if i.difficulty_level==5:
                        i.production+=5
                last_human_player=towns[0]
                for i in [warrior, mage, priest, rogue, knight, archer, pegasus_knight]:
                    while len(i.town_favors)!=classes.Town.players:
                        i.town_favors+=[i.town_favors[0]]
                if len(towns)==2:
                    next_elimination=150
                if len(towns)!=2:
                    next_elimination=120
                in_game=True
                on_set_up_menu=False
                
            collisions=mouse.rect.colliderect(set_up_back_button_rect)
            if collisions==1 and clicked==True and entering_name==False:
                on_set_up_menu=False
                on_main_menu=True
                
        if on_how_to_play_menu==True:
            ##
            background.blit(set_up_menu, set_up_menu_rect)
            
            background.blit(general_tab_back, general_tab_rect)
            if selected_tab==0:
                background.blit(general_context_tab_back, general_context_tab_rect)
                background.blit(general_playing_tab_back, general_playing_tab_rect)
                background.blit(general_heroes_tab_back, general_heroes_tab_rect)
                background.blit(general_winning_tab_back, general_winning_tab_rect)
                background.blit(general_the_dragon_tab_back, general_the_dragon_tab_rect)
            
            background.blit(stats_tab_back, stats_tab_rect)
            if selected_tab==1:
                background.blit(stats_production_tab_back, stats_production_tab_rect)
                background.blit(stats_gold_tab_back, stats_gold_tab_rect)
                background.blit(stats_defence_tab_back, stats_defence_tab_rect)
                background.blit(stats_food_tab_back, stats_food_tab_rect)
                background.blit(stats_favor_tab_back, stats_favor_tab_rect)
                background.blit(stats_happiness_tab_back, stats_happiness_tab_rect)
                background.blit(stats_population_tab_back, stats_population_tab_rect)
            
            background.blit(heroes_tab_back, heroes_tab_rect)
            if selected_tab==2:
                background.blit(heroes_warrior_tab_back, heroes_warrior_tab_rect)
                background.blit(heroes_mage_tab_back, heroes_mage_tab_rect)
                background.blit(heroes_priest_tab_back, heroes_priest_tab_rect)
                background.blit(heroes_rogue_tab_back, heroes_rogue_tab_rect)
                background.blit(heroes_knight_tab_back, heroes_knight_tab_rect)
                background.blit(heroes_archer_tab_back, heroes_archer_tab_rect)
                background.blit(heroes_pegasus_knight_tab_back, heroes_pegasus_knight_tab_rect)
                background.blit(heroes_hero_quests_tab_back, heroes_hero_quests_tab_rect)
            
            background.blit(buildings_tab_back, buildings_tab_rect)
            if selected_tab==3:
                background.blit(buildings_general_tab_back, buildings_general_tab_rect)
                background.blit(buildings_maintenance_tab_back, buildings_maintenance_tab_rect)
                background.blit(buildings_levels_1_2_3_tab_back, buildings_levels_1_2_3_tab_rect)
                background.blit(buildings_hero_buildings_tab_back, buildings_hero_buildings_tab_rect)
                background.blit(buildings_unique_buildings_tab_back, buildings_unique_buildings_tab_rect)
                background.blit(buildings_other_buildings_tab_back, buildings_other_buildings_tab_rect)


                
            #####
            collisions=mouse.rect.colliderect(general_tab_rect)
            if collisions==1 and clicked==True and selected_tab!=0:
                selected_tab=0
                selected_sub_tab=0
                selected_tab_for_blit=general_tab_back
                selected_tab_for_blit_rect=general_tab_rect
                selected_sub_tab_for_blit=general_context_tab_back
                selected_sub_tab_for_blit_rect=general_context_tab_rect
                selected_info_text_for_blit=general_context_info_text
            
            collisions=mouse.rect.colliderect(general_context_tab_rect)
            if collisions==1 and clicked==True and selected_tab==0:
                selected_sub_tab=0
                selected_sub_tab_for_blit=general_context_tab_back
                selected_sub_tab_for_blit_rect=general_context_tab_rect
                selected_info_text_for_blit=general_context_info_text
            
            collisions=mouse.rect.colliderect(general_playing_tab_rect)
            if collisions==1 and clicked==True and selected_tab==0:
                selected_sub_tab=1
                selected_sub_tab_for_blit=general_playing_tab_back
                selected_sub_tab_for_blit_rect=general_playing_tab_rect
                selected_info_text_for_blit=general_playing_info_text
                selected_info_text_for_blit=general_playing_info_text
            
            collisions=mouse.rect.colliderect(general_heroes_tab_rect)
            if collisions==1 and clicked==True and selected_tab==0:
                selected_sub_tab=2
                selected_sub_tab_for_blit=general_heroes_tab_back
                selected_sub_tab_for_blit_rect=general_heroes_tab_rect
                selected_info_text_for_blit=general_heroes_info_text
            
            collisions=mouse.rect.colliderect(general_winning_tab_rect)
            if collisions==1 and clicked==True and selected_tab==0:
                selected_sub_tab=3
                selected_sub_tab_for_blit=general_winning_tab_back
                selected_sub_tab_for_blit_rect=general_winning_tab_rect
                selected_info_text_for_blit=general_winning_info_text
            
            collisions=mouse.rect.colliderect(general_the_dragon_tab_rect)
            if collisions==1 and clicked==True and selected_tab==0:
                selected_sub_tab=4
                selected_sub_tab_for_blit=general_the_dragon_tab_back
                selected_sub_tab_for_blit_rect=general_the_dragon_tab_rect
                selected_info_text_for_blit=general_the_dragon_info_text
            
            
            collisions=mouse.rect.colliderect(stats_tab_rect)
            if collisions==1 and clicked==True and selected_tab!=1:
                selected_tab=1
                selected_sub_tab=0
                selected_tab_for_blit=stats_tab_back
                selected_tab_for_blit_rect=stats_tab_rect
                selected_sub_tab_for_blit=stats_production_tab_back
                selected_sub_tab_for_blit_rect=stats_production_tab_rect
                selected_info_text_for_blit=stats_production_info_text
            
            collisions=mouse.rect.colliderect(stats_production_tab_rect)
            if collisions==1 and clicked==True and selected_tab==1:
                selected_sub_tab=0
                selected_sub_tab_for_blit=stats_production_tab_back
                selected_sub_tab_for_blit_rect=stats_production_tab_rect
                selected_info_text_for_blit=stats_production_info_text
            
            collisions=mouse.rect.colliderect(stats_gold_tab_rect)
            if collisions==1 and clicked==True and selected_tab==1:
                selected_sub_tab=1
                selected_sub_tab_for_blit=stats_gold_tab_back
                selected_sub_tab_for_blit_rect=stats_gold_tab_rect
                selected_info_text_for_blit=stats_gold_info_text
            
            collisions=mouse.rect.colliderect(stats_defence_tab_rect)
            if collisions==1 and clicked==True and selected_tab==1:
                selected_sub_tab=2
                selected_sub_tab_for_blit=stats_defence_tab_back
                selected_sub_tab_for_blit_rect=stats_defence_tab_rect
                selected_info_text_for_blit=stats_defence_info_text
            
            collisions=mouse.rect.colliderect(stats_food_tab_rect)
            if collisions==1 and clicked==True and selected_tab==1:
                selected_sub_tab=3
                selected_sub_tab_for_blit=stats_food_tab_back
                selected_sub_tab_for_blit_rect=stats_food_tab_rect
                selected_info_text_for_blit=stats_food_info_text
            
            collisions=mouse.rect.colliderect(stats_favor_tab_rect)
            if collisions==1 and clicked==True and selected_tab==1:
                selected_sub_tab=4
                selected_sub_tab_for_blit=stats_favor_tab_back
                selected_sub_tab_for_blit_rect=stats_favor_tab_rect
                selected_info_text_for_blit=stats_favor_info_text
            
            collisions=mouse.rect.colliderect(stats_happiness_tab_rect)
            if collisions==1 and clicked==True and selected_tab==1:
                selected_sub_tab=5
                selected_sub_tab_for_blit=stats_happiness_tab_back
                selected_sub_tab_for_blit_rect=stats_happiness_tab_rect
                selected_info_text_for_blit=stats_happiness_info_text
            
            collisions=mouse.rect.colliderect(stats_population_tab_rect)
            if collisions==1 and clicked==True and selected_tab==1:
                selected_sub_tab=6
                selected_sub_tab_for_blit=stats_population_tab_back
                selected_sub_tab_for_blit_rect=stats_population_tab_rect
                selected_info_text_for_blit=stats_population_info_text
            
            collisions=mouse.rect.colliderect(heroes_tab_rect)
            if collisions==1 and clicked==True and selected_tab!=2:
                selected_tab=2
                selected_sub_tab=0
                selected_tab_for_blit=heroes_tab_back
                selected_tab_for_blit_rect=heroes_tab_rect
                selected_sub_tab_for_blit=heroes_warrior_tab_back
                selected_sub_tab_for_blit_rect=heroes_warrior_tab_rect
                selected_info_text_for_blit=heroes_warrior_info_text
            
            collisions=mouse.rect.colliderect(heroes_warrior_tab_rect)
            if collisions==1 and clicked==True and selected_tab==2:
                selected_sub_tab=0
                selected_sub_tab_for_blit=heroes_warrior_tab_back
                selected_sub_tab_for_blit_rect=heroes_warrior_tab_rect
                selected_info_text_for_blit=heroes_warrior_info_text
            
            collisions=mouse.rect.colliderect(heroes_mage_tab_rect)
            if collisions==1 and clicked==True and selected_tab==2:
                selected_sub_tab=1
                selected_sub_tab_for_blit=heroes_mage_tab_back
                selected_sub_tab_for_blit_rect=heroes_mage_tab_rect
                selected_info_text_for_blit=heroes_mage_info_text
            
            collisions=mouse.rect.colliderect(heroes_priest_tab_rect)
            if collisions==1 and clicked==True and selected_tab==2:
                selected_sub_tab=2
                selected_sub_tab_for_blit=heroes_priest_tab_back
                selected_sub_tab_for_blit_rect=heroes_priest_tab_rect
                selected_info_text_for_blit=heroes_priest_info_text
            
            collisions=mouse.rect.colliderect(heroes_rogue_tab_rect)
            if collisions==1 and clicked==True and selected_tab==2:
                selected_sub_tab=3
                selected_sub_tab_for_blit=heroes_rogue_tab_back
                selected_sub_tab_for_blit_rect=heroes_rogue_tab_rect
                selected_info_text_for_blit=heroes_rogue_info_text
            
            collisions=mouse.rect.colliderect(heroes_knight_tab_rect)
            if collisions==1 and clicked==True and selected_tab==2:
                selected_sub_tab=4
                selected_sub_tab_for_blit=heroes_knight_tab_back
                selected_sub_tab_for_blit_rect=heroes_knight_tab_rect
                selected_info_text_for_blit=heroes_knight_info_text
            
            collisions=mouse.rect.colliderect(heroes_archer_tab_rect)
            if collisions==1 and clicked==True and selected_tab==2:
                selected_sub_tab=5
                selected_sub_tab_for_blit=heroes_archer_tab_back
                selected_sub_tab_for_blit_rect=heroes_archer_tab_rect
                selected_info_text_for_blit=heroes_archer_info_text
            
            collisions=mouse.rect.colliderect(heroes_pegasus_knight_tab_rect)
            if collisions==1 and clicked==True and selected_tab==2:
                selected_sub_tab=6
                selected_sub_tab_for_blit=heroes_pegasus_knight_tab_back
                selected_sub_tab_for_blit_rect=heroes_pegasus_knight_tab_rect
                selected_info_text_for_blit=heroes_pegasus_knight_info_text
            
            collisions=mouse.rect.colliderect(heroes_hero_quests_tab_rect)
            if collisions==1 and clicked==True and selected_tab==2:
                selected_sub_tab=7
                selected_sub_tab_for_blit=heroes_hero_quests_tab_back
                selected_sub_tab_for_blit_rect=heroes_hero_quests_tab_rect
                selected_info_text_for_blit=heroes_hero_quests_info_text
            
            
            collisions=mouse.rect.colliderect(buildings_tab_rect)
            if collisions==1 and clicked==True and selected_tab!=3:
                selected_tab=3
                selected_sub_tab=0
                selected_tab_for_blit=buildings_tab_back
                selected_tab_for_blit_rect=buildings_tab_rect
                selected_sub_tab_for_blit=buildings_general_tab_back
                selected_sub_tab_for_blit_rect=buildings_general_tab_rect
                selected_info_text_for_blit=buildings_general_info_text
            
            collisions=mouse.rect.colliderect(buildings_general_tab_rect)
            if collisions==1 and clicked==True and selected_tab==3:
                selected_sub_tab=0
                selected_sub_tab_for_blit=buildings_general_tab_back
                selected_sub_tab_for_blit_rect=buildings_general_tab_rect
                selected_info_text_for_blit=buildings_general_info_text
            
            collisions=mouse.rect.colliderect(buildings_maintenance_tab_rect)
            if collisions==1 and clicked==True and selected_tab==3:
                selected_sub_tab=1
                selected_sub_tab_for_blit=buildings_maintenance_tab_back
                selected_sub_tab_for_blit_rect=buildings_maintenance_tab_rect
                selected_info_text_for_blit=buildings_maintenance_info_text
            
            collisions=mouse.rect.colliderect(buildings_levels_1_2_3_tab_rect)
            if collisions==1 and clicked==True and selected_tab==3:
                selected_sub_tab=2
                selected_sub_tab_for_blit=buildings_levels_1_2_3_tab_back
                selected_sub_tab_for_blit_rect=buildings_levels_1_2_3_tab_rect
                selected_info_text_for_blit=buildings_levels_1_2_3_info_text
            
            collisions=mouse.rect.colliderect(buildings_hero_buildings_tab_rect)
            if collisions==1 and clicked==True and selected_tab==3:
                selected_sub_tab=3
                selected_sub_tab_for_blit=buildings_hero_buildings_tab_back
                selected_sub_tab_for_blit_rect=buildings_hero_buildings_tab_rect
                selected_info_text_for_blit=buildings_hero_buildings_info_text
            
            collisions=mouse.rect.colliderect(buildings_unique_buildings_tab_rect)
            if collisions==1 and clicked==True and selected_tab==3:
                selected_sub_tab=4
                selected_sub_tab_for_blit=buildings_unique_buildings_tab_back
                selected_sub_tab_for_blit_rect=buildings_unique_buildings_tab_rect
                selected_info_text_for_blit=buildings_unique_buildings_info_text
            
            collisions=mouse.rect.colliderect(buildings_other_buildings_tab_rect)
            if collisions==1 and clicked==True and selected_tab==3:
                selected_sub_tab=5
                selected_sub_tab_for_blit=buildings_other_buildings_tab_back
                selected_sub_tab_for_blit_rect=buildings_other_buildings_tab_rect
                selected_info_text_for_blit=buildings_other_buildings_info_text
                
                
                
            collisions=mouse.rect.colliderect(how_to_play_back_button_rect)
            if collisions==1 and clicked==True:
                on_how_to_play_menu=False
                on_main_menu=True


            #####




            
            background.blit(tab_bottom_line, (85, 123))
            background.blit(tab_bottom_line, (85, 146))
            
            background.blit(selected_tab_for_blit, selected_tab_for_blit_rect)
            background.blit(selected_sub_tab_for_blit, selected_sub_tab_for_blit_rect)
            background.blit(selected_info_text_for_blit, (90, 150))
            
            background.blit(how_to_play_back_button, how_to_play_back_button_rect)
            
        
        
    if in_game==True:    
        
        
        if hero_turn==False and dragon_turn==False and hero_info_screen_up==False:
            collisions=mouse.rect.colliderect(empty_wheel_rect)
            if collisions==1:
                if clicked==True:
                    if to_build_menu_up==True:
                        to_build_menu_up=False
                    elif to_build_menu_up==False:
                        to_build_menu_up=True
            #This part of the code is used to see if the user clicks on a tab
            #on the menu containing the buildings. It also shifts things down
            #if you extend a menu found above it.
            if to_build_menu_up==True:
                collisions=mouse.rect.colliderect(to_build_level_1_rect)
                if collisions==1 or pressed_1==True:
                    if clicked==True or pressed_1==True:
                        pressed_1=False
                        change_by=(32*(6-last_human_player.level_1_buildings))
                        if to_build_level_1_down==True:
                            to_build_level_1_down=False
                            to_build_level_2_rect.top-=change_by
                            to_build_level_3_rect.top-=change_by
                            to_build_hero_building_rect.top-=change_by
                            to_build_unique_rect.top-=change_by
                            to_build_other_rect.top-=change_by
                            for i in to_build_list[6:]:
                                i.rect.top-=change_by
                        elif to_build_level_1_down==False:
                            to_build_level_1_down=True
                            to_build_level_2_rect.top+=change_by
                            to_build_level_3_rect.top+=change_by
                            to_build_hero_building_rect.top+=change_by
                            to_build_unique_rect.top+=change_by
                            to_build_other_rect.top+=change_by
                            for i in to_build_list[6:]:
                                i.rect.top+=change_by
                collisions=mouse.rect.colliderect(to_build_level_2_rect)
                if collisions==1 or pressed_2==True:
                    if clicked==True or pressed_2==True:
                        pressed_2=False
                        change_by=(32*(6-last_human_player.level_2_buildings))
                        if to_build_level_2_down==True:
                            to_build_level_2_down=False
                            to_build_level_3_rect.top-=change_by
                            to_build_hero_building_rect.top-=change_by
                            to_build_unique_rect.top-=change_by
                            to_build_other_rect.top-=change_by
                            for i in to_build_list[12:]:
                                i.rect.top-=change_by
                        elif to_build_level_2_down==False:
                            to_build_level_2_down=True
                            to_build_level_3_rect.top+=change_by
                            to_build_hero_building_rect.top+=change_by
                            to_build_unique_rect.top+=change_by
                            to_build_other_rect.top+=change_by
                            for i in to_build_list[12:]:
                                i.rect.top+=change_by
                collisions=mouse.rect.colliderect(to_build_level_3_rect)
                if collisions==1 or pressed_3==True:
                    if clicked==True or pressed_3==True:
                        pressed_3=False
                        change_by=(32*(6-last_human_player.level_3_buildings))
                        if to_build_level_3_down==True:
                            to_build_level_3_down=False
                            to_build_hero_building_rect.top-=change_by
                            to_build_unique_rect.top-=change_by
                            to_build_other_rect.top-=change_by
                            for i in to_build_list[18:]:
                                i.rect.top-=change_by
                        elif to_build_level_3_down==False:
                            to_build_level_3_down=True
                            to_build_hero_building_rect.top+=change_by
                            to_build_unique_rect.top+=change_by
                            to_build_other_rect.top+=change_by
                            for i in to_build_list[18:]:
                                i.rect.top+=change_by
                collisions=mouse.rect.colliderect(to_build_hero_building_rect)
                if collisions==1 or pressed_4==True:
                    if clicked==True or pressed_4==True:
                        pressed_4=False
                        change_by=(32*(7-last_human_player.hero_buildings))
                        if to_build_hero_building_down==True:
                            to_build_hero_building_down=False
                            to_build_unique_rect.top-=change_by
                            to_build_other_rect.top-=change_by
                            for i in to_build_list[25:]:
                                i.rect.top-=change_by
                        elif to_build_hero_building_down==False:
                            to_build_hero_building_down=True
                            to_build_unique_rect.top+=change_by
                            to_build_other_rect.top+=change_by
                            for i in to_build_list[25:]:
                                i.rect.top+=change_by
                collisions=mouse.rect.colliderect(to_build_unique_rect)
                if collisions==1 or pressed_5==True:
                    if clicked==True or pressed_5==True:
                        pressed_5=False
                        change_by=(32*(16-classes.Unique_Building.uniques_built))
                        if to_build_unique_down==True:
                            to_build_unique_down=False
                            to_build_other_rect.top-=change_by
                            for i in to_build_list[41:]:
                                i.rect.top-=change_by
                        elif to_build_unique_down==False:
                            to_build_unique_down=True
                            to_build_other_rect.top+=change_by
                            for i in to_build_list[41:]:
                                i.rect.top+=change_by
                collisions=mouse.rect.colliderect(to_build_other_rect)
                if collisions==1 or pressed_6==True:
                    if clicked==True or pressed_6==True:
                        pressed_6=False
                        change_by=(32)
                        if last_human_player.hero_in_town==True:
                            change_by+=32
                        if to_build_other_down==True:
                            to_build_other_down=False
                        elif to_build_other_down==False:
                            to_build_other_down=True   
                            
            #If the user opens up the Hero Info button
            collisions=mouse.rect.colliderect(hero_info_button_rect)
            if collisions==1 or pressed_i==True:
                if clicked==True or pressed_i==True:
                    pressed_i=False
                    hero_info_screen_up=True
                    to_build_menu_up=False    
            collisions=mouse.rect.colliderect(hero_info_button_rect)
            if collisions==1:
                if clicked==True:
                    to_build_menu_up=False
                
            #if you click next turn
            if current_player.ai==False:
                collisions=mouse.rect.colliderect(next_turn_rect)
                if collisions==1 or pressed_enter==True:
                    if clicked==True or pressed_enter==True:
                        pressed_enter=False
                        #if you still need to produce something
                        if current_player.constructing==None:
                            to_build_menu_up=True
                        construction_valid=True
                        if current_player.constructing==cater_to_build and current_player.catering_to==None:
                            construction_valid=False
                            to_build_menu_up=True
                        
                        #if you can end your turn
                        if current_player.constructing!=None and construction_valid==True:
                            player_turn+=1
                            while player_turn!=len(towns) and towns[player_turn].eliminated==True:
                                player_turn+=1
                            to_build_menu_up=False
                            to_build_scroll_height=0
                            to_build_level_1_down=False
                            to_build_level_2_down=False
                            to_build_level_3_down=False
                            to_build_hero_building_down=False
                            to_build_unique_down=False
                            to_build_other_down=False
                            arrows_selected=None
                            arrows_selected_num=0
                            if player_turn==len(towns):
                                turn_number+=1
                                hero_turn=True
                                hero_sprite_counter=0
                                functions.update_favor(towns)
                                for i in towns:
                                    i.turns_since_warrior_visit+=1
                                    i.turns_since_mage_visit+=1    
                                    i.turns_since_rogue_visit+=1    
                                    i.turns_since_priest_visit+=1    
                                    i.turns_since_knight_visit+=1    
                                    i.turns_since_archer_visit+=1    
                                    i.turns_since_pegasus_knight_visit+=1    
                                for i in hero_group:                        
                                    i.Move(towns)
                                if turn_number==next_elimination:
                                    if len(towns)!=2:
                                        next_elimination+=int(1/(len(towns)-2)*30)
                                    dragon_turn=True
                                    dragon.eliminate_towns(towns)
                                    for i in hero_group:
                                        i.destination="middle"
                                        i.c_destination="middle"
                                        i.moving=True
                                        if i.location!="middle":
                                            if abs(i.location.rect.centerx-370)*2<abs(i.location.rect.centery-220):
                                                if i.location.rect.centery>220:
                                                    i.moving_direction="up"
                                                if i.location.rect.centery<220:
                                                    i.moving_direction="down"
                                            elif abs(i.location.rect.centerx-370)>abs(i.location.rect.centery-220)*2:
                                                if i.location.rect.centerx>370:
                                                    i.moving_direction="left"
                                                if i.location.rect.centerx<370:
                                                    i.moving_direction="right"
                                            else:
                                                if i.location.rect.centerx>370 and i.location.rect.centery<220:
                                                    i.moving_direction="bottom_left"
                                                if i.location.rect.centerx>370 and i.location.rect.centery>220:
                                                    i.moving_direction="top_left"
                                                if i.location.rect.centerx<370 and i.location.rect.centery<220:
                                                    i.moving_direction="bottom_right"
                                                if i.location.rect.centerx<370 and i.location.rect.centery>220:
                                                    i.moving_direction="top_right"
                            if player_turn!=len(towns):
                                current_player=towns[player_turn] 
                                if current_player.ai==False:
                                    last_human_player=towns[player_turn] 
                                    cater_to_menu.blit(cater_to_clear, (0,5))
                                    for i in cater_to_hero_rect_list:
                                        cater_to_menu.blit(i[1], (i[2].left-128, i[2].top-355))
                                        if i[0] not in current_player.heroes_in_town:
                                            cater_to_menu.blit(blur_out_cater_to, (i[2].left-128, i[2].top-355))
                                    if current_player.constructing!=None:
                                        empty_production_wheel.blit(current_player.constructing_icon, (10,10))
                                current_player.gold+=current_player.gold_per_turn
                                functions.update_hero_events(current_player)
                                functions.apply_passive_hero_abilities(current_player)
                                functions.check_building_progress(current_player, towns)
                                functions.manage_population(current_player, turn_number)
                                functions.update_production(current_player)
                                functions.update_happiness(current_player, turn_number)
                                functions.update_to_build_menu(last_human_player, to_build_level_1_rect, to_build_level_2_rect, to_build_level_3_rect, to_build_hero_building_rect, to_build_unique_rect, to_build_other_rect, to_build_list, clear_to_build_tab, turns_to_build_font)
                                hero_info_screen=functions.update_hero_screen(last_human_player, hero_info_screen, hero_screen_clear, hero_info_font, towns)
                            
            to_build_discription_box.blit(to_build_discription_box_clear, (5,2))
            collisions=mouse.rect.colliderect(to_build_menu_rect)
            if collisions==1 or arrows_selected!=None:
                if to_build_menu_up==True:
                    #This part of the code is used when the user is scrolling 
                    #through the menue of things to build.
                    if scrolling_up==True:
                        if to_build_scroll_height!=0:
                            to_build_scroll_height+=10
                            for i in all_rects_in_to_build:
                                i.top+=10
                    if scrolling_down==True:
                        collisions_2=False
                        for i in to_build_group:
                            temp_collide=i.rect.colliderect(bottom_section_rect)
                            if temp_collide==1:
                                if i.level==1 and to_build_level_1_down==True:
                                    collisions_2=True
                                if i.level==2 and to_build_level_2_down==True:
                                    collisions_2=True
                                if i.level==3 and to_build_level_3_down==True:
                                    collisions_2=True
                                if i.level==0 and i.building_type=="hero building" and to_build_hero_building_down==True:
                                    collisions_2=True
                                if i.level==0 and i.building_type=="unique building" and to_build_unique_down==True:
                                    collisions_2=True
                                if i.level==0 and i.building_type=="other building" and to_build_other_down==True:
                                    collisions_2=True
                        for i in [to_build_level_1_rect, to_build_level_2_rect, to_build_level_3_rect, to_build_hero_building_rect, to_build_unique_rect, to_build_other_rect]:
                            temp_collide=i.colliderect(bottom_section_rect)
                            if temp_collide==1:
                                collisions_2=True
                        if collisions_2==True:
                            to_build_scroll_height-=10
                            for i in all_rects_in_to_build:
                                i.top-=10
                                
                    #This part of the code is used if the user clicks to build a
                    #building.
                    if current_player.ai==False:
                        collisions_2=pygame.sprite.spritecollide(mouse, to_build_group, False)
                        if len(collisions_2)!=0:
                            arrows_selected=None
                            arrows_selected_num=0
                            select_for_construction=False
                        if len(collisions_2)!=0 or arrows_selected!=None:
                            if arrows_selected!=None:
                                #if you selected a building using the arrow keys
                                modifier=1
                                if arrows_selected_num>7:
                                    modifier+=1
                                if arrows_selected_num>14:
                                    modifier+=1
                                if arrows_selected_num>21:
                                    modifier+=1
                                if arrows_selected_num>29:
                                    modifier+=1
                                if arrows_selected_num>45:
                                    modifier+=1
                                collisions_2=[to_build_list[arrows_selected_num-modifier]]
                            
                            #determining what you clicked on
                            #this is important since, if a building is built, it
                            #is no longer shown, and everything above it shifts
                            #upwards. This makes it so 2 Buildings_In_To_Build
                            #objects can exist in the same spot, and this code 
                            #is used to determine which one the user actually
                            #clicked on, and which one was being overlaped.
                            collision_to_use=None
                            for i in collisions_2:
                                valid_click=True
                                if i.building_type=="production building" and i.level<=current_player.production_building_level:
                                    valid_click=False
                                if i.building_type=="gold building" and i.level<=current_player.gold_building_level:
                                    valid_click=False
                                if i.building_type=="defence building" and i.level<=current_player.defence_building_level:
                                    valid_click=False
                                if i.building_type=="food building" and i.level<=current_player.food_building_level:
                                    valid_click=False
                                if i.building_type=="favor building" and i.level<=current_player.favor_building_level:
                                    valid_click=False
                                if i.building_type=="happiness building" and i.level<=current_player.happiness_building_level:
                                    valid_click=False
                                if i.name=="barracks" and current_player.warrior_building==True:
                                    valid_click=False
                                if i.name=="arcane_academy" and current_player.mage_building==True:
                                    valid_click=False
                                if i.name=="pub" and current_player.rogue_building==True:
                                    valid_click=False
                                if i.name=="church" and current_player.priest_building==True:
                                    valid_click=False
                                if i.name=="armory" and current_player.knight_building==True:
                                    valid_click=False
                                if i.name=="shooting_range" and current_player.archer_building==True:
                                    valid_click=False
                                if i.name=="stable" and current_player.pegasus_knight_building==True:
                                    valid_click=False
                                if i.name=="colosseum" and colosseum.built==True:
                                    valid_click=False
                                if i.name=="mystical_shrine" and mystical_shrine.built==True:
                                    valid_click=False
                                if i.name=="gambling_house" and gambling_house.built==True:
                                    valid_click=False
                                if i.name=="chapel" and chapel.built==True:
                                    valid_click=False
                                if i.name=="jousting_league" and jousting_league.built==True:
                                    valid_click=False
                                if i.name=="hunting_grounds" and hunting_grounds.built==True:
                                    valid_click=False
                                if i.name=="pegasus_olympics" and pegasus_olympics.built==True:
                                    valid_click=False
                                if i.name=="national_epic_(s)" and national_epic_s.built==True:
                                    valid_click=False
                                if i.name=="national_epic_(m)" and national_epic_m.built==True:
                                    valid_click=False
                                if i.name=="national_epic_(l)" and national_epic_l.built==True:
                                    valid_click=False
                                if i.name=="volcanic_forge" and volcanic_forge.built==True:
                                    valid_click=False
                                if i.name=="national_treasury" and national_treasury.built==True:
                                    valid_click=False
                                if i.name=="stronghold" and stronghold.built==True:
                                    valid_click=False
                                if i.name=="continental_gardens" and continental_gardens.built==True:
                                    valid_click=False
                                if i.name=="heroic_tribute" and heroic_tribute.built==True:
                                    valid_click=False
                                if i.name=="academy_of_art" and academy_of_art.built==True:
                                    valid_click=False
        
                                if valid_click==True:
                                    if i.level==1 and to_build_level_1_down==True:
                                        collision_to_use=i
                                    if i.level==2 and to_build_level_2_down==True:
                                        collision_to_use=i
                                    if i.level==3 and to_build_level_3_down==True:
                                        collision_to_use=i
                                    if i.level==0 and i.building_type=="hero building" and to_build_hero_building_down==True:
                                        collision_to_use=i
                                    if i.level==0 and i.building_type=="unique building" and to_build_unique_down==True:
                                        collision_to_use=i
                                    if i.level==0 and i.building_type=="other building" and to_build_other_down==True:
                                        collision_to_use=i
                            if collision_to_use!=None:
                                to_build_discription_box.blit(collision_to_use.discription_box, (3,2))
                                if clicked==True or select_for_construction==True:
                                    #This part of the code sees if the building
                                    #that was clicked on can be legaly built by
                                    #the user.
                                    valid_to_build=True
                                    if to_build_level_2_down==True and collision_to_use.level==2 and current_player.level_2_buildings_locked==True:
                                        valid_to_build=False
                                    if to_build_level_3_down==True and collision_to_use.level==3 and current_player.level_3_buildings_locked==True:
                                        valid_to_build=False
                                    if collision_to_use.building_type=="production building" and collision_to_use.level!=current_player.production_building_level+1:
                                        valid_to_build=False
                                    if collision_to_use.building_type=="gold building" and collision_to_use.level!=current_player.gold_building_level+1:
                                        valid_to_build=False
                                    if collision_to_use.building_type=="defence building" and collision_to_use.level!=current_player.defence_building_level+1:
                                        valid_to_build=False
                                    if collision_to_use.building_type=="food building" and collision_to_use.level!=current_player.food_building_level+1:
                                        valid_to_build=False
                                    if collision_to_use.building_type=="favor building" and collision_to_use.level!=current_player.favor_building_level+1:
                                        valid_to_build=False
                                    if collision_to_use.building_type=="happiness building" and collision_to_use.level!=current_player.happiness_building_level+1:
                                        valid_to_build=False
                                    if collision_to_use.building_type=="hero building" and current_player.favor_building_level==0:
                                        valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="colosseum":
                                        if colosseum.built==True or current_player.favor_building_level<2 or current_player.warrior_favor<classes.Hero.FavorForAlly or current_player.warrior_building==False:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="mystical_shrine":
                                        if mystical_shrine.built==True or current_player.favor_building_level<2 or current_player.mage_favor<classes.Hero.FavorForAlly or current_player.mage_building==False:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="gambling_house":
                                        if gambling_house.built==True or current_player.favor_building_level<2 or current_player.rogue_favor<classes.Hero.FavorForAlly or current_player.rogue_building==False:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="chapel":
                                        if chapel.built==True or current_player.favor_building_level<2 or current_player.priest_favor<classes.Hero.FavorForAlly or current_player.priest_building==False:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="jousting_league":
                                        if jousting_league.built==True or current_player.favor_building_level<2 or current_player.knight_favor<classes.Hero.FavorForAlly or current_player.knight_building==False:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="hunting_grounds":
                                        if hunting_grounds.built==True or current_player.favor_building_level<2 or current_player.archer_favor<classes.Hero.FavorForAlly or current_player.archer_building==False:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="pegasus_olympics":
                                        if pegasus_olympics.built==True or current_player.favor_building_level<2 or current_player.pegasus_knight_favor<classes.Hero.FavorForAlly or current_player.pegasus_knight_building==False:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="national_epic_(s)":
                                        if national_epic_s.built==True or current_player.level_1_buildings!=6:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="national_epic_(m)":
                                        if national_epic_m.built==True or current_player.level_2_buildings!=6:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="national_epic_(l)":
                                        if national_epic_l.built==True or current_player.level_3_buildings!=6:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="volcanic_forge":
                                        if volcanic_forge.built==True or current_player.production_building_level!=3:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="national_treasury":
                                        if national_treasury.built==True or current_player.gold_building_level!=3:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="stronghold":
                                        if stronghold.built==True or current_player.defence_building_level!=3:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="continental_gardens":
                                        if continental_gardens.built==True or current_player.food_building_level!=3:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="heroic_tribute":
                                        if heroic_tribute.built==True or current_player.favor_building_level!=3:
                                            valid_to_build=False
                                    if collision_to_use.building_type=="unique building" and collision_to_use.name=="academy_of_art":
                                        if academy_of_art.built==True or current_player.happiness_building_level!=3:
                                            valid_to_build=False
                                    
                                    if valid_to_build==True:
                                        current_player.constructing=collision_to_use
                                        current_player.constructing_icon=collision_to_use.icon_big
                                        empty_production_wheel.blit(collision_to_use.icon_big, (10,10))
                            select_for_construction=False
            
            #This part of the code displays messages for the user.
            if current_player.ai==True:
                current_player.messages_to_display=[]
            if current_player.messages_to_display!=[]:
                collisions=mouse.rect.colliderect(dismiss_event_button_rect)      
                if collisions==1 or pressed_o==True:
                    if clicked==True or pressed_o==True:
                        pressed_o=False
                        if len(current_player.messages_to_display)==1:
                            current_player.messages_to_display=[]
                        if len(current_player.messages_to_display)!=1:
                            current_player.messages_to_display=current_player.messages_to_display[1:]
                            
        if current_player.ai==False:
            if current_player.constructing==cater_to_build and clicked==True:
                for i in cater_to_hero_rect_list:
                    temp_collision=mouse.rect.colliderect(i[2])
                    if temp_collision==1:
                        if i[0] in current_player.heroes_in_town:
                            current_player.catering_to=i[0]
                        
        if arrows_selected!=None:
            while arrows_selected.bottom>bottom_section_rect.top:
                to_build_scroll_height-=10
                for i in all_rects_in_to_build:
                    i.top-=10
            while arrows_selected.top<to_build_menu_rect.top:
                to_build_scroll_height+=10
                for i in all_rects_in_to_build:
                    i.top+=10
                
        if hero_info_screen_up==True:
            collisions=mouse.rect.colliderect(exit_hero_info_button_rect)
            if collisions==1 or pressed_i==True:
                if clicked==True or pressed_i==True:
                    pressed_i=False
                    hero_info_screen_up=False
                
        if hero_turn==True and True not in [warrior.moving, mage.moving, rogue.moving, priest.moving, knight.moving, archer.moving, pegasus_knight.moving] and dragon_turn==False:
            
                
                
            hero_turn=False
            for i in towns:
                if i.eliminated==False:
                    i.hero_in_town=False
                    i.heroes_in_town=[]
                    if warrior.location==i:
                        i.hero_in_town=True
                        i.heroes_in_town+=[warrior]
                    if mage.location==i:
                        i.hero_in_town=True
                        i.heroes_in_town+=[mage]
                    if rogue.location==i:
                        i.hero_in_town=True
                        i.heroes_in_town+=[rogue]
                    if priest.location==i:
                        i.hero_in_town=True
                        i.heroes_in_town+=[priest]
                    if knight.location==i:
                        i.hero_in_town=True
                        i.heroes_in_town+=[knight]
                    if archer.location==i:
                        i.hero_in_town=True
                        i.heroes_in_town+=[archer]
                    if pegasus_knight.location==i:
                        i.hero_in_town=True
                        i.heroes_in_town+=[pegasus_knight]
                    
            player_turn=0
            while player_turn!=len(towns) and towns[player_turn].eliminated==True:
                player_turn+=1
            current_player=towns[player_turn] 
            if current_player.ai==False:
                last_human_player=towns[player_turn] 
                cater_to_menu.blit(cater_to_clear, (0,5))
                for i in cater_to_hero_rect_list:
                    cater_to_menu.blit(i[1], (i[2].left-128, i[2].top-355))
                    if i[0] not in current_player.heroes_in_town:
                        cater_to_menu.blit(blur_out_cater_to, (i[2].left-128, i[2].top-355))
                if current_player.constructing!=None:
                    empty_production_wheel.blit(current_player.constructing_icon, (10,10))
            current_player.gold+=current_player.gold_per_turn
            functions.update_hero_events(current_player)
            functions.apply_passive_hero_abilities(current_player)
            functions.check_building_progress(current_player, towns)
            functions.manage_population(current_player, turn_number)
            functions.update_production(current_player)
            functions.update_happiness(current_player, turn_number)
            functions.update_to_build_menu(last_human_player, to_build_level_1_rect, to_build_level_2_rect, to_build_level_3_rect, to_build_hero_building_rect, to_build_unique_rect, to_build_other_rect, to_build_list, clear_to_build_tab, turns_to_build_font)
            hero_info_screen=functions.update_hero_screen(last_human_player, hero_info_screen, hero_screen_clear, hero_info_font, towns)
        
        if hero_sprite_counter==2:
            hero_sprite_counter=0
        if dragon.sprite_phase!="moving" and dragon.sprite_phase!="falling_back" and dragon.sprite_phase!="recovering" :
            hero_group.update()
                
        if dragon_turn==True and hero_turn==False and dragon.attacking==None:
            dragon.attacks+=1
            dragon.attacking=dragon.to_attack_patern[dragon.attacks] 
            dragon.attack_stop_point=(dragon.to_attack_patern[-1].total_favor/dragon.attacking)*{}
                
        background.blit(full_map, (0, 20))
        town_group.draw(background)
        hero_group.draw(background)
        background.blit(arrow, (current_player.rect.centerx-10, current_player.rect.top-30))
        
        if dragon_turn==True:
            if True not in [warrior.moving, mage.moving, rogue.moving, priest.moving, knight.moving, archer.moving, pegasus_knight.moving] or dragon.sprite_phase!="intro":
                dragon_group.draw(background)
                dragon.update(towns)
                if dragon.on_screen==False:
                    dragon_turn=False
                    players_left=0
                    winner=None
                    for i in towns:
                        if i.eliminated==False:
                            players_left+=1
                            winner=i
                            
        if to_build_menu_up==True:
            #blitting all of the parts of the to menu of things to build.
            background.blit(to_build_menu_back, to_build_menu_rect)
            if to_build_level_1_down==False:
                img_to_use=to_build_level_1_plus
            if to_build_level_1_down==True:
                img_to_use=to_build_level_1_minus
                if last_human_player.production_building_level<1:
                    background.blit(workshop_to_build.image, workshop_to_build.rect)
                if last_human_player.gold_building_level<1:
                    background.blit(market_place_to_build.image, (market_place_to_build.rect))
                if last_human_player.defence_building_level<1:
                    background.blit(walls_to_build.image, (walls_to_build.rect))
                if last_human_player.food_building_level<1:
                    background.blit(wheat_feild_to_build.image, (wheat_feild_to_build.rect))
                if last_human_player.favor_building_level<1:
                    background.blit(garden_to_build.image, (garden_to_build.rect))
                if last_human_player.happiness_building_level<1:
                    background.blit(monument_to_build.image, (monument_to_build.rect))
            background.blit(img_to_use, (to_build_level_1_rect))
            if to_build_level_2_down==False:
                img_to_use=to_build_level_2_plus
            if to_build_level_2_down==True:
                img_to_use=to_build_level_2_minus
                if last_human_player.production_building_level<2:
                    background.blit(stone_works_to_build.image, (stone_works_to_build.rect))
                if last_human_player.gold_building_level<2:
                    background.blit(trading_post_to_build.image, (trading_post_to_build.rect))
                if last_human_player.defence_building_level<2:
                    background.blit(watchtower_to_build.image, (watchtower_to_build.rect))
                if last_human_player.food_building_level<2:
                    background.blit(farm_to_build.image, (farm_to_build.rect))
                if last_human_player.favor_building_level<2:
                    background.blit(inn_to_build.image, (inn_to_build.rect))
                if last_human_player.happiness_building_level<2:
                    background.blit(library_to_build.image, (library_to_build.rect))
            background.blit(img_to_use, (to_build_level_2_rect))
            if to_build_level_3_down==False:
                img_to_use=to_build_level_3_plus
            if to_build_level_3_down==True:
                img_to_use=to_build_level_3_minus
                if last_human_player.production_building_level<3:
                    background.blit(forge_to_build.image, (forge_to_build.rect))
                if last_human_player.gold_building_level<3:
                    background.blit(trade_network_to_build.image, (trade_network_to_build.rect))
                if last_human_player.defence_building_level<3:
                    background.blit(castle_to_build.image, (castle_to_build.rect))
                if last_human_player.food_building_level<3:
                    background.blit(granary_to_build.image, (granary_to_build.rect))
                if last_human_player.favor_building_level<3:
                    background.blit(theater_to_build.image, (theater_to_build.rect))
                if last_human_player.happiness_building_level<3:
                    background.blit(circus_to_build.image, (circus_to_build.rect))
            background.blit(img_to_use, (to_build_level_3_rect))
            
            if to_build_unique_down==False:
                img_to_use=to_build_unique_plus
            if to_build_unique_down==True:
                img_to_use=to_build_unique_minus
                if colosseum.built==False:
                    background.blit(colosseum_to_build.image, (colosseum_to_build.rect))
                if mystical_shrine.built==False:
                    background.blit(mystical_shrine_to_build.image, (mystical_shrine_to_build.rect))
                if gambling_house.built==False:
                    background.blit(gambling_house_to_build.image, (gambling_house_to_build.rect))
                if chapel.built==False:
                    background.blit(chapel_to_build.image, (chapel_to_build.rect))
                if jousting_league.built==False:
                    background.blit(jousting_league_to_build.image, (jousting_league_to_build.rect))
                if hunting_grounds.built==False:
                    background.blit(hunting_grounds_to_build.image, (hunting_grounds_to_build.rect))
                if pegasus_olympics.built==False:
                    background.blit(pegasus_olympics_to_build.image, (pegasus_olympics_to_build.rect))
                if national_epic_s.built==False:
                    background.blit(national_epic_s_to_build.image, (national_epic_s_to_build.rect))
                if national_epic_m.built==False:
                    background.blit(national_epic_m_to_build.image, (national_epic_m_to_build.rect))
                if national_epic_l.built==False:
                    background.blit(national_epic_l_to_build.image, (national_epic_l_to_build.rect))
                if volcanic_forge.built==False:
                    background.blit(volcanic_forge_to_build.image, (volcanic_forge_to_build.rect))
                if national_treasury.built==False:
                    background.blit(national_treasury_to_build.image, (national_treasury_to_build.rect))
                if stronghold.built==False:
                    background.blit(stronghold_to_build.image, (stronghold_to_build.rect))
                if continental_gardens.built==False:
                    background.blit(continental_gardens_to_build.image, (continental_gardens_to_build.rect))
                if heroic_tribute.built==False:
                    background.blit(heroic_tribute_to_build.image, (heroic_tribute_to_build.rect))
                if academy_of_art.built==False:
                    background.blit(academy_of_art_to_build.image, (academy_of_art_to_build.rect))
            background.blit(img_to_use, (to_build_unique_rect))
            
            if to_build_hero_building_down==False:
                img_to_use=to_build_hero_building_plus
            if to_build_hero_building_down==True:
                img_to_use=to_build_hero_building_minus
                if last_human_player.warrior_building==False:
                    background.blit(barracks_to_build.image, (barracks_to_build.rect))
                if last_human_player.mage_building==False:
                    background.blit(arcane_academy_to_build.image, (arcane_academy_to_build.rect))
                if last_human_player.rogue_building==False:
                    background.blit(pub_to_build.image, (pub_to_build.rect))
                if last_human_player.priest_building==False:
                    background.blit(church_to_build.image, (church_to_build.rect))
                if last_human_player.knight_building==False:
                    background.blit(armory_to_build.image, (armory_to_build.rect))
                if last_human_player.archer_building==False:
                    background.blit(shooting_range_to_build.image, (shooting_range_to_build.rect))
                if last_human_player.pegasus_knight_building==False:
                    background.blit(stable_to_build.image, (stable_to_build.rect))
            background.blit(img_to_use, (to_build_hero_building_rect))            
            if to_build_other_down==False:
                img_to_use=to_build_other_plus
            if to_build_other_down==True:
                img_to_use=to_build_other_minus
                background.blit(house_to_build.image, (house_to_build.rect))
                background.blit(cater_to_build.image, (cater_to_build.rect))
            background.blit(img_to_use, (to_build_other_rect))
            background.blit(to_build_discription_box, to_build_discription_box_rect)
            background.blit(to_build_menu, to_build_menu_rect)
            if last_human_player.constructing==cater_to_build:
                background.blit(cater_to_menu, (cater_to_menu_rect))
                
            if arrows_selected!=None:
                if arrows_selected==to_build_level_1_rect or arrows_selected==to_build_level_2_rect or arrows_selected==to_build_level_3_rect or arrows_selected==to_build_hero_building_rect or arrows_selected==to_build_unique_rect or arrows_selected==to_build_other_rect:
                    background.blit(to_build_selecter_s, (arrows_selected.left-1, arrows_selected.top))
                else:
                    background.blit(to_build_selecter_l, (arrows_selected.left, arrows_selected.top))
            
            
        #blitting images onto the top border
        production_amount_text=top_bar_amount_font.render("{}".format(last_human_player.production_progress), True, (207,133,0))
        if last_human_player.gold_per_turn>=0:
            gold_amount_text=top_bar_amount_font.render("{} (+{})".format(last_human_player.gold, last_human_player.gold_per_turn), True, (215,200,9))
        if last_human_player.gold_per_turn<0:
            gold_amount_text=top_bar_amount_font.render("{} ({})".format(last_human_player.gold, last_human_player.gold_per_turn), True, (215,200,9))
        defence_amount_text=top_bar_amount_font.render("{} (+{})".format(last_human_player.defence, len(last_human_player.heroes_in_town)*10), True, (79,90,238))
        food_amount_text=top_bar_amount_font.render("{}".format(last_human_player.food), True, (13,170,75))
        favor_amount_text=top_bar_amount_font.render("{}".format(last_human_player.favor), True, (231,76,60))
        happiness_amount_text=top_bar_amount_font.render("{}".format(last_human_player.happiness), True, (21,234,213))
        population_amount_text=top_bar_amount_font.render("{}".format(last_human_player.population), True, (32,255,47))
        houses_amount_text=top_bar_amount_font.render("{}".format(last_human_player.houses), True, (224,194,194))
        name_of_player_text=top_bar_amount_font.render("{}'s Turn".format(current_player.town_name), True, (255,255,255))
        turn_number_text=top_bar_amount_font.render("Turn: {}".format(turn_number), True, (252,238,197))
        
        background.blit(top_clear, (0, 0))
        background.blit(hammer_small, (3, 3))
        background.blit(production_amount_text, (20, 2))
        background.blit(gold_coin, (40, 3))
        background.blit(gold_amount_text, (57, 2))
        background.blit(defence_icon, (120, 3))
        background.blit(defence_amount_text, (137, 2))
        background.blit(food_icon, (190, 3))
        background.blit(food_amount_text, (207, 2))
        background.blit(favor_icon, (230, 3))
        background.blit(favor_amount_text, (247, 2))
        background.blit(happiness_icon, (270, 3))
        background.blit(happiness_amount_text, (287, 2))
        background.blit(population_icon, (310, 3))
        background.blit(population_amount_text, (327, 2))
        background.blit(houses_icon, (350, 3))
        background.blit(houses_amount_text, (367, 2))
        background.blit(name_of_player_text, (430, 2))
        background.blit(turn_number_text, (size[0]-turn_number_text.get_size()[0]-10, 2))
        
        background.blit(top_border, top_border_rect)
        background.blit(bottom_clear, (0, size[1]-80))
        background.blit(bottom_section, (bottom_section_rect))
            
        if True in [last_human_player.warrior_event, last_human_player.mage_event, last_human_player.rogue_event, last_human_player.priest_event, last_human_player.knight_event, last_human_player.archer_event, last_human_player.pegasus_knight_event]:
            turns_left_for_text=hero_event_info_bottom_font.render("Turns left for:", True, (255,255,255))
            background.blit(turns_left_for_text, (480, 403))
            event_text_x=400
            event_text_y=415
            if last_human_player.warrior_event==True:
                warrior_event_left_text=hero_event_info_bottom_font.render("Warrior Event: {}".format(last_human_player.turns_for_warrior_event), True, (255,255,255))
                background.blit(warrior_event_left_text, (event_text_x, event_text_y))
                event_text_y+=12
            if last_human_player.mage_event==True:
                mage_event_left_text=hero_event_info_bottom_font.render("Mage Event: {}".format(last_human_player.turns_for_mage_event), True, (255,255,255))
                background.blit(mage_event_left_text, (event_text_x, event_text_y))
                event_text_y+=12
            if last_human_player.rogue_event==True:
                rogue_event_left_text=hero_event_info_bottom_font.render("Rogue Event: {}".format(last_human_player.turns_for_rogue_event), True, (255,255,255))
                background.blit(rogue_event_left_text, (event_text_x, event_text_y))
                event_text_y+=12
            if last_human_player.priest_event==True:
                if event_text_y==451:
                    event_text_y=415
                    event_text_x+=100
                priest_event_left_text=hero_event_info_bottom_font.render("Priest Event: {}".format(last_human_player.turns_for_priest_event), True, (255,255,255))
                background.blit(priest_event_left_text, (event_text_x, event_text_y))
                event_text_y+=12
            if last_human_player.knight_event==True:
                if event_text_y==451:
                    event_text_y=415
                    event_text_x+=100
                knight_event_left_text=hero_event_info_bottom_font.render("Knight Event: {}".format(last_human_player.turns_for_knight_event), True, (255,255,255))
                background.blit(knight_event_left_text, (event_text_x, event_text_y))
                event_text_y+=12
            if last_human_player.archer_event==True:
                if event_text_y==451:
                    event_text_y=415
                    event_text_x+=100
                archer_event_left_text=hero_event_info_bottom_font.render("Archer Event: {}".format(last_human_player.turns_for_archer_event), True, (255,255,255))
                background.blit(archer_event_left_text, (event_text_x, event_text_y))
                event_text_y+=12
            if last_human_player.pegasus_knight_event==True:
                if event_text_x!=400:
                    event_text_y=451
                    event_text_x=400
                pegasus_knight_event_left_text=hero_event_info_bottom_font.render("Pegasus Knight Event: {}".format(last_human_player.turns_for_pegasus_knight_event), True, (255,255,255))
                background.blit(pegasus_knight_event_left_text, (event_text_x, event_text_y))
            
        background.blit(hero_info_button, hero_info_button_rect)
        
        display_next_turn=True
        if last_human_player.constructing==None:
            display_next_turn=False
            empty_production_wheel.blit(hammer, (10,10))
        if last_human_player.constructing==cater_to_build and last_human_player.catering_to==None:
            display_next_turn=False
        if display_next_turn==False:
            background.blit(chouse_production_bar, (chouse_production_bar_rect))
        if display_next_turn==True:
            background.blit(next_turn, (next_turn_rect))
        background.blit(empty_production_wheel, (empty_wheel_rect))
        
        if hero_info_screen_up==True:
            background.blit(hero_info_screen, (hero_info_screen_rect))
            background.blit(exit_hero_info_button, (exit_hero_info_button_rect))
        
        if hero_abilities_screen_up==True:
            pass
            
        if current_player.messages_to_display!=[] and hero_info_screen_up==False:
            dismiss_event_button_rect.top=current_player.messages_to_display[0].get_size()[1]+20
            background.blit(current_player.messages_to_display[0], (size[0]-200, 20))
            background.blit(dismiss_event_button, (dismiss_event_button_rect))
            
            
            
        #This part of the code simulates the ai's turn.
        if current_player.ai==True and hero_turn==False and dragon_turn==False and current_player.difficulty_level==1:
            current_player.constructing=None
            
            
            if current_player.production_building_level==0:
                current_player.constructing=workshop_to_build
            if current_player.defence_building_level==0 and current_player.constructing==None:
                current_player.constructing=walls_to_build
            if current_player.food_building_level==0 and current_player.constructing==None:
                current_player.constructing=farm_to_build
            if current_player.production_building_level==1 and current_player.constructing==None:
                current_player.constructing=stone_works_to_build
            if current_player.happiness_building_level==0 and current_player.constructing==None:
                current_player.constructing=monument_to_build
            if current_player.gold_building_level==0 and current_player.constructing==None:
                current_player.constructing=market_place_to_build
            if current_player.houses>20 and current_player.constructing==None:
                current_player.constructing=house_to_build
            if current_player.gold_building_level==1 and current_player.constructing==None:
                current_player.constructing=trading_post_to_build
            if current_player.favor_building_level==0 and current_player.constructing==None:
                current_player.constructing=garden_to_build
            if current_player.constructing==None and random.randrange(0,7)==0:
                functions.ai_build_hero_building(current_player, 3)
            if current_player.happiness_building_level==1 and current_player.constructing==None:
                current_player.constructing=library_to_build
            if current_player.defence_building_level==1 and current_player.constructing==None:
                current_player.constructing=castle_to_build
            if current_player.food_building_level==1 and current_player.constructing==None:
                current_player.constructing=granary_to_build
            
            
        if current_player.ai==True and hero_turn==False and dragon_turn==False and current_player.difficulty_level!=1:
            build_level_for_unlock=None
            
            if current_player.difficulty_level<4:
                current_player.constructing=None
                
            if current_player.constructing!=None and current_player.difficulty_level>=4:
                
                if current_player.constructing.building_type=="production building" and 1>current_player.production_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.building_type=="gold building" and 1>current_player.gold_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.building_type=="defence building" and 1>current_player.defence_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.building_type=="food building" and 1>current_player.food_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.building_type=="favor building" and 1>current_player.favor_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.building_type=="happiness building" and 1>current_player.happiness_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                #Hero buildings
                elif current_player.constructing.name=="barracks" and 1>current_player.warrior_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="arcane_academy" and 1>current_player.mage_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="pub" and 1>current_player.rogue_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="church" and 1>current_player.priest_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="armory" and 1>current_player.knight_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="shooting_range" and 1>current_player.archer_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="stable" and 1>current_player.pegasus_knight_building_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                #Unique buildings
                elif current_player.constructing.name=="colosseum" and 1>current_player.colosseum_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="mystical_shrine" and 1>current_player.mystical_shrine_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="gambling_house" and 1>current_player.gambling_house_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="chapel" and 1>current_player.chapel_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="jousting_league" and 1>current_player.jousting_league_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="hunting_grounds" and 1>current_player.hunting_grounds_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="pegasus_olympics" and 1>current_player.pegasus_olympics_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="national_epic_(s)" and 1>current_player.national_epic_s_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="national_epic_(m)" and 1>current_player.national_epic_m_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="national_epic_(l)" and 1>current_player.national_epic_l_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="volcanic_forge" and 1>current_player.volcanic_forge_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="national_treasury" and 1>current_player.national_treasury_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="stronghold" and 1>current_player.stronghold_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="continental_gardens" and 1>current_player.continental_gardens_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="heroic_tribute" and 1>current_player.heroic_tribute_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                elif current_player.constructing.name=="academy_of_art" and 1>current_player.academy_of_art_progress+(current_player.production_progress/current_player.constructing.production_needed)*2:
                    current_player.constructing=None
                #Houses
                elif current_player.constructing.name=="house":
                    current_player.constructing=None
                    
            
            #if the ai should build a gold building
            if current_player.constructing==None and current_player.gold_per_turn<=0 and current_player.gold<10:
                if current_player.gold_building_level==0:
                    current_player.constructing=trading_post_to_build
                if current_player.gold_building_level==1 and current_player.level_2_buildings_locked==False:
                    current_player.constructing=market_place_to_build
                if current_player.gold_building_level==1 and current_player.level_2_buildings_locked==True:
                    build_level_for_unlock=1
                if current_player.gold_building_level==2 and current_player.level_3_buildings_locked==False:
                    current_player.constructing=trade_network_to_build
                if current_player.gold_building_level==2 and current_player.level_3_buildings_locked==True:
                    build_level_for_unlock=2
                
            #if the ai should build a happiness building
            if current_player.constructing==None and current_player.happiness<=-8 and current_player.gold>0:
                if current_player.happiness_building_level==0:
                    current_player.constructing=monument_to_build
                if current_player.happiness_building_level==1 and current_player.level_2_buildings_locked==False:
                    build_level_for_unlock=1
                if current_player.happiness_building_level==1 and current_player.level_2_buildings_locked==True:
                    current_player.constructing=library_to_build
                if current_player.happiness_building_level==2 and current_player.level_3_buildings_locked==False:
                    current_player.constructing=circus_to_build
                if current_player.happiness_building_level==2 and current_player.level_3_buildings_locked==True:
                    build_level_for_unlock=2
                    
            #if the ai should build a happiness building
            if current_player.constructing==None and current_player.happiness<-4:
                if current_player.happiness_building_level==0:
                    current_player.constructing=monument_to_build
                if current_player.happiness_building_level==1 and current_player.level_2_buildings_locked==False:
                    current_player.constructing=library_to_build
                if current_player.happiness_building_level==1 and current_player.level_2_buildings_locked==True:
                    build_level_for_unlock=1
                if current_player.happiness_building_level==2 and current_player.level_3_buildings_locked==False:
                    current_player.constructing=circus_to_build
                if current_player.happiness_building_level==2 and current_player.level_3_buildings_locked==True:
                    build_level_for_unlock=2
                    
            #if the ai should build a food building
            if current_player.constructing==None and current_player.food<current_player.population:
                if current_player.food_building_level==0:
                    current_player.constructing=wheat_feild_to_build
                if current_player.food_building_level==1 and current_player.level_2_buildings_locked==False:
                    current_player.constructing=farm_to_build
                if current_player.food_building_level==1 and current_player.level_2_buildings_locked==True:
                    build_level_for_unlock=1
                if current_player.food_building_level==2 and current_player.level_3_buildings_locked==False:
                    current_player.constructing=grannary_to_build
                if current_player.food_building_level==2 and current_player.level_3_buildings_locked==True:
                    build_level_for_unlock=2
                    
            #if the ai should build a defence building
            if current_player.constructing==None and ((current_player.defence+(len(current_player.heroes_in_town)*10))+6)<current_player.population:
                if current_player.defence_building_level==0:
                    current_player.constructing=walls_to_build
                if current_player.defence_building_level==1 and current_player.level_2_buildings_locked==False:
                    current_player.constructing=watchtower_to_build
                if current_player.defence_building_level==1 and current_player.level_2_buildings_locked==True:
                    build_level_for_unlock=1
                if current_player.defence_building_level==2 and current_player.level_3_buildings_locked==False:
                    current_player.constructing=castle_to_build
                if current_player.defence_building_level==2 and current_player.level_3_buildings_locked==True:
                    build_level_for_unlock=2
                    
            #if the ai should build a gold building
            if current_player.constructing==None and current_player.gold_per_turn<0 and current_player.gold>=10:
                if current_player.gold_building_level==0:
                    current_player.constructing=trading_post_to_build
                if current_player.gold_building_level==1 and current_player.level_2_buildings_locked==False:
                    current_player.constructing=market_place_to_build
                if current_player.gold_building_level==1 and current_player.level_2_buildings_locked==True:
                    build_level_for_unlock=1
                if current_player.gold_building_level==2 and current_player.level_3_buildings_locked==False:
                    current_player.constructing=trade_network_to_build
                if current_player.gold_building_level==2 and current_player.level_3_buildings_locked==True:
                    build_level_for_unlock=2
                    
            #if the ai should build a defence building
            if current_player.constructing==None and (current_player.defence+(len(current_player.heroes_in_town)*10))<current_player.population:
                if current_player.defence_building_level==0:
                    current_player.constructing=walls_to_build
                if current_player.defence_building_level==1 and current_player.level_2_buildings_locked==False:
                    current_player.constructing=watchtower_to_build
                if current_player.defence_building_level==1 and current_player.level_2_buildings_locked==True:
                    build_level_for_unlock=1
                if current_player.defence_building_level==2 and current_player.level_3_buildings_locked==False:
                    current_player.constructing=castle_to_build
                if current_player.defence_building_level==2 and current_player.level_3_buildings_locked==True:
                    build_level_for_unlock=2
                    
                    
            #if the game is almost over and the ai should build a happiness building                    
            if current_player.constructing==None and current_player.happiness<0:
                    if current_player.happiness_building_level==0:
                        current_player.constructing=monument_to_build
                    if current_player.happiness_building_level==1 and current_player.level_2_buildings_locked==False:
                        current_player.constructing=library_to_build
                    if current_player.happiness_building_level==1 and current_player.level_2_buildings_locked==True:
                        build_level_for_unlock=1
                    if current_player.happiness_building_level==2 and current_player.level_3_buildings_locked==False:
                        current_player.constructing=circus_to_build
                    if current_player.happiness_building_level==2 and current_player.level_3_buildings_locked==True:
                        build_level_for_unlock=2
                    
                    
            #if the game is almost over and the ai should build a favor or happiness building
            if current_player.constructing==None and turn_number>=105 and current_player.difficulty_level>=4 and current_player.level_2_buildings_locked==False:
                
                if current_player.constructing==None and current_player.favor_building_level==1:
                    current_player.constructing=inn_to_build
                
                functions.ai_build_hero_building(current_player, 3)
                    
                if current_player.constructing==None and current_player.favor_building_level==2:
                    current_player.constructing=theater_to_build
                    
                if current_player.constructing==None and current_player.favor_building_level==3 and heroic_tribute_to_build.unique_object.built==False:
                    current_player.constructing=heroic_tribute_to_build
                    
                functions.ai_build_hero_building(current_player, 5)
                
                if current_player.constructing==None and current_player.favor_building_level>1:
                    all_left=[]
                    
                    if current_player.warrior_building==True and current_player.warrior_favor>=classes.Hero.FavorForAlly and colosseum_to_build.unique_object.built==False:
                        all_left+=[[current_player.colosseum_progress, colosseum_to_build]]
                    if current_player.mage_building==True and current_player.mage_favor>=classes.Hero.FavorForAlly and mystical_shrine_to_build.unique_object.built==False:
                        all_left+=[[current_player.mystical_shrine_progress, mystical_shrine_to_build]]
                    if current_player.priest_building==True and current_player.priest_favor>=classes.Hero.FavorForAlly and chapel_to_build.unique_object.built==False:
                        all_left+=[[current_player.chapel_progress, chapel_to_build]]
                    if current_player.rogue_building==True and current_player.rogue_favor>=classes.Hero.FavorForAlly and gambling_house_to_build.unique_object.built==False:
                        all_left+=[[current_player.gambling_house_progress, gambling_house_to_build]]
                    if current_player.knight_building==True and current_player.knight_favor>=classes.Hero.FavorForAlly and jousting_league_to_build.unique_object.built==False:
                        all_left+=[[current_player.jousting_league_progress, jousting_league_to_build]]
                    if current_player.archer_building==True and current_player.archer_favor>=classes.Hero.FavorForAlly and hunting_grounds_to_build.unique_object.built==False:
                        all_left+=[[current_player.hunting_grounds_progress, hunting_grounds_to_build]]
                    if current_player.pegasus_knight_building==True and current_player.pegasus_knight_favor>=classes.Hero.FavorForAlly and pegasus_olympics_to_build.unique_object.built==False:
                        all_left+=[[current_player.pegasus_olympics_progress, pegasus_olympics_to_build]]
                    
                    if all_left!=[]:
                        most_complete=[[-1]]
                        for i in all_left:
                            if i[0]>most_complete[0][0]:
                                most_complete=[i]
                            elif i[0]==most_complete[0][0]:
                                most_complete+=[i]
                                
                        current_player.constructing=most_complete[random.randrange(0, len(most_complete))][1]
                    
                functions.ai_build_hero_building(current_player, 7)  
                
                
                if current_player.constructing==None and current_player.happiness<6:
                    if current_player.happiness_building_level==0:
                        current_player.constructing=monument_to_build
                    if current_player.happiness_building_level==1 and current_player.level_2_buildings_locked==False:
                        current_player.constructing=library_to_build
                    if current_player.happiness_building_level==1 and current_player.level_2_buildings_locked==True:
                        build_level_for_unlock=1
                    if current_player.happiness_building_level==2 and current_player.level_3_buildings_locked==False:
                        current_player.constructing=circus_to_build
                    if current_player.happiness_building_level==2 and current_player.level_3_buildings_locked==True:
                        build_level_for_unlock=2
                
                        
            #Casual Construction
                            
            #if the ai should build a workshop
            if current_player.constructing==None and build_level_for_unlock==None and current_player.difficulty_level!=2:
                if current_player.production_building_level==0:
                    current_player.constructing=workshop_to_build  
                    
            #If its early enough for the ai to build a house
            if current_player.constructing==None and turn_number<100 and len(towns)<=4 and current_player.difficulty_level>=4:
                if current_player.houses<15:
                    current_player.constructing=house_to_build
            
                    
            #if the ai should build a garden
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.favor_building_level==0:
                    current_player.constructing=garden_to_build 
                        
            #if the ai should build a monument
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.happiness_building_level==0:
                    current_player.constructing=monument_to_build    
                    
            #if the ai should build a hero building
            functions.ai_build_hero_building(current_player, 1)
                        
            #if the ai should build walls
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.defence_building_level==0:
                    current_player.constructing=walls_to_build  
                        
            #if the ai should build a wheat feild
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.food_building_level==0:
                    current_player.constructing=wheat_feild_to_build  
                    
            #If the ai should build a house
            if current_player.constructing==None and turn_number<100 and current_player.difficulty_level!=2:
                if current_player.houses<22:
                    current_player.constructing=house_to_build
            
            #if the ai should build the stone works
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.production_building_level==1:
                    if current_player.level_2_buildings_locked==False:
                        current_player.constructing=stone_works_to_build     
                    if current_player.level_2_buildings_locked==True:
                        build_level_for_unlock=1    
                           
            #if the ai should build a unique building
            if current_player.constructing==None and build_level_for_unlock==None and current_player.difficulty_level!=2:
                #if the ai should build a national epic (small)
                if current_player.level_1_buildings==5 and national_epic_s.built==False:
                    if current_player.production_building_level==0:
                        current_player.constructing=workshop_to_build
                    if current_player.gold_building_level==0:
                        current_player.constructing=trading_post_to_build
                    if current_player.defence_building_level==0:
                        current_player.constructing=walls_to_build
                    if current_player.food_building_level==0:
                        current_player.constructing=wheat_feild_to_build
                    if current_player.favor_building_level==0:
                        current_player.constructing=garden_to_build
                    if current_player.happiness_building_level==0:
                        current_player.constructing=monument_to_build
                elif current_player.level_1_buildings==6 and national_epic_s.built==False:
                    current_player.constructing=national_epic_s_to_build
                    
                #if the ai should build a national epic (medium)
                elif current_player.level_2_buildings==6 and national_epic_m.built==False:
                    current_player.constructing=national_epic_m_to_build
                    
                #if the ai should build a national epic (large)
                elif current_player.level_3_buildings==6 and national_epic_l.built==False:
                    current_player.constructing=national_epic_l_to_build
                    
                #if the ai should build a hero unique
                hero_uniques=[]
                most_hero_unique_progress=-1
                if colosseum.built==False and current_player.warrior_favor>classes.Hero.FavorForAlly and current_player.warrior_building==True and current_player.favor_building_level>1:
                    hero_uniques+=[colosseum_to_build]
                    most_hero_unique_progress=current_player.colosseum_progress
                if mystical_shrine.built==False and current_player.mage_favor>classes.Hero.FavorForAlly and current_player.mage_building==True and current_player.favor_building_level>1:
                    if current_player.mystical_shrine_progress>most_hero_unique_progress:
                        hero_uniques=[mystical_shrine_to_build]
                        most_hero_unique_progress=current_player.mystical_shrine_progress
                    if current_player.mystical_shrine_progress==most_hero_unique_progress:
                        hero_uniques+=[mystical_shrine_to_build]
                if gambling_house.built==False and current_player.rogue_favor>classes.Hero.FavorForAlly and current_player.rogue_building==True and current_player.favor_building_level>1:
                    if current_player.gambling_house_progress>most_hero_unique_progress:
                        hero_uniques=[gambling_house_to_build]
                        most_hero_unique_progress=current_player.gambling_house_progress
                    if current_player.gambling_house_progress==most_hero_unique_progress:
                        hero_uniques+=[gambling_house_to_build]
                if chapel.built==False and current_player.priest_favor>classes.Hero.FavorForAlly and current_player.priest_building==True and current_player.favor_building_level>1:
                    if current_player.chapel_progress>most_hero_unique_progress:
                        hero_uniques=[chapel_to_build]
                        most_hero_unique_progress=current_player.chapel_progress
                    if current_player.chapel_progress==most_hero_unique_progress:
                        hero_uniques+=[chapel_to_build]
                if jousting_league.built==False and current_player.knight_favor>classes.Hero.FavorForAlly and current_player.knight_building==True and current_player.favor_building_level>1:
                    if current_player.jousting_league_progress>most_hero_unique_progress:
                        hero_uniques=[jousting_league_to_build]
                        most_hero_unique_progress=current_player.jousting_league_progress
                    if current_player.jousting_league_progress==most_hero_unique_progress:
                        hero_uniques+=[jousting_league_to_build]
                if hunting_grounds.built==False and current_player.archer_favor>classes.Hero.FavorForAlly and current_player.archer_building==True and current_player.favor_building_level>1:
                    if current_player.hunting_grounds_progress>most_hero_unique_progress:
                        hero_uniques=[hunting_grounds_to_build]
                        most_hero_unique_progress=current_player.hunting_grounds_progress
                    if current_player.hunting_grounds_progress==most_hero_unique_progress:
                        hero_uniques+=[hunting_grounds_to_build]
                if pegasus_olympics.built==False and current_player.pegasus_knight_favor>classes.Hero.FavorForAlly and current_player.pegasus_knight_building==True and current_player.favor_building_level>1:
                    if current_player.pegasus_olympics_progress>most_hero_unique_progress:
                        hero_uniques=[pegasus_olympics_to_build]
                        most_hero_unique_progress=current_player.pegasus_olympics_progress
                    if current_player.pegasus_olympics_progress==most_hero_unique_progress:
                        hero_uniques+=[pegasus_olympics_to_build]
                    
                if len(hero_uniques)==1:
                    current_player.constructing=hero_uniques[0]
                if len(hero_uniques)>1:
                    current_player.constructing=hero_uniques[random.randrange(0,len(hero_uniques))]
                    
            #if the ai should build an inn
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.favor_building_level==1:
                    if current_player.level_2_buildings_locked==False:
                        current_player.constructing=inn_to_build     
                    if current_player.level_2_buildings_locked==True:
                        build_level_for_unlock=1
                        
            #if the ai should build a library
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.happiness_building_level==1:
                    if current_player.level_2_buildings_locked==False:
                        current_player.constructing=library_to_build     
                    if current_player.level_2_buildings_locked==True:
                        build_level_for_unlock=1
                    
            #if the ai should build a hero building
            functions.ai_build_hero_building(current_player, 3)
                        
            #if the ai should build a theater
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.favor_building_level==2:
                    if current_player.level_3_buildings_locked==False:
                        current_player.constructing=theater_to_build     
                    if current_player.level_3_buildings_locked==True:
                        build_level_for_unlock=3
                            
            #if the ai should build a forge
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.production_building_level==2:
                    if current_player.level_3_buildings_locked==False:
                        current_player.constructing=forge_to_build     
                    if current_player.level_3_buildings_locked==True:
                        build_level_for_unlock=3
                            
            #if the ai should build a hero building
            if current_player.difficulty_level>=3 or random.randrange(0,4)==0:
                functions.ai_build_hero_building(current_player, 5)
                        
            #if the ai should build a circus
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.happiness_building_level==2:
                    if current_player.level_3_buildings_locked==False:
                        current_player.constructing=circus_to_build     
                    if current_player.level_3_buildings_locked==True:
                        build_level_for_unlock=3
                        
            #This makes the ai build a unique
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.production_building_level==3 and volcanic_forge.built==False:
                    current_player.constructing=volcanic_forge_to_build
                elif current_player.gold_building_level==3 and national_treasury.built==False:
                    current_player.constructing=national_treasury_to_build
                elif current_player.defence_building_level==3 and stronghold.built==False:
                    current_player.constructing=stronghold_to_build
                elif current_player.food_building_level==3 and continental_gardens.built==False:
                    current_player.constructing=continental_gardens_to_build
                elif current_player.favor_building_level==3 and heroic_tribute.built==False:
                    current_player.constructing=heroic_tribute_to_build
                elif current_player.happiness_building_level==3 and academy_of_art.built==False:
                    current_player.constructing=academy_of_art_to_build
                        
            #if the ai should build a house or a wheat feild
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.population<15:
                    if current_player.population==current_player.houses:
                        current_player.constructing=house_to_build
                    elif current_player.population==current_player.food and current_player.food_building_level==0:
                        current_player.constructing=wheat_feild_to_build
                        
            #if the ai should build a house or a farm
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.population<20:
                    if current_player.population==current_player.houses:
                        current_player.constructing=house_to_build
                    elif current_player.population==current_player.food and current_player.food_building_level==1:
                        if current_player.level_2_buildings_locked==False:
                            current_player.constructing=farm_to_build     
                        if current_player.level_2_buildings_locked==True:
                            build_level_for_unlock=1   
                        
            #if the ai should build a house or a garnnary                    
            if current_player.constructing==None and build_level_for_unlock==None:
                if current_player.population<26:
                    if current_player.population==current_player.houses:
                        current_player.constructing=house_to_build
                    elif current_player.population==current_player.food and current_player.food_building_level==2:
                        if current_player.level_3_buildings_locked==False:
                            current_player.constructing=grannary_to_build     
                        if current_player.level_3_buildings_locked==True:
                            build_level_for_unlock=2  
                         
            #This makes the ai build something to unlock the level 1 and 2 buildings                    
            if current_player.constructing==None and build_level_for_unlock==1:
                if current_player.production_building_level==0 and current_player.difficulty_level!=2:
                    current_player.constructing=workshop_to_build
                elif current_player.favor_building_level==0:
                    current_player.constructing=garden_to_build  
                elif current_player.happiness_building_level==0:
                    current_player.constructing=monument_to_build
                elif current_player.gold_building_level==0:
                    current_player.constructing=market_place_to_build
                    
            if current_player.constructing==None and build_level_for_unlock==2:
                if current_player.production_building_level==0 and current_player.difficulty_level!=2:
                    current_player.constructing=workshop_to_build
                elif current_player.production_building_level==1:
                    current_player.constructing=stone_works_to_build
                elif current_player.favor_building_level==0:
                    current_player.constructing=garden_to_build  
                elif current_player.favor_building_level==1:
                    current_player.constructing=inn_to_build  
                elif current_player.happiness_building_level==0:
                    current_player.constructing=monument_to_build  
                elif current_player.happiness_building_level==1:
                    current_player.constructing=library_to_build  
                elif current_player.gold_building_level==0:
                    current_player.constructing=market_place_to_build
                elif current_player.gold_building_level==1:
                    current_player.constructing=trading_post_to_build
        
        if current_player.ai==True and hero_turn==False and dragon_turn==False:  
            if current_player.constructing==None:
                current_player.constructing=house_to_build
                
            
            
                
            player_turn+=1
            while player_turn!=len(towns) and towns[player_turn].eliminated==True:
                player_turn+=1
            to_build_menu_up=False
            to_build_scroll_height=0
            to_build_level_1_down=False
            to_build_level_2_down=False
            to_build_level_3_down=False
            to_build_hero_building_down=False
            to_build_unique_down=False
            to_build_other_down=False
            arrows_selected=None
            arrows_selected_num=0
            if player_turn==len(towns):
                turn_number+=1
                hero_turn=True
                hero_sprite_counter=0
                functions.update_favor(towns)
                for i in towns:
                    i.turns_since_warrior_visit+=1
                    i.turns_since_mage_visit+=1    
                    i.turns_since_rogue_visit+=1    
                    i.turns_since_priest_visit+=1    
                    i.turns_since_knight_visit+=1    
                    i.turns_since_archer_visit+=1    
                    i.turns_since_pegasus_knight_visit+=1    
                for i in hero_group:                        
                    i.Move(towns)
                if turn_number==next_elimination:
                    if len(towns)!=2:
                        next_elimination+=int(1/(len(towns)-2)*30)
                    dragon_turn=True
                    dragon.eliminate_towns(towns)
                    for i in hero_group:
                        i.destination="middle"
                        i.c_destination="middle"
                        i.moving=True
                        if i.location!="middle":
                            if abs(i.location.rect.centerx-370)*2<abs(i.location.rect.centery-220):
                                if i.location.rect.centery>220:
                                    i.moving_direction="up"
                                if i.location.rect.centery<220:
                                    i.moving_direction="down"
                            elif abs(i.location.rect.centerx-370)>abs(i.location.rect.centery-220)*2:
                                if i.location.rect.centerx>370:
                                    i.moving_direction="left"
                                if i.location.rect.centerx<370:
                                    i.moving_direction="right"
                            else:
                                if i.location.rect.centerx>370 and i.location.rect.centery<220:
                                    i.moving_direction="bottom_left"
                                if i.location.rect.centerx>370 and i.location.rect.centery>220:
                                    i.moving_direction="top_left"
                                if i.location.rect.centerx<370 and i.location.rect.centery<220:
                                    i.moving_direction="bottom_right"
                                if i.location.rect.centerx<370 and i.location.rect.centery>220:
                                    i.moving_direction="top_right"
            if player_turn!=len(towns):
                current_player=towns[player_turn] 
                if current_player.ai==False:
                    last_human_player=towns[player_turn] 
                    cater_to_menu.blit(cater_to_clear, (0,5))
                    for i in cater_to_hero_rect_list:
                        cater_to_menu.blit(i[1], (i[2].left-128, i[2].top-355))
                        if i[0] not in current_player.heroes_in_town:
                            cater_to_menu.blit(blur_out_cater_to, (i[2].left-128, i[2].top-355))
                    if current_player.constructing!=None:
                        empty_production_wheel.blit(current_player.constructing_icon, (10,10))
                
                current_player.gold+=current_player.gold_per_turn
                functions.update_hero_events(current_player)
                functions.apply_passive_hero_abilities(current_player)
                functions.check_building_progress(current_player, towns)
                functions.manage_population(current_player, turn_number)
                functions.update_production(current_player)
                functions.update_happiness(current_player, turn_number)
                functions.update_to_build_menu(last_human_player, to_build_level_1_rect, to_build_level_2_rect, to_build_level_3_rect, to_build_hero_building_rect, to_build_unique_rect, to_build_other_rect, to_build_list, clear_to_build_tab, turns_to_build_font)
                hero_info_screen=functions.update_hero_screen(last_human_player, hero_info_screen, hero_screen_clear, hero_info_font, towns)
                
        if players_left==1:
            static_background=background
            congratulations_text=menu_font.render("Congratulations", True, (255,255,255))
            winner_name_text=menu_font.render(winner.town_name+"!", True, (255,255,255))
            you_have_managed_text=menu_font.render("You have managed", True, (255,255,255))
            to_outlast_all_text=menu_font.render("To outlast all", True, (255,255,255))
            other_towns_text=menu_font.render("other towns!", True, (255,255,255))
            you_win_text=menu_font.render("You win!", True, (255,255,255))
            in_game=False
            
            
    if True not in [in_game, on_main_menu, on_set_up_menu, on_how_to_play_menu]:
        #This part of the code blits the screen that congratulats the winner
        background.blit(static_background, (0,0))
        background.blit(winner_screen, (winner_screen_rect))
        background.blit(congratulations_text, ((size[0]/2)-(congratulations_text.get_size()[0]/2), 150))
        background.blit(winner_name_text, ((size[0]/2)-(winner_name_text.get_size()[0]/2), 170))
        background.blit(you_have_managed_text, ((size[0]/2)-(you_have_managed_text.get_size()[0]/2), 190))
        background.blit(to_outlast_all_text, ((size[0]/2)-(to_outlast_all_text.get_size()[0]/2), 210))
        background.blit(other_towns_text, ((size[0]/2)-(other_towns_text.get_size()[0]/2), 230))
        background.blit(you_win_text, ((size[0]/2)-(you_win_text.get_size()[0]/2), 250))
        background.blit(title_return_button, (title_return_button_rect))
        background.blit(title_return_text, (title_return_text_rect))
        
        collisions=mouse.rect.colliderect(title_return_text_rect)
        if collisions==1 and clicked==True:
            #This part of the code resets the game.
            players_left=0
            for i in towns:
                i.kill()
            classes.Town.players=0
            
            warrior.kill()
            rogue.kill()
            mage.kill()
            rogue.kill()
            priest.kill()
            knight.kill()
            archer.kill()
            pegasus_knight.kill()
            classes.Hero.heroes=[]
            
            dragon.kill()
            
            classes.Unique_Building.uniques_built=0
            for i in classes.Unique_Building.uniques:
                i.built=False
            
            towns=[]
            for i in range(0,2):
                temp_town=classes.Town("Player "+str(i+1), False, town, town_distroyed)
                towns+=[temp_town]
            town_group=pygame.sprite.Group(towns)
            
            warrior=classes.Hero("Eirika", "warrior", img_dirr, helvet)
            mage=classes.Hero("Lute", "mage", img_dirr, helvet)
            rogue=classes.Hero("Colm", "rogue", img_dirr, helvet)
            priest=classes.Hero("Moulder", "priest", img_dirr, helvet)
            knight=classes.Hero("Seth", "knight", img_dirr, helvet)
            archer=classes.Hero("Innes", "archer", img_dirr, helvet)
            pegasus_knight=classes.Hero("Venessa", "pegasus_knight", img_dirr, helvet)
            
            hero_group=pygame.sprite.OrderedUpdates([warrior, pegasus_knight, mage, archer, rogue, knight, priest])
            
            dragon=classes.Dragon(img_dirr)
            dragon_group=pygame.sprite.Group(dragon)
            dragon_turn=False  
            
            turn_number=1
            on_main_menu=True
            
    m_group.update()            
    screen.blit(background, (0, 0))
    pygame.display.flip()