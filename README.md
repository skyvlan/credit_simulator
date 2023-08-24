# Credit Simulator
## Description
- This is a technical assesment for recruitment purposes. The goal is to create a credit simulator that will calculate the monthly payment of a loan.
- The project is made using Python 3.8 and Poetry as a dependency manager.
- The project is using MVC architecture and Domain Driven Design.
- The project is using a CLI interface.
## Requirements
- Python 3.8 or higher
- Poetry 

## How To Run
1. Clone the repository
2. Install dependencies with poetry (if you don't have poetry install, install it with `pip install poetry` 
```bash
poetry install
```
3. Run the application
```bash
/bin/credit_simulator
```
you can also run it with poetry
```bash
poetry run python main.py
```
you can also use files as input
```bash
/bin/credit_simulator <file_name>
```
the file should contain following json format to be parsable:
```json
{
    "vehicleModel":{
        "vehicleCondition" : "Baru",
        "vehicleType" : "Mobil",
        "tahunMobil" : "2019",
        "jumlahDownPayment" : "25000000",
        "jumlahPinjaman" : "100000000",
        "tenorCicilan":"5"
    },
    "responseCode":"00",
    "responseMessage":"Succeed"
}
```


### Alternative installation
If you don't want to use poetry you can also use docker to run the application, specified in the Dockerfile in deployment/deploy/Dockerfile
```bash
docker build -t credit_simulator .
docker run -it credit_simulator
```
or you can get the image from dockerhub



