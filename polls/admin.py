from django.contrib import admin

import polls.models as dataModels

for model in [dataModels.School, dataModels.Department, dataModels.Course, dataModels.Student, dataModels.Review]:
    admin.site.register(model)