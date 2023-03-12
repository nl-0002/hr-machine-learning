import pytest
import pandas as pd
from src.model.models import InputData
from src.utils import preprocess, postprocess

@pytest.fixture
def sample_data():
    return InputData(
        enrollee_id=123,
        city_development_index=0.92,
        gender='Male',
        relevent_experience='Has relevent experience',
        enrolled_university='no_enrollment',
        education_level='Graduate',
        major_discipline='STEM',
        experience='9',
        company_size='50-99',
        company_type='Pvt Ltd',
        last_new_job='1',
        training_hours=20
    )

def test_preprocess(sample_data):
    enrollee_id, data = preprocess(sample_data)
    assert enrollee_id == 123
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (1, 11)
    assert set(data.columns) == set([
        'city_development_index', 'gender',
        'enrolled_university', 'education_level', 'major_discipline',
        'experience', 'company_size', 'company_type',
        'last_new_job','relevent_experience', 'training_hours'
    ])
    assert data.loc[0, 'city_development_index'] == 0.92
    assert data.loc[0, 'gender'] == 'Male'
    assert data.loc[0, 'relevent_experience'] == 'Has relevent experience'
    assert data.loc[0, 'enrolled_university'] == 'no_enrollment'
    assert data.loc[0, 'education_level'] == 'Graduate'
    assert data.loc[0, 'major_discipline'] == 'STEM'
    assert data.loc[0, 'experience'] == '9'
    assert data.loc[0, 'company_size'] == '50-99'
    assert data.loc[0, 'company_type'] == 'Pvt Ltd'
    assert data.loc[0, 'last_new_job'] == '1'
    assert data.loc[0, 'training_hours'] == 20

def test_preprocess_1(sample_data):
    enrollee_id, data = preprocess(sample_data)
    expected_data = pd.DataFrame({
        'city_development_index': [0.92],
        'gender': ['Male'],
        'relevent_experience': ['Has relevent experience'],
        'enrolled_university': ['no_enrollment'],
        'education_level': ['Graduate'],
        'major_discipline': ['STEM'],
        'experience': ['9'],
        'company_size': ['50-99'],
        'company_type': ['Pvt Ltd'],
        'last_new_job': ['1'],
        'training_hours': [20]
    })
    assert enrollee_id == 123
    assert data.equals(expected_data)

@pytest.mark.parametrize("enrollee_id, data, expected_response", [
    (123, [0], "Enrollee Id: 123 is likely to stay in the company"),
    (456, [1], "Enrollee Id: 456 is likely to leave the company"),
])
def test_postprocess(enrollee_id, data, expected_response):
    assert postprocess(enrollee_id, data) == expected_response