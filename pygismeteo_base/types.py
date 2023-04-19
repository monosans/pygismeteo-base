from __future__ import annotations

import sys
from typing import Mapping, Optional, Type, TypeVar, Union

from . import models

if sys.version_info < (3, 10):  # pragma: <3.10 cover
    from typing_extensions import TypeAlias
else:  # pragma: >=3.10 cover
    from typing import TypeAlias

if sys.version_info < (3, 8):  # pragma: <3.8 cover
    from typing_extensions import Literal
else:  # pragma: >=3.8 cover
    from typing import Literal

Lang: TypeAlias = Literal["ru", "en", "ua", "lt", "lv", "pl", "ro"]
Step3Days: TypeAlias = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Step6or24Days: TypeAlias = Literal[3, 4, 5, 6, 7, 8, 9, 10]
Params: TypeAlias = Optional[Mapping[str, Union[str, int, float]]]
Headers: TypeAlias = Mapping[str, str]
SearchLimit: TypeAlias = Literal[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
]

StepNModel: TypeAlias = Type[
    Union[models.step3.Model, models.step6.Model, models.step24.Model]
]
TDays = TypeVar("TDays", Step3Days, Step6or24Days)
TStepNModel = TypeVar(
    "TStepNModel", models.step3.Model, models.step6.Model, models.step24.Model
)
TStepNModelItem = TypeVar(
    "TStepNModelItem",
    models.step3.ModelItem,
    models.step6.ModelItem,
    models.step24.ModelItem,
)
