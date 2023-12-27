from django.db import transaction
import polls.models as dataModels
import pandas as pd

@transaction.atomic
def createSchool(name, country, website, description, courses: pd.DataFrame):
    school = dataModels.School(
        name=name,
        country=country,
        website=website,
        description=description
    )
    school.save()

    for name, group in courses.drop_duplicates('code').groupby('department'):
        department = dataModels.Department(
            name=name,
            school=school
        )
        department.save()

        for index, row in group.iterrows():
            course = dataModels.Course(
                school=school,
                department=department,
                code=row['code'],
                name=row['name'],
                credits=float(row.credits.rstrip(' Credit').rstrip(' Credits')),
                description=row['description'],
                url=row['url'],
            )
            course.save()

# columns = ['url', 'code', 'name', 'credits', 'description', 'department']
courses = pd.read_csv('./scripts/scraping/laurier/courses.csv')
createSchool(
    name='Wilfrid Laurier University',
    country='Canada',
    website='https://www.wlu.ca/',
    description='Wilfrid Laurier University is a public university in Waterloo, Ontario, Canada. Laurier has a second campus in Brantford and offices in Kitchener, Toronto and Chongqing, China.',
    courses=courses
)
