import random
from UpdateAttack import updateAttack
from ZeroOutAttack import zeroOutAttack
from DeleteAttack import deleteAttack
from InstertAttack import insertionAttack

# Add random noise (+- 10%) to the dataset return the updated array.
def multiFacedAttack(x, percentage):
    x = updateAttack(x, 0.3*percentage)
    x = insertionAttack(x, 0.3*percentage)
    x = deleteAttack(x, 0.3*percentage)
        
    return x
 
