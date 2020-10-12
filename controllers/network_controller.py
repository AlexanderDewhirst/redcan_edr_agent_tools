#!/usr/bin/env python

from utils.network_util import NetworkUtil

class NetworkController:

    def map_action(self, action, args) -> (str, str, bool):
        """
        This funciton maps the action to the corresponding method in NetworkUtil.
        Input:
            - action: str
            - args: Namespace
        Output:
            - str
            - str
            - bool
        """
        rest_args = self.__map_args(args)
        network_util = NetworkUtil(args.host, args.port, **rest_args)
        try:
            log, response = getattr(network_util, action)()
        except:
            raise BaseException(
                "Unexpected action: '{}' does not map to controller"
                .format(
                    action
                )
            )
        return self.__class__.__name__, log, response

    def __call__(self):
        super().__call__()

    def __map_args(self, namespace_args):
        """
        This function maps Namespace to a dict.
        ## TODO: exclude 'action' and 'command'
        Output:
            - dict
        """
        args = {}
        exclude = ['host', 'port']
        for key, value in vars(namespace_args).items():
            if key not in exclude:
                args[key] = value
        return args
