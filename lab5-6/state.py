class State:
    def next(self, context):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class Red(State):
    def next(self, context):
        context.set_state(Yellow())
        print("Switching from RED to YELLOW")

    def __str__(self):
        return "RED"


class Yellow(State):
    def next(self, context):
        context.set_state(Green())
        print("Switching from YELLOW to GREEN")

    def __str__(self):
        return "YELLOW"


class Green(State):
    def next(self, context):
        context.set_state(Red())
        print("Switching from GREEN to RED")

    def __str__(self):
        return "GREEN"
