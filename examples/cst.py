from z3 import Solver, sat, Int


class CSTExample:

    @staticmethod
    def execute():
        print("-- Execute circle square triangle example")
        solver = Solver()

        circle = Int('circle')
        square = Int('square')
        triangle = Int('triangle')

        solver.add(circle + circle == 10)
        solver.add(circle * square + square == 12)
        solver.add(circle * square - triangle * circle == circle)

        check = solver.check()
        print(check)
        if check == sat:
            print(solver.model())
