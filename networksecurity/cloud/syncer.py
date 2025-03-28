import os

class AzureBlobSync:
    def sync_folder_to_azure(self, folder, azure_container_url):
        command = f"az storage blob upload-batch -s {folder} -d {azure_container_url}"
        os.system(command)

    def sync_folder_from_azure(self, folder, azure_container_url):
        command = f"az storage blob download-batch -s {azure_container_url} -d {folder}"
        os.system(command)
    