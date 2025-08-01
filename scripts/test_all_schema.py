from chatbot.labguru_api import (
    list_pmlb_cases,
    list_pmlb_specimens,
    list_pmlb_organoids,
    list_pmlb_xenografts,
    list_growth_assay,
    list_pathogen_assay,
    list_flow_assay,
    list_STR_assay,
    list_histology_assay,
    list_WES,
    list_RNAseq,
    list_ATAC
)

def test_all_schemas():
    schema_fetchers = {
        "PMLB_case": list_pmlb_cases,
        "PMLB_specimen": list_pmlb_specimens,
        "PMLB_organoid": list_pmlb_organoids,
        "PMLB_xenograft": list_pmlb_xenografts,
        "growth_assay": list_growth_assay,
        "pathogen_assay": list_pathogen_assay,
        "flow_assay": list_flow_assay,
        "STR_assay": list_STR_assay,
        "histology_assay": list_histology_assay,
        "WES": list_WES,
        "RNAseq": list_RNAseq,
        "ATAC": list_ATAC,
    }

    print(f"{'Schema':<20} | {'# Entries':>9}")
    print("-" * 32)

    for schema, fetch_fn in schema_fetchers.items():
        try:
            items = fetch_fn()
            print(f"{schema:<20} | {len(items):>9}")
        except Exception as e:
            print(f"{schema:<20} | ❌ ERROR: {str(e)}")

if __name__ == "__main__":
    test_all_schemas()
