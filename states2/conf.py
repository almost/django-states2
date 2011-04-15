from django.conf import settings

base_conf = getattr(settings, 'STATES2_CONF', {})

# The model name for the state transition logs.
# It will be string replaced with %(model_name)s and %(field_name)s
# Example for when you use multiple ``StateField``s per object
#     '%(model_name)s%(field_name)sLog'
LOG_MODEL_NAME = base_conf.get(LOG_MODEL_NAME,
                               '%(model_name)s_StateTransition')
