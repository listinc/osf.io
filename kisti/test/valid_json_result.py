import json

result = "{\"hits\": {\"hits\": [{\"sort\": [1533896129153], \"_type\": \"creativeworks\", \"_source\": {\"contributors\": [\"\\uc0bc\\ub2e4\\uc218\", \"hyeonki min\"], \"date_updated\": \"2018-08-10T07:17:48.910159+00:00\", \"sources\": [\"CrossRef\", \"OSF\"], \"withdrawn\": null, \"retracted\": false, \"title\": \"tax\", \"id\": \"461C4-9CF-446\", \"affiliations\": [], \"subjects\": [\"bepress|Law\", \"bepress|Law|Banking and Finance Law\"], \"type\": \"preprint\", \"registration_type\": null, \"publishers\": [\"Center for Open Science\"], \"justification\": null, \"description\": \"abstract is abstract testabstract is abstract test\", \"tags\": [], \"lists\": {\"publishers\": [{\"name\": \"Center for Open Science\", \"identifiers\": [], \"affiliations\": [], \"awards\": [], \"types\": [\"institution\", \"organization\", \"agent\"], \"relation\": \"publisher\", \"type\": \"institution\", \"id\": \"64155-6D7-742\", \"cited_as\": \"\"}], \"contributors\": [{\"name\": \"\\uc0bc\\ub2e4\\uc218\", \"affiliations\": [], \"identifiers\": [\"http://osf.io/eu7s2/\"], \"order_cited\": 1, \"awards\": [], \"given_name\": \"\\uc0bc\\ub2e4\\uc218\", \"types\": [\"person\", \"agent\"], \"relation\": \"creator\", \"type\": \"person\", \"id\": \"64236-8FF-BCF\", \"cited_as\": \"\\uc0bc\\ub2e4\\uc218\"}, {\"family_name\": \"Min\", \"name\": \"Hyeonki Min\", \"affiliations\": [], \"identifiers\": [\"http://secure.gravatar.com/avatar/f57921d87a9933f6eda277c0cda0db17?d=identicon\", \"http://osf.io/vnsd3/\"], \"order_cited\": 0, \"awards\": [], \"given_name\": \"Hyeonki\", \"types\": [\"person\", \"agent\"], \"relation\": \"creator\", \"type\": \"person\", \"id\": \"64158-0D5-E27\", \"cited_as\": \"hyeonki min\"}]}, \"date_published\": \"2018-08-09T02:37:56.412541+00:00\", \"date\": \"2018-08-09T02:37:56.412541+00:00\", \"subject_synonyms\": [], \"types\": [\"preprint\", \"publication\", \"creative work\"], \"language\": null, \"date_modified\": \"2018-08-10T10:15:29.153252+00:00\", \"identifiers\": [\"http://dx.doi.org/10.31219/OSF.IO/KD5GZ\", \"http://osf.io/kd5gz/\"], \"date_created\": \"2018-08-09T02:38:03.573962+00:00\"}, \"_score\": null, \"_index\": \"share_customtax_1\", \"_id\": \"pretty&pretty\"}, {\"sort\": [1484715918438], \"_type\": \"creativeworks\", \"_source\": {\"contributors\": [\"Asian Development Bank (ADB)\"], \"date_updated\": \"2014-11-06T00:00:00+00:00\", \"sources\": [\"Research Papers in Economics\"], \"withdrawn\": null, \"retracted\": false, \"title\": \"A Comparative Analysis of Tax Administration in Asia and the Pacific\", \"id\": \"461CC-93E-D06\", \"affiliations\": [], \"subjects\": [], \"type\": \"preprint\", \"registration_type\": null, \"justification\": null, \"description\": \"A robust and sustainable tax system requires good tax administration. This report compares the administrative frameworks, functions, and performances of tax administration bodies in 22 jurisdictions in Asia and the Pacific. The descriptive analysis is based on surveys of tax administration conducted in 2012 and 2013. The surveys attempt to provide internationally comparable data on aspects of the sample jurisdictions\\u2019 tax systems and their administration. Tentative conclusions emerge from the descriptive and comparative analysis. tax system, tax administration, tax revenue, tax collection, nontax function, taxpayer, tax administration expenditure, tax expenditure, Electronic Tax Filing Systems, Electronic Tax Payment, Tax Debt Management, Administrative Review System, Gross Domestic Product, Internal Revenue Commission, taxation, fiscal resources, revenue bodies\", \"tags\": [\"repec\", \"preprint\"], \"lists\": {\"contributors\": [{\"family_name\": \"Bank\", \"name\": \"Asian Development Bank\", \"order_cited\": 0, \"additional_name\": \"Development\", \"type\": \"person\", \"identifiers\": [], \"affiliations\": [], \"awards\": [], \"given_name\": \"Asian\", \"relation\": \"creator\", \"cited_as\": \"Asian Development Bank (ADB)\", \"id\": \"640E4-AB0-E55\", \"types\": [\"person\", \"agent\"]}]}, \"date_published\": null, \"date\": \"2014-11-06T00:00:00+00:00\", \"subject_synonyms\": [], \"types\": [\"preprint\", \"publication\", \"creative work\"], \"language\": null, \"date_modified\": \"2017-01-18T05:05:18.438212+00:00\", \"identifiers\": [\"oai://repec/asd:wpaper:rpt146322\", \"http://www.adb.org/publications/comparative-analysis-tax-administration-asia-and-pacific\"], \"date_created\": \"2017-01-18T05:05:18.438467+00:00\"}, \"_score\": null, \"_index\": \"share_customtax_1\", \"_id\": \"1\"}], \"total\": 2, \"max_score\": null}, \"_shards\": {\"successful\": 5, \"failed\": 0, \"total\": 5}, \"took\": 34, \"aggregations\": {\"sources\": {\"buckets\": [{\"key\": \"crossref\", \"doc_count\": 1}, {\"key\": \"economics\", \"doc_count\": 1}, {\"key\": \"in\", \"doc_count\": 1}, {\"key\": \"osf\", \"doc_count\": 1}, {\"key\": \"papers\", \"doc_count\": 1}, {\"key\": \"research\", \"doc_count\": 1}], \"sum_other_doc_count\": 0, \"doc_count_error_upper_bound\": 0}}, \"timed_out\": false}"
# data = json.dumps(result)
data = json.loads(result)
print(data)