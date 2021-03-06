
class Entry:
    def __init__(self, obj, line_number = 1):
        self.obj = obj
        self.line_number = line_number

    def __repr__(self):
        return "In {}, line {}".format(self.obj.name, self.line_number)

class CallStack:
    def __init__(self, initial = None):
         self.__stack = [] if not initial else initial

    def __repr__(self):
        stk =  "\n".join([str(entry) for entry in self.__stack])
        return "Traceback (Most recent call last):\n" + stk + "\n"

    __str__ = __repr__

    def __len__(self):
        return len(self.__stack)

    def append(self, entry):
        self.__stack.append(entry)

    def pop(self):
        last = self.__stack[-1]
        self.__stack.pop()
        return last

    def __getitem__(self, index):
        if isinstance(index, slice):
            return CallStack(self.__stack[index])
        else: return self.__stack[index]

