from issue.models import Person, Position
from issue.serializers import PersonSerializer, PositionSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

position = Position(name='Pracownik', description = 'pracuje')
position.save()

person = Person(name='Jan', surname='Kowalski', sex=1, position=position)
person.save()

serializer = PositionSerializer(position)
serializer = PersonSerializer(person)
serializer.data

content = JSONRenderer().render(serializer.data)
stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = PersonSerializer(data=data)
deserializer.is_valid()
deserializer.errors
deserializer.fields
deserializer.validated_data
deserializer.save()
deserializer.data