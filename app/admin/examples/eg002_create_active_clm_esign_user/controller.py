from docusign_orgadmin import ApiClient, ProductPermissionProfilesApi, DSGroupsApi
from flask import session, json

from ....ds_config import DS_CONFIG
from app.admin.utils import get_organization_id

class Eg002Controller:
    @staticmethod
    def get_args():
        """Get required session and request arguments"""
        organization_id = get_organization_id()
        return {
            "account_id": session["ds_account_id"], # Represents your {ACCOUNT_ID}
            "access_token": session["ds_access_token"], # Represents your {ACCESS_TOKEN}
            "organization_id": organization_id, # Represents your {ORGANIZATION_ID}
        }

    @staticmethod
    def worker(args):
        """
        1. Create an API client with headers
        2. Get your monitor data via SDK
        """

        access_token = args["access_token"]
        account_id = args["account_id"]
        org_id = args["organization_id"]

        # Step 2 start
        # Create an API client with headers
        api_client = ApiClient(host=DS_CONFIG["admin_api_client_host"])
        api_client.set_default_header(
            header_name="Authorization",
            header_value=f"Bearer {access_token}"
        )
        # Step 2 end

        #Step 3 start
        product_permission_profiles_api = ProductPermissionProfilesApi(api_client=api_client)
        permission_profiles = product_permission_profiles_api.get_product_permission_profiles(organization_id=org_id, account_id=session["ds_account_id"])
        print(permission_profiles)
        # Step 3 end

        # Step 4 start
        ds_groups_api = DSGroupsApi(api_client)
        ds_groups = ds_groups_api.get_ds_groups(organization_id=org_id, account_id=session["ds_account_id"])
        # Step 4 end

        # Step 5 start
        

        # Step 5 end

        return permission_profiles