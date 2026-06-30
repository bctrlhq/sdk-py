"""Pydantic conversion helpers for invocation output schemas."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


JsonObject = dict[str, Any]
PydanticModel = type[BaseModel] | BaseModel


def to_output_schema(model: PydanticModel, *, label: str = "output_model") -> JsonObject:
    """Return a JSON Schema object from a Pydantic model class or instance.

    The HTTP API receives language-neutral JSON Schema. Python callers should
    pass a Pydantic v2 model class or instance.
    """

    if not _is_pydantic_model(model):
        raise TypeError(f"{label} must be a Pydantic BaseModel class or instance")

    value = _model_type(model).model_json_schema()
    if not isinstance(value, dict):
        raise TypeError(f"{label} must resolve to a JSON Schema object")
    result = dict(value)
    result.pop("$schema", None)
    return result


def parse_output(model: PydanticModel, value: Any, *, label: str = "output_model") -> BaseModel:
    """Parse an invocation output value into the supplied Pydantic model."""

    if not _is_pydantic_model(model):
        raise TypeError(f"{label} must be a Pydantic BaseModel class or instance")

    return _model_type(model).model_validate(value)


def _is_pydantic_model(model: Any) -> bool:
    if isinstance(model, type):
        return issubclass(model, BaseModel)
    return isinstance(model, BaseModel)


def _model_type(model: PydanticModel) -> type[BaseModel]:
    return model if isinstance(model, type) else type(model)
