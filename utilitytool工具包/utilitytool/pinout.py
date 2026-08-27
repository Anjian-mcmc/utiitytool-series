__all__ = ['pout','pin','endl','rel']
class __endl_base:
    def __repr__():return '\n'
class __rel_base:
    def __repr__():return '\r'
class __pout_base:
    @classmethod
    def __lshift__(other):
        if isinstance(other,__rel_base):
            print(end = '\r')
        elif isinstance(other,__endl_base):
            print()
        else:
            print(other,end = '')
        return __pout_base()
class __pin_base:
    @classmethod
    def __rshift__(other):
        other = input()
        return __pin_base()
pout = __pout_base()
pin = __pin_base()
endl = __endl_base()
rel = __rel_base()
