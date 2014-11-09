from django.template import Template, Context
from django.http import HttpResponse
import datetime

def hello(request):
	return HttpResponse("hello world")

def current_datetime(request):
	now = datetime.datetime.now()
	#html = "<html><body>It is now %s.</body></html>" % now
	t = Template("<html><body>It is now {{ current_date }}.</body></html>")
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	assert False
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>: %s</td></tr>' % (k, v))
	return HttpResponse('<table>%</table>' '\n'.join(html))
