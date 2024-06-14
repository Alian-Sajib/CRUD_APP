from django.shortcuts import render
from django.http.response import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
    HttpResponseRedirect,
)
from main_app.models import stock
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from main_app.forms import AddNew
from django.urls import reverse


# Create your views here.
def index(request):
    data_list = stock.objects.all()

    paginator = Paginator(data_list, 10)  # Show 10 items per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, "index.html", {"data_list": page_obj}
    )


@csrf_exempt
def save_json(request):
    if request.method == "POST":
        try:
            # Attempt to load JSON from request body
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            # If JSON decoding fails, handle the error appropriately
            return HttpResponseBadRequest("Invalid JSON data")

        if isinstance(payload, list):
            # If payload is a list, handle it accordingly
            for item in payload:
                save_stock(item)
        elif isinstance(payload, dict):
            # If payload is a dictionary, save the stock
            save_stock(payload)
        else:
            # Handle unexpected payload type
            return HttpResponseBadRequest("Unexpected payload type")

        return HttpResponse("JSON data saved successfully")

    return HttpResponseNotAllowed(["POST"])


@csrf_exempt
def save_stock(data):
    # Extract data from dictionary and create stock object
    date = data.get("date")
    trade_code = data.get("trade_code")
    high = data.get("high")
    low = data.get("low")
    open = data.get("open")
    close = data.get("close")
    volume = data.get("volume")

    Stock = stock.objects.create(
        date=date,
        trade_code=trade_code,
        high=high,
        low=low,
        open=open,
        close=close,
        volume=volume,
    )


@csrf_exempt
@require_http_methods(["PUT"])
def update_stock_data(request, id):
    data = json.loads(request.body)
    field = data.get("field")
    value = data.get("value")

    try:
        stock_data = stock.objects.get(id=id)
        setattr(stock_data, field, value)
        stock_data.save()
        return JsonResponse({"message": "Value updated successfully"})
    except stock.DoesNotExist:
        return JsonResponse({"error": "Stock data not found"}, status=404)


@csrf_exempt
def delete(request, id):
    return render(request, "delete_stock.html", context={"id": id})


def add_stock(request):
    form = AddNew()
    if request.method == "POST":
        form = AddNew(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request, "Add_new.html", context={"form": form})


def delete_stock_data(request, id):
    print(f"Deleting stock data with ID: {id}")
    stock_data = stock.objects.filter(id=id).first()
    if stock_data:
        stock_data.delete()
        print("Stock data deleted successfully")
    else:
        print("Stock data not found")
    return HttpResponseRedirect(reverse("index"))
