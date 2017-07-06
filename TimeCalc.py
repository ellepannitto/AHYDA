import datetime
import time

class TimeCalc:
	def __init__(self):
		self.last_print = datetime.datetime.now()
		pass
		
	def print_message (self, string):
		
		d = datetime.datetime.now()
		
		print string, "-", d - self.last_print
		
		self.last_print = d


if __name__=="__main__":
	
	t = TimeCalc()
	
	time.sleep(2)
	t.print_message("prova1")
	
	time.sleep(3)
	t.print_message("prova2")
