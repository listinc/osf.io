import json
import copy
from pprint import pprint

# data = {"query":{"bool":{"must":{"query_string":{"query":"tax"}},"filter":[{"bool":{"should":[{"terms":{"types":["preprint"]}},{"terms":{"sources":["Thesis Commons"]}}]}},{"terms":{"sources":["OSF","AfricArXiv","AgriXiv","Arabixiv","BITSS","EarthArXiv","ECSarXiv","engrXiv","FocUS Archive","Frenxiv","INA-Rxiv","LawArXiv","LIS Scholarship Archive","MarXiv","MindRxiv","NutriXiv","PaleorXiv","PsyArXiv","Research AZ","SocArXiv","SportRxiv","Thesis Commons","arXiv","bioRxiv","Preprints.org","PeerJ","Cogprints","Research Papers in Economics"]}}]}},"from":0,"aggregations":{"sources":{"terms":{"field":"sources","size":500}}}}
# data = {"size":0,"aggregations":{"sources":{"cardinality":{"field":"sources","precision_threshold":500}}}}
# data = {"size":0,"from":0,"query":{"bool":{"must":{"query_string":{"query":"*"}},"filter":[{"term":{"types":"preprint"}}]}}}
# data = {"from": 0,"query": {"bool": {"must": {"query_string": {"query": "*"}}, "filter": [{"bool": {"should": [{"terms": {"types": ["preprint"]} },{"terms": {"sources": ["Thesis Commons"]} }]}}]}},"aggregations": {"sources": {"terms": {"field": "sources","size": 200}}}}
# data = {"query":{"bool":{"must":{"query_string":{"query":"hyeonki"}},"filter":[{"bool":{"should":[{"terms":{"types":["preprint"]}},{"terms":{"sources":["Thesis Commons"]}}]}},{"bool":{"should":[{"match":{"subjects":"|Law"}}]}},{"terms":{"sources":["OSF","[TEST] engrXiv","[TEST] LawArXiv","[TEST] PsyArXiv","[TEST] SocArXiv","arXiv","bioRxiv","Cogprints","PeerJ","Research Papers in Economics","Preprints.org"]}}]}},"from":0,"aggregations":{"sources":{"terms":{"field":"sources","size":500}}}}
data = {"query":{"bool":{"must":{"query_string":{"query":"tax"}},"filter":[{"bool":{"should":[{"terms":{"types":["preprint"]}},{"terms":{"sources":["Thesis Commons"]}}]}},{"terms":{"sources":["OSF","[TEST] engrXiv","[TEST] LawArXiv","[TEST] PsyArXiv","[TEST] SocArXiv","arXiv","bioRxiv","Cogprints","PeerJ","Research Papers in Economics","Preprints.org"]}}]}},"from":0,"aggregations":{"sources":{"terms":{"field":"sources","size":500}}}}
json_data = json.dumps(data)
json_data = json.loads(json_data)
query = copy.deepcopy(json_data)
if 'query' in json_data:
	if 1 < len(query['query']['bool']['filter']) <= 2:
		try:
			del query['query']['bool']['filter'][1]
		except KeyError:
			pass
	elif 2 < len(query['query']['bool']['filter']):
		try:
			del query['query']['bool']['filter'][2]
		except KeyError:
			pass

print(query)