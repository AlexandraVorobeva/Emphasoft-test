from fastapi import APIRouter
from api.users import router as user_router
from api.auth import router as auth_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(user_router)
