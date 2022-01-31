class User:
    def __init__(self, sex, age):
        if sex not in ('m', 'м', 'мужской', 'f', 'ж', 'женский'):
            raise ValueError

        if not isinstance(age, int):
            raise TypeError

        self.age = age
        self.sex = sex
