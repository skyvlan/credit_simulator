from typing import List

from src.model.loan.domain.entity import LoanOutput
from src.view.BaseView import BaseView


class ConsoleView(BaseView):
    def __init__(self):
        pass

    def output(self, string):
        print(string)

    def input(self, string):
        return input(string)

    def input_vehicle_type(self):
        input = self.input("Masukkan Jenis Kendaraan (Motor|Mobil): ").lower()
        if not input.isalpha():
            self.output("Jenis Kendaraan tidak valid")
            return self.input_vehicle_type()
        if input != "motor" and input != "mobil":
            self.output("Jenis Kendaraan tidak valid")
            return self.input_vehicle_type()
        return input

    def input_vehicle_condition(self):
        input = self.input("Masukkan Kondisi Kendaraan (Baru|Bekas): ").lower()
        if not input.isalpha():
            self.output("Kondisi Kendaraan tidak valid")
            return self.input_vehicle_condition()
        if input != "baru" and input != "bekas":
            self.output("Kondisi Kendaraan tidak valid")
            return self.input_vehicle_condition()
        return input

    def input_vehicle_year(self):
        input = self.input("Masukkan Tahun Kendaraan: ")
        if not input.isnumeric() or int(input) < 1000 or int(input) > 9999:
            self.output("Tahun Kendaraan tidak valid")
            return self.input_vehicle_year()
        return int(input)

    def input_total_loan(self):
        input = self.input("Masukkan Jumlah Total Pinjaman: ")
        if not input.isnumeric():
            self.output("Total Pinjaman tidak valid")
            return self.input_total_loan()
        if int(input) >= 1000000000:
            self.output("Total Pinjaman tidak boleh melebihi 1 milyar")
            return self.input_total_loan()
        return float(input)

    def input_tenor(self):
        input = self.input("Masukkan Tenor Pinjaman: ")
        if not input.isnumeric():
            self.output("Tenor Pinjaman tidak valid")
            return self.input_tenor()
        if int(input) > 6:
            self.output("Tenor Pinjaman tidak boleh melebihi 6 tahun")
            return self.input_tenor()
        if int(input) < 1:
            self.output("Tenor Pinjaman tidak boleh kurang dari 1 tahun")
            return self.input_tenor()
        return int(input)

    def input_down_payment(self):
        input = self.input("Masukkan Uang Muka: ")
        if not input.isnumeric():
            self.output("Uang Muka tidak valid")
            return self.input_down_payment()
        return float(input)

    def output_loan(self, loan_output: List[LoanOutput]):
        for i in loan_output:
            self.output(
                f"Tahun {i.year}: Rp.{i.installment}/bln, Suku Bunga: {i.interest}"
            )
