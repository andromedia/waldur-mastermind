from django.test import TestCase

from nodeconductor_assembly_waldur.invoices.tasks import format_invoice_csv

from .. import models
from . import fixtures, factories


class TestReportFormatter(TestCase):
    def setUp(self):
        fixture = fixtures.InvoiceFixture()
        package = fixture.openstack_package
        invoice = models.Invoice.objects.get(customer=package.tenant.service_project_link.project.customer)
        self.invoice = invoice

    def test_invoice_items_are_properly_formatted(self):
        report = format_invoice_csv(self.invoice)
        lines = report.splitlines()
        self.assertEqual(2, len(lines))

        expected_header = 'customer_uuid;customer_name;project_uuid;project_name;' \
                          'invoice_uuid;invoice_number;invoice_year;invoice_month;' \
                          'invoice_date;due_date;invoice_price;invoice_tax;' \
                          'invoice_total;name;article_code;product_code;' \
                          'price;tax;total;unit_price;unit;start;end'
        self.assertEqual(lines[0], expected_header)

    def test_offering_items_are_serialized(self):
        self.offering_item = factories.OfferingItemFactory(invoice=self.invoice)
        self.offering_item.offering.type = 'OFFERING-001'
        self.offering_item.offering.save()

        report = format_invoice_csv(self.invoice)
        lines = report.splitlines()
        self.assertEqual(3, len(lines))
        self.assertTrue('OFFERING-001' in lines[-1])
