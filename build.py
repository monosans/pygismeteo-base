from __future__ import annotations

from pathlib import Path
from typing import Dict

from mypyc.build import mypycify
from typing_extensions import Any


def build(setup_kwargs: Dict[str, Any]) -> None:
    setup_kwargs["ext_modules"] = mypycify([
        str(file)
        for file in (Path(__file__).parent / "pygismeteo_base").rglob("*.py")
    ])
