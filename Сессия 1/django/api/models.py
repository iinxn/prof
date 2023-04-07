from tastypie.resources import ModelResource
from tastypie.constants import ALL
from django.contrib.auth.models import User
from web_site.models import Personal,Group

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        list_allowed_methods = ['post','get']
        filtering = {
          "password": ALL,
          "username": ALL,
          "id": ALL
        }
        
class PersonalResource(ModelResource):
  class Meta:
        queryset = Personal.objects.all()
        resource_name = 'personal'
        list_allowed_methods = ['post','get'] 
        filtering = {
          "id": ALL,
          "first_name": ALL,
          "last_name": ALL,
          "sur_name": ALL,
          "number": ALL,
        }

class GroupResource(ModelResource):
  class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'
        list_allowed_methods = ['post','get'] 
        filtering = {
          "id": ALL
        }

