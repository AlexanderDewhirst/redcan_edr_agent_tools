#!/usr/bin/env python

class ServiceHelper:

    @staticmethod
    def construct_response(status:bool, data:dict = None) -> dict:
        """
        This function constructs the data object for the Logger
        Input:
            - bool
            - dict (opt.)
        Output:
            - dict
        """
        response = {
            'status': status,
            'data': data
        }
        return response
