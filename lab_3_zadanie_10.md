Person.objects.all()
Person.objects.get(id=3)
Person.objects.filter(name__istartswith='A')
Position.objects.filter(id__in=Person.objects.values_list('position', flat=True))
Position.objects.order_by('-name')
Person.objects.create(
    name='Jan',
    surname='Kowalski',
    sex=1,
    position_id=Position.objects.first().id
)