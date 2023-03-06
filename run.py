import uvicorn
from src.config import APP_WORKERS

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="localhost", port=2222, workers=APP_WORKERS, reload=True)


# {
#     "city_development_index": "0.827",
#     "gender": "Male",
#     "relevent_experience": "Has relevent experience",
#     "enrolled_university": "Full time course",
#     "education_level": "Graduate",
#     "major_discipline": "STEM",
#     "experience": "9",
#     "company_size": "<10",
#     "company_type": null,
#     "last_new_job": "1",
#     "training_hours": "21",
# }
