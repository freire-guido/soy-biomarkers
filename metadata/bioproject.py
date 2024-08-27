import requests, re

def get_internal_id(accession):
    api_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=bioproject&term={accession}"
    res = requests.get(api_url)
    return re.search(r"<Id>(\d+)</Id>", res.text).group(1)

def get_pmid(doi):
    api_url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?tool=tesis_guido_freire&email=example@outlook.com&ids={doi}"
    res = requests.get(api_url)
    return re.search(r'pmid="(\d+)"', res.text).group(1)

def get_bioproject(bioproj_id):
    internal_id = get_internal_id(bioproj_id)
    api_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id={internal_id}"
    res = requests.get(api_url)
    return res.text

def get_abstract(doi):
    pmid = get_pmid(doi)
    api_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}"
    res = requests.get(api_url)
    return re.search(r'<AbstractText>(.*?)</AbstractText>', res.text).group(1)
