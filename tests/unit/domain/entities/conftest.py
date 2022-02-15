from typing import Dict, Any

import pytest


@pytest.fixture(name="valid_drawing_dict")
def valid_drawing_dict_fixture() -> Dict[str, Any]:
    return {
        "id": 1,
        "name": "test drawing",
        "parent": None,
        "category": "test category",
        "project": "test project",
        "drawing_data": {
            "test_data": "test data"
        },
        "path_to_file": "/home/test/test.some"
    }
