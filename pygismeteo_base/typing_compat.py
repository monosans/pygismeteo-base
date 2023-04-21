from __future__ import annotations

import sys

if sys.version_info < (3, 10):  # pragma: <3.10 cover
    from typing_extensions import TypeAlias
else:  # pragma: >=3.10 cover
    from typing import TypeAlias

if sys.version_info < (3, 8):  # pragma: <3.8 cover
    from typing_extensions import Literal
else:  # pragma: >=3.8 cover
    from typing import Literal

__all__ = ("Literal", "TypeAlias")
