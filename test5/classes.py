from datetime import datetime as dt 


class Animal():
    def __init__(self, animal_id, species, name, birthdate, owner_name, records):
        self.animal_id = animal_id
        self.species = species
        self.name = name
        self.birthdate = birthdate
        self.owner_name = owner_name
        self.records = records

    # 오늘 날짜를 기준으로 해당 동물의 생후 일수를 계산하여 반환
    def get_age_days():
        pass

    # 오늘 날짜를 기준으로 해당 동물의 생후 주차를 계산하여 반환
    def get_age_weeks():
        pass

    # 예방접종 기록을 추가한다.
    def add_record(self, record):
        pass

    # 예방접종 이름과 접종 날짜가 동시에 일치하는 기록 1건을 찾아 삭제한다.
    def remove_record(vaccine_name, shot_date):
        pass

    # 다음 예방접종 예정일 기준으로 기한이 도래했거나 지나버린 기록만 골라 리스트로 반환
    def get_due_records(base_date=None):
        pass




class VaccinRecord():
    def __init__(self, vaccine_name, shot_date, next_due_date):
        self.vaccine_name = vaccine_name
        self.shot_date = shot_date
        self.next_due_date = next_due_date

    # 다음 예방접종 예정일이 존재하는 경우 
    def is_due(self, base_date=None):
        pass

    def __str__(self):
        pass

