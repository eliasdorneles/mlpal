#!/bin/env python
# coding=utf-8

import unittest
from ..args import _normalize_setup_path, parse_args

class ArgsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_handles_paths_as_setup_path(self):
        self.assertEqual('setup', _normalize_setup_path('setup.py'))
        self.assertEqual('module.setup', _normalize_setup_path('module.setup'))
        self.assertEqual('module.setupy', _normalize_setup_path('module.setupy'))
        self.assertEqual('inner.module.setup', _normalize_setup_path('inner/module/setup.py'))
        self.assertEqual('inner.pymodule.setup', _normalize_setup_path('inner.pymodule.setup'))

    def test_defines_args_properly(self):
        # just checking if we're using ParseArgs properly
        self.assertIsNotNone(parse_args(['train', 'setup_def']))
