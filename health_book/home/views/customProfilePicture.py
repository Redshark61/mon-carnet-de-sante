from django.views import View
from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
from login_signup.models.customUser import CustomUser


class CustomProfilePicture(View):
    template_name = 'home/customProfilePicture.html'

    def get(self, request):
        initial = request.user.first_name[0] + request.user.last_name[0]
        fileName = f"profile_pictures/{request.user.first_name}-{request.user.last_name}-{request.user.id}.png"
        fullPath = f"media/{fileName}"
        fontSize = 300
        fnt = ImageFont.truetype('arial.ttf', fontSize)
        # create new image
        image = Image.new(mode="RGB", size=(int(fontSize / 2) *
                          (len(initial) + 1), fontSize + 50), color="grey")
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), initial, font=fnt, fill=(90, 90, 90))
        image.save(fullPath)

        request.user.profile_picture = fileName
        request.user.save()
        context = {
            'photo_name': fullPath
        }

        return render(request, self.template_name, context)
