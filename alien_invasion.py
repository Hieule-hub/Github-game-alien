import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
    #Initialize game and create a screen abject.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    
    #Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens, bullets)
        




run_game()