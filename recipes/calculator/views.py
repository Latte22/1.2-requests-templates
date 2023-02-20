from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def omlet(request):
    servings = int(request.GET.get("servings",1))
    return HttpResponse(f'яйца, шт: {2*servings}<br> молоко, л: {0.1*servings}<br> соль, ч.л.: {0.5*servings}')

def pasta(request):
    servings = int(request.GET.get("servings",1))
    return HttpResponse(f'макароны, г: {0.3 * servings}<br> сыр, г: {0.05 * servings}')


def buter(request):
    servings = int(request.GET.get("servings",1))
    return HttpResponse(f'хлеб, ломтик: {1 * servings}<br> колбаса, ломтик : {1 * servings} <br> сыр, ломтик: {1 * servings} <br> помидор, ломтик: {1 * servings}')



