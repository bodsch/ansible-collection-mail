#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) 2020, Bodo Schulz <bodo@boone-schulz.de>
# BSD 2-clause (see LICENSE or https://opensource.org/licenses/BSD-2-Clause)

from __future__ import absolute_import, division, print_function
import os
import hashlib
import json

data = [{'virtual': 'webmaster@yourdomain.com', 'alias': 'personal_email@gmail.com'}, {'virtual': 'billandbob@yourdomain.com', 'alias': 'bill@gmail.com, bob@gmail.com'}, {'virtual': 'ann-katrin@yourdomain.com', 'aliases': ['ann@gmail.com', 'bob@gmail.com', 'katrin@gmail.com']}]

def map_data(data):
    key = None
    values = None
    result = {}

    if isinstance(data, list):
        for i in data:
            res = {}
            if isinstance(i, dict):
                key = i[list(i.keys())[0]]
                values = i[list(i.keys())[1]]
                if isinstance(values, list):
                    values = ", ".join(values)
                res.update({key: values})
            result.update(res)

    print(f"= result: {result}")
    return result

re_mapped = map_data(data)
print(re_mapped)
