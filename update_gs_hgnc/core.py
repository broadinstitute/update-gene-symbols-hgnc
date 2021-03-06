# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['get_official_gene_symbol', 'get_gene_id']

# Cell
import requests, sys

def get_official_gene_symbol(gs):
    """Get official gene symbol from HGNC
    :param gs: str, gene symbol
    :return: off_gs, official HGNC gene symbol
    """
    gene_id_info = get_gene_id(gs)
    new_symbol = ''
    if len(gene_id_info)>0:
        for g in gene_id_info:
            server = "https://rest.ensembl.org/"
            ext = 'xrefs/id/'+g['id']+'?external_db=HGNC;all_levels=1;'
            r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
            id_info = r.json()
            if id_info[0]['display_id'] == gs:
                new_symbol = gs
                break
            else:
                new_symbol = id_info[0]['display_id']
        return new_symbol
    else:
        return 'Gene not found'

def get_gene_id(gs):
    """Get Ensembl gene ID of symbol
    :param gs: str, gene symbol
    :return: gene_id, Ensembl gene ID
    """
    server = "https://rest.ensembl.org/"
    ext = 'xrefs/symbol/homo_sapiens/'+gs+'?external_db=HGNC;feature_type=gene;all_levels=1;'
    r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
    if not r.ok:
        r.raise_for_status()
        sys.exit("Gene not found")
    gene_id_info = r.json()
    return gene_id_info