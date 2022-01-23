# from django.shortcuts import render
#
# # Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from gensim.models import Word2Vec
from .forms import GeeksForm

# Create your views here.
@csrf_protect
def index(request):
    context = {}
    context['form'] = GeeksForm()
    return render(request, 'quizz\index.html',context)

# Create your views here.
@csrf_protect
def results(request):
    a0 = request.POST.get('colour_field', '')
    a1 = request.POST.get('pet_field', '')
    a2 = request.POST.get('values_field', '')
    a3 = request.POST.get('feature_field', '')
    a4 = request.POST.get('friends_field', '')

    model = Word2Vec.load("quizz/model_file_cbow.model")
    princesses = ["cinderella", "aurora", "ariel","belle", "jasmine", "pocahontas", "mulan", "tiana", "rapunzel", "merida", "moana"]
    top_score = 0
    name = princesses[0]
    for i in princesses:
        score = model.wv.n_similarity([a0,a1,a2,a3,a4], [i])
        if score > top_score :
            top_score = score
            name = i.capitalize()

    return render(request, 'quizz\\results.html', {'a0': a0,'a1': a1, 'a2': a2,'a3': a3, 'a4':a4, "name": name, 'score': round(top_score,3)})