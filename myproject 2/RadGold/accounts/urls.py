

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')