import random
import string

def create_gen(panjang_gen):
    """Membuat string acak dari karakter ASCII 32–126."""
    gen = ''.join(chr(random.randint(32, 126)) for _ in range(panjang_gen))
    return gen