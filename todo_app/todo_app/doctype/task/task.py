from frappe.model.document import Document

class Task(Document):
	def validate(self):
		"""Validate the Task document before saving."""
		pass
	
	def before_save(self):
		"""Execute before saving the Task document."""
		pass
	
	def on_submit(self):
		"""Execute when the Task document is submitted."""
		pass

