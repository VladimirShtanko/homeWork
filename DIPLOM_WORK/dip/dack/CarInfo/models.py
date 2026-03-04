from django.db import models
from accounts.models import Users


class Car(models.Model):
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        abstract = False

    factory_number = models.CharField('Зав. № машины', max_length=75, unique=True)
    model = models.ForeignKey(
        'CarModelReference',
        verbose_name='Модель машины',
        on_delete=models.CASCADE,
        related_name='Car_model'
    )

    dvig_model = models.ForeignKey(
        'DvigModel',
        verbose_name='Модель двигателя',
        on_delete=models.CASCADE,
        related_name='Dvig_model'
    )
    dvig_number = models.CharField('Зав. № двигателя', max_length=100, blank=True, null=True)

    transmission_model = models.ForeignKey(
        'TransmissionModelReference',
        verbose_name='Модель трансмиссии',
        on_delete=models.CASCADE,
        related_name='transmission_model',
        blank=True,
        null=True
    )
    transmission_number = models.CharField('Зав. № трансмиссии', max_length=100, unique=True, blank=True, null=True)

    main_bridge_model = models.ForeignKey(
        'MainBridgeModelReference',
        verbose_name='Модель ведущего моста',
        on_delete=models.CASCADE,
        related_name='main_bridge_model',
        blank=True,
        null=True
    )
    main_bridge_number = models.CharField('Зав. № ведущего моста', max_length=100, blank=True, null=True)

    controlled_bridge_model = models.ForeignKey(
        'ControlledBridgeModelReference',
        verbose_name='Модель управляемого моста',
        on_delete=models.CASCADE,
        related_name='controlled_bridge_model',
        blank=True,
        null=True
    )
    controlled_bridge_number = models.CharField('Зав. № управляемого моста', max_length=100, blank=True, null=True)

    postavka = models.CharField('Договор поставки №, дата', max_length=250, blank=True, null=True)
    date_of_out = models.DateTimeField('Дата отгрузки с завода', blank=True, null=True)
    usering = models.CharField('Грузополучатель (конечный потребитель)', max_length=250, blank=True, null=True)
    address = models.CharField('Адрес поставки (эксплуатации)', max_length=250, blank=True, null=True)
    complete_set = models.CharField('Комплектация (доп. опции)', max_length=250, blank=True, null=True)

    client = models.ForeignKey(
        Users,
        verbose_name='Клиент',
        on_delete=models.CASCADE,
        related_name='client_machine',
        blank=True,
        null=True
    )
    company = models.ForeignKey(
        Users,
        verbose_name='Cервисная компания',
        on_delete=models.CASCADE,
        related_name='company',
        blank=True,
        null=True
    )

    def __str__(self):
        return '{}'.format(f'{self.model} {self.factory_number}')


class CarModelReference(models.Model):
    class Meta:
        verbose_name = 'Модель машины'
        verbose_name_plural = 'Документация по эксплуатации моделей машин'
        abstract = False

    name = models.CharField('Модель', max_length=150, unique=True)
    description = models.TextField('Описание', max_length=5000, null=True, blank=True)

    def __str__(self):
        return '{}'.format(f'{self.name}')


class DvigModel(models.Model):
    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Документация по эксплуатации моделей двигателей'

    name = models.CharField('Модель', max_length=150, unique=True)
    description = models.TextField('Описание', max_length=5000, null=True, blank=True)

    def __str__(self):
        return '{}'.format(f'{self.name}')


class TransmissionModelReference(models.Model):
    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Документация по эксплуатации моделей трансмиссий'
        abstract = False

    name = models.CharField('Модель', max_length=150, unique=True)
    description = models.TextField('Описание', max_length=5000, null=True, blank=True)

    def __str__(self):
        return '{}'.format(f'{self.name}')


class MainBridgeModelReference(models.Model):
    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Документация по эксплуатации моделей ведущего моста'
        abstract = False

    name = models.CharField('Модель', max_length=150, unique=True)
    description = models.TextField('Описание', max_length=5000, null=True, blank=True)

    def __str__(self):
        return '{}'.format(f'{self.name}')


class ControlledBridgeModelReference(models.Model):
    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Документация по эксплуатации моделей управляемого моста'
        abstract = False

    name = models.CharField('Модель', max_length=150, unique=True)
    description = models.TextField('Описание', max_length=5000, null=True, blank=True)

    def __str__(self):
        return '{}'.format(f'{self.name}')


class TO(models.Model):
    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Технические обслуживания'
        abstract = False

    type_of_maintenance = models.ForeignKey(
        'TypeOfMaintenance',
        verbose_name='Вид технического обслуживания',
        on_delete=models.CASCADE,
        related_name='type_of_maintenance'
    )

    date = models.DateTimeField('Дата проведения ТО', auto_created=True)
    time_work = models.DecimalField('Наработка, м/час', max_digits=11, decimal_places=2)

    order_number = models.CharField('№ заказ-наряда', max_length=100, unique=True)
    order_date = models.DateTimeField('Дата заказ-наряда')

    car = models.ForeignKey(
        'Car',
        verbose_name='Машина',
        related_name='TO',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}'.format(f'{self.order_number} {self.type_of_maintenance}')


class TypeOfMaintenance(models.Model):
    class Meta:
        verbose_name = 'Вид технического обслуживания'
        verbose_name_plural = 'Документация видов ТО'
        abstract = False

    name = models.CharField('Вид ТО', max_length=150, unique=True)
    description = models.TextField('Описание', max_length=5000, null=True, blank=True)

    def __str__(self):
        return '{}'.format(f'{self.name}')


class MaintenanceOrganisationReference(models.Model):
    class Meta:
        verbose_name = 'Уполномоченная в ТО организация'
        verbose_name_plural = 'Справочник уполномоченных в ТО организаций'
        abstract = False

    name = models.CharField('Наименование', max_length=150, unique=True)
    description = models.TextField('Описание', max_length=5000, null=True, blank=True)

    def __str__(self):
        return '{}'.format(f'{self.name}')


class Reclamation (models.Model):
    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'
        abstract = False

    date = models.DateTimeField('Дата отказа', null=True, blank=True)
    time_work = models.DecimalField('Наработка, м/час', max_digits=11, decimal_places=2)

    failure_node = models.ForeignKey(
        'FailureNode',
        verbose_name='Oтказа',
        on_delete=models.CASCADE,
        related_name='failure_node',
    )
    failure_description = models.CharField('Oтказа', max_length=250, null=True, blank=True)

    recovery_method = models.ForeignKey(
        'RecoveryMethod',
        verbose_name='Способ восстановления',
        on_delete=models.CASCADE,
        related_name='recovery_method',
    )

    parts_used = models.TextField('Используемые запасные части', max_length=1000, blank=True, null=True)
    date_of_restoration = models.DateTimeField('Дата восстановления', blank=True, null=True)
    equipment_downtime = models.IntegerField('Время простоя техники (Часов)', default=0)

    Car = models.ForeignKey(
        'Car',
        verbose_name='Машина',
        on_delete=models.CASCADE,
        related_name='complaint',
    )

    def get_equipment_downtime(self):
        result = self.date_of_restoration - self.date
        self.equipment_downtime = result.seconds // 3600
        self.save()
        return self.equipment_downtime

    def __str__(self):
        return '{}'.format(f'{self.date} {self.Car}')


class FailureNode(models.Model):
    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Справочник узлов отказа'
        abstract = False

    name = models.CharField('Наименование', max_length=150, unique=True)
    description = models.TextField('Описание', max_length=5000, null=True, blank=True)

    def __str__(self):
        return '{}'.format(f'{self.name}')


class RecoveryMethod(models.Model):
    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'окументация способов восстановления'
        abstract = False

    name = models.CharField('Наименование', max_length=150, unique=True)
    description = models.TextField('Описание', max_length=5000, null=True, blank=True)

    def __str__(self):
        return '{}'.format(f'{self.name}')