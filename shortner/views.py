from .forms import UrlForm
from django.shortcuts import render
from .baseconv import base62
from .models import Link, ShortLink
from django.http import HttpResponsePermanentRedirect, Http404


def get_link(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            # add to database
            print(form.cleaned_data['link_url'])
            try:
                owned_link = Link.objects.get(link_url=form.cleaned_data['link_url'])
                # if link is already in db, just provide shortened link
                short = ShortLink.objects.filter(source_link_id=owned_link.id).first()
                print("Short link = " + short.__str__())
                # return HttpResponseRedirect(reverse('proceed'))
                return render(request,'shortner/result.html', {'short_link': short.__str__,
                                                               'long_link': form.cleaned_data['link_url']})
            except Link.DoesNotExist:
                print("Creating new db entry..")
                link = form.save()
                link.save()
                short = ShortLink.objects.create(source_link=link, short_url=base62.from_decimal(link.id))
                return render(request, 'shortner/result.html', {'short_link': short.__str__,
                                                               'long_link': form.cleaned_data['link_url']})
    else:
        form = UrlForm()

    return render(request, 'short.html', {'form': form})


def redirect_link(request):
    path = request.path[1:]  # remove '/'
    link = ShortLink.objects.filter(short_url=path).first()
    if link is None:
        return Http404("Invalid link")
    target = link.__str__()
    return HttpResponsePermanentRedirect(target)
