# Copyright (c) 2024 PaddlePaddle Authors. All Rights Reserved.
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

from api_base import ApiBase
import paddle
import pytest
import numpy as np


@pytest.mark.elementwise_sub
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_elementwise_sub_1():
    test = ApiBase(
        func=paddle.subtract,
        feed_names=["X", "Y"],
        feed_shapes=[[16, 1, 704, 1280], [16, 1, 704, 1280]],
        threshold=1.0e-5,
        rel_tol=1.0e-5,
    )
    x = np.random.random(size=[16, 1, 704, 1280]).astype("float32")
    y = np.random.random(size=[16, 1, 704, 1280]).astype("float32")
    test.run(feed=[x, y])


@pytest.mark.elementwise_sub
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_elementwise_sub_2():
    test = ApiBase(
        func=paddle.subtract,
        feed_names=["X", "Y"],
        feed_shapes=[[1], [1]],
        threshold=1.0e-5,
        rel_tol=1.0e-5,
    )
    x = np.random.random(size=[1]).astype("float32")
    y = np.random.random(size=[1]).astype("float32")
    test.run(feed=[x, y])


@pytest.mark.elementwise_sub
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_elementwise_sub_3():
    test = ApiBase(
        func=paddle.subtract,
        feed_names=["X", "Y"],
        feed_shapes=[[16, 704, 1280], [16, 704, 1280]],
        threshold=1.0e-5,
        rel_tol=1.0e-5,
    )
    x = np.random.random(size=[16, 704, 1280]).astype("float32")
    y = np.random.random(size=[16, 704, 1280]).astype("float32")
    test.run(feed=[x, y])


@pytest.mark.elementwise_add
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_elementwise_add_4():
    test = ApiBase(
        func=paddle.subtract,
        feed_names=["X", "Y"],
        feed_shapes=[[16, 10, 1, 1], [10]],
        threshold=1.0e-5,
        rel_tol=1.0e-5,
    )
    x = np.random.random(size=[16, 10, 1, 1]).astype("float32")
    y = np.random.random(size=[10]).astype("float32")
    test.run(feed=[x, y])


"""
paddle cpu result is wrong, ignore this case

@pytest.mark.elementwise_sub
@pytest.mark.filterwarnings('ignore::UserWarning')
def test_elementwise_sub_5():
    test = ApiBase(func=paddle.subtract,
                   feed_names=['X', 'Y'],
                   feed_shapes=[[16, 1, 704, 1280], [1]])
    x = np.random.random(size=[16, 1, 704, 1280]).astype('float32')
    y = np.random.random(size=[1]).astype('float32')
    test.run(feed=[x, y])
"""
