from rest_framework import serializers


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if 'https://' in value.get('title'):
            if 'youtube' not in value.get('title'):
                raise serializers.ValidationError('Ссылки на сторонние ресурсы не допустимы')
