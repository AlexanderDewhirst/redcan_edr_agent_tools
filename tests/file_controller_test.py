#!/usr/bin/env python

import unittest
from unittest.mock import MagicMock, PropertyMock
from controllers.file_controller import FileController


class FileControllerTest(unittest.TestCase):

    def setUp(self):
        mock_namespace = MagicMock()
        action = PropertyMock(return_value = 'create')
        filename = PropertyMock(return_value = 'output.csv')
        command = PropertyMock(return_value = 'file_manager')
        bar = PropertyMock(return_value = 'bar')
        type(mock_namespace).action = action
        type(mock_namespace).file = filename
        type(mock_namespace).command = command
        type(mock_namespace).foo = bar
        self.mock_namespace = mock_namespace
        self.file_controller = FileController(mock_namespace)

    def test_file_controller(self):
        self.assertEqual(
            self.file_controller.action,
            self.mock_namespace.action
        )
        self.assertEqual(
            self.file_controller.file,
            self.mock_namespace.file
        )
        self.assertIsNone(self.file_controller.status)
        self.assertIsNone(self.file_controller.data)

    def test_map_action(self):
        response = self.file_controller.map_action()
        self.assertTrue(response['status'])