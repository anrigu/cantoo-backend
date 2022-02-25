from django.urls import reverse


class CustomAdapter(DefaultAccountAdapter):
  def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        user.save()
        return user