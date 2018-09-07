from random import randint


class Subject():
    subject = {}

    def __init__(self):

        self.subject['law'] = ['5b584935cd0fb4000147522e']
        self.subject['art'] = ['5b584936cd0fb40001475243']
        self.subject['business'] = ['5b584936cd0fb40001475247']
        self.subject['life'] = ['5b584936cd0fb40001475250']
        self.subject['medicine'] = ['5b584936cd0fb40001475271']
        self.subject['social'] = ['5b584937cd0fb400014752ba']
        self.subject['education'] = ['5b584937cd0fb400014752c9']
        self.subject['science'] = ['5b584937cd0fb400014752ea']
        self.subject['architecture'] = ['5b584937cd0fb400014752eb']
        self.subject['engineering'] = ['5b584938cd0fb4000147531e']
        self.subject['library'] = ['5b584937cd0fb400014752ba', '5b584937cd0fb400014752cd']

    def random_subject(self):
        val = randint(0, 9)
        return self.numbering(val)

    def numbering(self, x):
        return {
            0: 'science',
            1: 'law',
            2: 'art',
            3: 'business',
            4: 'life',
            5: 'medicine',
            6: 'social',
            7: 'education',
            8: 'architecture',
            9: 'engineering'
        }.get(x, 4)

    def get_subject(self, po):

        library = ['한국기록관리학회', '한국기록학회', '한국도서관·정보학회', '한국문헌정보학회', '한국비블리아학회', '한국서지학회', '한국정보관리학회']
        law = ['법', '법률', '법학']
        art = ['예술', '영화', '음악']
        business = ['경영', '경상', '경제', '산업', '무역', '정책', '도시']
        life = ['생활', '여성', '남성', '행정', '한문', '한글', '문화', '인문', '아시아', '문학', '외국어', '학술', '국어']
        medicine = ['초음파', '조현병', '치료', '치주', '암', '의료']
        social = ['사회', '동북아', '정보', '복지']
        education = ['교육', ]
        science = ['암석', '수학', '조류', '과학', '우주']
        architecture = ['건축', '인테리어']
        engineering = ['전산', '유체', '컴퓨터', '전기', '전자']

        if po in library:
            return self.subject['library']
        for i in law:
            if i in po:
                return self.subject['law']
        for i in art:
            if i in po:
                return self.subject['art']
        for i in business:
            if i in po:
                return self.subject['business']
        for i in life:
            if i in po:
                return self.subject['life']
        for i in medicine:
            if i in po:
                return self.subject['medicine']
        for i in social:
            if i in po:
                return self.subject['social']
        for i in education:
            if i in po:
                return self.subject['education']
        for i in science:
            if i in po:
                return self.subject['science']
        for i in architecture:
            if i in po:
                return self.subject['architecture']
        for i in engineering:
            if i in po:
                return self.subject['engineering']
        return self.subject[self.random_subject()]
