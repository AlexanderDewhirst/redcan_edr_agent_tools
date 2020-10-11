#!/usr/bin/env python

from utils.file_util import FileUtil

class FileController:

    def map_action(self, action, args):
        file_util = FileUtil(args['file'], **args)
        try:
            response, log = getattr(file_util, action)()
        except:
            raise BaseException(
                "Unexpected action: '{}' does not map to controller"
                .format(
                    action
                )
            )
        return response, log
