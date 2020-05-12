from django.shortcuts import render
from .models import Card
from django.http import HttpResponse 
from django.template import loader
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from django.views.decorators.csrf import csrf_exempt
import json

def cards(request):
    all_cards = Card.objects.all()
    template = loader.get_template('scanner/index.html')
    return HttpResponse(template.render({'cards':all_cards}, request))

@csrf_exempt
def new(request, base_image=None):
    if request.method == 'POST':
        base_image = Image.open(request.FILES['source_image'])
        image_str = pytesseract.image_to_string(base_image)
        new_card = Card(name=image_str)
        if new_card.source_image:
            im = Image.open(new_card.source_image)
            im.thumbnail((220, 130), Image.ANTIALIAS)
            thumb_io = BytesIO()
            im.save(thumb_io, im.format, quality=60)
            new_card.source_image.save(im.filename, ContentFile(thumb_io.get_value()), save=False)
        new_card.save()

    return HttpResponse("Card scanned successfully")