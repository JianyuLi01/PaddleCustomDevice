#   Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
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

from __future__ import print_function

import numpy as np
import unittest
from tests.op_test import OpTest
import paddle

paddle.enable_static()

import os

intel_hpus_module_id = os.environ.get("FLAGS_selected_intel_hpus", 0)


# Correct: General.
class TestSqueeze2Op(OpTest):
    def setUp(self):
        self.set_hpu()
        self.op_type = "squeeze2"
        self.init_test_case()
        self.inputs = {"X": np.random.random(self.ori_shape).astype("float32")}
        self.init_attrs()
        self.outputs = {
            "Out": self.inputs["X"].reshape(self.new_shape),
            "XShape": np.random.random(self.ori_shape).astype("float32"),
        }

    def set_hpu(self):
        self.__class__.use_custom_device = True
        self.place = paddle.CustomPlace("intel_hpu", int(intel_hpus_module_id))

    def test_check_output(self):
        self.check_output_with_place(self.place, no_check_set=["XShape"])

    def init_test_case(self):
        self.ori_shape = (1, 3, 1, 40)
        self.axes = (0,)
        self.new_shape = (3, 1, 40)

    def init_attrs(self):
        self.attrs = {"axes": self.axes}


"""
# Correct: There is mins axis.
class TestSqueeze2Op1(TestSqueeze2Op):
    def init_test_case(self):
        self.ori_shape = (1, 20, 1, 5)
        self.axes = (0, -2)
        self.new_shape = (20, 5)
"""


# Correct: No axes input.
class TestSqueeze2Op1(TestSqueeze2Op):
    def init_test_case(self):
        self.ori_shape = (1, 20, 1, 5)
        self.axes = (2,)
        self.new_shape = (1, 20, 5)


# Correct: No axes input.
class TestSqueeze2Op2(TestSqueeze2Op):
    def init_test_case(self):
        self.ori_shape = (1, 20, 1, 5)
        self.axes = ()
        self.new_shape = (20, 5)


# Correct: No axes input.
class TestSqueeze2Op3(TestSqueeze2Op):
    def init_test_case(self):
        self.ori_shape = (1, 20, 1, 5)
        self.axes = (-2,)
        self.new_shape = (1, 20, 5)


"""
# Correct: Just part of axes be squeezed.
class TestSqueeze2Op3(TestSqueeze2Op):
    def init_test_case(self):
        self.ori_shape = (6, 1, 5, 1, 4, 1)
        self.axes = (1, -1)
        self.new_shape = (6, 5, 1, 4)
"""

"""
# Correct: Just part of axes be squeezed.
class TestSqueeze2Op4(TestSqueeze2Op):
    def init_test_case(self):
        self.ori_shape = (1, 3, 1, 40)
        self.axes = (0, 2)
        self.new_shape = (3, 40)
"""

if __name__ == "__main__":
    unittest.main()
