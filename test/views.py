from django.shortcuts import render
from user.models import ExtendedUser


def test(request):
    # qs = ExtendedUser.objects.all().prefetch_related('user_inter_tags')
    qs = ExtendedUser.objects.all().prefetch_related('interests_tags', 'own_interests')
    return render(request, 'test/test.html', {'qs': qs})
