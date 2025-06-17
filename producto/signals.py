from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import Product, Supplier
import logging

# Configurar logger
logger = logging.getLogger(__name__)

# Signal para verificar que los signals se están cargando correctamente
logger.info("¡SIGNALS DE PRODUCTO CARGADOS CORRECTAMENTE!")

# Signal para registrar cuando un producto baja de stock
@receiver(post_save, sender=Product)
def check_product_stock(sender, instance, **kwargs):
    logger.info(f"Signal activado: check_product_stock para {instance.name}")
    if instance.stock <= 5:
        logger.warning(f"Stock bajo para el producto {instance.name} - Quedan {instance.stock} unidades")
        # TODO: Aquí podría enviar un correo electrónico o notificación

# Signal para actualizar el timestamp manualmente si es necesario
@receiver(pre_save, sender=Product)
def update_product_timestamp(sender, instance, **kwargs):
    logger.info(f"Signal activado: update_product_timestamp para {instance.name}")
    if instance.pk:
        try:
            old_instance = Product.objects.get(pk=instance.pk)
            # Si el precio ha cambiado, registra el cambio
            if old_instance.price != instance.price:
                logger.info(f"Precio del producto {instance.name} actualizado: {old_instance.price} → {instance.price}")
        except Product.DoesNotExist:
            pass

# Signal para registrar eliminación de productos
@receiver(pre_delete, sender=Product)
def log_product_deletion(sender, instance, **kwargs):
    logger.info(f"Producto eliminado: {instance.name} (ID: {instance.pk})")

# Signal para registrar cuando se crea un nuevo proveedor
@receiver(post_save, sender=Supplier)
def new_supplier_notification(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Nuevo proveedor registrado: {instance.name}")
        # TODO: Aquí podría enviar una notificación o correo 