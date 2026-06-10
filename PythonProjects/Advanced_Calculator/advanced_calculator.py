from __future__ import annotations

import ast
import json
import logging
import math
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Callable, Final


# ===================== LOGGING =====================

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ===================== CUSTOM EXCEPTIONS =====================

class CalculatorError(Exception):
    """Base exception for calculator errors."""


class InvalidExpressionError(CalculatorError):
    """Raised when expression is invalid."""


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero occurs."""


# ===================== DATA MODELS =====================

@dataclass
class HistoryRecord:
    expression: str
    result: float
    timestamp: str


# ===================== HISTORY SERVICE =====================

class HistoryService:
    def __init__(self, file_path: str = "history.json") -> None:
        self.file_path = Path(file_path)
        self.records: list[HistoryRecord] = []

    def add(self, expression: str, result: float) -> None:
        record = HistoryRecord(
            expression=expression,
            result=result,
            timestamp=datetime.now().isoformat(timespec="seconds")
        )
        self.records.append(record)

    def show(self) -> None:
        if not self.records:
            print("No history found.")
            return

        for index, record in enumerate(self.records, start=1):
            print(f"{index}. {record.expression} = {record.result} [{record.timestamp}]")

    def save(self) -> None:
        data = [asdict(record) for record in self.records]

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"History saved to {self.file_path}")

    def clear(self) -> None:
        self.records.clear()
        print("History cleared.")


# ===================== MEMORY SERVICE =====================

class MemoryService:
    def __init__(self) -> None:
        self._memory: float = 0.0

    def add(self, value: float) -> float:
        self._memory += value
        return self._memory

    def subtract(self, value: float) -> float:
        self._memory -= value
        return self._memory

    def clear(self) -> None:
        self._memory = 0.0

    @property
    def value(self) -> float:
        return self._memory


# ===================== OPERATION ABSTRACTION =====================

class Operation(ABC):
    @abstractmethod
    def execute(self) -> float:
        pass


class BinaryOperation(Operation):
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b


class Add(BinaryOperation):
    def execute(self) -> float:
        return self.a + self.b


class Subtract(BinaryOperation):
    def execute(self) -> float:
        return self.a - self.b


class Multiply(BinaryOperation):
    def execute(self) -> float:
        return self.a * self.b


class Divide(BinaryOperation):
    def execute(self) -> float:
        if self.b == 0:
            raise DivisionByZeroError("Cannot divide by zero.")
        return self.a / self.b


class Power(BinaryOperation):
    def execute(self) -> float:
        return self.a ** self.b


class SquareRoot(Operation):
    def __init__(self, value: float) -> None:
        self.value = value

    def execute(self) -> float:
        if self.value < 0:
            raise CalculatorError("Square root of negative number is not allowed.")
        return math.sqrt(self.value)


class Factorial(Operation):
    def __init__(self, value: float) -> None:
        self.value = value

    def execute(self) -> float:
        if self.value < 0:
            raise CalculatorError("Factorial of negative number is not allowed.")
        if not self.value.is_integer():
            raise CalculatorError("Factorial only works for whole numbers.")

        return float(math.factorial(int(self.value)))


# ===================== SAFE EXPRESSION EVALUATOR =====================

class SafeExpressionEvaluator:
    ALLOWED_FUNCTIONS: Final[dict[str, Callable[..., float]]] = {
        "sqrt": math.sqrt,
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "log": math.log10,
        "ln": math.log,
        "abs": abs,
        "round": round,
    }

    ALLOWED_CONSTANTS: Final[dict[str, float]] = {
        "pi": math.pi,
        "e": math.e,
    }

    ALLOWED_OPERATORS: Final[dict[type, Callable[[float, float], float]]] = {
        ast.Add: lambda a, b: a + b,
        ast.Sub: lambda a, b: a - b,
        ast.Mult: lambda a, b: a * b,
        ast.Div: lambda a, b: a / b,
        ast.Pow: lambda a, b: a ** b,
        ast.Mod: lambda a, b: a % b,
    }

    ALLOWED_UNARY_OPERATORS: Final[dict[type, Callable[[float], float]]] = {
        ast.UAdd: lambda a: +a,
        ast.USub: lambda a: -a,
    }

    def evaluate(self, expression: str) -> float:
        try:
            tree = ast.parse(expression, mode="eval")
            return float(self._evaluate_node(tree.body))
        except ZeroDivisionError:
            raise DivisionByZeroError("Cannot divide by zero.")
        except CalculatorError:
            raise
        except Exception as error:
            raise InvalidExpressionError("Invalid mathematical expression.") from error

    def _evaluate_node(self, node: ast.AST) -> float:
        if isinstance(node, ast.Constant):
            if isinstance(node.value, int | float):
                return float(node.value)
            raise InvalidExpressionError("Only numbers are allowed.")

        if isinstance(node, ast.Name):
            if node.id in self.ALLOWED_CONSTANTS:
                return self.ALLOWED_CONSTANTS[node.id]
            raise InvalidExpressionError(f"Unknown name: {node.id}")

        if isinstance(node, ast.BinOp):
            operator_type = type(node.op)

            if operator_type not in self.ALLOWED_OPERATORS:
                raise InvalidExpressionError("Operator not allowed.")

            left = self._evaluate_node(node.left)
            right = self._evaluate_node(node.right)

            return self.ALLOWED_OPERATORS[operator_type](left, right)

        if isinstance(node, ast.UnaryOp):
            operator_type = type(node.op)

            if operator_type not in self.ALLOWED_UNARY_OPERATORS:
                raise InvalidExpressionError("Unary operator not allowed.")

            value = self._evaluate_node(node.operand)
            return self.ALLOWED_UNARY_OPERATORS[operator_type](value)

        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise InvalidExpressionError("Invalid function call.")

            function_name = node.func.id

            if function_name not in self.ALLOWED_FUNCTIONS:
                raise InvalidExpressionError(f"Function not allowed: {function_name}")

            args = [self._evaluate_node(arg) for arg in node.args]

            return float(self.ALLOWED_FUNCTIONS[function_name](*args))

        raise InvalidExpressionError("Expression contains unsupported syntax.")


# ===================== CALCULATOR CORE =====================

class Calculator:
    def __init__(self) -> None:
        self.history = HistoryService()
        self.memory = MemoryService()
        self.evaluator = SafeExpressionEvaluator()

    def calculate(self, expression: str, operation: Operation) -> float:
        result = operation.execute()
        self.history.add(expression, result)
        logging.info("%s = %s", expression, result)
        return result

    def evaluate_expression(self, expression: str) -> float:
        result = self.evaluator.evaluate(expression)
        self.history.add(expression, result)
        logging.info("%s = %s", expression, result)
        return result


# ===================== CLI APPLICATION =====================

class CalculatorCLI:
    def __init__(self) -> None:
        self.calculator = Calculator()

    def run(self) -> None:
        while True:
            self._show_menu()

            choice = input("Choose option: ").strip()

            try:
                match choice:
                    case "1":
                        self._binary_operation("+", Add)

                    case "2":
                        self._binary_operation("-", Subtract)

                    case "3":
                        self._binary_operation("*", Multiply)

                    case "4":
                        self._binary_operation("/", Divide)

                    case "5":
                        self._binary_operation("^", Power)

                    case "6":
                        value = self._get_number("Enter number: ")
                        result = self.calculator.calculate(f"sqrt({value})", SquareRoot(value))
                        print("Result:", result)

                    case "7":
                        value = self._get_number("Enter number: ")
                        result = self.calculator.calculate(f"{value}!", Factorial(value))
                        print("Result:", result)

                    case "8":
                        expression = input("Enter expression: ")
                        result = self.calculator.evaluate_expression(expression)
                        print("Result:", result)

                    case "9":
                        value = self._get_number("Enter value to add to memory: ")
                        print("Memory:", self.calculator.memory.add(value))

                    case "10":
                        value = self._get_number("Enter value to subtract from memory: ")
                        print("Memory:", self.calculator.memory.subtract(value))

                    case "11":
                        print("Memory:", self.calculator.memory.value)

                    case "12":
                        self.calculator.memory.clear()
                        print("Memory cleared.")

                    case "13":
                        self.calculator.history.show()

                    case "14":
                        self.calculator.history.save()

                    case "15":
                        self.calculator.history.clear()

                    case "0":
                        print("Calculator closed.")
                        break

                    case _:
                        print("Invalid option.")

            except CalculatorError as error:
                print("Error:", error)
                logging.error("Calculator error: %s", error)

    def _show_menu(self) -> None:
        print("\n========== PRODUCTION-GRADE OOP CALCULATOR ==========")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Factorial")
        print("8. Evaluate Expression")
        print("9. Memory Add")
        print("10. Memory Subtract")
        print("11. Show Memory")
        print("12. Clear Memory")
        print("13. Show History")
        print("14. Save History")
        print("15. Clear History")
        print("0. Exit")

    def _get_number(self, message: str) -> float:
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Please enter a valid number.")

    def _binary_operation(
        self,
        symbol: str,
        operation_class: type[BinaryOperation]
    ) -> None:
        a = self._get_number("Enter first number: ")
        b = self._get_number("Enter second number: ")

        expression = f"{a} {symbol} {b}"
        operation = operation_class(a, b)

        result = self.calculator.calculate(expression, operation)
        print("Result:", result)


# ===================== ENTRY POINT =====================

def main() -> None:
    app = CalculatorCLI()
    app.run()


if __name__ == "__main__":
    main()