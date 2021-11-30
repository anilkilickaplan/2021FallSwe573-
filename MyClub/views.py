from django.core.checks import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls.base import reverse
from django.views import View
from .models import Offer, OfferApplication, UserProfile, Event, Review
from .forms import OfferForm, EventForm, ReviewForm
from django.views.generic.edit import UpdateView, DeleteView
from datetime import datetime
from django.http import HttpResponseRedirect, request
from django.contrib import  messages
from django.shortcuts import render, redirect, get_object_or_404




# OFFER RELATED 
class OfferListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        offers = Offer.objects.all().order_by('-offerCreatedDate')
        form = OfferForm()

        context = {
            'offer_list': offers,
            'form': form,
        }

        return render(request, 'myclub/offer_list.html', context)

    def post(self, request, *args, **kwargs):
        submitted = False
        offers = Offer.objects.all().order_by('-offerCreatedDate')
        form = OfferForm(request.POST)

        if form.is_valid():
            new_offer = form.save(commit=False)
            new_offer.offerOwner = request.user
            new_offer.save()


        context = {
            #'offer_list': offers,
            'form': form,
            'submitted': submitted
        }
        return render(request, 'myclub/offer_list.html', context)

        #return render(request, 'myclub/create_offer.html', context)


class OfferDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        offer = Offer.objects.get(pk=pk)
        form = OfferForm()
        # form = ReviewForm()

        context = {
            'offer': offer,
            'form': form,
            # 'reviews': reviews,
        }

        return render(request, 'myclub/offer_detail.html', context)

    def post(self, request, *args, **kwargs):
        pass

    """
    def post(self, request, pk, *args, **kwargs):
        offer = Offer.objects.get(pk=pk)
        form = ReviewForm(request.POST)

        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.reviewowner = request.user
            new_review.offer = offer
            new_review.save()
        
        reviews = Review.objects.filter(offer=offer).order_by('-offerCreatedDate')

        context = {
            'offer': offer,
            'form': form,
            'reviews': reviews,
        }

        return render(request, 'myclub/offer_detail.html', context)
    """


class OfferEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Offer
    fields = ['description']
    template_name = 'myclub/offer_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('offer-detail', kwargs={'pk': pk})

    def test_func(self):
        offer = self.get_object()
        return self.request.user == offer.offerOwner


class OfferDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Offer
    template_name = 'myclub/offer_delete.html'
    success_url = reverse_lazy('offer-list')

    def test_func(self):
        offer = self.get_object()
        return self.request.user == offer.offerOwner



# EVENT RELATED
class EventListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        events = Event.objects.all().order_by('-eventCreatedDate')
        form = EventForm()

        context = {
            'event_list': events,
            'form': form,
        }

        return render(request, 'myclub/event_list.html', context)


    def post(self, request, *args, **kwargs):
        submitted = False

        #events = Event.objects.all().order_by('-eventCreatedDate')
        form = EventForm(request.POST)

        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.eventOwner = request.user
            new_event.save()
            submitted = True
            #return redirect('event/create_event', submitted=True)
            return HttpResponseRedirect('create_event' + '?' + 'submitted=True')
     

        context = {
            #'event_list': events,
            'form': form,
            'submitted': submitted,
            }

        return render(request, 'myclub/create_event.html', context)



class EventDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        event = Event.objects.get(pk=pk)
        form = EventForm()

        context = {
            'event': event,
            'form': form,
        }

        return render(request, 'myclub/event_detail.html', context)

    def post(self, request, *args, **kwargs):
        pass


class EventEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['eventName', 'eventDescription', 'eventDate', 'eventLocation', 'eventCapacity']
    template_name = 'myclub/event_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('event-detail', kwargs={'pk': pk})

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.eventOwner


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'myclub/event_delete.html'
    success_url = reverse_lazy('event-list')

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.eventOwner


# USER PROFILE RELATED
class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        userfollowers = user.userfollowers.all()
        if len(userfollowers) == 0:
            is_following = False
        for follower in userfollowers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False
        
        
        number_of_followers = len(userfollowers)
        context = {
            'user': user,
            'profile': profile,
            'number_of_followers': number_of_followers,
            'is_following': is_following
        }
        return render(request, 'myclub/profile.html', context)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'bio', 'birth_date', 'location', 'picture']
    template_name = 'myclub/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


def allEvents (request): 
    event_list = Event.objects.all()
    return render (request, 'myclub/event_list.html', 
    {'event_list': event_list})

def allOffers (request): 
    offer_list = Event.objects.all()
    return render (request, 'myclub/offer_list.html', 
    {'offer_list': offer_list})

def searchEvents(request):
    
    if request.method == "POST":
        searched = request.POST['searched']
        events = Event.objects.filter(name__contains = searched)

        return render (request, 
        'myclub/search_events.html', 
            {'searched': searched, 'events':events})
    else:
        return render(request, 
        'myclub/search_events.html',
        {})



def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    return render (request, 'myclub/home.html', 
    {})

class myEventsView(View):
    def get(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated:
            myevents = Event.objects.filter(eventOwner = request.user.id)
            return render(request, 
            'myclub/my_events_list.html', 
            {'myevents':myevents})
        else:
            messages.WARNING(request,("There is a problem with authentication. my_events (views) could not fetch user authentication"))

class myOffersView(View):
    def get(self, request, pk, *args, **kwargs):
            
        if request.user.is_authenticated:
            # myoffers = Offer.objects.filter(offerOwner=me)
            myoffers = Offer.objects.filter(offerOwner = request.user.id)
            return render(request, 
            'myclub/my_offers_list.html', 
            {'myoffers':myoffers})

        else:
            messages.WARNING(request,("There is a problem with authentication. my_offers (views) could not fetch user authentication"))



class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'bio', 'birth_date', 'location', 'picture']
    template_name = 'social/profile_edit.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})
    
    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.userFollowers.add(request.user)
        return redirect('profile', pk=profile.pk)

class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.userFollowers.remove(request.user)
        return redirect('profile', pk=profile.pk)

class RemoveMyFollower(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        userFollower_pk = self.kwargs['userFollower_pk']
        userFollower = UserProfile.objects.get(pk=userFollower_pk).user
        profile = UserProfile.objects.get(pk=request.user.pk)
        profile.userFollowers.remove(userFollower)
        return redirect('userFollowers', pk=request.user.pk)

class FollowersListView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        userFollowers = profile.userFollowers.all()

        context = {
            'userFollowers': userFollowers,
            'profile': profile,
        }

        return render(request, 'myclub/userfollowers_list.html', context)

class ApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = OfferApplication
    template_name = 'social/application_delete.html'

    def get_success_url(self):
        pk = self.kwargs['offer_pk']
        return reverse_lazy('offer-detail', kwargs={'pk': pk})
    
    def test_func(self):
        application = self.get_object()
        return self.request.user == application.applicant

class ApplicationEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OfferApplication
    fields = ['approved']
    template_name = 'offer/application_edit.html'
    
    def get_success_url(self):
        pk = self.kwargs['offer_pk']
        return reverse_lazy('offer-detail', kwargs={'pk': pk})
    
    def test_func(self):
        application = self.get_object()
        return self.request.user == application.offer.creater
