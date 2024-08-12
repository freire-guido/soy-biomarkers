import json

def list_duplicates(ordered_pairs):
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            if type(d[k]) is list:
                d[k].append(v)
            else:
                d[k] = [d[k],v]
        else:
           d[k] = v
    return d


def from_attributes(attributes):
    string = attributes.replace('"', "'").replace("\\", "").replace('{k=', '"').replace(', v=', '": "').replace('},', '",').replace('}', '').strip()
    string = '{' + string[1:-1] + '"}'
    return json.loads(string, object_pairs_hook=list_duplicates)