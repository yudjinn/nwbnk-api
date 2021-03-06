from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, bank, company, transaction

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(bank.router, prefix="/bank", tags=["bank"])
api_router.include_router(company.router, prefix="/company", tags=["company"])
api_router.include_router(
    transaction.router, prefix="/transaction", tags=["transaction"]
)
