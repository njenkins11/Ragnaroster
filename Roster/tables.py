import django_tables2 as tables
from .models import Roster

class RosterTable(tables.Table):
    class Meta:
        model = Roster
        fields = ("options","name", "start_time","end_time","realm","guild","faction")
        template_name = "django_tables2/bootstrap.html"
        

    options = tables.TemplateColumn(template_name='column.html')

