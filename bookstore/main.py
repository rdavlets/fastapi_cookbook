import books
import authors
import json
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.responses import JSONResponse

app = FastAPI()
app.include_router(books.router)
app.include_router(authors.router)


@app.get("/")
async def read_root():
    return {"msg": "Welcome to Bookstore!"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "Oops! Something wend wrong"},
    )


@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(
        "This is a plain text response:" f" \n{json.dumps(exc.errors(), indent=2)}",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
