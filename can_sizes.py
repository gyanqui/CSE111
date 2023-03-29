"""
File: L04 Teach: Team Activity
Author: Gab Yanqui
Date: 01/24/2023
Purpose: Practice calling functions applying a discount. 
"""
"""
Write a Python program named can_sizes.py that computes and prints the storage 
efficiency for each of the following 12 steel can sizes. Then visually examine the 
output and answer this question, “Which can size has the highest storage efficiency?”

Name Radius(cm) Height(cm) Cost per Can(U.S. dollars)
#1 Picnic	6.83	10.16	$0.28
#1 Tall	    7.78	11.91	$0.43
#2	        8.73	11.59	$0.45
#2.5	    10.32	11.91	$0.61
#3 Cylinder	10.79	17.78	$0.86
#5	        13.02	14.29	$0.83
#6Z	        5.40	8.89	$0.22
#8Z short	6.83	7.62	$0.26
#10	        15.72	17.78	$1.53
#211	    6.83	12.38	$0.34
#300	    7.62	11.27	$0.38
#303	    8.10	11.11	$0.42
"""
from math import pi

print(f'\tName              Volume   Surface Area   Storage efficiency   Cost Efficiency')

def main():
    # Create a list for each attributes of the can
    can_names = [
        "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", 
        "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"
    ]
    can_radiuses = [
        6.83, 7.78, 8.73, 10.32, 10.79, 13.02,
        5.4, 6.83, 15.72, 6.83, 7.62, 8.1
    ]
    can_heights = [
        10.16, 11.91, 11.59, 11.91, 17.78, 14.29,
        8.89, 7.62, 17.78, 12.38, 11.27, 11.11
    ]
    can_costs = [
        0.28, 0.43, 0.45, 0.61, 0.86, 0.83,
        0.22, 0.26, 1.53, 0.34, 0.38, 0.42
    ]

    # Create variable to compute the best store and cost
    best_store = None
    best_cost = None
    max_store_eff = -1
    max_cost_eff = -1

    # For each can in the parallel lists, unpack the values
    # into the variables name, radius, height, and cost.
    for i in range(len(can_names)):
        name= can_names[i]
        radius= can_radiuses[i]
        height= can_heights[i]
        cost= can_costs[i]

        # Call the volume fuction to get the volume of the cans
        volume = compute_volume(radius, height)
        # Call the surface_area fuction to get the surface area of the cans
        surface_area = compute_surface_area(radius, height)
        # Call the storage_efficiency fuction to get the storage
        # eff. of the cans
        store_eff = compute_storage_efficiency(radius, height)
        # Call the cost_eff fuction to get the cost eff. of the cans
        cost_eff = compute_cost_efficiency(radius, height, cost)

        # Print the can size name, storage and cost efficiency
        print(f'\t{name:13} {volume:10.2f} {surface_area:14.2f} {store_eff:19.2f} {cost_eff:17.0f}')

        # If the storage efficiency of the current can size is
        # greater than the maximum storage efficiency, save then
        # the current can size name and its storage efficiency.
        if store_eff > max_store_eff:
            best_store = name
            max_store_eff = store_eff

        # If the cost efficiency of the current can size is
        # greater than the maximum cost efficiency, then save
        # the current can size name and its cost efficiency.
        if cost_eff > max_cost_eff:
            best_cost = name
            max_cost_eff = cost_eff

    print()#blank line
    #Print the best storage and cost efficiency
    print(f'Best can size in storage efficiency: {best_store}')
    print(f'Best can size in cost efficiency: {best_cost}')

def compute_volume(radius, height):
    """Compute and return the volume of a cyinder.
    
    Parameters:
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the volume of the cylinder
    """
    volume = pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder.
    
    Parameters:
        radius: the radius of the cylinder
        height: the height of the cylinder
    Return: the surface area of the cylinder
    """
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    """Compute and return the storage efficiency of the can list

    Parameters:
        radius: the radius of the can
        height: the height of the can
    Return: the storage efficiency of the can
    """
    # Call the volume function to get the volume of the cylinder
    volume = compute_volume(radius, height)
    # Call the surface_area function to get the surface area of the cylinder
    surface_area = compute_surface_area(radius, height)
    storage_efficiency= volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(radius, height, cost):
    """Compute and return the cost efficiency of the can list

    Parameters:
        radius: the radius of the can
        height: the height of the can
        cost: cost of the can
    Return: the cost efficiency of the can
    """
    # Call the volume function to get the volume of the cylinder
    volume = compute_volume(radius, height)
    cost_efficiency = volume / cost
    return cost_efficiency

# Start program
main()