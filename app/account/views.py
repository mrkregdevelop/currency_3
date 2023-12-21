from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView, RedirectView
from django.urls import reverse_lazy

from account.forms import UserSignUpForm

User = get_user_model()


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
        'avatar'
    )

    def get_object(self, queryset=None):
        qs = self.get_queryset()

        return qs.get(id=self.request.user.id)


class UserSignUpView(CreateView):
    queryset = User.objects.all()
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    form_class = UserSignUpForm


class UserActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')

        user = User.objects.filter(username=username).only('id').first()

        if user is not None:
            user.is_active = True
            user.save(update_fields=('is_active',))

        return super().get_redirect_url(*args, **kwargs)


"""
1. Email + password + confirm password (get email)
2. Email (get email) + password + confirm password
3. Email (get email) + 7 days
4. phone + passport + code (confirm) + login


1. form (email, password, confirm password)
2. send email with confirmation link
3. Activation endpoint
"""
