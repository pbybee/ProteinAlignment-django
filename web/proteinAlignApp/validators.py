import re
from django import forms
from django.core.exceptions import ValidationError


def validateAminos(value):
	aminos = [ 'A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

	cleanString = re.sub(r"\W", "", value)
	for char in cleanString:
		if char not in aminos:
			raise ValidationError("Please only use the single letter abbreciations for amino acids \n"
								  "A C D E F G H I K L M N Q R S T V W Y")
