#!/usr/bin/env python

from services.network_service import NetworkService

class NetworkController(object):

    def __init__(self, namespace_args):
        self.action   = namespace_args.action
        self.host     = namespace_args.host
        self.port     = namespace_args.port
        self.args     = self.__map_args(namespace_args)
        self.status   = None
        self.data     = None

    def __call__(self):
        response = self.map_action()
        self.status   = response['status']
        self.data     = response['data']
        return self

    def map_action(self) -> (str, bool):
        """
        This function maps the action to the corresponding method in NetworkService.
        Input:
            - action: str
            - args: Namespace
        Output:
            - str
            - str
            - bool
        """
        network_service = NetworkService(self.host, self.port, **self.args)
        try:
            response = getattr(network_service, self.action)()
        except:
            raise BaseException(
                "Unexpected action: '{}' does not map to controller"
                .format(
                    self.action
                )
            )
        return response

    def __map_args(self, namespace_args):
        """
        This function maps Namespace to a dict.
        Input:
            - Namespace
        Output:
            - dict
        """
        args = {}
        exclude = ['command', 'action', 'host', 'port']
        for key, value in vars(namespace_args).items():
            if key not in exclude:
                args[key] = value
        return args
