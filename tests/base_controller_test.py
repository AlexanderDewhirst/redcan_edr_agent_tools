#!/usr/bin/env python

import unittest
from unittest.mock import MagicMock, PropertyMock
from controllers.base_controller import BaseController

class BaseControllerTest(unittest.TestCase):

    def setUp(self):
        mock_namespace = MagicMock()
        command = PropertyMock(return_value = 'file_manager')
        bar = PropertyMock(return_value = 'bar')
        type(mock_namespace).command = command
        type(mock_namespace).foo = bar
        self.mock_namespace = mock_namespace
        self.base_controller = BaseController(mock_namespace)

    def test_base_controller(self):
        self.assertEqual(
            self.base_controller.command,
            self.mock_namespace.command
        )
        self.assertEqual(
            self.base_controller.args,
            self.mock_namespace
        )

