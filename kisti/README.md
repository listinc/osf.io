## How to run the scripts for kisti

1. Set up your environment
- Implement the requirements setting `pip install psycopg2`

2. Set up your db, ip, file
- `./osf/request.py` change host, email(default)
- `./osf/read_json.py` change file_name
- `./osf/confirm.py` change host
- `./osf/subject.py` chage subject value
> This value will be changed when it installed
    Subject is below to sql

    `select * from osf_subject where parent_id IS NULL;`

    social and behavioral sciences - library and information science

    `select * from osf_subject where parent_id = 143;`
    
- `./osf/formdata.py` change licenses value
> 'licenses' value will be changed when it installed

	license_data['id'] is below to sql, license _id is no license
	
	`select * from osf_nodelicense;`

3. Check your api server on
- `python ./test/request_test.py`

4. Run command
- create user `python ./script/create_user.py`
- confirm user `python ./script/confirm_user.py`
- create_preprints `python ./script/create_preprints.py`
- create index `python ./script/indexing.py`


