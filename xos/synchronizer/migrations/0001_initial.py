# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-21 16:28
from __future__ import unicode_literals

import core.models.xosbase_header
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenStackService',
            fields=[
                ('service_decl_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Service_decl')),
                ('auth_url', core.models.xosbase_header.StrippedCharField(blank=True, help_text=b'Auth url for the OpenStack controller', max_length=200, null=True)),
                ('admin_user', core.models.xosbase_header.StrippedCharField(blank=True, help_text=b'Username of an admin user at this OpenStack', max_length=200, null=True)),
                ('admin_password', core.models.xosbase_header.StrippedCharField(blank=True, help_text=b'Password of theadmin user at this OpenStack', max_length=200, null=True)),
                ('admin_tenant', core.models.xosbase_header.StrippedCharField(blank=True, help_text=b'Name of the tenant the admin user belongs to', max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'OpenStack Service',
            },
            bases=('core.service',),
        ),
        migrations.CreateModel(
            name='OpenStackServiceInstance',
            fields=[
                ('computeserviceinstance_decl_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.ComputeServiceInstance_decl')),
                ('admin_password', core.models.xosbase_header.StrippedCharField(blank=True, help_text=b'Admin password for instance', max_length=200, null=True)),
                ('flavor', models.ForeignKey(blank=True, help_text=b'Flavor of this instance', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='openstackinstance', to='core.Flavor')),
                ('node', models.ForeignKey(blank=True, help_text=b'Node on which to deploy this instance', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='openstackinstances', to='core.Node')),
            ],
            options={
                'verbose_name': 'OpenStack Service Instance',
            },
            bases=('core.computeserviceinstance',),
        ),
    ]
