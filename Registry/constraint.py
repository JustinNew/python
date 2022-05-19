class BaseConstraint:
    """Constraint interface"""

    def __init__(self):
        pass

    def _get_data(self):
        raise NotImplementedError

    def _calculate_constraint(self):
        raise NotImplementedError

    def get_constraint(self):
        raise NotImplementedError

class ConstraintManager:
    """The registery for constraints. Can be used to create constraints from name"""

    constraints = {}

    @classmethod
    def register_constraint(cls, constraint: BaseConstraint):
        if constraint.__name__ in cls.constraints:
            raise NameError(f"The class name {constraint.__name__} has been used")
        cls.constraints[constraint.__name__] = constraint
        return constraint

    @classmethod
    def create_constraint(cls, name):
        return cls.constraints[name]

