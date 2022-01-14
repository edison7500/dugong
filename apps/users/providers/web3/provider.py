from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.base import Provider


class Web3Account(ProviderAccount):
    pass


class Web3Provider(Provider):
    id = "web3"
    name = "WEB3"
    account_class = Web3Account


provider_classes = [Web3Provider]
