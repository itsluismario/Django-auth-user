# Generated by Django 4.1 on 2022-10-06 04:39

import core.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email_address"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ProjectName",
                    models.CharField(max_length=50, verbose_name="Project name"),
                ),
                (
                    "Created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created date"
                    ),
                ),
                (
                    "Updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated date"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "CompanyName",
                    models.CharField(max_length=50, verbose_name="Company name"),
                ),
                (
                    "FirstName",
                    models.CharField(max_length=50, verbose_name="First name"),
                ),
                ("LastName", models.CharField(max_length=50, verbose_name="Last name")),
                (
                    "PhoneNumber",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Phone number"
                    ),
                ),
                (
                    "User",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "CompanyName",
                    models.CharField(max_length=50, verbose_name="Company name"),
                ),
                ("Token", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "FirstName",
                    models.CharField(max_length=50, verbose_name="First name"),
                ),
                ("LastName", models.CharField(max_length=50, verbose_name="Last name")),
                (
                    "Email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email_address"
                    ),
                ),
                (
                    "PhoneNumber",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Phone number"
                    ),
                ),
                (
                    "Builder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="BuilderContact",
                        to="core.userprofile",
                        verbose_name="Builder",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Quote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created date"
                    ),
                ),
                (
                    "Updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated date"),
                ),
                ("fileUp", models.FileField(upload_to=core.models.PDFFile)),
                ("is_upload", models.BooleanField(default=False)),
                (
                    "Project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.project",
                        verbose_name="Project",
                    ),
                ),
                (
                    "Supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Supplier",
                        to="core.supplier",
                        verbose_name="Supplier",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Material",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=50, verbose_name="Name")),
                ("Qty", models.IntegerField(blank=True, null=True, verbose_name="Qty")),
                (
                    "Created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created date"
                    ),
                ),
                (
                    "Updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated date"),
                ),
                (
                    "Quote",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.quote",
                        verbose_name="Project",
                    ),
                ),
                (
                    "Supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.supplier",
                        verbose_name="Supplier",
                    ),
                ),
            ],
        ),
    ]
