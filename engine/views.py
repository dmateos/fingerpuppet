from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from .forms import UserForm
import datetime


def index(request):
    context = {}
    return render(request, "engine/index.html", context)


@login_required
def home(request):
    context = {}
    return render(request, "engine/home.html", context)


class UserRegister(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        context = {"form": form}
        return render(request, "engine/user_register.html", context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/home")
        return redirect("accounts/login")


# class DynamicEntryUpdate(LoginRequiredMixin, UpdateView):
# 	model = DynamicEntry
# 	fields = [ "name", "domain", "record_type", "record_value" ]
# 	template_name_suffix = "_update_form"
# 	success_url = "/home"

#   def get_object(self, *args, **kwargs):
#       obj = super().get_object(*args, **kwargs)
#       if obj.account.user != self.request.user:
#           raise PermissionDenied()
#       return obj
