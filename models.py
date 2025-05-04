from sqlalchemy import Column
from sqlalchemy.dialects.mysql import JSON
from sqlmodel import SQLModel, Field


class StudentEntity(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str = Field(..., title="First Name", max_length=100)
    last_name: str = Field(..., title="Last Name", max_length=100)
    street_address: str = Field(..., title="Street Address", max_length=255)
    city: str = Field(..., title="City", max_length=100)
    state: str = Field(..., title="State", max_length=100)
    zip: str = Field(..., title="ZIP Code", max_length=10)
    phone_number: str = Field(..., title="Phone Number", max_length=15)
    email: str = Field(..., title="Email", max_length=255)
    date_of_survey: str = Field(..., title="Date of Survey")
    liked_most: list[str] = Field(
        default_factory=list,
        title="What you liked most about the campus",
        sa_column=Column(JSON)
    )
    interest_source: str = Field(..., title="How you became interested in the university")
    recommend_likelihood: str = Field(..., title="Likelihood of recommending the school")
