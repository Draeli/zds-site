# coding: utf-8

from django.contrib.auth.models import Group, User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class GroupContact(models.Model):
    """
    Groups displayed in contact page and their informations.
    """

    class Meta:
        verbose_name = _('Groupe de la page de contact')
        verbose_name_plural = _('Groupes de la page de contact')

    group = models.OneToOneField(Group, verbose_name=_('Groupe d\'utilisateur'))
    name = models.CharField(_('Nom (ex: Le staff)'), max_length=32, unique=True)
    description = models.TextField(_('Description (en markdown)'), blank=True, null=True)
    email = models.EmailField(_('Adresse mail du groupe'), blank=True, null=True)
    person_in_charge = models.ForeignKey(User, verbose_name=_('Responsable'), blank=True, null=True)
    position = models.PositiveSmallIntegerField(_('Position dans la page'), unique=True)

    def __unicode__(self):
        return self.name
