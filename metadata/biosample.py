import re, requests

def get_biosample(biosamp_id):
    api_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id={biosamp_id}&rettype=full&retmode=text"
    res = requests.get(api_url)
    return res.text

def from_biosample(metadata):
    res = {}
    res['title'] = metadata.split('\n')[0].replace('1: ', '')
    identifiers = re.search(r'Identifiers: (.+)', metadata)
    if identifiers:
        res['Identifiers'] = {k.strip(): v.strip() for k, v in 
                                [item.split(':') if ':' in item else (item, "")
                                    for item in identifiers.group(1).split(';')]}
    organism = re.search(r'Organism: (.+)', metadata)
    if organism:
        res['Organism'] = organism.group(1).strip()
    attributes = re.findall(r'/(\w+)="([^"]+)"', metadata)
    if attributes:
        res['Attributes'] = {k: v for k, v in attributes}
    accession = re.search(r'Accession: (\w+)', metadata)
    if accession:
        res['Accession'] = accession.group(1)
    id_match = re.search(r'ID: (\d+)', metadata)
    if id_match:
        res['ID'] = id_match.group(1)
    
    return res