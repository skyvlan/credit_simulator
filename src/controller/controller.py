from src.model.loan.service.loan import LoanService, LoanInputService
from src.model.loan.adapter.uow import LoanUnitOfWork
from src.view.ConsoleView import ConsoleView
class LoanController:
    def __init__(self, uow: LoanUnitOfWork = LoanUnitOfWork()):
        self.loan_service = None
        self.loan_input_service = None
        self.uow = uow
        self.view = ConsoleView()

    def run_menu(self):
        self.view.output("Menu")
        self.view.output("1. Masukkan Data Pinjaman")
        self.view.output("2. Load Data Pinjaman Existing")
        self.view.output("3. Exit")
        menu = self.view.input("Pilih Menu: ")
        if menu == "1":
            self.run_input_calculation()
    def run_input_calculation(self):
        vehicle_type = self.view.input_vehicle_type()

        vehicle_condition = self.view.input_vehicle_condition()
        vehicle_year = self.view.input_vehicle_year()
        total_loan = self.view.input_total_loan()
        tenor = self.view.input_tenor()
        down_payment = self.view.input_down_payment()
        if down_payment > total_loan:
            while down_payment > total_loan:
                self.view.output("Uang Muka tidak boleh lebih besar dari total pinjaman")
                down_payment = self.view.input_down_payment()
        if vehicle_condition == "baru" and down_payment / total_loan <= 0.35:
            while vehicle_condition == "baru" and down_payment / total_loan <= 0.35:
                self.view.output("Uang Muka untuk kendaraan baru tidak boleh kurang dari 35% dari total pinjaman")
                down_payment = self.view.input_down_payment()
        if vehicle_condition == "bekas" and down_payment / total_loan <= 0.25:
            while vehicle_condition == "bekas" and down_payment / total_loan <= 0.25:
                self.view.output("Uang Muka untuk kendaraan bekas tidak boleh kurang dari 25% dari total pinjaman")
                down_payment = self.view.input_down_payment()
        print(vehicle_type, vehicle_condition, vehicle_year, total_loan, tenor, down_payment)
        self.loan_input_service = LoanInputService(uow=self.uow)
        self.loan_input_service.input_vehicle(vehicle_type=vehicle_type, vehicle_condition=vehicle_condition, vehicle_year=vehicle_year)
        self.loan_input_service.input_loan(total_loan=total_loan, tenor=tenor, down_payment=down_payment)
        self.loan_service = LoanService(uow=self.uow)
        calculation = self.loan_service.calculate_loan()
        self.view.output_loan(calculation)
        self.run_menu()

    def run_calculation_from_file(self):
        pass


