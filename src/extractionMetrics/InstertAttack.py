import random

# Add random noise (+- 10%) to the dataset return the updated array.
def insertionAttack(x, percentage):
    # Get some basic info like the size and dimensions of the data.
    size = len(x)
    dim = len(x[0])

    # Keep track of updated indeces
    updated = set()

    # For a certain percentage of the data.
    for _ in range(int(size * percentage)):
        toUpdateIndex = random.randint(0, size - 1)
        while (updated.__contains__(toUpdateIndex)):
            toUpdateIndex = random.randint(0, size)

        new = []
        for _ in range(dim):
            new.append(random.randint(0, 100))
        x[toUpdateIndex] = new

    return x
 

