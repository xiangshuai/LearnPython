from django.shortcuts import render_to_response, RequestContext
from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
def thanks(reqeust):
	return render_to_response('thanks.html')

def contact(request):
	errors = []
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['475645831@qq.com'],
            )
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial = {'subject': 'I love your site!'}
		)
	return render_to_response('contact_form.html',{'form': form},
         context_instance=RequestContext(request))
