#!/usr/bin/env python

from utils.file_util import FileUtil

class FileController:

    def map_action(self, action, args):
        """
        This funciton maps the action to the corresponding method in FileUtil.
        Input:
            - action: str
            - args: dict
        Output:
            - str
            - str
            - bool
        """
        file_util = FileUtil(args['file'], **args)
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