import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()

connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("AZURE_CONTAINER_NAME")


def get_container_client():
    if not connect_str:
        raise ValueError("Missing AZURE_STORAGE_CONNECTION_STRING")

    if not container_name:
        raise ValueError("Missing AZURE_CONTAINER_NAME")

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    return blob_service_client.get_container_client(container_name)


def upload_file(local_path, blob_path):
    container_client = get_container_client()

    with open(local_path, "rb") as data:
        container_client.upload_blob(
            name=blob_path,
            data=data,
            overwrite=True
        )

    print(f"Uploaded {local_path} to {blob_path}")


def download_file(blob_path, local_path):
    container_client = get_container_client()

    blob_client = container_client.get_blob_client(blob_path)

    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    with open(local_path, "wb") as f:
        f.write(blob_client.download_blob().readall())

    print(f"Downloaded {blob_path} to {local_path}")