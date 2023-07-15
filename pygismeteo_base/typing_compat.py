from __future__ import annotations

import sys
from typing import Literal

if sys.version_info < (3, 10):  # pragma: <3.10 cover
    from typing_extensions import TypeAlias
else:  # pragma: >=3.10 cover
    from typing import TypeAlias


__all__ = ("Literal", "TypeAlias")
