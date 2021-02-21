from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *


def index(request):
    return render(request, "auctions/index.html",{
        "listings":Listing.objects.filter(available=True)
        })

def viewprofile(request):
    return render(request,"auctions/viewprofile.html")

@login_required
def mywinnings(request):
    return render(request,"auctions/mywinnings.html",{
        "winnings":Winner.objects.filter(user=request.user)
        })

@login_required
def mybids(request):
    bids=Bid.objects.filter(user=request.user)
    return render(request,"auctions/mybids.html",{
        "bids":bids
        })

@login_required
def makewinner(request,listingid,username,amount):
    user=User.objects.get(username=username)
    listing=Listing.objects.get(id=listingid)
    winner=Winner(user=user,listing=listing,amount=amount)
    winner.save()
    listing.available=False
    listing.save()
    return HttpResponseRedirect(reverse("index"))
    # return HttpResponse(f'you are at {listingid} and {username}')


@login_required
def addcomment(request,listingid):
    msg=request.POST['comment']
    comment=Comment(listing=Listing.objects.get(id=listingid),comment=msg,user=request.user)
    comment.save()
    return HttpResponseRedirect(reverse('viewlisting',args=[listingid]))


def viewlisting(request,listingid):
    cur_listing=Listing.objects.get(id=listingid)
    bids=cur_listing.bids.all()
    max_bid=max(bids,key=lambda x:x.amount) if len(bids)>0 else None
    allcomments=cur_listing.comments.all()
    if request.method=='GET':
        return render(request,"auctions/viewlisting.html",{
            "listing":Listing.objects.get(id=listingid),
            "bids":bids,
            "maxbid":max_bid,
            "len_bids":len(bids),
            "message":"",
            "comments":allcomments
            })
    else:
        bidamount=int(request.POST['bidamount'])
        newbid=Bid(listing=Listing.objects.get(id=listingid),user=request.user,amount=bidamount)
        newbid.save()
        max_bid=max(cur_listing.bids.all(),key=lambda x:x.amount) if len(bids)>0 else None
        return render(request,"auctions/viewlisting.html",{
            "listing":Listing.objects.get(id=listingid),
            "bids":bids,
            "maxbid":max_bid,
            "message":"your bid is placed",
            "len_bids":len(cur_listing.bids.all()),
            "comments":allcomments
            })

@login_required
def mylistings(request):
    return render(request,"auctions/mylistings.html",{
        "listings":Listing.objects.filter(user=request.user)
        })

@login_required
def createlisting(request):
    if request.method=="POST":
        name=request.POST['name']
        try:
            available=True if request.POST['available']=='on' else False
        except:available=False
        startbid=int(request.POST['startbid'])
        newlisting=Listing(name=name,startbid=startbid,available=available,user=request.user)
        newlisting.save()
        return HttpResponseRedirect(reverse("viewlisting",args=[newlisting.id]))
    else:
        return render(request,"auctions/createlisting.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
