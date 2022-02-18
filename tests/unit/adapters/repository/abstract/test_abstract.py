from copy import deepcopy

import pytest

from adapters.repository import AbstractSession, AbstractRepository


class TestAbstractSession:
    @pytest.mark.unit
    def test_cannot_create_instance(self):
        with pytest.raises(TypeError):
            AbstractSession()

    @pytest.mark.unit
    def test_cannot_create_subclass_without_required_methods(self, class_inherited_from_abstract_session):
        methods = {method_name: (lambda: None) for method_name in ("add", "get", "list", "update", "delete")}
        for method in methods:
            new_methods = deepcopy(methods)
            new_methods.pop(method)
            with pytest.raises(TypeError):
                class_inherited_from_abstract_session(**new_methods)()


class TestAbstractRepository:
    @pytest.mark.unit
    def test_cannot_create_instance(self):
        with pytest.raises(TypeError):
            assert AbstractRepository()

    @pytest.mark.unit
    def test_cannot_create_subclass_without_required_methods(self, class_inherited_from_abstract_session):
        methods = {method_name: (lambda: None) for method_name in ("add", "get", "list", "update", "delete")}
        for method in methods:
            new_methods = deepcopy(methods)
            new_methods.pop(method)
            with pytest.raises(TypeError):
                class_inherited_from_abstract_session(**new_methods)()
