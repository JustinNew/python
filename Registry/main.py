from real_time_engine.constraint.constraint import ConstraintManager
from importlib import import_module

def main(config_file="zone_day_offline"):
    config = import_module(f".{config_file}", "real_time_engine.configs")
    constraint = ConstraintManager.create_constraint(config.CONSTRAINT_CONFIG.CONSTRAINT)(config.CONSTRAINT_CONFIG)

    constraint.get_constraint(1)


if __name__ == "__main__":
    main()