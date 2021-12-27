# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# project imports
from utils.core.models import TimeStampable
from common.managers.device_token import (
    DeviceTokenQueryset,
    DeviceTokenManager,
)
from common import constants

USER = get_user_model()


class DeviceToken(TimeStampable):
    """
    Description of DeviceToken Model
    """
    user = models.ForeignKey(
        verbose_name=_('User'),
        to=USER,
        on_delete=models.CASCADE,
        related_name='user_device_tokens',
        null=True,
        blank=True,
    )
    device_token = models.CharField(
        verbose_name=_('Device Token'), max_length=256, db_index=True
    )
    device_type = models.CharField(
        verbose_name=_('Device Type'),
        choices=constants.DEVICE_TOKEN_DEVICES,
        default=constants.ANDROID,
        max_length=16,
    )

    objects = DeviceTokenManager.from_queryset(DeviceTokenQueryset)()

    class Meta:
        app_label = 'common'
        verbose_name = _('Device Token')
        verbose_name_plural = _('Device Tokens')

    def __str__(self):
        return self.device_token

    def __unicode__(self):
        return self.device_token