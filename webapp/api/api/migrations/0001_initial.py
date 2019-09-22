# Generated by Django 2.2.3 on 2019-09-22 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotatedEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000)),
                ('start_ind', models.IntegerField()),
                ('end_ind', models.IntegerField()),
                ('acc', models.FloatField()),
                ('correct', models.BooleanField(choices=[(0, 'False'), (1, 'True')], default=True)),
                ('validated', models.BooleanField(choices=[(0, 'False'), (1, 'True')], default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pretty_name', models.CharField(max_length=300)),
                ('cui', models.CharField(max_length=100, unique=True)),
                ('desc', models.TextField(blank=True, default='')),
                ('tui', models.CharField(max_length=20)),
                ('semantic_type', models.CharField(blank=True, max_length=200, null=True)),
                ('vocab', models.CharField(max_length=100)),
                ('synonyms', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='ConceptDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdb_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('original_file', models.FileField(upload_to='')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, default='')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetaTaskValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, default='')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('cuis', models.TextField(blank=True, default=None)),
                ('tuis', models.TextField(blank=True, default=None)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Dataset')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_api.project_set+', to='contenttypes.ContentType')),
                ('validated_documents', models.ManyToManyField(to='api.Document')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vocab_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAnnotateEntities',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Project')),
                ('require_entity_validation', models.BooleanField(choices=[(0, 'False'), (1, 'True')], default=False)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.project',),
        ),
        migrations.CreateModel(
            name='MetaTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, default='')),
                ('values', models.ManyToManyField(related_name='values', to='api.MetaTaskValue')),
            ],
        ),
        migrations.CreateModel(
            name='MetaAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc', models.FloatField()),
                ('validated', models.BooleanField(choices=[(0, 'Not Validated'), (1, 'Validated')])),
                ('annotated_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AnnotatedEntity')),
                ('meta_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MetaTask')),
                ('meta_task_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MetaTaskValue')),
            ],
        ),
        migrations.CreateModel(
            name='MedCATModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cdb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ConceptDB')),
                ('vocab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Vocabulary')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('concept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Concept')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='annotatedentity',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotated_entity', to='api.Document'),
        ),
        migrations.AddField(
            model_name='annotatedentity',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Entity'),
        ),
        migrations.AddField(
            model_name='annotatedentity',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project'),
        ),
        migrations.AddField(
            model_name='annotatedentity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProjectMetaAnnotate',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Project')),
                ('project_annotate_entities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ProjectAnnotateEntities')),
                ('tasks', models.ManyToManyField(to='api.MetaTask')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.project',),
        ),
        migrations.AddField(
            model_name='projectannotateentities',
            name='medcat_models',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.MedCATModel'),
        ),
    ]
