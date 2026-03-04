from fastapi import FastAPI

from models import CustomerCreate, Customer, Transaction, Invoice

app = FastAPI()

current_id: int = 0


@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate):
    Customer.model_validate(customer_data.model_dump())
    return customer_data


@app.post("/transactions")
async def create_transactions(transactions_data: Transaction):
    return transactions_data


@app.post("/invoices")
async def create_invoices(invoices_data: Invoice):
    return invoices_data
