#!/usr/bin/env python

from utils.network_util import NetworkUtil

class NetworkController:

    def map_action(self, action, args) -> (str, str, bool):
        """
        This funciton maps the action to the corresponding method in NetworkUtil.
        Input:
            - action: str
            - args: dict
        Output:
            - str
            - str
            - bool
        """
        network_util = NetworkUtil(args.host, args.port, **args)
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