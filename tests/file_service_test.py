#!/usr/bin/env python

import unittest
from services.file_service import FileService

class FileServiceTest(unittest.TestCase):

    def setUp(self):
        self.filename = 'output.csv'
        self.additional_args = {'data': 'foo', 'new_line': False, 'replace_data': 'foo', 'row': 1, 'column': 1}
        self.file_service = FileService(self.filename, **self.additional_args)

    def test_file_service(self):
        self.assertEqual(
            self.file_service.filename,
            self.filename
        )
        self.assertEqual(
            self.file_service.args,
            self.additional_args
        )

    def test_create(self):
        response = self.file_service.create()
        self.assertIsNotNone(response)
        self.assertTrue(response['status'])

    def test_send(self):
        response = self.file_service.send()
        self.assertIsNotNone(response)
        self.assertTrue(response['status'])
    
    def test_replace(self):
        response = self.file_service.replace()
        self.assertIsNotNone(response)
        self.assertFalse(response['status'])

    def test_delete(self):
        response = self.file_service.delete()
        self.assertIsNotNone(response)
        self.assertTrue(response['status'])
