class MyLexic:
    company = 'IT Resume'

    def __init__(self, code, problem_id):
        self.code = code
        self.problem_id = problem_id

    def describe(self):
        return f'Компания: {self.company}, код: {self.code}, номер задачи: {self.problem_id}.'

    def strip_code(self):
        ...


class MyPythonLexic(MyLexic):

    def __init__(self, code, problem_id, version):
        super().__init__(code, problem_id)
        self.version = version

    def strip_code(self):
        return self.code.strip().split()


class MyJavaLexic(MyLexic):

    def __init__(self, code, problem_id, platform):
        super().__init__(code, problem_id)
        self.platform = platform

    def strip_code(self):
        line = [i.strip("{}") for i in self.code.split("\n")]
        return line


o1 = MyJavaLexic("{ print(1)  }\n  print(2)  ", 2, platform="SE")

print(o1.platform)
# SE

print(o1.strip_code())
# [" print(1)  ", "   print(2)  "]

o1 = MyPythonLexic(" print(1)  \n   print(2)  ", 2, version="3.8")

print(o1.strip_code())
# ["print(1)", "print(2)"]

o1 = MyLexic(" print(1)  \n   print(2)  ", 2)

print(o1.strip_code())
# None

print(o1.version)
# Error
