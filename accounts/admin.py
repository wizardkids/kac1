from django.contrib import admin

from accounts.models import UserProfile

# here is one method of changing the header in admin pages
# admin.site.site_header = "KAC Administration"


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'age', 'email')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        # sort the userProfile table (queryset) according to the following order_by
        # -age means reversed order of age
        queryset = queryset.order_by('-age', 'user')
        return queryset

    user_info.short_description = 'User Information'


admin.site.register(UserProfile, UserProfileAdmin)
