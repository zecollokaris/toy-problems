#############################################################################################################

######Question######

# Create a combat function that takes the player's current health and the amount of damage recieved, 

# and returns the player's new health. 

# Health can't be less than 0.

#############################################################################################################

######BDD######

# 1. Subtract health - damage

# 2. If health - damge is less than 0 we must return 0
 
# 3. return health - damage 

#############################################################################################################

######Solution#####

def combat(health,damage):
    if health-damage < 0:
        return 0
    return health - damage

#############################################################################################################
#############################################################################################################