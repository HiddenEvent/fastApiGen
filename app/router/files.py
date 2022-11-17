from fastapi import APIRouter, Depends
from starlette.responses import FileResponse

from app.common.config import base_dir

router = APIRouter()


@router.get("/download")
def download_file():
    # file_path = base_dir + "\Richard_KIM.mp4"
    # file_path = "/home/abc/videos/movie1.mp4"
    # return FileResponse(path=file_path, filename=file_path)
    file_path = base_dir + '\generator.txt'
    file = open(file_path, 'w', encoding='utf8')
    file.write('test합니다.222211')
    file.close()
    return FileResponse(path=file_path, filename=file_path)
