# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework import serializers

# project imports
from apps.portfolio.models import Timeline


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = "__all__"
        datetime_fields = ("create_date", "modified_date")
