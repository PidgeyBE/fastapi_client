import inspect

from example.client import models
from example.client.api_client import (  # noqa F401
    ApiClient,
    AsyncApis,
    SyncApis,
)
from pydantic import BaseModel

for model in inspect.getmembers(models, inspect.isclass):
    if model[1].__module__ == "example.client.models":
        model_class = model[1]
        if isinstance(model_class, BaseModel):
            model_class.update_forward_refs()
