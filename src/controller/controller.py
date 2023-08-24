import datetime
import json

import requests

from src.model.loan.adapter.uow import LoanUnitOfWork
from src.model.loan.service.loan import LoanInputService, LoanService
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
        elif menu == "2":
            self.run_calculation_from_api(
                url="http://www.mocky.io/v2/5d06e6ae3000005300051d16"
            )

    def run_input_calculation(self):
        vehicle_type = self.view.input_vehicle_type()

        vehicle_condition = self.view.input_vehicle_condition()
        vehicle_year = self.view.input_vehicle_year()
        if vehicle_condition == "baru" and vehicle_year < int(
            datetime.date.today().year - 1
        ):
            while vehicle_condition == "baru" and vehicle_year < int(
                datetime.date.today().year - 1
            ):
                self.view.output(
                    "Tahun kendaraan baru tidak boleh lebih dari 1 tahun"
                )
                vehicle_year = self.view.input_vehicle_year()
        total_loan = self.view.input_total_loan()
        tenor = self.view.input_tenor()
        down_payment = self.view.input_down_payment()
        if down_payment > total_loan:
            while down_payment > total_loan:
                self.view.output(
                    "Uang Muka tidak boleh lebih besar dari total pinjaman"
                )
                down_payment = self.view.input_down_payment()
        if vehicle_condition == "baru" and down_payment / total_loan < 0.35:
            while (
                vehicle_condition == "baru"
                and down_payment / total_loan < 0.35
            ):
                self.view.output(
                    "Uang Muka untuk kendaraan baru tidak boleh kurang dari 35% dari total pinjaman"
                )
                down_payment = self.view.input_down_payment()
        if vehicle_condition == "bekas" and down_payment / total_loan < 0.25:
            while (
                vehicle_condition == "bekas"
                and down_payment / total_loan < 0.25
            ):
                self.view.output(
                    "Uang Muka untuk kendaraan bekas tidak boleh kurang dari 25% dari total pinjaman"
                )
                down_payment = self.view.input_down_payment()
        self.loan_input_service = LoanInputService(uow=self.uow)
        self.loan_input_service.input_vehicle(
            vehicle_type=vehicle_type,
            vehicle_condition=vehicle_condition,
            vehicle_year=vehicle_year,
        )
        self.loan_input_service.input_loan(
            total_loan=total_loan, tenor=tenor, down_payment=down_payment
        )
        self.loan_service = LoanService(uow=self.uow)
        calculation = self.loan_service.calculate_loan()
        self.view.output_loan(calculation)
        self.run_menu()

    def run_calculation_from_file(self, filepath):
        with open(filepath, "r") as file:
            data = file.read()
        try:
            json_data = json.loads(data)
        except json.decoder.JSONDecodeError:
            self.view.output("File tidak valid")
            self.run_menu()
        json_data = json_data["vehicleModel"]
        self.loan_input_service = LoanInputService(uow=self.uow)
        self.loan_input_service.input_vehicle(
            vehicle_type=json_data["vehicleType"].lower(),
            vehicle_condition=json_data["vehicleCondition"].lower(),
            vehicle_year=json_data["tahunMobil"],
        )
        self.loan_input_service.input_loan(
            total_loan=float(json_data["jumlahPinjaman"]),
            tenor=int(json_data["tenorCicilan"]),
            down_payment=float(json_data["jumlahDownPayment"]),
        )
        self.loan_service = LoanService(uow=self.uow)
        calculation = self.loan_service.calculate_loan()
        self.view.output_loan(calculation)
        self.run_menu()

    def run_calculation_from_api(self, url):
        data = requests.get(url)
        stripped_data = data.text.replace('"responseCode":"00",', "")
        stripped_data = stripped_data.replace(
            '"responseMessage":"Succeed"', ""
        )
        json_data = json.loads(stripped_data)
        json_data = json_data["vehicleModel"]
        self.loan_input_service = LoanInputService(uow=self.uow)
        self.loan_input_service.input_vehicle(
            vehicle_type=json_data["vehicleType"].lower(),
            vehicle_condition=json_data["vehicleCondition"].lower(),
            vehicle_year=json_data["tahunMobil"],
        )
        self.loan_input_service.input_loan(
            total_loan=float(json_data["jumlahPinjaman"]),
            tenor=int(json_data["tenorCicilan"]),
            down_payment=float(json_data["jumlahDownPayment"]),
        )
        self.loan_service = LoanService(uow=self.uow)
        calculation = self.loan_service.calculate_loan()
        self.view.output_loan(calculation)
        self.run_menu()
