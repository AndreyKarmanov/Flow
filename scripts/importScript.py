from django.db import transaction
from polls.models import Course
import pandas as pd

@transaction.atomic
def insert_courses_into_db():
    df2 = pd.read_csv('laurier_courses.csv')
    school_pk = 2
    department_pk = 2

    for index, row in df2.iterrows():
        course = Course(
            school_id=school_pk,
            department_id=department_pk,
            title=row.name,
            credits=row.credits,
            code=row.title,
            description=row.description
        )
        course.save()

# Call the function to insert the courses into the database
insert_courses_into_db()
