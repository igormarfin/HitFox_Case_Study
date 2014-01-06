#! /usr/bin/env python


import pkg_resources


import os
import sys
import optparse

import types
import math
import unittest
import logging
import inspect


pkg_resources.get_distribution("os").version
pkg_resources.get_distribution("sys").version
pkg_resources.get_distribution("optparse").version
pkg_resources.get_distribution("types").version
pkg_resources.get_distribution("math").version
pkg_resources.get_distribution("unittest").version
pkg_resources.get_distribution("logging").version
pkg_resources.get_distribution("inspect").version

