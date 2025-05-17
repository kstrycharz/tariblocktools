
from __future__ import print_function
import base_node_pb2
import base_node_pb2_grpc
import grpc


import logging



# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
 
    with grpc.insecure_channel("node.taritracker.com:18142") as channel:
        stub = base_node_pb2_grpc.BaseNodeStub(channel)
        response = stub.GetVersion(base_node_pb2.StringValue())
        block = stub.GetBlocks(base_node_pb2.GetBlocksRequest(heights=[1000]))
    print(response)
    print(block)


if __name__ == "__main__":
    logging.basicConfig()
    run()
