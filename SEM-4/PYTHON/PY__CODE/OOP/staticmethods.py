''' using static method()
class Shape:
    def info(msg):
        print(msg)
        print("Wlcome my friend")
Shape.info=staticmethod(Shape.info)
Shape.info("Hello")
'''

# using @static method
class Shape2:
    @staticmethod
    def info(msg):
        print(msg)
        print("Wlcome my friend")
Shape2.info("Hello")