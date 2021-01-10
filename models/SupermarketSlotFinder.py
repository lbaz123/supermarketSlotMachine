from abc import ABC, abstractmethod
import io 
from bs4 import BeautifulSoup

class SupermarketSlotFinder(ABC):

	def open_html_file(self, file_name: str):
	    with io.open (file_name,'r',encoding='utf8') as f:
	        contents = f.read()
	        soup = BeautifulSoup(contents, 'lxml')
	    
	    return soup

	@abstractmethod
	def get_content(self):
		pass

	@abstractmethod 
	def find_slots(self):
		pass	

