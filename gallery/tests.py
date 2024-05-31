from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Image, Category

class GalleryViewTests(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='Category 1')
        self.category2 = Category.objects.create(name='Category 2')
        self.image1 = Image.objects.create(
            title='Image 1',
            image='test_image_1.jpg',
            created_date=timezone.now(),
            age_limit=18
        )
        self.image1.categories.add(self.category1)
        self.image2 = Image.objects.create(
            title='Image 2',
            image='test_image_2.jpg',
            created_date=timezone.now(),
            age_limit=18
        )
        self.image2.categories.add(self.category2)

    def test_gallery_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/gallery.html')
        self.assertContains(response, 'Category 1')
        self.assertContains(response, 'Category 2')
        self.assertContains(response, 'Image 1')
        self.assertContains(response, 'Image 2')
