# Encoding: utf-8

# --
# Copyright (c) 2008-2021 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from nagare import gevent_patch  # noqa: F401

import grpc.experimental.gevent
grpc.experimental.gevent.init_gevent()
