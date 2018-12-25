import types


class A:
    def speak(self):
        return "hello"


def speak_patch(self):
    return "world"


A.speak = types.MethodType(speak_patch, A)
a = A()
print('a.speak():', a.speak())

a2 = A()
print('a2.speak():', a2.speak())


