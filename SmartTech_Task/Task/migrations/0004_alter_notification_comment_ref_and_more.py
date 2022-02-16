# Generated by Django 4.0.2 on 2022-02-16 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_comment_document_ref_comment_protein_ref_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='comment_ref',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Task.comment'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='document_ref',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Task.document'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='protein_ref',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Task.protein'),
        ),
    ]
