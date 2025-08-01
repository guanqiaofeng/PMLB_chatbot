import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
LABGURU_API_TOKEN = os.getenv("LABGURU_API_TOKEN")
BASE_URL = os.getenv("LABGURU_BASE_URL", "https://ca.labguru.com")

# Headers for authenticated API calls
HEADERS = {
    "Accept": "application/json"
}

def get_all_pages(endpoint: str, collection_name: str, meta: bool = False):
    """
    Retrieves all items from a paginated biocollection.
    """
    all_items = []
    page = 1

    while True:
        params = {"page": page}
        if meta:
            params["meta"] = "true"
        params["token"] = LABGURU_API_TOKEN

        url = f"{BASE_URL}/api/v1/{endpoint}/{collection_name}"
        response = requests.get(url, headers={"Accept": "application/json"}, params=params)
        response.raise_for_status()
        page_data = response.json()

        if not page_data:
            break

        all_items.extend(page_data)
        page += 1

    return all_items


def list_pmlb_cases():
    return get_all_pages("biocollections", "PMLB_case")

def list_pmlb_specimens():
    return get_all_pages("biocollections", "PMLB_specimen")

def list_pmlb_organoids():
    return get_all_pages("biocollections", "PMLB_organoid")

def list_pmlb_xenografts():
    return get_all_pages("biocollections", "PMLB_xenograft")

def list_growth_assay():
    return get_all_pages("biocollections", "growth_assay")

def list_pathogen_assay():
    return get_all_pages("biocollections", "pathogen_assay")

def list_flow_assay():
    return get_all_pages("biocollections", "flow_assay")

def list_STR_assay():
    return get_all_pages("biocollections", "STR_assay")

def list_histology_assay():
    return get_all_pages("biocollections", "histology_assay")

def list_WES():
    return get_all_pages("biocollections", "WES")

def list_RNAseq():
    return get_all_pages("biocollections", "RNAseq")

def list_ATAC():
    return get_all_pages("biocollections", "ATAC")

# def get(endpoint: str, params: dict = None):
#     """
#     Generic GET request to Labguru using token as query param.
#     """
#     if params is None:
#         params = {}

#     # Inject token into query string (not headers!)
#     params["token"] = LABGURU_API_TOKEN

#     url = f"{BASE_URL}/api/v1/{endpoint}"
#     response = requests.get(url, headers={"Accept": "application/json"}, params=params)
#     response.raise_for_status()
#     return response.json()



# def get_biocollection_items(collection_name: str, page: int = 1, include_meta: bool = False):
#     """
#     Retrieve items from a specific generic biocollection, e.g., 'PMLB_case'.

#     Args:
#         collection_name (str): Name of the biocollection (e.g., 'PMLB_case')
#         page (int): Page number for pagination
#         include_meta (bool): Whether to return metadata only

#     Returns:
#         list or dict: Collection items (or metadata if meta=true)
#     """
#     params = {"page": page}
#     if include_meta:
#         params["meta"] = "true"
#     return get(f"biocollections/{collection_name}", params=params)


# # ---- Optional Convenience Wrappers for Each Collection ----

# def list_pmlb_cases(page: int = 1):
#     """List all PMLB_case entries."""
#     return get_biocollection_items("PMLB_case", page=page)


# def list_pmlb_specimens(page: int = 1):
#     """List all PMLB_specimen entries."""
#     return get_biocollection_items("PMLB_specimen", page=page)


# def list_pmlb_organoids(page: int = 1):
#     """List all PMLB_organoid entries."""
#     return get_biocollection_items("PMLB_organoid", page=page)


# def list_pmlb_xenografts(page: int = 1):
#     """List all PMLB_xenograft entries."""
#     return get_biocollection_items("PMLB_xenograft", page=page)
