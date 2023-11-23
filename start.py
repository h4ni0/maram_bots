import os
from dotenv import load_dotenv

load_dotenv()

"""
This file is the entry file of the program
"""
from bots.ten_recitations import TenRecitations


TenRecitations(os.getenv('TR_TOKEN')).run()
