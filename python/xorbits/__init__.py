# -*- coding: utf-8 -*-
# Copyright 2022 XProbe Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from . import _version
from .core import run
from .deploy import init, shutdown


def _install():
    from .numpy import _install as _install_numpy
    from .pandas import _install as _install_pandas
    from .web import _install as _install_web

    _install_pandas()
    _install_numpy()
    _install_web()


_install()
del _install


__version__ = _version.get_versions()["version"]

__all__ = ["init", "shutdown"]
