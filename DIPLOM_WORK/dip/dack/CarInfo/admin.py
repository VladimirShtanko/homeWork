from django.contrib import admin
from .models import Car, CarModelReference, DvigModel, TransmissionModelReference, MainBridgeModelReference, ControlledBridgeModelReference, TO, TypeOfMaintenance,  MaintenanceOrganisationReference, Reclamation, FailureNode, RecoveryMethod

admin.site.register(Car)
admin.site.register(CarModelReference)
admin.site.register(DvigModel)
admin.site.register(TransmissionModelReference)
admin.site.register(MainBridgeModelReference)
admin.site.register(ControlledBridgeModelReference)
admin.site.register(TO)
admin.site.register(TypeOfMaintenance)
admin.site.register(MaintenanceOrganisationReference)
admin.site.register(Reclamation)
admin.site.register(FailureNode)
admin.site.register(RecoveryMethod)