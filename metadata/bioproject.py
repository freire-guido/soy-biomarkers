import requests

def get_bioproject(bioproj_id):
    api_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id={bioproj_id}"
    res = requests.get(api_url)
    return res.text