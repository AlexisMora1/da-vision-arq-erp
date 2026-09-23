import json
from pathlib import Path
from uuid import uuid4

import aiofiles

from app.domain.storage import FileNotFoundError, FileRepositoryPort
from app.domain.storage.ports import (
    DownloadFile,
    DownloadFileSigned,
    FileMetadata,
    UploadFile,
    UploadFileSigned,
)


class LocalFileRepositoryAdapter(FileRepositoryPort):
    """Emulates an S3-like object store on the local filesystem. Meant to be replaced by an S3 adapter."""

    def __init__(self, storage_dir: Path, base_url: str):
        self.storage_dir = storage_dir
        self.blobs_dir = storage_dir / "blobs"
        self.metadata_path = storage_dir / "metadata.json"
        self.base_url = base_url.rstrip("/")

        self.blobs_dir.mkdir(parents=True, exist_ok=True)
        if not self.metadata_path.exists():
            self.metadata_path.write_text(json.dumps({}))

        self.metadata: dict = json.loads(self.metadata_path.read_text())

    async def _persist_metadata(self) -> None:
        async with aiofiles.open(self.metadata_path, "w") as f:
            await f.write(json.dumps(self.metadata, indent=4))

    def _get_metadata_or_raise(self, file_id: str) -> dict:
        file_metadata = self.metadata.get(file_id)
        if file_metadata is None:
            raise FileNotFoundError(f"File with ID '{file_id}' not found.")
        return file_metadata

    async def get_upload_file_url(self, file_name: str) -> UploadFileSigned:
        file_id = str(uuid4())
        self.metadata[file_id] = {"file_name": file_name, "mime_type": None}
        await self._persist_metadata()

        return UploadFileSigned(
            file_id=file_id,
            file_name=file_name,
            mime_type="",
            url=f"{self.base_url}/files/{file_id}/upload"
        )

    async def get_download_file_url(self, file_id: str) -> DownloadFileSigned:
        file_metadata = self._get_metadata_or_raise(file_id)

        return DownloadFileSigned(
            file_id=file_id,
            file_name=file_metadata["file_name"],
            mime_type=file_metadata["mime_type"] or "",
            url=f"{self.base_url}/files/{file_id}/download"
        )

    async def upload_file(self, file_id: str, data: bytes, mime_type: str) -> UploadFile:
        file_metadata = self._get_metadata_or_raise(file_id)

        async with aiofiles.open(self.blobs_dir / file_id, "wb") as f:
            await f.write(data)

        file_metadata["mime_type"] = mime_type
        await self._persist_metadata()

        return UploadFile(
            file_id=file_id,
            file_name=file_metadata["file_name"],
            mime_type=mime_type
        )

    async def download_file(self, file_id: str) -> DownloadFile:
        file_metadata = self._get_metadata_or_raise(file_id)
        blob_path = self.blobs_dir / file_id

        if not blob_path.exists():
            raise FileNotFoundError(f"File with ID '{file_id}' has not been uploaded yet.")

        async with aiofiles.open(blob_path, "rb") as f:
            data = await f.read()

        return DownloadFile(
            file_id=file_id,
            file_name=file_metadata["file_name"],
            mime_type=file_metadata["mime_type"] or "",
            data=data
        )

    async def get_file_metadata(self, file_id: str) -> FileMetadata:
        file_metadata = self._get_metadata_or_raise(file_id)

        return FileMetadata(
            file_id=file_id,
            file_name=file_metadata["file_name"],
            mime_type=file_metadata["mime_type"] or ""
        )
