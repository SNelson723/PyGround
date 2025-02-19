# Step 1 => Install pywebio => DONE
# Step 2 => Import all required modules
# Step 3 => Set GET requests with requests.requerst()

import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact():
  # Clear the screen
  clear()
  
  # Put HTML content for the fun fact generator header
  # put_