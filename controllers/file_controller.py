#!/usr/bin/env python

from utils.file_util import FileUtil

class FileController:

    def map_action(self, action, args):
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