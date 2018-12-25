class A:
    def speak(self):
        return "hello"


def speak_patch(self):
    return "world"


A.speak = speak_patch
some_class = A()
print('some_class.speak():', some_class.speak())

some_class2 = A()
print('some_class2.speak():', some_class2.speak())
