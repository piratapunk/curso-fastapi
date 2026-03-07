from fastapi import FastAPI, HTTPException
from models import CustomerCreate, Customer, Transaction, Invoice
from db import SessionDep

app = FastAPI()

db_customers: list[Customer] = []


@app.get("/customers", response_model=list[Customer])
async def list_customer():
    return db_customers


@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int):
    for customer in db_customers:
        if customer.id == customer_id:
            return customer
    raise HTTPException(
        status_code=404, detail=f"No se encontró un cliente con el id {customer_id}"
    )


@app.post("/customers", response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    customer.id = len(db_customers)
    db_customers.append(customer)
    return customer


@app.post("/transactions")
async def create_transactions(transactions_data: Transaction):
    return transactions_data


@app.post("/invoices")
async def create_invoices(invoices_data: Invoice):
    return invoices_data
