import json

def array_on_duplicate_keys(ordered_pairs):
    """Convert duplicate keys to arrays."""
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


def attr_json(attributes):
    print(attributes)
    string = attributes.replace('"', "'").replace("\\", "").replace('{k=', '"').replace(', v=', '": "').replace('},', '",').replace('}', '').strip()
    string = '{' + string[1:-1] + '"}'
    print(string)
    return json.loads(string, object_pairs_hook=array_on_duplicate_keys)