class Person: # 클래스 객체 생성 (클래스 정의)
    name = '이름이란, 사람이 공통적으로 가지는 속성'
    age = '나이란, 내가 태어나서 죽을때까지의 기간'

    def greeting(self):
        return f'{self.name}이 인사합니다. 안녕하세요!'

    def aging(self):
        return f'{self.name}은 {self.age}살 입니다.'

    @classmethod
    def age_means(cls):
        return f'{cls.name}은 나라마다 다르다.'

p1 = Person()
p1.name = "김현수"
p1.age = 100
print(Person.name)
print(Person.age)
print(p1.name)
print(p1.age)
print(p1.greeting())
print(p1.aging())
print(Person.age_means())
print(p1.age_means())