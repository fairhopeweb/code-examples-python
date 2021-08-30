from os import path
from docusign_admin.apis import BulkImportsApi
from flask import session

from app.admin.utils import create_admin_api_client, get_organization_id
from app.ds_config import DS_CONFIG


class Eg004Controller:

    @staticmethod
    def worker(request):
        """
        Create a user list import request and
        returns a list of pending and completed import requests:
        1. Create the import API object
        2. Getting a CSV file from a form and converting it to a string
        3. Creating an import API object
        4. Setting headers for creating bulk import request
        5. Returns the response from the create_bulk_import_add_users_request method
        """

        # Get organization ID
        organization_id = get_organization_id()

        # Create the export API object
        # Step 2 start
        api_client = create_admin_api_client(
            access_token=session["ds_access_token"]
        )
        # Step 2 end

        # Getting a CSV file from a form and saving it
        uploaded_file = request.files['csv_file']
        csv_folder_path = path.abspath(path.join(path.dirname(path.realpath(__file__)), "csv"))
        csv_file_path = path.join(csv_folder_path, "uploaded_file.csv")
        uploaded_file.save(csv_file_path)

        # Creating an import API object
        import_api = BulkImportsApi(api_client=api_client)

        # Setting headers for creating bulk import request
        header_name, header_value = "Content-Disposition", "filename=myfile.csv"
        api_client.set_default_header(header_name, header_value)

        # Returns the response from the create_bulk_import_add_users_request method
        # Step 3 start
        return import_api.create_bulk_import_add_users_request(
            organization_id,
            csv_file_path
        )
        # Step 3 end

    @staticmethod
    def get_example_csv():
        """
        Creates an example of a CSV file, such as that needs to be sent to the Docusign server
        """

        # Returns an example of a CSV file
        return (
            "AccountID,UserName,UserEmail,PermissionSet\n"
            "{account_id},First1,Last1,example1@sampleemail.example,DS Admin"
            "{account_id},First2,Last2,example2@sampleemail.example,DS Admin"
        )
