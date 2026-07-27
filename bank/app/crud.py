from sqlalchemy.orm import Session

from . import models, schemas


def create_customer(db: Session, customer: schemas.CustomerCreate) -> models.Customer:
    db_customer = models.Customer(
        name=customer.name,
        email=customer.email,
        phone=customer.phone,
        address=customer.address,
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def list_customers(db: Session):
    return db.query(models.Customer).order_by(models.Customer.id).all()


def create_transaction(db: Session, transaction: schemas.TransactionCreate) -> models.Transaction:
    customer = db.query(models.Customer).filter(models.Customer.id == transaction.customer_id).first()
    if customer is None:
        raise ValueError("Customer not found")

    db_transaction = models.Transaction(
        customer_id=transaction.customer_id,
        transaction_type=transaction.transaction_type,
        amount=transaction.amount,
        description=transaction.description,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def list_transactions(db: Session):
    return db.query(models.Transaction).order_by(models.Transaction.id).all()
