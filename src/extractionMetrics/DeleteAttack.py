import random

# Add random noise (+- 10%) to the dataset return the updated array.
def deleteAttack(x, percentage):
    # Get some basic info like the original size of the data.
    size = len(x)
    var_size = len(x)

    # For a certain percentage of the data.
    for _ in range(int(size * percentage)):
        toDeleteIndex = random.randint(0, var_size - 1)
        x.pop(toDeleteIndex)
        var_size = len(x)
    return x
 
