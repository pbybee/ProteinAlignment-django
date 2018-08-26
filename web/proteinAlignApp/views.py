from django.shortcuts import render, redirect
from django.views import generic,View
from .models import Align
from django import forms
from .forms import PostForm
from .globalalignment import global_alignment
from django.core.exceptions import ValidationError

class AlignHome(View):

	def __init__(self):
		self.the_form = PostForm()
		self.context = {
			'title': "Simple Protein Alignment App",
			'form': self.the_form,
		}

	def get(self, request, *args, **kwargs):
		if "aligned" in request.path:
			return(self.postAlign(request))
		else:
			return(render(request, "align/align.html", self.context))

	def post(self, request, *args, **kwargs):
		if request.method == "POST":
			context = self.context
			context['form'] = PostForm(request.POST)
			if context['form'].is_valid():
				post = context['form'].save(commit=False)
				post.save()

				return(redirect('postalignment'))
			else:
				return(render(request, "align/align.html", context))

	def postAlign(self, request):
		context = self.context
		if len(Align.objects.all()) > 0:
			alignedStrings = Align.objects.last()
			alignedStrings.alignedV, alignedStrings.alignedW = global_alignment(alignedStrings.align, alignedStrings.reference).split(':')
		# print(alignedStrings.alignedStrings.replace("\n",''))
			alignedStrings.save()
			context['alignedStrings'] = alignedStrings
		return(render(request, 'align/aligned.html', context))
