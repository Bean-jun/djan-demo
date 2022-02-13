from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from . import models
from utils import funs


class BaseView(View):
    def get_or_post_to_dic(self, post):
        return {k: v for k, v in post.items()}

    def get(self, *args, **kwargs):

        raise Exception("error method")

    def post(self, *args, **kwargs):

        raise Exception("error method")


@method_decorator(csrf_exempt, name='dispatch')
class UserView(BaseView):

    def get(self, *args, **kwargs):
        users = models.User.objects.all()

        return JsonResponse(funs.to_dic_list(users, *("password",)), safe=False)

    def post(self, *args, **kwargs):
        dic = self.get_or_post_to_dic(self.request.POST)

        user = models.User(**dic)
        if "password" in dic:
            user.password = user.hash_password(dic["password"])
        user.save()

        return JsonResponse(funs.to_dict(user, *("password",)))
