from django.contrib import admin
from .models import *

admin.site.register([OrgnizationalInformation, Admin, Services, Team,Contact])
