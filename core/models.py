from django.db import models
from djongo import models as djongo_models

class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    age_range = models.CharField(max_length=50, null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    custom_field = djongo_models.JSONField(default=list)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    fid = models.CharField(max_length=50, null=True, blank=True)

class Branch(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    fid = models.CharField(max_length=50, null=True, blank=True)

class BranchGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    fid = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract = True

class Channel(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50)
    fid = models.CharField(max_length=50, null=True, blank=True)

class Web(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    fid = models.CharField(max_length=50, null=True, blank=True)

class Template(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    fid = models.CharField(max_length=50, null=True, blank=True)

class FieldValue(models.Model):
    value = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

class FeedbackCustomField(models.Model):
    field_name = models.CharField(max_length=255, null=True, blank=True)
    field_label = models.CharField(max_length=255, null=True, blank=True)
    value_type = models.IntegerField()
    field_value = djongo_models.EmbeddedField(model_container=FieldValue)

    class Meta:
        abstract = True

class BranchSLI(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    service = djongo_models.JSONField(default=list)

class Feedback(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    id = models.IntegerField(unique=True)
    fid = models.CharField(max_length=50, null=True, blank=True)
    lang_code = models.CharField(max_length=10, null=True, blank=True)
    feedback_custom_field = djongo_models.ArrayField(model_container=FeedbackCustomField)
    company = models.CharField(max_length=255, null=True, blank=True)
    feedback_origin = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    extra_data = models.TextField()
    comment = models.TextField()
    
    branch = djongo_models.EmbeddedField(model_container=Branch)
    channel = djongo_models.EmbeddedField(model_container=Channel)
    web = djongo_models.EmbeddedField(model_container=Web)
    device = models.CharField(max_length=255, null=True, blank=True)
    campaign = models.CharField(max_length=255, null=True, blank=True)
    ticket = models.CharField(max_length=255, null=True, blank=True)
    customer = djongo_models.EmbeddedField(model_container=Customer)
    template = djongo_models.EmbeddedField(model_container=Template)
    branch_groups = djongo_models.ArrayField(model_container=BranchGroups)
    
    sli = models.IntegerField(default=0)
    rate_count = models.IntegerField(default=0)
    branch_sli = djongo_models.EmbeddedField(model_container=BranchSLI)
    rate_option = djongo_models.JSONField()
    feedback_rate = djongo_models.JSONField(default=list)







# from mongoengine import Document, EmbeddedDocument, fields
# from django.db import models

# class Customer(EmbeddedDocument):
#     id = fields.IntField(primary_key=True)
#     full_name = fields.StringField(max_length=255, blank=True)
#     email = fields.EmailField(null=True, blank=True)
#     phone_number = fields.StringField(max_length=20, null=True, blank=True)
#     age_range = fields.StringField(max_length=50, null=True, blank=True)
#     gender = fields.IntField(null=True, blank=True)
#     custom_field = fields.ListField(fields.DictField(), default=list)
#     created_at = fields.DateTimeField()
#     updated_at = fields.DateTimeField()
#     fid = fields.StringField(max_length=50, null=True, blank=True)

# class Branch(EmbeddedDocument):
#     id = fields.IntField(primary_key=True)
#     name = fields.StringField(max_length=255)
#     fid = fields.StringField(max_length=50, null=True, blank=True)

# class BranchGroups(EmbeddedDocument):
#     id = fields.IntField(primary_key=True)
#     name = fields.StringField(max_length=255)
#     fid = fields.StringField(max_length=50, null=True, blank=True)

#     meta = {'abstract': True}

# class Channel(EmbeddedDocument):
#     id = fields.IntField(primary_key=True)
#     type = fields.StringField(max_length=50)
#     fid = fields.StringField(max_length=50, null=True, blank=True)

# class Web(EmbeddedDocument):
#     id = fields.IntField(primary_key=True)
#     name = fields.StringField(max_length=255)
#     fid = fields.StringField(max_length=50, null=True, blank=True)

# class Template(EmbeddedDocument):
#     id = fields.IntField(primary_key=True)
#     name = fields.StringField(max_length=255)
#     fid = fields.StringField(max_length=50, null=True, blank=True)

# class FieldValue(EmbeddedDocument):
#     value = fields.StringField(max_length=255, null=True, blank=True)

#     meta = {'abstract': True}

# class FeedbackCustomField(EmbeddedDocument):
#     field_name = fields.StringField(max_length=255, null=True, blank=True)
#     field_label = fields.StringField(max_length=255, null=True, blank=True)
#     value_type = fields.IntField()
#     field_value = fields.EmbeddedDocumentField(FieldValue)

#     meta = {'abstract': True}

# class BranchSLI(EmbeddedDocument):
#     id = fields.IntField(primary_key=True)
#     name = fields.StringField(max_length=255)
#     service = fields.ListField(fields.DictField(), default=list)

# class Feedback(Document):
#     id = fields.IntField(unique=True)
#     fid = fields.StringField(max_length=50, null=True, blank=True)
#     lang_code = fields.StringField(max_length=10, null=True, blank=True)
#     feedback_custom_field = fields.ListField(fields.EmbeddedDocumentField(FeedbackCustomField))
#     company = fields.StringField(max_length=255, null=True, blank=True)
#     feedback_origin = fields.StringField(max_length=50)
#     created_at = fields.DateTimeField()
#     updated_at = fields.DateTimeField()
#     extra_data = fields.StringField()
#     comment = fields.StringField()
    
#     branch = fields.EmbeddedDocumentField(Branch)
#     channel = fields.EmbeddedDocumentField(Channel)
#     web = fields.EmbeddedDocumentField(Web)
#     device = fields.StringField(max_length=255, null=True, blank=True)
#     campaign = fields.StringField(max_length=255, null=True, blank=True)
#     ticket = fields.StringField(max_length=255, null=True, blank=True)
#     customer = fields.EmbeddedDocumentField(Customer)
#     template = fields.EmbeddedDocumentField(Template)
#     branch_groups = fields.ListField(fields.EmbeddedDocumentField(BranchGroups))
    
#     sli = fields.IntField(default=0)
#     rate_count = fields.IntField(default=0)
#     branch_sli = fields.EmbeddedDocumentField(BranchSLI)
#     rate_option = fields.ListField(fields.DictField())
#     feedback_rate = fields.ListField(fields.DictField(), default=list)

#     meta = {'collection': 'feedback'}
