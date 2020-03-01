import sys
import os
import time
import random

default_delay = 0.001
default_num_words = 3
password_database = 'data/ultimate.txt'

def random_char():
   return chr(random.randrange(32, 128))

def simulate_hack(password, delay):
   guess = ''
   for ch in password:
      rand = random_char()
      while rand != ch:
         print(f'\r{guess}{rand}', end='')
         sys.stdout.flush()
         time.sleep(delay)
         rand = random_char()
      guess += ch
   print('\r' + guess)

def retrieve_password(hint, num_words):
   random.seed(hint)
   with open(password_database) as pass_db:
      possible_pass_list = pass_db.read().split('\n')
      pass_indices = random.sample(range(0, len(possible_pass_list)), k=num_words)
      full_password = ''.join([possible_pass_list[i].title() for i in pass_indices])
   return full_password + str(random.randrange(0, 100))

def hack(hint):
   """finds the password in the ultimate database that corresponds to the 
   advice given by 'hint'. time_constraint is the number of seconds that this 
   function must find the password by. 'hack' will succeed in finding a 
   password no matter the case."""
   password = retrieve_password(hint, default_num_words)
   simulate_hack(password, default_delay)