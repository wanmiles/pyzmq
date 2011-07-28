#
#    Copyright (c) 2010-2011 Brian E. Granger & Min Ragan-Kelley
#
#    This file is part of pyzmq.
#
#    pyzmq is free software; you can redistribute it and/or modify it under
#    the terms of the Lesser GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    pyzmq is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    Lesser GNU General Public License for more details.
#
#    You should have received a copy of the Lesser GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

import zmq
from zmq.utils.strtypes import asbytes

from zmq.tests import BaseZMQTestCase, SkipTest

#-----------------------------------------------------------------------------
# Tests
#-----------------------------------------------------------------------------

class TestMultipart(BaseZMQTestCase):

    def test_router_dealer(self):
        if zmq.zmq_version() == '3.0.0':
            raise SkipTest("Known bug in libzmq 3.0.0, see https://zeromq.jira.com/browse/LIBZMQ-232")
        router, dealer = self.create_bound_pair(zmq.ROUTER, zmq.DEALER)

        msg1 = asbytes('message1')
        dealer.send(msg1)
        ident = router.recv()
        more = router.rcvmore()
        self.assertEquals(more, True)
        msg2 = router.recv()
        self.assertEquals(msg1, msg2)
        more = router.rcvmore()
        self.assertEquals(more, False)

