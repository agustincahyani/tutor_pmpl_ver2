# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def find_dupes(apps, schema_editor):
	List = apps.get_model("lists", "List")
	for list_ in List.objects.all():
		items = lists_.item_set.all()
		texts = set()
		for ix, item in enumerate(items):
			if item.text in texts:
				item.text = '{} ({})'.format(item.text, ix)
				item.save()
			texts.add(item.text)

class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20150922_1225'),
    ]

    operations = [
	migrations.RunPython(find_dupes),
    ]
