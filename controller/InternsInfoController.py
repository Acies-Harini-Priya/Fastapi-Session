from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from controller.dto.AddNewInternBody import AddNewInternBody
from controller.dto.UpdateInternBody import UpdateInternBody
from services.InternsInfoService import InternsInfoService

interns_info_service = InternsInfoService()
interns_info_router = APIRouter(prefix="/InternsInfo")

# READ / GET all interns
@interns_info_router.get("/GetInterns")
async def getInterns():
    try:
        interns = interns_info_service.getAllInterns()
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"data": interns, "message": "Fetched successfully"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# CREATE / ADD Intern
@interns_info_router.post("/Addintern")
async def addIntern(body: AddNewInternBody):
    try:
        result = interns_info_service.addNewIntern(body)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=result
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    
# PUT / UPDATE Intern
@interns_info_router.put("/UpdateIntern/{id}")
async def updateIntern(id: int, body: UpdateInternBody):
    try:
        result = interns_info_service.updateIntern(id, body)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=result
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    
# DELETE / DELETE Intern
@interns_info_router.delete("/DeleteIntern/{id}")
async def deleteIntern(id: int):
    try:
        result = interns_info_service.deleteIntern(id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=result
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )