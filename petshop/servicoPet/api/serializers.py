from rest_framework.serializers import ModelSerializer
from servicoPet.models import ServicoPet

class ServicoPetSerializer(ModelSerializer):
    
    class Meta:
        model = ServicoPet
        fields = "__all__"