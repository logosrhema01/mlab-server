from typing import Any
from fastapi import File, UploadFile
from pydantic import BaseModel


class DatasetIn(BaseModel):
    """Dataset in"""

    name: str
    description: str
    owner_id: str
    file: UploadFile = File()
    private: bool
    # tags: list = []

class DatasetResponse(BaseModel):
    """Dataset response"""

    id: str
    name: str
    description: str
    git_name: str
    clone_url: str
    private: bool
    owner_id: str
    created_at: str
    updated_at: str
    files: list[Any] = []
    # tags: list = []
