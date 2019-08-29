

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def define_template(nb):
	"""
	gets the templates to use for correlation
	"""
	if nb = 1:
		template = np.exp(np.linspace(0,1,5)
	elif nb = 2:
		template = gaussian(-np.linspace(0,1,5),0.5,1)
	elif nb == 3:
		template = [0.,0,1,1]
	else:
		print("I dont undertsand the templace shape")
		exit(0)
	return template

 
def find_correlation(signal, coord, template):
	"""
	Function to find max correlation between a template shape
	and a signal, and find the location of that maximum.
	user input: signal ( =a 1D array with the profile), 
	coord ( = corresponding 1D array with coordinate values),
	template ( = number, corresponding to pre-defined template shape, nb 1, 2, or 3)
	returns: 
	"""
	temp = define_template(template)
	
