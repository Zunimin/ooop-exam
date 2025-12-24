# Adaptee
class OldPrinter:
    def print_old(self, text):
        return f"OLD: {text}"


# Target
class NewPrinter:
    def print_new(self, text):
        pass


# Адаптер
class PrinterAdapter(NewPrinter):
    def __init__(self, old_printer):
        self.old = old_printer

    def print_new(self, text):
        old_result = self.old.print_old(text)
        return old_result.replace("OLD: ", "")  # адаптируем


# Использование
old = OldPrinter()
adapter = PrinterAdapter(old)

print(adapter.print_new("Hello World"))
