#!/usr/bin/env python

from utils.file_util import FileUtil

class FileController:

    def map_action(self, action, args):
        """
        This funciton maps the action to the corresponding method in FileUtil.
        Input:
            - action: str
            - args: Namespace
        Output:
            - str
            - str
            - bool
        """
        rest_args = self.__map_args(args)
        file_util = FileUtil(args.file, **rest_args)
        try:
            log, response = getattr(file_util, action)()
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
        exclude = ['file']
        for key, value in vars(namespace_args).items():
            if key not in exclude:
                args[key] = value
        return args
