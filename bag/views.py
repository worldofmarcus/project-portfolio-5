from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def view_bag(request):
    """ This view renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ This view adds the quantity of a specific item
    to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                # messages.success(request,
                #                  (f'Updated size {size.upper()} '
                #                   f'{product.name} quantity to '
                #                   f'{bag[item_id]["items_by_size"][size]}'))
            else:
                bag[item_id]['items_by_size'][size] = quantity
                # messages.success(request,
                #                  (f'Added size {size.upper()} '
                #                   f'{product.name} to your bag'))
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            # messages.success(request,
            #                  (f'Added size {size.upper()} '
            #                   f'{product.name} to your bag'))
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            # messages.success(request,
            #                  (f'Updated {product.name} '
            #                   f'quantity to {bag[item_id]}'))
        else:
            bag[item_id] = quantity
            # messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)