import random
import string

def mutation(child, laju_mutasi):
    """Melakukan mutasi dengan probabilitas laju_mutasi."""
    mutant = child.copy()

    gen_list = list(mutant["gen"])

    for i in range(len(gen_list)):
        if random.random() <= laju_mutasi:
            gen_list[i] = chr(random.randint(32, 126))

    mutant["gen"] = "".join(gen_list)
    return mutant
