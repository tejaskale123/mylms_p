# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cache(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cache'


class CacheLocks(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    owner = models.CharField(max_length=255)
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cache_locks'


class Courses(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'


class DevAdmins(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dev_admins'


class Employees(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_code = models.CharField(unique=True, max_length=50)
    institute = models.ForeignKey('Institutes', models.DO_NOTHING)
    email = models.CharField(unique=True, max_length=255)
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    joining_date = models.DateField()
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Institutes(models.Model):
    id = models.BigAutoField(primary_key=True)
    org = models.ForeignKey('Organizations', models.DO_NOTHING)
    institute_name = models.CharField(max_length=255)
    aicte_code = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institutes'


class JobBatches(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    total_jobs = models.IntegerField()
    pending_jobs = models.IntegerField()
    failed_jobs = models.IntegerField()
    failed_job_ids = models.TextField()
    options = models.TextField(blank=True, null=True)
    cancelled_at = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField()
    finished_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_batches'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Organizations(models.Model):
    id = models.BigAutoField(primary_key=True)
    org_name = models.CharField(max_length=255)
    reg_num = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    address_one = models.CharField(max_length=255)
    address_two = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organizations'


class PasswordResetTokens(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_reset_tokens'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.TextField()
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Routes(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    route = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routes'


class SampleUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample_users'


class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Students(models.Model):
    id = models.BigAutoField(primary_key=True)
    institute = models.ForeignKey(Institutes, models.DO_NOTHING)
    enrollment_no = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    course_name = models.CharField(max_length=100, blank=True, null=True)
    current_year = models.CharField(max_length=20, blank=True, null=True)
    division = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class UserAuthentications(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True)
    routes = models.ForeignKey(Routes, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_authentications'


class UserLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ipaddress = models.CharField(max_length=45, blank=True, null=True)
    route = models.ForeignKey(Routes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_logs'


class UserRoles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    roles_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_roles'


class UserTypes(models.Model):
    user_type = models.CharField(primary_key=True, max_length=10)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_types'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    is_otp_verified = models.IntegerField()
    institute = models.ForeignKey(Institutes, models.DO_NOTHING, blank=True, null=True)
    organization = models.ForeignKey(Organizations, models.DO_NOTHING, blank=True, null=True)
    password = models.CharField(max_length=255)
    user_type = models.ForeignKey(UserTypes, models.DO_NOTHING, db_column='user_type')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    is_password_changed = models.IntegerField()
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    is_online = models.IntegerField()
    is_alumni = models.IntegerField()
    in_usergroup = models.IntegerField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'