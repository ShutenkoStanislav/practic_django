import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practic.settings")
django.setup()

from forpractic.models import Ganre, Games


# game1 = Games.objects.create(
#     title="CS2",
#     year=2023,
#     rating=7.8,

# )

# game2 = Games.objects.create(
#      title="Dota2",
#      year=2013,
#      rating=8.9,

#  )

# game3 = Games.objects.create(
#      title="Apex",
#      year=2020,
#      rating=7.9,

#  )



# ganre1 = Ganre.objects.create(     
#   ganre="FPS game"
#  )
# ganre2 = Ganre.objects.create(
#      ganre="Mobo"
#  )



# game1.conn.add(ganre1)       
# game2.conn.add(ganre2)        
# game3.conn.add(ganre1)  


print("✅ Дані успішно додано!")


