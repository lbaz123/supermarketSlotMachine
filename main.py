import pandas as pd

from models.Iceland import Iceland
from models.Sainsburys import Sainsburys
from models.Asda import Asda
from models.Tesco import Tesco
from models.Waitrose import Waitrose
from models.Morrisons import Morrisons
from models.Ocado import Ocado

def find_all_slots(list_of_shops: list):

	slots: list = list()

	switcher: dict = {
	'sainsburys': Sainsburys,
	'tesco': Tesco,
	'waitrose': Waitrose,
	'ocado': Ocado,
	'morrisons': Morrisons,
	'iceland': Iceland,
	'asda': Asda
	}

	for supermarket in list_of_shops:

		if supermarket in switcher:
			slotFinder = switcher[supermarket]()		
		
			slots.append(slotFinder.find_slots())
		else:
			raise ValueError('Invalid supermarket name!')	

	df = pd.DataFrame(slots)
	df.to_csv('available_slots.csv', index = False)

list_of_shops = ['sainsburys','tesco','waitrose','morrisons','ocado','iceland','asda']

find_all_slots(list_of_shops)
