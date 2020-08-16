from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.



class RegisterView(View):
    template = 'register.html'
    form = UserRegisterForm

    def get(self, request):

        context = {
            'form': self.form}
        return render(request, self.template, context)

    def post(self, request):
        if request.method == "POST":
            form = UserRegisterForm(request.POST)

            if form.is_valid():

                user = form.save()
                messages.success(request, f"User Created Succesfully!")
                return redirect("register")

            else:

                messages.success(request, 'Check The error Below')
                return render(request, self.template, {'form': form})
