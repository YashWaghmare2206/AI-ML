

## So whenever we make an file then its special name is __name__ = "__main__" but when we import it in some other file the its special name changes to module name __name__ = "<filename>"
class Converter:

    def to_celsius(self , far):
        celsius = (far - 32) * 5/9
        return celsius

    def to_far(self , cel):

        far = (cel * 9/5) + 32
        return far

