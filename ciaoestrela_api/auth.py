from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import requests

from ciaoestrela_api.settings import OKTA_CLIENT_ID, OKTA_CLIENT_SECRET

AUTH = (OKTA_CLIENT_ID, OKTA_CLIENT_SECRET)


class AuthenticatedUser():
    def is_authenticated(self):
        pass


class OktaAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
            data = {'token': token}
            response = requests.post('https://dev-777810.okta.com/oauth2/default/v1/introspect', auth=AUTH, data=data)
            response_json = response.json()
            if not response_json['active']:
                raise Exception()
            return (AuthenticatedUser(), None)
        except Exception as error:
            return None
