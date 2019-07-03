from django.http import HttpResponse
from django.views.generic.edit import FormView
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def proceed(request):
    return  HttpResponse("Your url: ")


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)