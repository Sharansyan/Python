# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:44:50 2020

@author: Sharan
"""

from PIL import Image

end=100

def show_board():
    img = Image.open('Game_1.jpg')
    img.show()
    
show_board()