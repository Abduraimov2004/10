from django.shortcuts import render, redirect
from .models import Comment

def comment_view(request):
    if request.method == 'POST':
        # Retrieve POST data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        comment_text = request.POST.get('comment')

        # Create and save the comment
        comment = Comment(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            comment=comment_text
        )
        comment.save()

        return redirect('comment_view')

    # Sorting logic
    sort_order = request.GET.get('sort', 'new')  # Default to 'new' if no sort parameter is provided
    if sort_order == 'old':
        comments = Comment.objects.all().order_by('created_at')  # Oldest first
    else:
        comments = Comment.objects.all().order_by('-created_at')  # Newest first

    return render(request, 'index.html', {'comments': comments, 'sort_order': sort_order})
