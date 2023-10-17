from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserModelAdmin(BaseUserAdmin):
  # The fields to be used in displaying the User model.
  # These override the definitions on the base UserModelAdmin
  # that reference specific fields on auth.User.
  list_display = ('id', 'email', 'name','date_of_birth', 'gender', 'occupation', 'contno', 'id_type', 'id_issue', 'id_number', 'issue_state', 'issue_date', 'add_type', 'address', 'nation', 'state', 'district', 'pincode', 'is_admin')
  list_filter = ('is_admin',)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('name', 'date_of_birth', 'gender', 'occupation', 'contno', 'id_type', 'id_issue', 'id_number', 'issue_state', 'issue_date', 'add_type', 'address', 'nation', 'state', 'district', 'pincode')}),
      ('Permissions', {'fields': ('is_admin',)}),
  )
  # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
  # overrides get_fieldsets to use this attribute when creating a user.
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'name', 'date_of_birth', 'gender', 'occupation', 'contno', 'id_type', 'id_issue', 'id_number', 'issue_state', 'issue_date', 'add_type', 'address', 'nation', 'state', 'district', 'pincode', 'password1', 'password2'),
      }),
  )
  search_fields = ('email',)
  ordering = ('email', 'id')
  filter_horizontal = ()


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)