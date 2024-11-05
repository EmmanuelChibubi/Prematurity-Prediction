from django.shortcuts import render, redirect
from .forms import PredictionForm
from .models import PredictionData
from profiles.models import UserProfile

def prediction_form(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            prediction = form.save(commit=False)
            prediction.user = UserProfile.objects.get(user=request.user)
            prediction.result = "Pending Analysis"  # Replace with model prediction later
            prediction.save()
            return redirect('prediction_result', prediction_id=prediction.id)
    else:
        form = PredictionForm()
    return render(request, 'prediction/prediction_form.html', {'form': form})

def prediction_result(request, prediction_id):
    prediction = PredictionData.objects.get(id=prediction_id)
    return render(request, 'prediction/prediction_result.html', {'prediction': prediction})
