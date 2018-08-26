from django.test import TestCase
from .models import Align
from . import globalalignment

# class Align(models.Model):
# 	align = models.TextField()
# 	reference = models.TextField()
# 	alignedV = models.TextField()
# 	alignedW = models.TextField()

class AlignmentTestCase(TestCase):
    def setup(self):
        dbEntry = Align(align="FAKEPROTEIN", reference="CAKEQRTOEIN")
        dbEntry.save()

    def test_global_alignment(self):
        alignedStrings = Align.objects.last()
        alignedStrings.alignedV, alignedStrings.alignedW = global_alignment(alignedStrings.align,
                                                                            alignedStrings.reference).split(':')
        alignedStrings.save()

        # globalalignment(alignedStrings)
