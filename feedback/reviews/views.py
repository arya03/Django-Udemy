from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ReviewForm
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Create your views here.

# Class-based views


class ReviewView(CreateView):
  model = Review
  # fields = "__all__"
  form_class = ReviewForm
  template_name = "reviews/review.html"
  success_url = "/thank-you"
    
  # def post(self, request):
  #   form = ReviewForm(request.POST)
  #   if form.is_valid():
  #     form.save()
  #     return HttpResponseRedirect("/thank-you")
    
  #   return render(request, "reviews/review.html", {
  #     "form": form
  # })

# def review(request):
#   if request.method == "POST":
#     form = ReviewForm(request.POST)
#     if form.is_valid():
#       # entered_username = form.cleaned_data["user_name"]
#       form.save()
#       return HttpResponseRedirect("/thank-you")
  
#   else:
#     form = ReviewForm()
#   return render(request, "reviews/review.html", {
#       "form": form
#   })


class ThankYouView(TemplateView):
  template_name = "reviews/thank_you.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["message"] = "This works!"
    return context

# def thank_you(request):
#   return render(request, "reviews/thank_you.html")

class ReviewsListView(ListView):
  template_name = "reviews/review_list.html"
  model = Review
  context_object_name = "reviews"
  
    # def get_queryset(self):
    #   base_query = super().get_queryset().filter(rating__gt=4)
    #   return base_query
  
class SingleReviewView(DetailView):
  template_name = "reviews/single_review.html"
  model = Review
  
