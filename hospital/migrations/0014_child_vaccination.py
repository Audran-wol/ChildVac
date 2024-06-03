from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_service_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('parent_name', models.CharField(max_length=120)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('picture', models.ImageField(upload_to='children/', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinations', to='hospital.Child')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinations', to='hospital.Service')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccinations', to='hospital.Doctor')),
            ],
        ),
    ]