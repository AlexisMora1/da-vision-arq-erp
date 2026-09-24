from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes.catalog.route import router as catalog_router
from app.routes.customers.route import router as sales_router
from app.routes.projects.route import router as projects_router
from app.routes.storage.route import router as storage_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="DotAxion App", lifespan=lifespan)
app.include_router(projects_router)
app.include_router(sales_router)
app.include_router(storage_router)
app.include_router(catalog_router)

