#modules
# lefchiper/__init__.py

from .core.glasicc import glasicc_encrypt, glasicc_decrypt
from .core.lefchaos import chaos_encrypt, chaos_decrypt
from .core.lefchaos import chaos_encrypt as encrypt, chaos_decrypt as decrypt
from .core.lefkey import generate_key
