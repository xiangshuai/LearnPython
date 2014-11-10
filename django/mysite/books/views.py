from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book

# Create your views here.
def search_form(request):
	return render_to_response('search_form.html')

##### version 1 ###########

#def search(request):
#	#if 'q' in request.GET:
#	#	message = 'You searched for: %r' % request.GET['q']
#	#else:
#	#	message = 'You submitted an empty form.'
#	#return HttpResponse(message)
#
#	if 'q' in request.GET and request.GET['q']:
#		q = request.GET['q']
#		books = Book.objects.filter(title__icontains=q)
#		return render_to_response('search_results.html', {'books':books, 'query':q})
#	else:
#		#return HttpResponse('Please submit a search term.')
#		return render_to_response('search_form.html', {'error': True})


##### version 2 ###########

#def search(request):
#	error = False
#	if 'q' in request.GET:
#		q = request.GET['q']
#		if not q:
#			error = True
#		elif len(q) > 20:
#			error = True
#		else:
#			books = Book.objects.filter(title__icontains=q)
#			return render_to_response('search_results.html', {'books': books, 'query': q})
#	return render_to_response('search_form.html', {'error': error})


##### version 3 ###########

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html', {'books': books, 'query': q})
	return render_to_response('search_form.html', {'errors': errors})

