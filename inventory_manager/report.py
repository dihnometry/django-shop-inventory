from django.http import JsonResponse

ITEM_NOT_FOUND = "item not found"


def inventory_report(request, item_id):
    if item_id is None:
        return JsonResponse({"error": ITEM_NOT_FOUND}, status=404)
    try:
        quantity = int(request.GET.get("quantity", "1"))
    except ValueError:
        return JsonResponse({"error": "quantity must be an integer"}, status=400)

    return JsonResponse({"item_id": item_id, "quantity": quantity})
