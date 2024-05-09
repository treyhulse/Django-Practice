# Generated by Django 5.0.4 on 2024-05-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_gondolashelving_wall_mount_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gondolashelving',
            name='side_a_base_depth',
        ),
        migrations.RemoveField(
            model_name='gondolashelving',
            name='side_b_base_depth',
        ),
        migrations.RemoveField(
            model_name='gondolashelving',
            name='upper_shelves_quantity_per_section',
        ),
        migrations.RemoveField(
            model_name='gondolashelving',
            name='width',
        ),
        migrations.AddField(
            model_name='gondolashelving',
            name='side_a_base_width',
            field=models.CharField(choices=[('13', '13'), ('16', '16'), ('19', '19'), ('22', '22'), ('25', '25'), ('28', '28'), ('31', '31')], default='13', max_length=3),
        ),
        migrations.AddField(
            model_name='gondolashelving',
            name='side_b_base_width',
            field=models.CharField(choices=[('13', '13'), ('16', '16'), ('19', '19'), ('22', '22'), ('25', '25'), ('28', '28'), ('31', '31')], default='13', max_length=3),
        ),
        migrations.AddField(
            model_name='gondolashelving',
            name='upper_shelf_quantity',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='gondolashelving',
            name='base_height',
            field=models.CharField(choices=[('06', '06'), ('LB', 'LB')], default='06', max_length=2),
        ),
        migrations.AlterField(
            model_name='gondolashelving',
            name='color',
            field=models.CharField(choices=[('CHR', 'CHR'), ('PLT', 'PLT')], default='CHR', max_length=3),
        ),
        migrations.AlterField(
            model_name='gondolashelving',
            name='configuration',
            field=models.CharField(choices=[('island', 'Island/Gondola (double-sided)'), ('wall', 'Wall (single-sided)')], default='island', max_length=6),
        ),
        migrations.AlterField(
            model_name='gondolashelving',
            name='height',
            field=models.CharField(choices=[('48', '48'), ('54', '54'), ('60', '60'), ('66', '66'), ('72', '72'), ('78', '78'), ('84', '84'), ('90', '90'), ('96', '96')], default='48', max_length=3),
        ),
        migrations.AlterField(
            model_name='gondolashelving',
            name='side_a_back_panel_type',
            field=models.CharField(choices=[('pegboard', 'Pegboard'), ('solid', 'Solid')], default='pegboard', max_length=8),
        ),
        migrations.AlterField(
            model_name='gondolashelving',
            name='side_b_back_panel_type',
            field=models.CharField(choices=[('pegboard', 'Pegboard'), ('solid', 'Solid')], default='pegboard', max_length=8),
        ),
        migrations.AlterField(
            model_name='gondolashelving',
            name='upper_shelf_depth',
            field=models.CharField(choices=[('13', '13'), ('16', '16'), ('19', '19'), ('22', '22'), ('25', '25'), ('28', '28'), ('31', '31')], default='13', max_length=3),
        ),
        migrations.AlterField(
            model_name='gondolashelving',
            name='upper_shelf_type',
            field=models.CharField(choices=[('TL', 'Tilt-in'), ('DL', 'Drop-in')], default='TL', max_length=2),
        ),
    ]
