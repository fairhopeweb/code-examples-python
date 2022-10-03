""" Example 034: Creating an envelope where the workflow is routed
to different recipients based on the value of a transaction """

from os import path

from docusign_esign.client.api_exception import ApiException
from flask import render_template, session, Blueprint

from ..examples.eg034_use_conditional_recipients import Eg034UseConditionalRecipientsController
from ...docusign import authenticate, ensure_manifest, get_example_by_number
from ...ds_config import DS_CONFIG
from ...error_handlers import process_error

example_number = 34
eg = f"eg0{example_number}"  # Reference (and URL) for this example
eg034 = Blueprint(eg, __name__)


@eg034.route(f"/{eg}", methods=["POST"])
@ensure_manifest(manifest_url=DS_CONFIG["esign_manifest_url"])
@authenticate(eg=eg)
def use_conditional_recipients():
    """
    1. Get required arguments
    2. Call the worker method
    3. Render success response with envelopeId
    """
    example = get_example_by_number(session["manifest"], example_number)

    # 1. Get required arguments
    args = Eg034UseConditionalRecipientsController.get_args()
    try:
        # 1. Call the worker method
        results = Eg034UseConditionalRecipientsController.worker(args)
    except ApiException as err:
        return process_error(err)

    # 2. Render success response with envelopeId
    return render_template(
        "example_done.html",
        envelope_ok=True,
        title=example["ExampleName"],
        message=f"Envelope ID {results['envelope_id']} with the conditional"
                f" routing criteria has been created and sent to the first recipient!"
    )


@eg034.route(f"/{eg}", methods=["GET"])
@ensure_manifest(manifest_url=DS_CONFIG["esign_manifest_url"])
@authenticate(eg=eg)
def get_view():
    """Responds with the form for the example"""
    example = get_example_by_number(session["manifest"], example_number)

    return render_template(
        "eg034_use_conditional_recipients.html",
        title=example["ExampleName"],
        example=example,
        source_file= "eg034_use_conditional_recipients.py",
        source_url=DS_CONFIG["github_example_url"] + "eg034_use_conditional_recipients.py",
        documentation=DS_CONFIG["documentation"] + eg,
        show_doc=DS_CONFIG["documentation"],
        signer1_name=DS_CONFIG["signer_name"],
        signer1_email=DS_CONFIG["signer_email"]
    )
