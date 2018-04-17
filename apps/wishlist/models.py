from __future__ import unicode_literals
from ..login.models import User
from django.db import models


class ItemManager(models.Manager):
	def validate(self, form_data):
		errors = []
		name = form_data['name']

		if len(name) == 0:
			errors.append("Please type name of item")
		if len(name) < 3:
			errors.append("Item name should be more than 3 characters long")

		return errors

	def add_wish(self, item_id, user_id):
		user = User.objects.get(id= user_id)
		item = Item.objects.get(id= item_id)
		user.wishes.add(item)


	def remove_wish(self, item_id, user_id):
		user = User.objects.get(id= user_id)
		item = Item.objects.get(id= item_id)
		user.wishes.remove(item)


	def create_item(self, form_data, user_id):
		user = User.objects.get(id=user_id)
		wish = self.create(
		name = form_data['name'],
		added_by = user
		)
		return wish

	def delete_item(self, item_id):
		item = Item.objects.get(id= item_id).delete()


class Item(models.Model):
	name = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	added_by = models.ForeignKey(User, related_name="added_items")
	wished_by = models.ManyToManyField(User, related_name="wishes")
	objects = ItemManager()

	def __str__(self):
		return "{} {} {}".format(self.name, self.added_by, self.wished_by)
