from flowers.models import Flowers

from typing import Any

def upload_flowers(request, d_dict: dict[str, Any]):
    try:
        user = request.user

        Flowers.objects.create(
            user=user,
            flower_name= d_dict['flower_name'],
            flower_language= d_dict['flower_language'],
            flower_growth_location= d_dict['flower_growth'],
            flower_information= d_dict['flower_introduction'],
            flower_image= request.FILES.get('flower_pic'),
        )
        return {
            'status': 200,
            'msg': 'Upload is success'
        }
    except Exception as e:
        print(f'flower create failed: {e}')
        return {
            'status': 404,
            'msg': 'flower upload failed'
        }








    # Flowers.objects.update_or_create(
    #     user=user,
    #     default={
    #         'flower_name': d_dict['flower_name'],
    #         'flower_language': d_dict['flower_language'],
    #         'flower_growth_location': d_dict['flower_growth'],
    #         'flower_information': d_dict['flower_introduction'],
    #         'flower_image': request.FILES.get('flower_pic'),
    #     }
    # )