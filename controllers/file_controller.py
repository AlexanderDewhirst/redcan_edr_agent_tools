#!/usr/bin/env python

from utils.file_util import FileUtil

class FileController(object):

    def __init__(self, namespace_args):
        self.action     = namespace_args.action
        self.file       = namespace_args.file
        self.args       = self._map_args(namespace_args)
        self.response   = None
        self.status     = None

    def __call__(self):
        response, status = self.map_action()
        self.response = response
        self.status = status
        return self

    def map_action(self) -> (str, bool):
        """
        This function maps the action to the corresponding method in FileUtil.
        Input:
            - action: str
            - args: Namespace
        Output:
            - str
            - str
            - bool
        """
        file_util = FileUtil(self.file, **self.args)
        try:
            log, response = getattr(file_util, self.action)()
        except:
            raise BaseException(
                "Unexpected action: '{}' does not map to controller"
                .format(
                    self.action
                )
            )
        return log, response

    def _map_args(self, namespace_args):
        """
        This function maps Namespace to a dict.
        Input:
            - Namespace
        Output:
            - dict
        """
        args = {}
        exclude = ['command', 'action', 'file']
        for key, value in vars(namespace_args).items():
            if key not in exclude:
                args[key] = value
        return args
