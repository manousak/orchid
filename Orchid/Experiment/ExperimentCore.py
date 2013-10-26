from Algorithm import SampleClassifier


class ExperimentList():
	def __init__(self, *args):
		for experiment in args:
			print experiment
			


experiments = ExperimentList(SampleClassifier.SampleClassifier)
	
		# this is where hopefully the main work will be done