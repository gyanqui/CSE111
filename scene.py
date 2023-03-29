"""
File: L04 Prove: Assignment
Author: Gab Yanqui
Date: 01/28/2023
Purpose: Write User-Defined with parameters and call
those functions multiple times with arguments.
"""
"""
You work for a retail store that wants to increase sales on Tuesday
Write a Python program that draws a semi-realistic outdoor scene
in a computer window. Your program can draw any outdoor scene that 
you like as long as it meets these requirements:

The scene must be outdoor and include part of the sky.
The sky must have clouds.
The scene must include repetitive objects, such as blades of grass, 
trees, leaves on a tree, birds, flowers, insects, fish, pickets in 
a fence, dashed lines on a road, buildings, bales of hay, snowmen, 
snowflakes, or icicles.
Your program must be divided into functions such as draw_sky, 
draw_cloud, draw_ground, draw_bird, draw_flower, draw_insect, 
draw_fish, or draw_snowman.
Each of the objects in your scene should be drawn in its own 
function. To draw the shapes in the scene, your program will call 
functions in a Python library named Draw 2-D.
"""

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_oval, \
    draw_rectangle, draw_polygon, finish_drawing

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    # draw_sky(canvas, scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the draw_moon function to draw the moon in the sky
    draw_moon(canvas, 0, 300, 200, 500)

    # Call the draw_cloud fuction to draw a cloud 1
    draw_clouds(canvas, 150, 275, 230, 350)
    # Call the draw_cloud fuction to draw a cloud 2
    draw_clouds(canvas, 200, 275, 280, 350)
    # Call the draw_cloud fuction to draw a cloud 3
    draw_clouds(canvas, 250, 275, 330, 350)
    
    # Call the draw_cloud fuction to draw a cloud 4
    draw_clouds(canvas, 230, 350, 310, 425)
    # Call the draw_cloud fuction to draw a cloud 5
    draw_clouds(canvas, 280, 350, 360, 425)
    # Call the draw_cloud fuction to draw a cloud 6
    draw_clouds(canvas, 330, 350, 410, 425)
    # Call the draw_cloud fuction to draw a cloud 7
    draw_clouds(canvas, 380, 350, 460, 425)

    # Call the draw_cloud fuction to draw a cloud 8
    draw_clouds(canvas, 400, 275, 480, 350)
    # Call the draw_cloud fuction to draw a cloud 9
    draw_clouds(canvas, 450, 275, 530, 350)
    # Call the draw_cloud fuction to draw a cloud 10
    draw_clouds(canvas, 500, 275, 580, 350)
    
    # Call the draw_cloud fuction to draw a cloud 11
    draw_clouds(canvas, 530, 350, 610, 425)
    # Call the draw_cloud fuction to draw a cloud 12
    draw_clouds(canvas, 580, 350, 660, 425)
    # Call the draw_cloud fuction to draw a cloud 13
    draw_clouds(canvas, 630, 350, 710, 425)
    # Call the draw_cloud fuction to draw a cloud 14
    draw_clouds(canvas, 680, 350, 760, 425)

    # Call the draw_pine_tree fuction to draw a pine tree 1
    draw_pine_tree(canvas, 400, 400)
    # Call the draw_pine_tree fuction to draw a pine tree 2
    draw_pine_tree(canvas, 550, 400)
    # Call the draw_pine_tree fuction to draw a pine tree 3
    draw_pine_tree(canvas, 700, 400)

    # Call the draw_cloud fuction to draw a grass 1
    draw_grass(canvas, 10, 100, 20, 100)
    # Call the draw_cloud fuction to draw a grass 2
    draw_grass(canvas, 30, 100, 40, 120)
    # Call the draw_grass fuction to draw a grass 3
    draw_grass(canvas, 50, 100, 60, 100)
    # Call the draw_cloud fuction to draw a grass 4
    draw_grass(canvas, 70, 100, 80, 120)
    # Call the draw_cloud fuction to draw a grass 5
    draw_grass(canvas, 90, 100, 100, 100)
    # Call the draw_cloud fuction to draw a grass 6 
    draw_grass(canvas, 110, 100, 120, 120)
    # Call the draw_cloud fuction to draw a grass 7
    draw_grass(canvas, 130, 100, 140, 100)
    # Call the draw_cloud fuction to draw a grass 8
    draw_grass(canvas, 150, 100, 160, 120)
    # Call the draw_cloud fuction to draw a grass 9
    draw_grass(canvas, 170, 100, 180, 100)
    # Call the draw_cloud fuction to draw a grass 10
    draw_grass(canvas, 190, 100, 200, 120)
    # Call the draw_cloud fuction to draw a grass 11
    draw_grass(canvas, 210, 100, 220, 100)
    # Call the draw_cloud fuction to draw a grass 12
    draw_grass(canvas, 230, 100, 240, 120)
    # Call the draw_cloud fuction to draw a grass 13
    draw_grass(canvas, 250, 100, 260, 100)
    # Call the draw_cloud fuction to draw a grass 14
    draw_grass(canvas, 270, 100, 280, 120)
    # Call the draw_cloud fuction to draw a grass 15
    draw_grass(canvas, 290, 100, 300, 100)
    # Call the draw_cloud fuction to draw a grass 16
    draw_grass(canvas, 310, 100, 320, 120)
    # Call the draw_cloud fuction to draw a grass 17
    draw_grass(canvas, 330, 100, 340, 100)
    # Call the draw_cloud fuction to draw a grass 18
    draw_grass(canvas, 350, 100, 360, 120)
    # Call the draw_cloud fuction to draw a grass 19
    draw_grass(canvas, 370, 100, 380, 100)
    # Call the draw_cloud fuction to draw a grass 20
    draw_grass(canvas, 390, 100, 400, 120)
    # Call the draw_cloud fuction to draw a grass 21
    draw_grass(canvas, 410, 100, 420, 100)
    # Call the draw_cloud fuction to draw a grass 22
    draw_grass(canvas, 430, 100, 440, 120)
    # Call the draw_cloud fuction to draw a grass 23
    draw_grass(canvas, 450, 100, 460, 100)
    # Call the draw_cloud fuction to draw a grass 24
    draw_grass(canvas, 470, 100, 480, 120)
    # Call the draw_cloud fuction to draw a grass 25
    draw_grass(canvas, 490, 100, 500, 100)
    # Call the draw_cloud fuction to draw a grass 26
    draw_grass(canvas, 510, 100, 520, 120)
    # Call the draw_cloud fuction to draw a grass 27
    draw_grass(canvas, 530, 100, 540, 100)
    # Call the draw_cloud fuction to draw a grass 28
    draw_grass(canvas, 550, 100, 560, 120)
    # Call the draw_cloud fuction to draw a grass 29
    draw_grass(canvas, 570, 100, 580, 100)
    # Call the draw_cloud fuction to draw a grass 30
    draw_grass(canvas, 590, 100, 600, 120)
    # Call the draw_cloud fuction to draw a grass 31
    draw_grass(canvas, 610, 100, 620, 100)
    # Call the draw_cloud fuction to draw a grass 32
    draw_grass(canvas, 630, 100, 640, 120)
    # Call the draw_cloud fuction to draw a grass 33
    draw_grass(canvas, 650, 100, 660, 100)
    # Call the draw_cloud fuction to draw a grass 34
    draw_grass(canvas, 670, 100, 680, 120)
    # Call the draw_cloud fuction to draw a grass 35
    draw_grass(canvas, 690, 100, 700, 100)
    # Call the draw_cloud fuction to draw a grass 36
    draw_grass(canvas, 710, 100, 720, 120)
    # Call the draw_cloud fuction to draw a grass 37
    draw_grass(canvas, 730, 100, 740, 100)
    # Call the draw_cloud fuction to draw a grass 38
    draw_grass(canvas, 750, 100, 760, 120)
    # Call the draw_cloud fuction to draw a grass 39
    draw_grass(canvas, 770, 100, 780, 100)
    # Call the draw_cloud fuction to draw a grass 40
    draw_grass(canvas, 790, 100, 800, 120)

    # Call the finish_drawing fuction to finish drawing in the canvas
    finish_drawing(canvas)

def draw_sky(canvas, width, height):
    """Compute the coordinates where to draw the sky in our canvas using
        width, and height.
    
    Parameters
        canvas: The canvas where this function
            will draw a grass. 
        width: the width in pixel of the canvas
        height: the height in pixel of the canvas
    Return: nothing
    """
    # Draw the sky
    draw_rectangle(canvas, 
        width *  0, height / 3, width, height, width=0, fill="blue4")

def draw_ground(canvas, width, height):
    """Compute the coordinates where to draw the ground in our canvas using
        width, and height.
    
    Parameters
        canvas: The canvas where this function
            will draw a grass. 
        width: the width in pixel of the canvas
        height: the height in pixel of the canvas
    Return: nothing
    """

    # Draw the ground
    draw_rectangle(canvas, 
        width * 0, height * 0, width, height / 3, width=0, fill= "tan4")

def draw_moon(canvas, moon_left, moon_bottom, moon_right, moon_top):
    """Compute the coordinates where to draw the moon in our canvas using
        moon_left, moon_bottom, moon_right, moon_top
    
    Parameter
        Parameters: 
        canvas: The canvas where this function
            will draw a moon. 
        moon_left: moon left coordinate
        moon_right: moon right coordinate
        moon_bottom: moon bottom coordinate
        moon_top: moon top coordinate
    Return: nothing
    """
    # Draw the moon
    draw_oval(canvas, 
        moon_left, moon_bottom, moon_right, 
        moon_top, outline="gray20", width=0, fill= "white")

def draw_clouds(canvas, cloud_left, cloud_bottom, cloud_right, cloud_top):
    """Compute the coordinates where to draw the cloud in our canvas using
        peak_x0, peak_y0, peak_x1, peak_y1
    
    Parameter
        Parameters: 
        canvas: The canvas where this function
            will draw a cloud. 
        cloud_left: cloud left coordinate
        cloud_right: cloud right coordinate
        cloud_bottom: cloud bottom coordinate
        cloud_top: cloud top coordinate
    Return: nothing
    """
    # Draw the cloud
    draw_oval(canvas, 
        cloud_left, cloud_bottom, cloud_right, 
        cloud_top, outline="gray20", width=0, fill= "steelblue4")

def draw_grass(canvas, peak_x0, peak_y0, peak_x1, peak_y1):
    """Draw one grass at location (peak_x0, peak_y0, peak_x1, peak_y1)
    
    Parameters: 
        canvas: The canvas where this function
            will draw a grass. 
        peak_x0: grass left coordinate
        peak_x1: grass right coordinate
        peak_y0: grass bottom coordinate
        peak_y1: grass top coordinate
    Return: nothing
    """
    # Compute the coordinates of the grass.
    grass_left = peak_x0 - 5
    grass_right = peak_x1
    grass_bottom = peak_y0 -50
    grass_top = peak_y1
    # Draw the grass
    draw_rectangle(canvas, 
        grass_left, grass_bottom, grass_right, 
        grass_top, width=0, fill="green")

def draw_pine_tree(canvas, peak_x, peak_y):
    """Draw one pine tree at location (peak_x, peak_y)
    Parameters
        canvas: The canvas where this function
            will draw a grass. 
        peak_x: pine tree left and right location
        peak_y: pine tree coordinate to get the bottom
    Return: nothing
    """
    # Compute the coordinates of the skirt and trunk.
    skirt_left  = peak_x - 70
    skirt_right = peak_x + 70
    skirt_bottom = peak_y - 210

    trunk_left  = peak_x - 10
    trunk_right = peak_x + 10
    trunk_bottom = peak_y - 260

    # Draw the tree trunk.
    draw_rectangle(canvas, trunk_left, trunk_bottom,
            trunk_right, skirt_bottom, fill="brown")
    # Draw the tree skirt.
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,
            skirt_right, skirt_bottom, fill="forestGreen")

# Call the main function so that
# this program will start executing.
main()