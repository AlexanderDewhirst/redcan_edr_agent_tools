#!/usr/bin/env python

import unittest
from unittest.mock import MagicMock, PropertyMock
from controllers.network_controller import NetworkController

class NetworkControllerTest(unittest.TestCase):

    def setUp(self):
        mock_namespace = MagicMock()
        action = PropertyMock(return_value = 'connect')
        host = PropertyMock(return_value = 'localhost')
        port = PropertyMock(return_value = 4000)
        command = PropertyMock(return_value = 'network_manager')
        bar = PropertyMock(return_value = 'bar')
        type(mock_namespace).action = action
        type(mock_namespace).host = host
        type(mock_namespace).port = port
        type(mock_namespace).foo = bar
        self.mock_namespace = mock_namespace
        self.network_controller = NetworkController(mock_namespace)

    def test_network_controller(self):
        self.assertEqual(
            self.network_controller.action,
            self.mock_namespace.action
        )
        self.assertEqual(
            self.network_controller.host,
            self.mock_namespace.host
        )
        self.assertEqual(
            self.network_controller.port,
            self.mock_namespace.port
        )
        self.assertIsNone(self.network_controller.status)
        self.assertIsNone(self.network_controller.data)